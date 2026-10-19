#!/usr/bin/env python3
"""Independently inspect completed corrected-adapter baseline evidence only."""
from collections import defaultdict
import csv
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
MATRIX = OUT / 'matrix'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def median(values):
    values = sorted(values)
    return (values[len(values)//2 - 1] + values[len(values)//2]) / 2

def close(left, right):
    assert abs(float(left) - float(right)) < 1e-8, (left, right)

def read_rows(path, size, requested, seed, member_bytes):
    rows = list(csv.DictReader(io.StringIO(path.read_text())))
    assert tuple(row['case'] for row in rows) == tuple(PLAN['cases'])
    for row in rows:
        assert int(row['size']) == size and int(row['requested_ops']) == requested
        assert int(row['seed']) == seed and int(row['member_bytes']) == member_bytes
        actual, elapsed = int(row['operations']), int(row['elapsed_ns'])
        assert actual > 0 and elapsed > 0 and int(row['tree_bytes']) > 0
        case = row['case']
        traversals = (requested + size - 1) // size
        if case in ('insert', 'delete'):
            assert actual == size
        elif case in ('iterate', 'scan'):
            assert int(row['traversals']) == traversals
            assert actual >= traversals * size
            if case == 'iterate':
                assert actual == traversals * size
        else:
            assert actual == requested
        if case == 'insert':
            assert int(row['checksum']) == 0 and int(row['warmup_passes']) == 0
        elif case == 'lookup-miss':
            assert int(row['checksum']) == 0
        elif case in ('update', 'delete'):
            assert int(row['checksum']) == actual
        elif case == 'iterate':
            assert int(row['checksum']) == traversals * size * (size - 1) // 2
        elif case in ('lookup-hit', 'rank') and requested % size == 0:
            assert int(row['checksum']) == (requested // size) * size * (size - 1) // 2
        if case != 'insert':
            assert int(row['warmup_passes']) == 1
        ratio = Fraction(elapsed, actual)
        assert abs(float(ratio) - float(row['ns_per_op'])) <= 0.00050001
    # Hit lookup and rank consume the same known shuffled member indices.
    by_case = {row['case']: row for row in rows}
    assert by_case['lookup-hit']['checksum'] == by_case['rank']['checksum']
    return rows

PLAN = json.loads((OUT / 'PLAN.json').read_text())

def main():
    manifest = json.loads((MATRIX / 'manifest.json').read_text())
    launch = json.loads((OUT / 'LAUNCH.json').read_text())
    reported = json.loads((MATRIX / 'summary.json').read_text())
    summary_csv = list(csv.DictReader(io.StringIO((MATRIX / 'summary.csv').read_text())))
    assert manifest['status'] == 'complete' and len(manifest['runs']) == 120
    assert PLAN['sizes'] == manifest['sizes'] == [100, 1000, 10000, 100000, 1000000]
    assert manifest['arguments']['ops'] == PLAN['requested_ops'] == 1000000
    assert manifest['arguments']['member_bytes'] == PLAN['member_bytes'] == 16
    assert manifest['commit'] == launch['commit'] == '7f299a5f5d2742141e5e9d9963e8f71e9a421466'
    expected_order = []
    sizes = PLAN['sizes']
    for block in range(6):
        order = sizes[block % len(sizes):] + sizes[:block % len(sizes)]
        for size in order:
            for step, label in enumerate('ABBA'):
                expected_order.append((block, 1 + block % 3, size, step, label))
    observed_order = [(r['block'], r['seed'], r['size'], r['step'], r['label'])
                      for r in manifest['runs']]
    assert observed_order == expected_order
    groups, row_count, logs = defaultdict(list), 0, {}
    for run in manifest['runs']:
        assert run['returncode'] == 0
        for key in ('csv', 'stderr'):
            path = MATRIX / run[key]
            assert sha(path) == run[key + '_sha256']
            logs[run[key]] = sha(path)
        rows = read_rows(MATRIX / run['csv'], run['size'], PLAN['requested_ops'],
                         run['seed'], PLAN['member_bytes'])
        expected_cmd = [PLAN['build_directory'] + '/btree-bench', '--size', str(run['size']),
                        '--ops', '1000000', '--member-bytes', '16', '--seed', str(run['seed'])]
        assert run['command'] == expected_cmd
        row_count += len(rows)
        for row in rows:
            groups[(run['size'], row['case'])].append(dict(row, block=run['block'],
                                                         step=run['step'], label=run['label']))
    assert len(logs) == 240
    assert len(list((MATRIX / 'raw').glob('*.csv'))) == 120
    assert len(list((MATRIX / 'raw').glob('*.stderr'))) == 120
    assert row_count == 960 and len(groups) == len(reported) == len(summary_csv) == 40
    saved = {(r['size'], r['case']): r for r in reported}
    saved_csv = {(int(r['size']), r['case']): r for r in summary_csv}
    computed = []
    for size in sizes:
        for case in PLAN['cases']:
            rows = groups[(size, case)]
            assert len(rows) == 24
            effects, memory = [], []
            for block in range(6):
                paired = sorted([r for r in rows if r['block'] == block], key=lambda r: r['step'])
                assert ''.join(r['label'] for r in paired) == 'ABBA'
                assert len({(r['operations'], r['checksum'], r['seed']) for r in paired}) == 1
                assert len({r['tree_bytes'] for r in paired}) == 1
                times = [Fraction(int(r['elapsed_ns']), int(r['operations'])) for r in paired]
                effects.append(100 * ((times[1] + times[2]) / (times[0] + times[3]) - 1))
                owned = [Fraction(r['tree_bytes']) for r in paired]
                memory.append(100 * ((owned[1] + owned[2]) / (owned[0] + owned[3]) - 1))
            values = [Fraction(int(r['elapsed_ns']), int(r['operations'])) for r in rows]
            shortest = Fraction(min(int(r['elapsed_ns']) for r in rows), 1000000)
            numbers = dict(observations=24, median_ns_op=median(values), min_ns_op=min(values),
                           max_ns_op=max(values), aa_max_abs_pct=max(map(abs, effects)),
                           shortest_timed_ms=shortest,
                           tree_bytes_median=median([Fraction(r['tree_bytes']) for r in rows]))
            for key, value in numbers.items():
                close(value, saved[(size, case)][key])
                close(value, saved_csv[(size, case)][key])
            for exact, value in zip(effects, saved[(size, case)]['aa_block_effects_pct']):
                close(exact, value)
            computed.append(dict(size=size, case=case, **{k: float(v) for k, v in numbers.items()},
                effects_pct=list(map(float, effects)), exact_effect_fractions=list(map(str, effects)),
                memory_effects_pct=list(map(float, memory)),
                qualified=max(map(abs, effects)) <= 1 and shortest >= 10,
                short_window=shortest < 10))
    assert [r['name'] for r in manifest['validation']] == [
        'release-build-check', 'sanitize-build-check',
        *['sanitize-size-' + str(n) for n in sizes]]
    validations = []
    for record in manifest['validation']:
        assert record['returncode'] == 0
        name = record['name']
        stdout, stderr = MATRIX / (name + '.stdout'), MATRIX / (name + '.stderr')
        if name.endswith('build-check'):
            text = re.sub(r'\x1b\[[0-9;]*m', '', stdout.read_text())
            assert '43 passed' in text and '0 failed, 43 total' in text
        else:
            size = int(name.rsplit('-', 1)[1])
            read_rows(stdout, size, 2 * size + 1, 101, 16)
        validations.append(dict(name=name, returncode=0, stdout_sha256=sha(stdout),
                                stderr_sha256=sha(stderr),
                                provenance='Recorded return code plus current retained output; original manifest does not store validation-log hashes.'))
    source_checks, commit_checks = {}, {}
    for path, expected in manifest['source_hashes'].items():
        source_checks[path] = sha(ROOT / path) == expected
        blob = subprocess.run(['git', 'show', manifest['commit'] + ':' + path],
                              capture_output=True, check=True).stdout
        commit_checks[path] = hashlib.sha256(blob).hexdigest() == expected
    assert all(source_checks.values()) and all(commit_checks.values())
    previous = json.loads((OUT.parent / '010-assertion-contract-review/review.json').read_text())
    for path, expected in PLAN['adapter'].items():
        assert sha(ROOT / path) == expected == previous['private_sources']['noreturn'][path]
    assert sha(ROOT / 'src/zset_btree.c') == PLAN['source_c_sha256']
    assert sha(ROOT / 'src/zset_btree.h') == PLAN['source_h_sha256']
    assert sha(ROOT / PLAN['build_directory'] / 'btree-bench') == manifest['binary_sha256'] == manifest['binary_sha256_after']
    checked = datetime.fromisoformat(launch['fix_acknowledgement']['checked_utc'])
    launched = datetime.fromisoformat(launch['utc'])
    began = datetime.fromisoformat(manifest['started_utc'])
    ended = datetime.fromisoformat(manifest['finished_utc'])
    assert checked < launched <= began < ended <= datetime.fromisoformat(PLAN['budgets']['absolute_stop_utc'])
    assert manifest['timing_seconds'] <= PLAN['budgets']['wall_seconds'] == 600
    result = dict(status='PASS', reviewer='/root/followup_proposal_c',
        backend='GPT-6/Codex family', exact_model=None, token_usage=None, monetary_cost=None,
        independence='Independent arithmetic audit of root-run baseline; reviewer authored the earlier private adapter review, not an independent second semantic review of that adapter.',
        raw_csv_files=120, raw_stderr_files=120, raw_rows=row_count, cells=40,
        qualified_cells=sum(r['qualified'] for r in computed), short_cells=sum(r['short_window'] for r in computed),
        results=computed, validation_results=validations, source_hash_checks=source_checks,
        source_hashes_match_published_fix_commit=commit_checks, adapter_matches_reviewed_private_patch=True,
        binary_sha256=manifest['binary_sha256'], same_binary_before_after_and_now=True,
        timing_wall_seconds=manifest['timing_seconds'],
        sum_raw_operation_timer_seconds=sum(int(r['elapsed_ns']) for rows in groups.values() for r in rows) / 1e9,
        total_manifest_elapsed_wall_seconds=(ended - began).total_seconds(),
        limits=['The120 synchronous subprocess invocations and listed order support serial driver execution, but no per-child UTC start/end timestamps were captured. No interval/nonoverlap certificate is claimed.',
                'The160.052970917s value is recorded aggregate wall time for the timing subprocess loop, including setup/warmup/checks/overhead; it cannot be reconstructed from individual operation timers.',
                'Validation outputs have current audit hashes, but those log hashes were not frozen in the original manifest.',
                'This is a corrected-adapter baseline, not an old-versus-new adapter speed comparison or a tree optimization. Old qualification does not transfer.',
                'Frequency/DVFS/exact residency/PMU remain unknown; CPU endpoints do not establish within-window residency.'],
        decision='Baseline coverage and data audit pass;35/40 cells remain unqualified, source optimization NONE.',
        evidence_sha256={name: sha(OUT / name) for name in ['PLAN.json', 'LAUNCH.json', 'matrix/manifest.json', 'matrix/summary.json', 'matrix/summary.csv']},
        raw_hashes=logs, audit_script_sha256=sha(Path(__file__)),
        finished_utc=datetime.now(timezone.utc).isoformat())
    (OUT / 'INDEPENDENT-AUDIT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['status', 'raw_csv_files', 'raw_rows', 'qualified_cells', 'short_cells',
                                           'timing_wall_seconds', 'sum_raw_operation_timer_seconds']}, indent=2))

if __name__ == '__main__':
    main()
