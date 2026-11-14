#!/usr/bin/env python3
"""Q4 baseline-only ARM qualification. Fleet execution; offline analysis is pure."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import subprocess
import time

EXP = Path('experiments/ARM-LOOKUP-CONT-001')
OWNER = 'bplus ARM-LOOKUP-CONT-001'
UPSTREAM = 'ee8e7f70152404649ac947157fd662d11b4a00d5'
BASE_SOURCE = '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9'
CASES = {'hit':50000, 'score':50000, 'miss':100000, 'long':20000, 'external':20000, 'update':20000}
PHASES = ('Q4-lto-43', 'Q4-lto-29', 'Q4-lto-17', 'Q4-native-17')
BASELINES = {
    'gcc15-lto': ('bin/gcc15-lto/lookup', '77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb'),
    'native': ('bin/native/lookup', '2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf'),
}
REFEREE_PINS = {'current/compat/server.h': '2e287290fe2b3492098d36c4dfee783be0c43b9cde5954a176c84aa28d4f36dd',
 'current/compat/standalone.c': '300e1c37c1679014e25446fd82f1c2d0bf36c46c79d29255c856782e14c10d71',
 'current/src/zset_btree.c': '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9',
 'current/src/zset_btree.h': 'e1575e812cdff6fae794c4dd619a4d6d7c586c5df01ac0c881376acd294161ac',
 'current/vendor/sds.h': '5109573260ba9e3297030a851a0da1e485512a8c8f5b3cdbd6b062bef023a7b4',
 'current/vendor/siphash.c': '2e53f604ab8389a744efa55c3891eb9ff8983d18314400338e17ecc6c5b4f75e',
 'current/vendor/testhelp.h': 'b8c5243aac89758f44db1578735d6e3afc8e975dc1daa976ad4160ce55cbe9bd',
 'lookup.c': '1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, 'Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(), object_pairs_hook=unique,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')


def append(path, value):
    with Path(path).open('a') as f:
        f.write(json.dumps(value, allow_nan=False) + '\n')


def phase_spec(phase):
    require(phase in PHASES, 'Unknown Q4 phase')
    cohort = 'native' if phase == 'Q4-native-17' else 'gcc15-lto'
    seed = int(phase.rsplit('-', 1)[1])
    return cohort, seed, 1 if cohort == 'native' else 5


RAW_FIELDS = {'case', 'seed', 'ops', 'elapsed_ns', 'hits', 'score_sum', 'owned_bytes'}
ROW_FIELDS = RAW_FIELDS | {'phase', 'cohort', 'block', 'slot', 'label', 'sweeps',
                           'source_sha256', 'referee_sha256', 'binary_sha256'}


def check_raw(row, case, seed, sweeps):
    """Independent original lookup model. No I/O, clocks, or ambient state."""
    require(type(row) is dict and set(row) == RAW_FIELDS, 'Unexpected raw row schema')
    require(row['case'] == case, 'Wrong case')
    for field in RAW_FIELDS - {'case'}:
        require(type(row[field]) is int, 'Noninteger/nonfinite field: ' + field)
    require(row['seed'] == seed and row['ops'] == sweeps * 500, 'Wrong seed/count')
    require(row['hits'] == (0 if case == 'miss' else sweeps * 500), 'Wrong hit model')
    require(row['score_sum'] == (125250 * sweeps if case == 'score' else 0), 'Wrong score model')
    require(row['elapsed_ns'] > 0 and row['owned_bytes'] > 0, 'Nonpositive duration/memory')


def analyse_rows(phase, rows):
    """Pure complete-grid A/A analysis. Rejects malformed grids; never excludes a row."""
    cohort, seed, scale = phase_spec(phase)
    require(type(rows) is list and len(rows) == 72, 'Missing/extra Q4 row')
    blocks, offset = [], 0
    for case, native_sweeps in CASES.items():
        case_rows = rows[offset:offset+12]
        for block in range(3):
            rr = case_rows[block*4:block*4+4]
            for slot, r in enumerate(rr):
                require(type(r) is dict and set(r) == ROW_FIELDS, 'Unexpected augmented row schema')
                require(r['phase'] == phase and r['cohort'] == cohort and
                        type(r['block']) is int and r['block'] == block and
                        type(r['slot']) is int and r['slot'] == slot and
                        r['label'] == 'ABBA'[slot], 'Wrong/duplicate/reordered grid coordinate')
                require(type(r['sweeps']) is int and r['sweeps'] == native_sweeps * scale,
                        'Wrong frozen count')
                require(r['source_sha256'] == BASE_SOURCE and
                        r['referee_sha256'] == REFEREE_PINS['lookup.c'] and
                        r['binary_sha256'] == BASELINES[cohort][1], 'Wrong immutable identity')
                check_raw({k:r[k] for k in RAW_FIELDS}, case, seed, native_sweeps * scale)
            a_sum = rr[0]['elapsed_ns'] + rr[3]['elapsed_ns']
            b_sum = rr[1]['elapsed_ns'] + rr[2]['elapsed_ns']
            # Integer comparison avoids a floating rounding waiver at exactly1%.
            contrast_pass = abs(b_sum-a_sum)*100 <= a_sum
            minimum = min(r['elapsed_ns'] for r in rr)
            memory_pass = len({r['owned_bytes'] for r in case_rows}) == 1
            blocks.append({'case':case, 'block':block,
                           'delta_pct':100*(b_sum/a_sum-1),
                           'min_window_ns':minimum, 'same_memory_all_case_rows':memory_pass,
                           'pass':contrast_pass and minimum >= 250000000 and memory_pass})
        offset += 12
    return {'phase':phase, 'cohort':cohort, 'seed':seed, 'rows':72,
            'blocks':blocks, 'all_pass':all(b['pass'] for b in blocks),
            'source_adoption':False, 'candidate_executed':False}


def claim_sequence(root, admission):
    """Atomic one-use overall claim; even a failed/partial sequence cannot resume."""
    root = Path(root)
    require(not any((root / phase).exists() for phase in PHASES), 'Q4 phase already exists')
    out = root / 'Q4-profiler-off'
    out.mkdir()  # Existing directory is an irrevocable consumed attempt.
    write(out / 'admission.json', admission)
    return out


def claim_phase(root, phase, completed):
    require(list(completed) == list(PHASES[:PHASES.index(phase)]), 'Cannot skip/reorder phase')
    require(all(report.get('all_pass') is True for report in completed.values()),
            'Prior failed/partial phase forbids next cohort')
    out = Path(root) / phase
    out.mkdir()  # No overwrite, including failed or partial phases.
    return out


def validate_record(record, review, root, isolation_pin, collector_pin):
    """Validate reviewed operational declaration. Live proof is checked separately."""
    require(record['schema_version'] == 1 and record['owner'] == OWNER and
            Path(record['run_root']).resolve() == Path(root).resolve(), 'Wrong isolation ownership/root')
    require(type(record['deadline']) in (int, float) and math.isfinite(record['deadline']),
            'Invalid isolation deadline')
    require(type(record['coordinator']['pid']) is int and record['coordinator']['pid'] > 0 and
            str(record['coordinator']['start_ticks']).isdigit(), 'Bad coordinator identity')
    service = record['service']
    require(service == {'name':'snap.parca-agent.parca-agent-svc.service',
                        'saved_active_state':'active', 'saved_cpu_affinity':'',
                        'saved_allowed_cpus':''}, 'Saved Parca state/policy differs from preregistration')
    timers = record['cleanup_timers']
    require(type(timers) is list and len(timers) == 2 and len(set(timers)) == 2 and
            all(type(t) is str and t.endswith('.timer') and '/' not in t for t in timers),
            'Two distinct cleanup timers required')
    services = record['cleanup_services']
    require(type(services) is list and len(services) in (1, 2) and
            len({s['unit'] for s in services}) == len(services), 'Invalid cleanup service set')
    require(all(s['unit'].endswith('.service') and '/' not in s['unit'] for s in services),
            'Invalid cleanup unit name')
    require(record['restore_service'] is True and record['resume_saved_coordinator'] is True and
            record['reap_owned_children_before_resume'] is True, 'Recovery obligations missing')
    artifacts = record['cleanup_artifacts']
    require(type(artifacts) is list and artifacts and
            len({a['path'] for a in artifacts}) == len(artifacts), 'Missing/duplicate cleanup artifacts')
    pins = [record['lease_sha256'], isolation_pin, collector_pin] + \
           [a['sha256'] for a in artifacts] + [s['exec_start_sha256'] for s in services]
    require(all(type(h) is str and len(h) == 64 and all(c in '0123456789abcdef' for c in h)
                for h in pins), 'Invalid hash pin')
    require(review['schema_version'] == 1 and review['decision'] == 'APPROVED' and
            type(review['reviewer_role']) is str and bool(review['reviewer_role'].strip()) and
            review['isolation_sha256'] == isolation_pin and
            review['collector_sha256'] == collector_pin, 'Missing/mismatched independent review')


def identities(root, collector_pin, isolation_path, isolation_pin, review_path, review_pin, record):
    require(sha(__file__) == collector_pin, 'Collector bytes changed')
    require(sha(isolation_path) == isolation_pin and sha(review_path) == review_pin,
            'Reviewed operational record changed')
    for relative, expected in REFEREE_PINS.items():
        require(sha(root / EXP / relative) == expected, 'Frozen source/referee changed: ' + relative)
    for relative, expected in BASELINES.values():
        require(sha(root / relative) == expected, 'Original baseline ELF changed: ' + relative)
    for artifact in record['cleanup_artifacts']:
        path = Path(artifact['path'])
        if not path.is_absolute():
            path = root / path
        require(sha(path) == artifact['sha256'], 'Reviewed cleanup artifact changed')


def isolation(root, record, out, stem):
    """Fleet-only operational audit. Every command/raw result is retained."""
    audit = out / 'isolation'
    audit.mkdir(exist_ok=True)
    def command(argv, name):
        started = time.time()
        try:
            p = subprocess.run(argv, capture_output=True, timeout=30)
            stdout, stderr, code = p.stdout, p.stderr, p.returncode
        except subprocess.TimeoutExpired as error:
            stdout, stderr, code = error.stdout or b'', error.stderr or b'', None
        (audit / (stem + '-' + name + '.stdout')).write_bytes(stdout)
        (audit / (stem + '-' + name + '.stderr')).write_bytes(stderr)
        append(out / 'isolation-commands.jsonl', {'argv':argv, 'stem':stem+'-'+name,
               'started':started, 'finished':time.time(), 'returncode':code})
        require(code == 0 and not stderr, 'Isolation command failed: ' + name)
        return stdout
    def show(unit, properties, name):
        data = command(['systemctl','show',unit] + ['--property='+p for p in properties], name)
        values = dict(line.split('=',1) for line in data.decode().splitlines())
        require(set(values) == set(properties), 'Incomplete systemd state')
        return values
    snapshot = {'checked':time.time(), 'controller_affinity':sorted(os.sched_getaffinity(0))}
    write(audit / (stem + '-snapshot.json'), snapshot)
    lease_path = root / 'reservation.json'
    require(sha(lease_path) == record['lease_sha256'], 'Owned lease changed')
    lease = read(lease_path)
    require(lease['owner'] == OWNER and lease['state'] == 'RESERVED' and
            lease['deadline'] == record['deadline'] and time.time() < lease['deadline']-300,
            'Owned lease/cleanup margin unavailable')
    pid, ticks = record['coordinator']['pid'], str(record['coordinator']['start_ticks'])
    require(lease['coordinator_pid'] == pid and str(lease['coordinator_ticks']) == ticks,
            'Lease coordinator differs from reviewed identity')
    stat = (Path('/proc') / str(pid) / 'stat').read_text()
    fields = stat.rsplit(') ',1)[1].split()
    snapshot['coordinator'] = {'pid':pid, 'state':fields[0], 'start_ticks':fields[19]}
    require(fields[0] == 'T' and fields[19] == ticks, 'Saved coordinator not identically paused')
    require(os.sched_getaffinity(0) == {0} and platform.machine() == 'aarch64',
            'Controller must be ARM CPU0')
    cpu = Path('/sys/devices/system/cpu/cpu2')
    snapshot['cpu2_online'] = (cpu/'online').read_text().strip()
    snapshot['cpu2_siblings'] = (cpu/'topology/thread_siblings_list').read_text().strip()
    require(snapshot['cpu2_online'] == '1' and snapshot['cpu2_siblings'] == '2',
            'CPU2 offline or unexpected sibling')
    expected_services = {s['unit']:s['exec_start_sha256'] for s in record['cleanup_services']}
    used_services = set()
    for i, timer in enumerate(record['cleanup_timers']):
        state = show(timer, ['ActiveState','Unit','NextElapseUSecRealtime'], 'timer'+str(i))
        require(state['ActiveState'] == 'active' and state['Unit'] in expected_services and
                state['NextElapseUSecRealtime'] not in ('', '0', 'n/a'),
                'Cleanup timer inactive/unarmed/unreviewed target')
        used_services.add(state['Unit'])
    require(used_services == set(expected_services), 'Reviewed cleanup service not armed by timer')
    for i, (unit, expected) in enumerate(expected_services.items()):
        raw = command(['systemctl','show',unit,'--property=ExecStart','--value'], 'cleanup-exec'+str(i))
        require(hashlib.sha256(raw).hexdigest() == expected, 'Cleanup service ExecStart changed')
    state = show(record['service']['name'], ['ActiveState','SubState','MainPID','CPUAffinity','AllowedCPUs'], 'parca')
    require(state == {'ActiveState':'inactive','SubState':'dead','MainPID':'0',
                      'CPUAffinity':'','AllowedCPUs':''}, 'Parca active/process/policy state mismatch')
    matches = []
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            comm = (path/'comm').read_bytes().lower()
            cmdline = (path/'cmdline').read_bytes().lower()
        except FileNotFoundError:
            continue  # Process exited; permission/read failures remain fatal.
        if b'parca' in comm or b'parca-agent' in cmdline:
            matches.append({'pid':int(path.name), 'comm':comm.decode(errors='replace').strip(),
                            'cmdline':cmdline.decode(errors='replace')})
    snapshot['parca_processes'] = matches
    write(audit / (stem + '-snapshot.json'), snapshot)
    require(not matches, 'Parca process remains')
    require(not command(['docker','ps','-q'], 'docker').strip(), 'Concurrent Docker work')
    snapshot['passed'] = True
    write(audit / (stem + '-snapshot.json'), snapshot)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--collector-sha256', required=True)
    parser.add_argument('--isolation-record', required=True)
    parser.add_argument('--isolation-sha256', required=True)
    parser.add_argument('--isolation-review', required=True)
    parser.add_argument('--review-sha256', required=True)
    args = parser.parse_args()
    root = Path(args.root).resolve()
    iso_path, review_path = Path(args.isolation_record).resolve(), Path(args.isolation_review).resolve()
    admission = {'phases':list(PHASES), 'collector_sha256':args.collector_sha256,
                 'isolation_sha256':args.isolation_sha256, 'review_sha256':args.review_sha256,
                 'baseline_only':True, 'source_adoption':False}
    overall = claim_sequence(root, admission)
    completed = {}
    current_out = None
    try:
        record, review = read(iso_path), read(review_path)
        validate_record(record, review, root, args.isolation_sha256, args.collector_sha256)
        def identity():
            identities(root, args.collector_sha256, iso_path, args.isolation_sha256,
                       review_path, args.review_sha256, record)
        identity()
        for phase in PHASES:
            out = claim_phase(root, phase, completed)
            current_out = out
            cohort, seed, scale = phase_spec(phase)
            binary_path, binary_hash = BASELINES[cohort]
            metadata = dict(admission, phase=phase, cohort=cohort, seed=seed,
                sweeps={k:v*scale for k,v in CASES.items()}, upstream=UPSTREAM,
                baseline_sha256=binary_hash, source_sha256=BASE_SOURCE,
                referee_pins=REFEREE_PINS, started=time.time())
            write(out/'metadata.json', metadata)
            def run(mode, case, count, stem):
                identity()
                isolation(root, record, out, stem+'-pre')
                argv = ['taskset','-c','2',str(root/binary_path),mode,case,str(seed),str(count)]
                command = {'argv':argv, 'stem':stem, 'started':time.time(),
                           'binary_sha256':binary_hash, 'preflight_passed':True}
                append(out/'launches.jsonl', command)  # Retained even if the controller is killed mid-child.
                proc = None
                before = resource.getrusage(resource.RUSAGE_CHILDREN)
                try:
                    with (out/(stem+'.stdout')).open('wb') as stdout, (out/(stem+'.stderr')).open('wb') as stderr:
                        proc = subprocess.Popen(argv, stdout=stdout, stderr=stderr,
                            preexec_fn=lambda: os.sched_setaffinity(0, {2}))
                        command['pid'] = proc.pid
                        command['child_affinity'] = sorted(os.sched_getaffinity(proc.pid))
                        append(out/'child-starts.jsonl', {'stem':stem,'pid':proc.pid,
                               'affinity':command['child_affinity']})
                        require(command['child_affinity'] == [2], 'Workload child affinity differs')
                        proc.wait(timeout=240)
                except BaseException as error:
                    command['child_error'] = type(error).__name__ + ': ' + str(error)
                    if proc is not None and proc.poll() is None:
                        proc.kill()
                        proc.wait()
                after = resource.getrusage(resource.RUSAGE_CHILDREN)
                command['rusage'] = {name:getattr(after,name)-getattr(before,name) for name in
                    ('ru_utime','ru_stime','ru_minflt','ru_majflt','ru_nvcsw','ru_nivcsw')}
                command['rusage_scope'] = 'Whole taskset/baseline child; includes setup/warmup; outside frozen inner loop'
                command.update(returncode=None if proc is None else proc.returncode, finished=time.time())
                append(out/'commands.jsonl', command)
                # Postflight runs even after failed/timeout workload processes.
                identity()
                isolation(root, record, out, stem+'-post')
                require(command['returncode'] == 0 and 'child_error' not in command and
                        not (out/(stem+'.stderr')).read_bytes(), 'Workload failed; attempt consumed')
                return read(out/(stem+'.stdout'))
            for case in CASES:
                verified = run('verify',case,1,'verify-'+case)
                require(set(verified) == {'verified','case','seed','members','owned_bytes'} and
                        verified['verified'] is True and verified['case'] == case and
                        type(verified['seed']) is int and verified['seed'] == seed and
                        verified['members'] == 500 and type(verified['owned_bytes']) is int and
                        verified['owned_bytes'] > 0, 'Baseline-only verification model failed')
            allrows = []
            for case, count in CASES.items():
                for block in range(3):
                    for slot, label in enumerate('ABBA'):
                        stem = f'aa-{case}-{block}-{slot}'
                        raw = run('measure',case,count*scale,stem)
                        check_raw(raw,case,seed,count*scale)
                        row = dict(raw,phase=phase,cohort=cohort,block=block,slot=slot,label=label,
                            sweeps=count*scale,source_sha256=BASE_SOURCE,
                            referee_sha256=REFEREE_PINS['lookup.c'],binary_sha256=binary_hash)
                        append(out/'aa.jsonl',row)
                        allrows.append(row)
                        print(phase,stem,flush=True)
            report = analyse_rows(phase,allrows)
            write(out/'analysis.json',report)
            write(out/'result.json',{'status':'PASS' if report['all_pass'] else 'PARK',
                'complete':True,'rows':72,'source_adoption':False,'candidate_executed':False})
            completed[phase] = report
            if not report['all_pass']:
                write(overall/'result.json',{'status':'PARK','stopped_at':phase,
                    'completed_phases':list(completed),'source_adoption':False,'candidate_executed':False})
                return
        write(overall/'result.json',{'status':'PASS','completed_phases':list(completed),
              'source_adoption':False,'candidate_executed':False})
    except BaseException as error:
        result = {'status':'ERROR','attempt_consumed':True,'error_type':type(error).__name__,
                  'error':str(error),'completed_phases':list(completed),
                  'source_adoption':False,'candidate_executed':False}
        write(overall/'result.json',result)
        if current_out is not None:
            write(current_out/'result.json',result)
        raise


if __name__ == '__main__':
    main()
