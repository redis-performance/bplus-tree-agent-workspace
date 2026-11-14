#!/usr/bin/env python3
"""One-shot fleet-only H6 descriptor guards; importing this module does no work."""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import signal
import subprocess
import sys
import time

EXP = Path('experiments/ARM-LOOKUP-CONT-001')
UPSTREAM = 'ee8e7f70152404649ac947157fd662d11b4a00d5'
CASES = {'member-forward': 1000000, 'member-reverse': 1000000,
         'lookup-inline': 100000, 'lookup-external': 500000}
SOURCE_PINS = {
    'base': '16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9',
    'A': 'ffd548a1fba1db452e98fbe1dd3902b2ba34f44af797edeaed9976783444e744',
    'B': '5f6bfd216350dceee6ed486d5fc6e1535162a64c037c3ceee746ceae9b0813ae',
    'C': 'bf2cbbe66b36d178692ba214fd192af1b5dc6b1c67f1619e2d782c839b2da825'}
REFEREE_PINS = {
    'descriptor-guards/guards.c': '1f5ea1beb4391e5ae1818a5df60167c85e0931f2172efa300fd5cc2aea90fed9',
    'descriptor-guards/build.sh': '1c8c4f8f4cd1233a2d71f4e660cb144bccd675fe37337dad02bb1bc5ce761d78',
    'descriptor-guards/PROTOCOL.md': '39f44530191b246f6efb3345243d524af190f66b4d5688df73ee5ae0c444a04c',
    'current/src/zset_btree.h': 'e1575e812cdff6fae794c4dd619a4d6d7c586c5df01ac0c881376acd294161ac',
    'current/compat/server.h': '2e287290fe2b3492098d36c4dfee783be0c43b9cde5954a176c84aa28d4f36dd',
    'current/compat/standalone.c': '300e1c37c1679014e25446fd82f1c2d0bf36c46c79d29255c856782e14c10d71',
    'current/vendor/sds.h': '5109573260ba9e3297030a851a0da1e485512a8c8f5b3cdbd6b062bef023a7b4',
    'current/vendor/siphash.c': '2e53f604ab8389a744efa55c3891eb9ff8983d18314400338e17ecc6c5b4f75e',
    'current/vendor/testhelp.h': 'b8c5243aac89758f44db1578735d6e3afc8e975dc1daa976ad4160ce55cbe9bd'}
MEMORY = ('owned_bytes_before', 'owned_bytes_after')
TIMEOUT = 240


def require(value, message):
    if not value:
        raise RuntimeError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write_new(path, value):
    with Path(path).open('x') as file:
        json.dump(value, file, indent=2)
        file.write('\n')


def contained(root, relative):
    require(not Path(relative).is_absolute(), 'Absolute artifact path')
    path = root / relative
    require(path.resolve().is_relative_to(root), 'Artifact escapes fleet root')
    return path


def phase_name(host, cohort, seed):
    require(host in ('arm', 'intel') and cohort in ('native', 'gcc15-lto') and
            seed in (17, 29, 43), 'Unsupported cohort/seed')
    return f'H6-descriptor-{host}-{cohort}-r0-seed{seed}'


def exclusions(root):
    path = root / 'H6-exclusions.json'  # Required even when empty; global across H6 cohorts.
    data = read(path)
    require(type(data) is dict, 'Invalid H6 exclusion registry')
    for variant, entry in data.items():
        require(type(variant) is str and variant in ('A', 'B', 'C') and type(entry) is dict and
                entry.get('source_sha256') == SOURCE_PINS[variant] and
                isinstance(entry.get('reason'), str) and entry['reason'].strip(),
                'Unknown/stale H6 exclusion source or missing reason')
    return data


def expected(case, sweeps):
    require(case in CASES and type(sweeps) is int and 0 < sweeps <= 2000000,
            'Unknown case or invalid count')
    lengths = [0, *range(1, 18), 24, 32, 64, 127, 128, 129, 252, 253,
               254, 255, 318, 319, 320, 321, 512, 1024]
    members = [(n, r) for n in lengths for r in range(16 if n else 1)]
    totals = dict(ops=0, hits=0, bytes=0, samples=0, scores=0, weighted=0)
    for ordinal, index in enumerate(reversed(range(529)) if case == 'member-reverse'
                                    else range(529), 1):
        n, replica = members[index]
        if case.startswith('member-'):
            def byte(offset):
                return replica if offset == 0 else (0 if offset % 7 == 0 else
                                                    (37 * offset + 11 * replica) % 256)
            sample = byte(0) + 257 * byte(n // 2) + 65537 * byte(n - 1) if n else 0
            totals['ops'] += 1
            totals['hits'] += 1
            totals['bytes'] += n
            totals['samples'] += sample * ordinal
            totals['scores'] += index + 1
            totals['weighted'] += (index + 1) * ordinal
        elif (n < 320) == (case == 'lookup-inline'):
            totals['ops'] += 2
            totals['hits'] += 1
            totals['scores'] += index + 1 - 123
            totals['weighted'] += index + 1
    return {key: value * sweeps for key, value in totals.items()}


def check_row(row, case, seed, sweeps, mode):
    require(type(row) is dict, 'Nonobject row')
    require(row.get('verified') is True and type(row.get('revision')) is int and row['revision'] == 0 and
            row.get('mode') == mode and row.get('case') == case and
            type(row.get('seed')) is int and row['seed'] == seed and
            type(row.get('sweeps')) is int and row['sweeps'] == sweeps and
            type(row.get('members')) is int and row['members'] == 529, 'Row identity mismatch')
    for key, value in expected(case, sweeps).items():
        require(type(row.get(key)) is int and row[key] == value, 'Bad checksum: ' + key)
    for key in (*MEMORY, 'owned_bytes_after_validation'):
        require(type(row.get(key)) is int and row[key] > 0, 'Invalid memory: ' + key)
    if mode == 'measure':
        require(type(row.get('elapsed_ns')) is int and row['elapsed_ns'] >= 250000000,
                'Row below 250 ms or invalid clock; attempt consumed')
    else:
        require('elapsed_ns' not in row, 'Verification unexpectedly timed')


def block_result(rows, qualification):
    require(len(rows) == 4 and [r['label'] for r in rows] == list('ABBA') and
            [r['slot'] for r in rows] == list(range(4)), 'Invalid ABBA order')
    a, b = [rows[0], rows[3]], rows[1:3]
    at = sum(r['elapsed_ns'] for r in a)
    bt = sum(r['elapsed_ns'] for r in b)
    # Integer comparisons make the exact 1% boundary independent of rounding.
    passed = abs(bt - at) * 100 <= at if qualification else (bt - at) * 100 <= at
    memory = {}
    for key in MEMORY:
        av, bv = sum(r[key] for r in a), sum(r[key] for r in b)
        memory[key] = 100 * (bv - av) / av
        passed = passed and ((av == bv) if qualification else (bv - av) * 100 <= av)
    minimum = min(r['elapsed_ns'] for r in rows)
    return dict(delta_pct=100 * (bt - at) / at, memory_delta_pct=memory,
                min_window_ns=minimum, passed=bool(passed and minimum >= 250000000))


def analyze(rows, variants, seed, qualification):
    require(variants and len(set(variants)) == len(variants) and
            all(v in ('base', 'A', 'B', 'C') for v in variants) and
            (not qualification or variants == ['base']), 'Invalid analysis variant grid')
    require(len(rows) == 48 * len(variants), 'Missing/extra raw rows')
    blocks, memory = [], {}
    for variant in variants:
        for case, count in CASES.items():
            for block in range(3):
                rr = [r for r in rows if (r['variant'], r['case'], r['block']) ==
                      (variant, case, block)]
                for row in rr:
                    check_row(row, case, seed, count, 'measure')
                    key = (row['binary_sha256'], case)
                    endpoints = tuple(row[k] for k in MEMORY)
                    require(key not in memory or memory[key] == endpoints,
                            'Memory endpoints differ within binary/case')
                    memory[key] = endpoints
                result = block_result(rr, qualification)
                blocks.append(dict(variant=variant, case=case, block=block, **result))
    return dict(rows=len(rows), blocks=blocks, passed=all(b['passed'] for b in blocks))


def discovery_gate(metadata, report, variant, cohort, baseline_sha256):
    require(metadata['cohort'] == cohort and str(metadata['seed']) == '17' and
            metadata['source_freeze'] == UPSTREAM and
            metadata['baseline_sha256'] == baseline_sha256 and
            metadata['variants'][variant]['source_sha256'] == SOURCE_PINS[variant] and
            re.fullmatch(r'[0-9a-f]{64}', metadata['variants'][variant]['binary_sha256']) and
            report['variants'][variant]['eligible'] is True,
            'Original H6 discovery did not pass for this source/cohort')


def cpu_list(text):
    result = set()
    for item in text.strip().split(','):
        values = item.split('-')
        result.update(range(int(values[0]), int(values[-1]) + 1))
    return result


def leasecheck(root, host, saved=None, margin=300):
    lease = read(root / 'reservation.json')
    require(lease['owner'] == 'bplus ARM-LOOKUP-CONT-001' and lease['state'] == 'RESERVED'
            and time.time() + margin < lease['deadline'], 'Lease or cleanup margin unavailable')
    identity = [lease['coordinator_pid'], str(lease['coordinator_ticks']), lease['deadline']]
    require(saved is None or saved == identity, 'Lease/coordinator identity changed')
    require(subprocess.run(['systemctl', 'is-active', '--quiet', root.name + '-release.timer'],
                           capture_output=True).returncode == 0, 'Release timer inactive')
    fields = (Path('/proc') / str(identity[0]) / 'stat').read_text().rsplit(') ', 1)[1].split()
    require(fields[0] == 'T' and fields[19] == identity[1], 'Coordinator not original/stopped')
    require(os.sched_getaffinity(0) == {0}, 'Controller must be on CPU0')
    require(platform.machine() == ('aarch64' if host == 'arm' else 'x86_64'), 'Wrong host architecture')
    cpu = Path('/sys/devices/system/cpu/cpu2')
    require((cpu / 'online').read_text().strip() == '1', 'CPU2 offline')
    siblings = cpu_list((cpu / 'topology/thread_siblings_list').read_text())
    require(all(i == 2 or Path(f'/sys/devices/system/cpu/cpu{i}/online').read_text().strip() == '0'
                for i in siblings), 'Effective SMT sibling online')
    require(not subprocess.check_output(['docker', 'ps', '-q'], text=True).strip(), 'Concurrent container')
    if host == 'intel':
        require('sibling50_online' in lease and
                Path('/sys/devices/system/cpu/cpu50/online').read_text().strip() == '0', 'Intel SMT state missing')
        service = subprocess.run(['systemctl', 'show', '--property=ActiveState', '--value',
                                  'snap.parca-agent.parca-agent-svc.service'], capture_output=True, text=True)
        require(service.returncode == 0 and service.stdout.strip() == 'inactive', 'Intel profiler not inactive')
    # Existing collectors do not share our lock: also reject another collector,
    # compiler, profiler or benchmark process. Do not print process arguments.
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit() or int(proc.name) in (os.getpid(), int(identity[0])):
            continue
        try:
            state = (proc / 'stat').read_text().rsplit(') ', 1)[1].split()[0]
            if state in ('Z', 'T', 't'):
                continue
            comm = (proc / 'comm').read_text().strip()
            args = (proc / 'cmdline').read_bytes().split(b'\0')
        except (FileNotFoundError, ProcessLookupError):
            continue
        competing = comm in {'perf', 'toplev', 'cc', 'cc1', 'cc1plus', 'gcc', 'clang',
                             'ld', 'as', 'lto1', 'lto-wrapper', 'memtier_benchmark', 'redis-benchmark'}
        competing |= any(re.fullmatch(r'fleet_[\w-]+\.py', Path(x.decode(errors='replace')).name)
                         for x in args if x)
        competing |= any(x.decode(errors='replace').startswith(str(root / 'bin') + '/') or
                         '/H6-descriptor-' in x.decode(errors='replace') and '/bin/' in x.decode(errors='replace')
                         for x in args if x)
        require(not competing, 'Competing process: PID ' + proc.name + ' (' + comm + ')')
    return identity


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--platform', choices=['arm', 'intel'], required=True)
    parser.add_argument('--cohort', choices=['native', 'gcc15-lto'], required=True)
    parser.add_argument('--seed', type=int, choices=[17, 29, 43], default=17)
    parser.add_argument('--variants', default='ABC', help='Ordered unique subset of ABC; identical across actions')
    parser.add_argument('--action', choices=['build', 'qualify', 'compare'], required=True)
    parser.add_argument('--collector-sha256', required=True)
    parser.add_argument('--approval-sha256', help='Required for qualification/comparison; pins codegen.json')
    args = parser.parse_args()
    root = Path(args.root).resolve()
    require(root.parent == Path('/opt') and root.name.startswith('bplus-arm-lookup-cont-'),
            'Only reserved /opt/bplus-arm-lookup-cont-* fleet roots are accepted')
    require(args.variants and args.variants == ''.join(sorted(set(args.variants))) and
            set(args.variants) <= set('ABC'), 'Variants must be an ordered unique subset of ABC')
    os.chdir(root)
    phase = root / phase_name(args.platform, args.cohort, args.seed)
    stage = phase / args.action
    require(not stage.exists(), 'Action already claimed; no overwrite, resume or retry')
    for name in ('LD_PRELOAD', 'LD_LIBRARY_PATH', 'CPATH', 'C_INCLUDE_PATH', 'LIBRARY_PATH',
                 'COMPILER_PATH', 'GCC_EXEC_PREFIX', 'TASK_CC'):
        require(not os.environ.get(name), 'Unreviewed toolchain/runtime environment: ' + name)
    freeze_path = root / EXP / 'descriptor-guards/FREEZE.json'
    freeze = read(freeze_path)
    require(freeze.get('status') == 'FROZEN' and freeze.get('revision') == 0 and
            freeze.get('source_hashes') == SOURCE_PINS and freeze.get('referee_sha256') == REFEREE_PINS and
            freeze.get('cases') == CASES and freeze.get('collector_sha256') == args.collector_sha256,
            'Controller freeze missing or differs from reviewed inputs')
    source_group = 'H6-native' if args.cohort == 'native' else 'H6-lto'
    sources = {'base': EXP / 'current/src/zset_btree.c', **{
        v: Path('variants') / source_group / v / 'zset_btree.c' for v in args.variants}}
    pins = {freeze_path: sha(freeze_path), Path(__file__).resolve(): args.collector_sha256}
    pins.update({root / EXP / p: h for p, h in REFEREE_PINS.items()})
    excluded = exclusions(root)
    exclusion_pin = sha(root / 'H6-exclusions.json')
    prior = read(root / 'baseline/metadata.json')
    pins[root / 'baseline/metadata.json'] = sha(root / 'baseline/metadata.json')
    require(prior['source_manifest']['upstream_sha'] == UPSTREAM and
            prior['source_manifest']['files']['current/src/zset_btree.c']['sha256'] == SOURCE_PINS['base'],
            'Wrong original baseline')
    lock = (root / '.descriptor-guards.lock').open('a')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    lease = leasecheck(root, args.platform, margin=TIMEOUT + 300)

    def identities():
        for path, pin in pins.items():
            require(sha(path) == pin, 'Immutable input changed: ' + str(path))
        require(sha(root / 'H6-exclusions.json') == exclusion_pin, 'Global H6 exclusions changed during action')
        exclusions(root)  # Recheck exact source bindings even for exclusions not being measured.
        for v, path in sources.items():
            require(sha(contained(root, path)) == SOURCE_PINS[v], 'Source mismatch: ' + v)
            if v != 'base':
                require(not any((root / path.parent / name).exists() for name in ('server.h', 'zset_btree.h')),
                        'Unpinned source-adjacent header')

    identities()
    if args.action == 'build':
        require(not phase.exists(), 'Build phase already exists; no retry under same identity')
        phase.mkdir()
    else:
        meta_path = phase / 'build/metadata.json'
        meta = read(meta_path)
        require(meta['platform'] == args.platform and meta['cohort'] == args.cohort and
                meta['seed'] == args.seed and meta['cases'] == CASES and
                meta['collector_sha256'] == args.collector_sha256 and meta['lease'] == lease and
                meta['freeze_sha256'] == sha(freeze_path) and meta['referee_sha256'] == REFEREE_PINS,
                'Build identity or reservation mismatch')
        require(list(meta['binaries']) == ['base', *args.variants], 'Use identical built variant list')
        pins[meta_path] = sha(meta_path)
        for v, entry in meta['binaries'].items():
            require(entry['source_sha256'] == SOURCE_PINS[v], 'Build source differs from freeze')
            for key in ('binary', 'assembly'):
                pins[contained(root, entry[key + '_path'])] = entry[key + '_sha256']
            for key in ('compiler_version', 'size'):
                pins[contained(root, entry[key + '_path'])] = entry[key + '_sha256']
        approval_path = phase / 'codegen.json'
        require(args.approval_sha256 and sha(approval_path) == args.approval_sha256, 'Unpinned codegen approval')
        approval = read(approval_path)
        require(approval['metadata_sha256'] == sha(meta_path) and approval['reviewer'] and
                approval['binaries']['base']['eligible'] is True, 'Missing baseline codegen approval')
        pins[approval_path] = args.approval_sha256
        review = contained(root, approval['review_path'])
        pins[review] = approval['review_sha256']
        eligible = []
        for v, entry in meta['binaries'].items():
            decision = approval['binaries'][v]
            require(all(decision[k] == entry[k] for k in ('binary_sha256', 'assembly_sha256', 'source_sha256')),
                    'Codegen approval does not name exact source/ELF/assembly')
            require(type(decision['eligible']) is bool, 'Invalid eligibility')
            if decision['eligible']:
                require(decision['timer_and_loops_pass'] is True, 'Timer/loop screen missing')
                if v != 'base':
                    require(decision['descriptor_mechanism_pass'] is True, 'Candidate mechanism ineligible')
                    origin = decision['discovery']
                    for key in ('metadata', 'analysis'):
                        path = contained(root, origin[key + '_path'])
                        pins[path] = origin[key + '_sha256']
                    om = read(root / origin['metadata_path'])
                    report = read(root / origin['analysis_path'])
                    discovery_gate(om, report, v, args.cohort, prior['binary_sha256'][args.cohort])
                    if v not in excluded:
                        eligible.append(v)
        require(eligible, 'No eligible nonexcluded H6 candidate; no timing authorized')
    identities()
    stage.mkdir()  # Atomic one-shot action claim, before any child process.
    write_new(stage / 'started.json', dict(action=args.action, started=time.time(), lease=lease,
              collector_sha256=args.collector_sha256, exclusions=excluded,
              exclusions_sha256=exclusion_pin, approval_sha256=args.approval_sha256))

    def run(command, stem, allow_stderr=False, container=None):
        identities()
        leasecheck(root, args.platform, lease, TIMEOUT + 300)
        write_new(stage / (stem + '.started.json'), dict(argv=command, started=time.time(),
                  preflight='lease/coordinator/timer/CPU/isolation/identities/exclusions passed'))
        stdout = stderr = ''
        code = None
        with (stage / (stem + '.stdout')).open('x') as out, (stage / (stem + '.stderr')).open('x') as err:
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    text=True, start_new_session=True)
            try:
                stdout, stderr = proc.communicate(timeout=TIMEOUT)
                code = proc.returncode
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                stdout, stderr = proc.communicate()
                if container:
                    cleanup = subprocess.run(['docker', 'rm', '-f', container], capture_output=True, text=True)
                    write_new(stage / (stem + '.cleanup.json'), dict(returncode=cleanup.returncode,
                              stdout=cleanup.stdout, stderr=cleanup.stderr))
            out.write(stdout)
            err.write(stderr)
        write_new(stage / (stem + '.finished.json'), dict(returncode=code, finished=time.time()))
        require(code == 0 and (allow_stderr or not stderr), 'Child failed; action consumed: ' + stem)
        identities()
        leasecheck(root, args.platform, lease)
        write_new(stage / (stem + '.postflight.json'), dict(passed=True, checked=time.time()))
        return stdout

    try:
        if args.action == 'build':
            (stage / 'bin').mkdir()
            binaries = {}
            compiler_image = prior['gcc15_image'] if args.cohort == 'gcc15-lto' else None
            native_compiler = None
            if compiler_image:
                require(re.fullmatch(r'sha256:[0-9a-f]{64}', compiler_image), 'Mutable compiler image')
            else:
                compiler = Path(shutil.which('cc')).resolve()
                pins[compiler] = sha(compiler)
                native_compiler = dict(path=str(compiler), sha256=sha(compiler))
            for v, source in sources.items():
                binary = stage / 'bin' / v
                command = ['sh', str(EXP / 'descriptor-guards/build.sh'), str(source),
                           str(binary.relative_to(root)), 'lto' if compiler_image else 'native']
                name = phase.name.lower() + '-build-' + v.lower()
                prefix = ['docker', 'run', '--rm', '--name', name, '--cpuset-cpus', '0-3',
                          '--network', 'none', '-v', str(root) + ':/work', '-w', '/work', compiler_image]
                version = prefix + ['cc', '--version'] if compiler_image else ['cc', '--version']
                run(version, 'compiler-' + v, container=name if compiler_image else None)
                run(prefix + command if compiler_image else command, 'build-' + v,
                    allow_stderr=True, container=name if compiler_image else None)
                pins[binary] = sha(binary)
                run(['objdump', '-d', str(binary)], 'assembly-' + v)
                run(['size', str(binary)], 'size-' + v)
                assembly = stage / ('assembly-' + v + '.stdout')
                pins[assembly] = sha(assembly)
                binaries[v] = dict(source_path=str(source), source_sha256=SOURCE_PINS[v],
                    binary_path=str(binary.relative_to(root)), binary_sha256=sha(binary),
                    assembly_path=str(assembly.relative_to(root)), assembly_sha256=sha(assembly))
                for key, name in (('compiler_version', 'compiler-' + v), ('size', 'size-' + v)):
                    path = stage / (name + '.stdout')
                    pins[path] = sha(path)
                    binaries[v].update({key + '_path': str(path.relative_to(root)), key + '_sha256': sha(path)})
                for case in CASES:
                    row = json.loads(run(['taskset', '-c', '2', str(binary), 'verify', case,
                                          str(args.seed), '2'], 'verify-' + v + '-' + case))
                    check_row(row, case, args.seed, 2, 'verify')
            write_new(stage / 'metadata.json', dict(platform=args.platform, cohort=args.cohort,
                seed=args.seed, cases=CASES, lease=lease, compiler_image=compiler_image,
                native_compiler=native_compiler,
                collector_sha256=args.collector_sha256, referee_sha256=REFEREE_PINS,
                freeze_sha256=sha(freeze_path), binaries=binaries, finished=time.time()))
            return
        qualification = args.action == 'qualify'
        if not qualification:
            qdir = phase / 'qualify'
            qreport = read(qdir / 'result.json')
            qrows = [json.loads(x) for x in (qdir / 'rows.jsonl').read_text().splitlines()]
            qstart = read(qdir / 'started.json')
            require(qstart['approval_sha256'] == args.approval_sha256 and
                    qstart['collector_sha256'] == args.collector_sha256 and qstart['lease'] == lease,
                    'Approval, collector or reservation changed after A/A')
            require(qreport == analyze(qrows, ['base'], args.seed, True) and qreport['passed'],
                    'A/A incomplete, corrupt or failed')
            for row in qrows:
                require(row['binary_sha256'] == meta['binaries']['base']['binary_sha256'], 'A/A wrong baseline ELF')
            for filename in ('result.json', 'rows.jsonl', 'started.json'):
                pins[qdir / filename] = sha(qdir / filename)
        variants = ['base'] if qualification else eligible
        write_new(stage / 'selection.json', dict(requested=list(args.variants), measured=variants,
                  excluded=excluded, codegen_or_discovery_ineligible=[v for v in args.variants if v not in eligible]))
        run(['taskset', '-c', '2', sys.executable, '-c',
             'import os,sys;sys.exit(0 if os.sched_getaffinity(0)=={2} else 1)'], 'affinity-zero-work')
        allrows, endpoints = [], {}
        for variant in variants:
            for case, count in CASES.items():
                for block in range(3):
                    rr = []
                    for slot, label in enumerate('ABBA'):
                        which = 'base' if qualification or label == 'A' else variant
                        entry = meta['binaries'][which]
                        stem = f'{variant}-{case}-{block}-{slot}'
                        row = json.loads(run(['taskset', '-c', '2', str(root / entry['binary_path']),
                                             'measure', case, str(args.seed), str(count)], stem))
                        check_row(row, case, args.seed, count, 'measure')
                        row.update(variant=variant, block=block, slot=slot, label=label,
                                   binary_sha256=entry['binary_sha256'])
                        point = tuple(row[k] for k in MEMORY)
                        key = (which, case)
                        require(key not in endpoints or endpoints[key] == point, 'Unstable memory endpoint')
                        endpoints[key] = point
                        if not qualification and which == 'base':
                            control = next(r for r in qrows if r['case'] == case)
                            require(point == tuple(control[k] for k in MEMORY), 'Baseline memory differs from A/A')
                        with (stage / 'rows.jsonl').open('a') as file:
                            file.write(json.dumps(row) + '\n')
                        rr.append(row)
                        allrows.append(row)
                    result = block_result(rr, qualification)
                    write_new(stage / (f'{variant}-{case}-{block}.json'), result)
                    # Preserve a complete declared grid even if an effect gate
                    # fails. Invalid/short rows or changing isolation stop at once.
        result = analyze(allrows, variants, args.seed, qualification)
        write_new(stage / 'result.json', result)
        print(json.dumps(dict(action=args.action, **result)), flush=True)
    except Exception as error:
        write_new(stage / 'FAILED.json', dict(error=str(error), failed=time.time(), retry_permitted=False))
        raise


if __name__ == '__main__':
    main()
