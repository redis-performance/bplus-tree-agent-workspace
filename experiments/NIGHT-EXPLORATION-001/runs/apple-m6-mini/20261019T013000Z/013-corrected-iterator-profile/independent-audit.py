#!/usr/bin/env python3
"""Inspect retained profile evidence without executing the profiler or driver."""
from collections import Counter
import csv
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import io
import json
from pathlib import Path
import re
import struct
import subprocess

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
PLAN = json.loads((OUT / 'PLAN.json').read_text())
CONTRACTS = {c['id']: c for c in PLAN['contracts']}
MASK64 = (1 << 64) - 1

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dt(value):
    return datetime.fromisoformat(value)

@lru_cache(None)
def fingerprint(n, seed):
    state = seed
    def random_word():
        nonlocal state
        state = (state + 0x9e3779b97f4a7c15) & MASK64
        value = state
        value = ((value ^ (value >> 30)) * 0xbf58476d1ce4e5b9) & MASK64
        value = ((value ^ (value >> 27)) * 0x94d049bb133111eb) & MASK64
        return value ^ (value >> 31)
    for _ in range(16):
        random_word()
    order = list(range(n))
    for end in range(n, 1, -1):
        pick = random_word() % end
        order[end - 1], order[pick] = order[pick], order[end - 1]
    value = 14695981039346656037
    for member_id in order:
        value = ((value ^ member_id) * 1099511628211) & MASK64
    return value

@lru_cache(None)
def checksum(n, encoding, mask, requested):
    total = n
    if mask & 1:
        total += sum(i & 255 for i in range(n))
    if mask & 2:
        total += n * 16
    if mask & 4:
        total += sum(struct.unpack('<Q', struct.pack('<d', float(i - n//2) +
                         (0.25 if encoding == 'fraction' else 0.0)))[0] for i in range(n))
    return total * ((requested + n - 1) // n) & MASK64

def log_paths(logs):
    paths = {}
    for channel, log in logs.items():
        public = OUT / log['file']
        assert sha(public) == log['sha256']
        assert log['original_raw'].startswith('ignored ')
        private = ROOT / log['original_raw'][len('ignored '):]
        assert sha(private) == log['original_raw_sha256']
        paths[channel] = (public, private)
    return paths

def read_row(text, n, requested, seed, contract, warmup):
    rows = list(csv.DictReader(io.StringIO(text)))
    assert len(rows) == 1
    row = rows[0]
    actual = ((requested + n - 1) // n) * n
    assert row['case'] == 'iterator-modes'
    assert int(row['size']) == n and int(row['seed']) == seed
    assert int(row['requested_ops']) == requested and int(row['operations']) == actual
    assert int(row['traversals']) == actual // n
    assert row['direction'] == contract['direction'] and row['encoding'] == contract['encoding']
    assert int(row['mask']) == contract['mask'] and int(row['member_bytes']) == 16
    assert int(row['warmup_passes']) == warmup
    assert int(row['checksum']) == int(row['expected_checksum']) == checksum(n, contract['encoding'], contract['mask'], requested)
    assert int(row['construction_fingerprint']) == fingerprint(n, seed)
    assert int(row['tree_bytes']) > 0
    # Elapsed columns are retained but deliberately never read or calculated.
    return row

def main():
    summary = json.loads((OUT / 'summary.json').read_text())
    state = json.loads((OUT / 'capture-status.json').read_text())
    frozen = json.loads((OUT / 'freeze.json').read_text())
    authorization = json.loads((OUT / 'AUTHORIZATION.json').read_text())
    launch = json.loads((OUT / 'LAUNCH.json').read_text())
    planned = json.loads((OUT / 'planned-commands.json').read_text())
    commands = [json.loads(line) for line in (OUT / 'commands.jsonl').read_text().splitlines()]
    assert len(commands) == 30 and len({c['name'] for c in commands}) == 30
    command_map = {c['name']: c for c in commands}
    for command in commands:
        log_paths(command['logs'])
        assert command['returncode'] == 0 and command['timed_out'] is False
        assert command['process_reaped'] is True
        assert command['wall_seconds'] <= command['timeout_seconds'] <= 120
    assert len(frozen['files_sha256']) == 18 and len(frozen['binaries_sha256']) == 3
    for path, expected in {**frozen['files_sha256'], **frozen['binaries_sha256']}.items():
        assert sha(ROOT / path) == expected
    assert summary['status'] == state['status'] == 'complete'
    assert state['all_children_reaped'] is True
    assert summary['planned'] == summary['completed'] == summary['sufficient'] == summary['total_captures'] == 16
    assert summary['elapsed_fields_unused'] is True and summary['no_optimization_selected'] is True
    assert all(state[key] == value for key, value in summary.items())
    assert not (ROOT / 'scratch/m6-corrected-iterator-profile/CAPTURE.lock').exists()
    assert len(PLAN['captures']) == planned['count'] == len(planned['commands']) == 16
    assert len(summary['captures']) == 16
    assert authorization['status'] == 'authorized' and authorization['authorized_action'] == 'captures'
    assert authorization['exclusive_runner'] is True and authorization['other_work_idle'] is True
    for key, name in [('freeze_sha256', 'freeze.json'), ('driver_sha256', 'run.py'), ('plan_sha256', 'PLAN.json')]:
        assert authorization[key] == sha(OUT / name)
    assert summary['ack_sha256'] == launch['authorization_sha256'] == sha(OUT / 'AUTHORIZATION.json')
    assert launch['published_freeze_commit'] == authorization['published_commit'] == '7c8f5c0bdcbfdc32ce779ea2e6c36cb1b0378529'
    assert dt(authorization['authorized_utc']) < dt(launch['launched_utc']) <= dt(summary['started_utc'])
    relative = OUT.relative_to(ROOT)
    for label in ['iterator-native', 'iterator-san', 'iterator-profile']:
        flags = PLAN['flags'].copy()
        if label == 'iterator-san':
            flags[flags.index('-O3')] = '-O1'
            flags += ['-fsanitize=address,undefined', '-fno-sanitize-recover=all']
        if label == 'iterator-profile':
            flags += PLAN['profile_extra_flags']
        expected = ['clang', *flags, '-Isrc', '-Icompat', '-Ivendor/redis',
                    str(relative / 'iterator.c'),
                    *([str(relative / 'apple-sampler-bridge.c')] if label == 'iterator-profile' else []),
                    'src/zset_btree.c', 'compat/standalone.c', 'vendor/redis/siphash.c',
                    '-lm', '-o', 'scratch/m6-corrected-iterator-profile/' + label]
        assert command_map['build-' + label]['command'] == expected
    for name in ['freeze.json', 'run.py', 'PLAN.json', 'planned-commands.json']:
        blob = subprocess.run(['git', 'show', authorization['published_commit'] + ':' + str(relative / name)],
                              capture_output=True, check=True).stdout
        assert hashlib.sha256(blob).hexdigest() == sha(OUT / name)
    # Reproduce the exact capture inventory independently of the generated command list.
    canonical = [(n, contract, seed) for n in [100000, 1000000]
                 for contract in CONTRACTS for seed in [1, 2]]
    assert [(c['size'], c['contract'], c['seed']) for c in PLAN['captures']] == canonical
    captures = []
    capture_commands = []
    private_pc_files = []
    memory_reference = json.loads((OUT.parent / '012-contract-diagnostic/compare.json').read_text())['runs']
    for item, job, declared in zip(summary['captures'], planned['commands'], PLAN['captures']):
        n, seed = declared['size'], declared['seed']
        contract = CONTRACTS[declared['contract']]
        name = f'n{n}-{declared["contract"]}-s{seed}'
        expected_command = ['scratch/m6-corrected-iterator-profile/iterator-profile',
                            '--size', str(n), '--ops', str(declared['requested_items']), '--seed', str(seed),
                            '--member-bytes', '16', '--warmup-passes', str(declared['warmup_passes']),
                            '--direction', contract['direction'], '--mask', str(contract['mask']),
                            '--encoding', contract['encoding']]
        assert job == dict(name=name, command=expected_command, environment={'PROFILE_USEC': '1000'}, child_seconds_max=120)
        command = command_map[name]
        assert command['command'] == expected_command and command['environment_override'] == job['environment']
        assert command['logs'] == item['raw']
        assert (item['size'], item['contract'], item['seed']) == (n, declared['contract'], seed)
        assert all(item[key] == contract[key] for key in ['mask', 'direction', 'encoding'])
        assert item == json.loads((OUT / 'profiles' / (name + '.json')).read_text())
        paths = log_paths(item['raw'])
        row = read_row(paths['stdout'][1].read_text(), n, declared['requested_items'], seed,
                       contract, declared['warmup_passes'])
        for key in ['checksum', 'expected_checksum', 'construction_fingerprint']:
            assert item[key] == row[key]
        assert item['operations'] == int(row['operations']) and item['tree_bytes'] == int(row['tree_bytes'])
        comparable = [r for r in memory_reference if r['adapter'] == 'new' and r['seed'] == seed
                      and r['cell'] == f'n{n}-{declared["contract"]}'.removeprefix('n')]
        assert comparable and all(r['tree_bytes'] == item['tree_bytes'] for r in comparable)
        raw_stderr = paths['stderr'][1].read_text()
        public_stderr = paths['stderr'][0].read_text()
        private_pc_files.append(dict(path=item['raw']['stderr']['original_raw'],
                                     sha256=item['raw']['stderr']['original_raw_sha256']))
        pc_rows = [line.split(',') for line in raw_stderr.splitlines() if line.startswith('PC,')]
        headers = [line.split(',') for line in raw_stderr.splitlines() if line.startswith('PROFILE,')]
        assert len(headers) == 1
        header = headers[0]
        assert header == ['PROFILE', 'iterator-existing-profile-hooks', '1000', str(len(pc_rows)), '0']
        assert item['samples'] == len(pc_rows) >= PLAN['minimum_pcs'] == item['minimum_samples'] == 25
        assert item['sufficient'] is True and item['requested_interval_us'] == PLAN['requested_sample_interval_us'] == 1000
        symbols, bins = Counter(), Counter()
        for pc in pc_rows:
            assert len(pc) == 6
            module, address, base, symbol, symbol_start = pc[1:]
            address, start = int(address, 16), int(symbol_start, 16)
            offset = address - start if start != 0 and address >= start else None
            symbols[symbol] += 1
            bins[(Path(module).name, symbol, offset)] += 1
        expected_bins = [dict(module=key[0], symbol=key[1], offset_bytes=key[2], count=count)
                         for key, count in sorted(bins.items(), key=lambda p: (p[0][0], p[0][1], -1 if p[0][2] is None else p[0][2]))]
        assert dict(symbols) == item['symbols'] and expected_bins == item['pc_bins']
        assert sum(symbols.values()) == sum(x['count'] for x in expected_bins) == item['samples']
        assert not any(line.startswith('PC,') for line in public_stderr.splitlines())
        expected_public = [line for line in raw_stderr.splitlines() if not line.startswith('PC,')]
        assert public_stderr.splitlines() == expected_public + ['RAW_PC_ROWS_RETAINED_PRIVATELY,' + str(len(pc_rows))]
        assert item['counts_not_costs'] is True and item['emitted_elapsed_fields_unused'] is True
        assert item['scope'] == PLAN['sampling_scope']
        assert item['started_utc'] == command['started_utc'] and item['finished_utc'] == command['finished_utc']
        assert dt(summary['started_utc']) <= dt(item['started_utc']) < dt(item['finished_utc']) <= dt(summary['finished_utc'])
        captures.append(dict(name=name, samples=len(pc_rows), symbols=dict(symbols), pc_bins=expected_bins,
                             checksum=row['checksum'], construction_fingerprint=row['construction_fingerprint'],
                             tree_bytes=int(row['tree_bytes']), public_private_pc_mapping_verified=True,
                             applied_environment_override=command['environment_override']))
        capture_commands.append(command)
    assert [r['name'] for r in commands if r['command'][0] == 'scratch/m6-corrected-iterator-profile/iterator-profile'] == [r['name'] for r in capture_commands]
    assert all(dt(a['finished_utc']) <= dt(b['started_utc']) for a, b in zip(capture_commands, capture_commands[1:]))
    assert state['wall_seconds'] <= PLAN['budgets']['capture_phase_wall_seconds']
    assert dt(state['finished_utc']) <= dt(PLAN['budgets']['absolute_capture_stop_utc'])
    for copied in ['iterator.c', 'microbench.c', 'apple-sampler-bridge.c']:
        assert (OUT / copied).read_bytes() == (OUT.parent / '009-iterator-profile' / copied).read_bytes()
    # Static launcher and hook review: the corrected explicit override reaches Popen.
    driver = (OUT / 'run.py').read_text()
    assert 'start_new_session=True, env=env)' in driver
    assert "min(120,remaining),env=env)" in driver
    hook = (OUT / 'iterator.c').read_text()
    begin = hook.index('    sample_begin();')
    traversal = hook.index('uint64_t checksum=traverse(', begin)
    end = hook.index('    sample_end();', traversal)
    assert hook.index('uint64_t warmstart=') < begin < hook.index('const char *q0=', begin) < traversal
    assert traversal < hook.index('const char *q1=', traversal) < end < hook.index('serverAssert(checksum==expected*traversals', end)
    bridge = (OUT / 'apple-sampler-bridge.c').read_text()
    assert 'sample_start();' in bridge and 'sample_stop("iterator-existing-profile-hooks")' in bridge
    for control in frozen['sampler_prior_controls']:
        path = ROOT / control['file']
        assert sha(path) == control['sha256']
        pcs = [line for line in path.read_text().splitlines() if line.startswith('PC,')]
        assert len(pcs) == control['captured_pcs'] and all('sampler_probe' in line for line in pcs)
    validation = json.loads((OUT / 'validation.json').read_text())
    assert validation['status'] == 'PASS' and validation['native_sanitizer_runs'] == len(validation['checks']) == 8
    for check in validation['checks']:
        paths = log_paths(check['logs'])
        row = read_row(paths['stdout'][1].read_text(), 1000, 2003, 1, CONTRACTS[check['contract']], 1)
        assert int(row['operations']) == check['operations'] == 3000
        assert row['checksum'] == check['checksum'] and int(row['tree_bytes']) == check['tree_bytes']
    reused = json.loads((OUT / 'reused-tests.json').read_text())
    for path, digest in reused['source_identity'].items():
        assert sha(ROOT / path) == digest
    for path, digest in reused['native_sanitizer_evidence'].items():
        log = OUT.parent / path
        assert sha(log) == digest
        assert '43 passed' in re.sub(r'\x1b\[[0-9;]*m', '', log.read_text())
    launcher_fix = json.loads((OUT / 'LAUNCHER-FIX.json').read_text())
    assert launcher_fix['final_freeze_sha256'] == sha(OUT / 'freeze.json')
    assert launcher_fix['final_driver_sha256'] == sha(OUT / 'run.py')
    assert launcher_fix['prior_freeze_sha256'] == sha(OUT / 'freeze-before-launcher-fix.json')
    assert launcher_fix['profile_binary_executed'] is False and launcher_fix['no_binary_rebuild_or_semantic_check_rerun'] is True
    result = dict(status='PASS', participant='/root/followup_proposal_c', backend='GPT-6/Codex family',
        exact_model=None, token_usage=None, monetary_cost=None,
        independence='Independent raw-PC/metadata audit of A-authored profile driver and root-run captures. Region analysis is separate and was not read or changed.',
        captures_verified=16, sufficient_captures=16,
        sample_count_min=min(c['samples'] for c in captures), sample_count_max=max(c['samples'] for c in captures),
        frozen_inputs_verified=18, frozen_binaries_verified=3,
        command_records_verified=30, public_private_log_pairs_verified=60,
        planned_environment_applied={'PROFILE_USEC': '1000'},
        serial_capture_intervals_verified=16, all_children_recorded_reaped=True, capture_lock_absent=True,
        phase_wall_seconds=state['wall_seconds'],
        private_pc_file_identities=private_pc_files, captures=captures,
        independent_fixture_fingerprint_cases=fingerprint.cache_info().currsize,
        independent_checksum_cases=checksum.cache_info().currsize,
        memory_matches_same_fixture_corrected_012=True,
        sampling_scope_verified='Existing sample_begin/end enclose traversal plus QoS/CPU/thread-clock observations. Construction, initial verification, warmup, post-traversal semantic verification, output and teardown are outside.',
        elapsed_fields_used=False, old_009_samples_pooled=False,
        acknowledgement_provenance=dict(published_freeze_commit=authorization['published_commit'],
                                        local_published_blobs_match=True, remote_rechecked=False),
        interpretation='Sufficient baseline PC captures for their declared sampling scope; no cycles, cache, cost shares, frequency or elapsed-speed claim; no source optimization selected.',
        limitations=['Symbol/offset counts are reconstructed evidence, not unbiased dynamic cost or exact time attribution.',
                     'The1000us value is the requested/applied interval, not a measured delivery-rate guarantee.',
                     'Historical002 sampler controls are reused with unchanged sampler text; no new corrected-adapter calibration is claimed.',
                     'Recorded intervals establish seriality among retained children, not proof every host process was idle.',
                     'No live remote publication verification or fresh benchmark was performed.'],
        evidence_sha256={name: sha(OUT / name) for name in ['PLAN.json', 'freeze.json', 'AUTHORIZATION.json', 'LAUNCH.json', 'planned-commands.json', 'run.py', 'summary.json', 'capture-status.json', 'commands.jsonl', 'LAUNCHER-FIX.json']},
        audit_script_sha256=sha(Path(__file__)), finished_utc=datetime.now(timezone.utc).isoformat())
    (OUT / 'INDEPENDENT-AUDIT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'captures_verified', 'sufficient_captures',
                                           'sample_count_min', 'sample_count_max', 'phase_wall_seconds']}, indent=2))

if __name__ == '__main__':
    main()
