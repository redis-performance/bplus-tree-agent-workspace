#!/usr/bin/env python3
"""Read-only independent reconstruction of the matched adapter diagnostic."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
import csv
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
CELLS = {cell['id']: cell for cell in PLAN['cells']}
MASK64 = (1 << 64) - 1

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dt(value):
    return datetime.fromisoformat(value)

def close(left, right):
    assert abs(float(left) - float(right)) < 1e-8, (left, right)

def median(values):
    ordered = sorted(values)
    return (ordered[len(ordered)//2 - 1] + ordered[len(ordered)//2]) / 2

@lru_cache(None)
def fingerprint(size, seed):
    """Independent Python SplitMix64/shuffle/FNV reconstruction of the fixture."""
    state = seed
    def random_word():
        nonlocal state
        state = (state + 0x9e3779b97f4a7c15) & MASK64
        z = state
        z = ((z ^ (z >> 30)) * 0xbf58476d1ce4e5b9) & MASK64
        z = ((z ^ (z >> 27)) * 0x94d049bb133111eb) & MASK64
        return z ^ (z >> 31)
    for _ in range(16):
        random_word()
    order = list(range(size))
    for end in range(size, 1, -1):
        index = random_word() % end
        order[end - 1], order[index] = order[index], order[end - 1]
    value = 14695981039346656037
    for member_id in order:
        value = ((value ^ member_id) * 1099511628211) & MASK64
    return value

@lru_cache(None)
def checksum(size, encoding, output_mask, requested):
    """Sum independently known item count/member byte/length/exact score bits."""
    value = size
    if output_mask & 1:
        value += sum(i & 255 for i in range(size))
    if output_mask & 2:
        value += size * PLAN['member_bytes']
    if output_mask & 4:
        for i in range(size):
            score = float(i - size // 2) + (0.25 if encoding == 'fraction' else 0.0)
            value += struct.unpack('<Q', struct.pack('<d', score))[0]
    traversals = (requested + size - 1) // size
    return (value * traversals) & MASK64

def verify_logs(logs):
    for item in logs.values():
        assert sha(OUT / item['file']) == item['sha256'], item['file']
        raw = item['original_raw']
        assert raw.startswith('ignored ')
        assert sha(ROOT / raw[len('ignored '):]) == item['original_raw_sha256']

def raw_row(run):
    verify_logs(run['logs'])
    rows = list(csv.DictReader(io.StringIO((OUT / run['logs']['stdout']['file']).read_text())))
    assert len(rows) == 1 and rows[0] == run['csv']
    row = rows[0]
    cell = CELLS[run['cell']]
    n = cell['size']
    assert row['case'] == 'iterator-modes'
    assert int(row['size']) == n and int(row['seed']) == run['seed']
    assert int(row['requested_ops']) == PLAN['ops']
    operations = ((PLAN['ops'] + n - 1) // n) * n
    assert int(row['operations']) == run['operations'] == operations
    assert int(row['traversals']) == operations // n
    assert int(row['member_bytes']) == PLAN['member_bytes']
    assert int(row['warmup_passes']) == PLAN['warmup_passes']
    assert row['direction'] == cell['direction'] and int(row['mask']) == cell['mask']
    assert row['encoding'] == cell['encoding']
    assert int(row['checksum']) == int(row['expected_checksum']) == checksum(n, cell['encoding'], cell['mask'], PLAN['ops'])
    assert row['checksum'] == run['checksum']
    assert int(row['construction_fingerprint']) == fingerprint(n, run['seed'])
    assert int(row['elapsed_ns']) == run['elapsed_ns'] > 0
    assert int(row['tree_bytes']) == run['tree_bytes'] > 0
    close(Fraction(run['elapsed_ns'], operations), run['ns_op'])
    return row

def phase_audit(document, name, controls):
    assert document['status'] == 'complete' and document['all_children_reaped'] is True
    assert document['unknown_timed_work_on_failure'] is False
    assert document['source_optimization'] == 'NONE'
    runs = document['runs']
    assert len(runs) == (384 if name == 'aa' else 192)
    assert [json.loads(line) for line in (OUT / (name + '-runs.jsonl')).read_text().splitlines()] == runs
    state = json.loads((OUT / (name + '-state.json')).read_text())
    assert state['status'] == 'complete' and state['completed_rows'] == len(runs)
    assert state['all_children_reaped'] is True
    close(state['timing_seconds'], document['timing_seconds'])
    actual_order = []
    for run in runs:
        raw_row(run)
        assert run['phase'] == name and run['seed'] == PLAN['seeds'][run['block']]
        expected_adapter = run['comparison'] if name == 'aa' else ('old' if run['label'] == 'A' else 'new')
        assert run['adapter'] == expected_adapter
        actual_order.append((run['block'], run['cell'], run['comparison'], run['step'], run['label']))
    expected_order = []
    cells = list(CELLS)
    for block in range(6):
        order = cells[block % len(cells):] + cells[:block % len(cells)]
        if block % 2:
            order.reverse()
        for cell in order:
            comparisons = (['old', 'new'] if block % 2 == 0 else ['new', 'old']) if name == 'aa' else ['old-vs-new']
            for comparison in comparisons:
                expected_order.extend((block, cell, comparison, step, label) for step, label in enumerate('ABBA'))
    assert actual_order == expected_order
    reported = {(r['comparison'], r['cell']): r for r in document['results']}
    results = []
    comparisons = ['old', 'new'] if name == 'aa' else ['old-vs-new']
    for comparison in comparisons:
        for cell in CELLS:
            rows = [r for r in runs if r['comparison'] == comparison and r['cell'] == cell]
            assert len(rows) == 24
            effects, memories = [], []
            for block in range(6):
                paired = sorted([r for r in rows if r['block'] == block], key=lambda r: r['step'])
                assert len(paired) == 4 and ''.join(r['label'] for r in paired) == 'ABBA'
                assert len({(r['operations'], r['checksum'], r['tree_bytes'], r['csv']['construction_fingerprint']) for r in paired}) == 1
                numerator = paired[1]['elapsed_ns'] + paired[2]['elapsed_ns']
                denominator = paired[0]['elapsed_ns'] + paired[3]['elapsed_ns']
                effects.append(100 * (Fraction(numerator, denominator) - 1))
                memories.append(100 * (Fraction(paired[1]['tree_bytes'] + paired[2]['tree_bytes'],
                                                paired[0]['tree_bytes'] + paired[3]['tree_bytes']) - 1))
            shortest = Fraction(min(r['elapsed_ns'] for r in rows), 1000000)
            qualified = all(abs(e) <= 1 for e in effects) and shortest >= 10 if name == 'aa' else None
            both = None if name == 'aa' else all(controls[(a, cell)] for a in ['old', 'new'])
            r = reported[(comparison, cell)]
            assert r['qualified'] == qualified and r['both_adapter_controls_qualified'] == both
            assert r['all_comparison_windows_minimum_met'] == (shortest >= 10)
            if name == 'compare':
                assert r['interpretation'].startswith('conditional:') == (not both or shortest < 10)
            for a, b in zip(effects, r['effects_pct']):
                close(a, b)
            for a, b in zip(memories, r['memory_effects_pct']):
                close(a, b)
            for field, exact in [('median_pct', median(effects)), ('observed_min_pct', min(effects)),
                                 ('observed_max_pct', max(effects)), ('shortest_window_ms', shortest)]:
                close(r[field], exact)
            results.append(dict(comparison=comparison, cell=cell, effects_pct=list(map(float, effects)),
                exact_effect_fractions=list(map(str, effects)), median_pct=float(median(effects)),
                min_pct=float(min(effects)), max_pct=float(max(effects)),
                shortest_window_ms=float(shortest), qualified=qualified,
                both_adapter_controls_qualified=both,
                memory_effects_pct=list(map(float, memories))))
    total = Fraction(sum(r['elapsed_ns'] for r in runs), 1000000000)
    close(total, document['timing_seconds'])
    assert total <= PLAN['budgets']['timed_seconds_per_phase']
    assert document['wall_seconds'] <= PLAN['budgets']['wall_seconds_per_phase']
    assert dt(document['finished_utc']) <= dt(PLAN['budgets']['absolute_stop_utc'])
    for run in runs:
        assert dt(document['started_utc']) <= dt(run['started_utc']) < dt(run['finished_utc']) <= dt(document['finished_utc'])
    assert all(dt(a['finished_utc']) <= dt(b['started_utc']) for a, b in zip(runs, runs[1:]))
    return results

def published_blob(commit, path):
    return subprocess.run(['git', 'show', commit + ':' + str(path)], capture_output=True, check=True).stdout

def main():
    aa = json.loads((OUT / 'aa.json').read_text())
    comparison = json.loads((OUT / 'compare.json').read_text())
    controls_result = phase_audit(aa, 'aa', {})
    controls = {(r['comparison'], r['cell']): r['qualified'] for r in controls_result}
    compare_result = phase_audit(comparison, 'compare', controls)
    measured_rows = aa['runs'] + comparison['runs']
    assert dt(aa['finished_utc']) < dt(comparison['started_utc'])
    assert len({r['name'] for r in measured_rows}) == 576
    commands = [json.loads(line) for line in (OUT / 'commands.jsonl').read_text().splitlines()]
    assert len({r['name'] for r in commands}) == len(commands)
    command_map = {r['name']: r for r in commands}
    for command in commands:
        verify_logs(command['logs'])
    measured_commands = []
    for run in measured_rows:
        command = command_map[run['name']]
        assert command['returncode'] == 0 and command['timed_out'] is False
        assert command['process_reaped'] is True
        assert command['logs'] == run['logs']
        assert command['started_utc'] == run['started_utc'] and command['finished_utc'] == run['finished_utc']
        assert 0 < command['timeout_seconds'] <= PLAN['budgets']['child_seconds']
        assert command['wall_seconds'] <= command['timeout_seconds']
        assert run['elapsed_ns'] / 1e9 <= command['wall_seconds']
        cell = CELLS[run['cell']]
        expected = ['scratch/m6-contract-diagnostic/' + run['adapter'] + '/iterator',
                    '--size', str(cell['size']), '--ops', str(PLAN['ops']), '--seed', str(run['seed']),
                    '--member-bytes', str(PLAN['member_bytes']), '--warmup-passes', str(PLAN['warmup_passes']),
                    '--direction', cell['direction'], '--mask', str(cell['mask']), '--encoding', cell['encoding']]
        assert command['command'] == expected
        measured_commands.append(command)
    assert all(dt(a['finished_utc']) <= dt(b['started_utc']) for a, b in zip(measured_commands, measured_commands[1:]))
    frozen = json.loads((OUT / 'freeze.json').read_text())
    hashes = {**frozen['files_sha256'], **frozen['binaries_sha256']}
    assert all(sha(ROOT / path) == expected for path, expected in hashes.items())
    authorization = json.loads((OUT / 'AUTHORIZATION.json').read_text())
    assert authorization['status'] == 'authorized' and authorization['exclusive_runner'] is True
    for key, name in [('freeze_sha256', 'freeze.json'), ('driver_sha256', 'driver.py'), ('plan_sha256', 'PLAN.json')]:
        assert authorization[key] == sha(OUT / name)
    assert any(r['reviewer'] == '/root' and r['status'] == 'PASS' for r in authorization['reviews'])
    assert any(r['reviewer'] != '/root' and r['status'] == 'PASS' for r in authorization['reviews'])
    for phase in [aa, comparison]:
        assert phase['authorization']['sha256'] == sha(OUT / 'AUTHORIZATION.json')
        assert phase['authorization']['evidence'] == authorization
        assert dt(authorization['authorized_utc']) < dt(phase['started_utc'])
    relative = OUT.relative_to(ROOT)
    commit = authorization['published_commit']
    for name in ['freeze.json', 'driver.py', 'PLAN.json']:
        assert hashlib.sha256(published_blob(commit, relative / name)).hexdigest() == sha(OUT / name)
    launch_aa = json.loads((OUT / 'AA-LAUNCH.json').read_text())
    launch_compare = json.loads((OUT / 'COMPARE-LAUNCH.json').read_text())
    assert launch_aa['published_freeze_commit'] == commit
    assert launch_aa['authorization_sha256'] == sha(OUT / 'AUTHORIZATION.json')
    assert dt(authorization['authorized_utc']) <= dt(launch_aa['launched_utc']) <= dt(aa['started_utc'])
    assert dt(aa['finished_utc']) < dt(launch_compare['launched_utc']) <= dt(comparison['started_utc'])
    assert hashlib.sha256(published_blob(launch_compare['aa_published_commit'], relative / 'aa.json')).hexdigest() == sha(OUT / 'aa.json')
    assert not (ROOT / 'scratch/m6-contract-diagnostic/MEASUREMENT.lock').exists()
    # Inspect sealed pre-measurement correctness without executing tests again.
    validation = json.loads((OUT / 'validation.json').read_text())
    assert validation['status'] == 'PASS' and len(validation['runs']) == 16
    for item in validation['runs']:
        verify_logs(item['logs'])
        row = list(csv.DictReader(io.StringIO((OUT / item['logs']['stdout']['file']).read_text())))[0]
        cell = next(c for c in CELLS.values() if c['contract'] == item['contract'])
        assert int(row['operations']) == item['operations'] == 3000
        assert int(row['checksum']) == int(row['expected_checksum']) == checksum(1000, cell['encoding'], cell['mask'], 2003)
        assert int(row['construction_fingerprint']) == fingerprint(1000, 1)
    reused = json.loads((OUT / 'reused-tests.json').read_text())
    for adapter, info in reused.items():
        for path, digest in info['source_identity'].items():
            actual = ROOT / path
            if path.startswith('compat/') and adapter == 'old':
                actual = ROOT / PLAN['adapters']['old'] / Path(path).name
            assert sha(actual) == digest
        for path, digest in info['native_sanitizer_evidence'].items():
            log = OUT.parent / path
            assert sha(log) == digest
            assert '43 passed' in re.sub(r'\x1b\[[0-9;]*m', '', log.read_text())
    curation = json.loads((OUT / 'public-metadata-curation.json').read_text())
    assert sha(ROOT / curation['raw_journal_preserved'][len('ignored '):]) == curation['raw_journal_sha256']
    assert curation['measured_phases_started'] is False and dt(curation['utc']) < dt(aa['started_utc'])
    driver_checks = json.loads((OUT / 'driver-validation.json').read_text())
    assert driver_checks['status'] == 'PASS' and driver_checks['all_children_stopped'] is True
    expected_cleanup = {'driver-timeout-control', 'driver-interrupt-control', 'driver-race-control'}
    nonzero = [r for r in commands if r['returncode'] != 0 or r['timed_out']]
    assert {r['name'] for r in nonzero} == expected_cleanup
    assert all(r['returncode'] == -9 and r['process_reaped'] is True and
               dt(r['finished_utc']) < dt(aa['started_utc']) for r in nonzero)
    descriptive = json.loads((OUT / 'ENDPOINT-CENSUS.json').read_text())
    endpoint_results = {}
    for name, phase in [('aa', aa), ('compare', comparison)]:
        rows = [r['csv'] for r in phase['runs']]
        ratios = [100 * (Fraction(int(r['elapsed_ns']), int(r['thread_elapsed_ns'])) - 1)
                  for r in rows]
        values = dict(rows=len(rows), cpu_start=dict(Counter(r['cpu_start'] for r in rows)),
                      cpu_end=dict(Counter(r['cpu_end'] for r in rows)),
                      different_cpu_endpoints=sum(r['cpu_start'] != r['cpu_end'] for r in rows),
                      reported_qos_start=dict(Counter(r['qos_reported_start'] for r in rows)),
                      effective_qos=dict(Counter(r['qos_effective'] for r in rows)))
        saved = descriptive['phases'][name]
        for key, value in values.items():
            assert saved[key] == value
        inflation = dict(minimum=min(ratios), median=median(ratios), maximum=max(ratios))
        for key, value in inflation.items():
            close(value, saved['wall_over_thread_pct'][key])
        values['wall_over_thread_pct'] = {k: float(v) for k, v in inflation.items()}
        endpoint_results[name] = values
    joint = sum(all(controls[(a, cell)] for a in ['old', 'new']) for cell in CELLS)
    assert joint == 0 and all(not r['both_adapter_controls_qualified'] for r in compare_result)
    result = dict(status='PASS', participant='/root/followup_proposal_c', backend='GPT-6/Codex family',
        exact_model=None, token_usage=None, monetary_cost=None,
        independence='Independent evidence/arithmetic audit of B-authored driver and root-run phases; reviewer authored earlier private adapter contract review, not a second semantic reviewer of that adapter.',
        rows=dict(aa=384, comparison=192, total=576), command_records=len(commands),
        measured_command_intervals_verified=576, public_and_private_command_log_pairs_verified=len(commands) * 2,
        frozen_artifacts_verified=len(hashes),
        controls_qualified={adapter: sum(controls[(adapter, cell)] for cell in CELLS) for adapter in ['old', 'new']},
        joint_qualified_cells=joint, conditional_comparisons=8,
        aa=controls_result, comparison=compare_result,
        timed_seconds=dict(aa=aa['timing_seconds'], comparison=comparison['timing_seconds']),
        wall_seconds=dict(aa=aa['wall_seconds'], comparison=comparison['wall_seconds']),
        all_children_recorded_reaped=True, measurement_lock_absent=True,
        independent_fixture_fingerprints={f'n{n}-s{seed}': fingerprint(n, seed)
                                          for n, seeds in [(1000, [1]), (100000, [1, 2, 3]),
                                                           (1000000, [1, 2, 3])] for seed in seeds},
        fingerprint_reconstruction_cases=fingerprint.cache_info().currsize,
        checksum_reconstruction_cases=checksum.cache_info().currsize,
        acknowledgement_provenance=dict(frozen_publication_commit=commit, aa_publication_commit=launch_compare['aa_published_commit'],
                                        local_published_blobs_match=True, remote_rechecked=False),
        nonzero_preparation_command_results=[dict(name=r['name'], returncode=r['returncode'], timed_out=r['timed_out']) for r in commands if r['returncode'] != 0 or r['timed_out']],
        nonzero_preparation_results_are_expected_cleanup_controls=True,
        descriptive_endpoint_census=endpoint_results,
        endpoint_census_is_posthoc_not_a_gate=True,
        interpretation='All eight matched adapter effects remain conditional because no cell qualifies both adapter controls. Harness-only diagnostic; no source candidate, acceptance or optimization population.',
        limitations=['Recorded intervals establish seriality among retained measured children, not proof that every process on the machine was idle.',
                     'ACK/local commit contents establish retained publication provenance; no live remote verification was performed.',
                     'No fresh timing confirmation, throughput guard expansion or hardware-counter attribution is supplied by this audit.',
                     'Frequency/DVFS/core residency/effective QoS/PMU remain unknown.'],
        evidence_sha256={name: sha(OUT / name) for name in ['PLAN.json', 'freeze.json', 'AUTHORIZATION.json', 'AA-LAUNCH.json', 'COMPARE-LAUNCH.json', 'aa.json', 'compare.json', 'aa-state.json', 'compare-state.json', 'commands.jsonl', 'aa-runs.jsonl', 'compare-runs.jsonl', 'ENDPOINT-CENSUS.json', 'driver-validation.json', 'public-metadata-curation.json']},
        audit_script_sha256=sha(Path(__file__)), finished_utc=datetime.now(timezone.utc).isoformat())
    (OUT / 'INDEPENDENT-AUDIT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'rows', 'command_records', 'controls_qualified',
                                           'joint_qualified_cells', 'conditional_comparisons']}, indent=2))

if __name__ == '__main__':
    main()
