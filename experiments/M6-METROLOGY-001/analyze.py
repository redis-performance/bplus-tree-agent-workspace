#!/usr/bin/env python3
"""Read sealed EXP-009 rows only; never launches native work or edits its inputs."""
import csv
import hashlib
import io
import json
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = ROOT / 'experiments/EXP-009'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    inputs = json.loads((HERE / 'inputs.json').read_text())['files']
    for name, expected in inputs.items():
        assert sha(ROOT / name) == expected, name
    seals = {}
    for name in ['input-manifest-v2.json', 'timing-manifest.json']:
        manifest = json.loads((OLD / name).read_text())['files_sha256']
        for relative, expected in manifest.items():
            assert sha(ROOT / relative) == expected, relative
        seals[name] = {'sha256': sha(OLD / name), 'verified_entries': len(manifest)}
    streams = json.loads((OLD / 'bench-results/aa/public-raw-manifest.json').read_text())['streams']
    assert len(streams) == 96
    for stream in streams:
        path = ROOT / stream['public']
        assert sha(path) == stream['sha256'] and path.stat().st_size == stream['bytes'], path
        inputs[stream['public']] = stream['sha256']
    for name in ['harness/lookup.c', 'bench-results/build/commands.jsonl', 'host.json']:
        path = OLD / name
        inputs[str(path.relative_to(ROOT))] = sha(path)
    schedule = json.loads((OLD / 'bench-results/calibrate/aa-schedule.json').read_text())
    commands = [json.loads(line) for line in (OLD / 'bench-results/aa/commands.jsonl').read_text().splitlines()]
    assert len(schedule) == len(commands) == 48
    rows = []
    for index, (scheduled, command) in enumerate(zip(schedule, commands)):
        assert scheduled['index'] == index and command['name'] == f'{index:03}'
        assert command['returncode'] == 0 and not command['timed_out']
        assert all(command[key] for key in ['child_reaped', 'owned_group_empty', 'release_safe'])
        path = OLD / f'bench-results/aa/raw/{index:03}.stdout'
        assert sha(path) == command['raw']['stdout']['sha256']
        parsed = list(csv.DictReader(io.StringIO(path.read_text())))
        assert len(parsed) == 1
        raw = parsed[0]
        for key in ['size', 'seed', 'operations', 'member_bytes', 'warmup_passes']:
            assert int(raw[key]) == scheduled[key]
        assert raw['case'] == scheduled['case']
        wall, thread = int(raw['elapsed_ns']), int(raw['thread_elapsed_ns'])
        assert wall > 0 and thread > 0
        rows.append({**scheduled, **{key: int(raw[key]) for key in [
            'elapsed_ns', 'thread_elapsed_ns', 'warmup_elapsed_ns', 'cpu_start', 'cpu_end', 'tree_bytes', 'checksum']},
            'residual_ns': wall - thread,
            'qos_effective': raw['qos_effective'],
            'command_started_utc': command['started_utc'],
            'command_finished_utc': command['finished_utc']})
    original_blocks = json.loads((OLD / 'bench-results/aa/summary.json').read_text())['blocks']
    blocks = []
    for size in [100000, 1000000]:
        for block in range(6):
            group = sorted([row for row in rows if row['size'] == size and row['block'] == block], key=lambda r: r['position'])
            assert len(group) == 4 and [r['side'] for r in group] == list('ABBA')
            for key in ['operations', 'checksum', 'tree_bytes', 'seed']:
                assert len({r[key] for r in group}) == 1
            aw, bw = (sum(group[i]['elapsed_ns'] for i in pair) for pair in [(0, 3), (1, 2)])
            at, bt = (sum(group[i]['thread_elapsed_ns'] for i in pair) for pair in [(0, 3), (1, 2)])
            ar, br = aw - at, bw - bt
            assert bw - aw == (bt - at) + (br - ar)
            wall_ok = abs(bw - aw) * 100 <= aw
            thread_ok = abs(bt - at) * 100 <= at
            old = next(b for b in original_blocks if b['size'] == size and b['block'] == block)
            assert old['baseline_elapsed_sum'] == aw and old['paired_elapsed_sum'] == bw
            assert old['qualified'] == wall_ok
            blocks.append({'size': size, 'block': block, 'seed': group[0]['seed'],
                'row_indices': [r['index'] for r in group],
                'wall_A_ns': aw, 'wall_B_ns': bw, 'thread_A_ns': at, 'thread_B_ns': bt,
                'residual_A_ns': ar, 'residual_B_ns': br,
                'wall_contrast_ns': bw - aw, 'thread_contrast_ns': bt - at,
                'residual_contrast_ns': br - ar,
                'wall_effect_percent': 100 * (bw - aw) / aw,
                'thread_effect_percent': 100 * (bt - at) / at,
                'thread_contribution_wall_denominator_pp': 100 * (bt - at) / aw,
                'residual_contribution_wall_denominator_pp': 100 * (br - ar) / aw,
                'original_wall_qualified': wall_ok, 'diagnostic_thread_within_1pct': thread_ok})
    cells = []
    for size in [100000, 1000000]:
        group = [r for r in rows if r['size'] == size]
        cell_blocks = [b for b in blocks if b['size'] == size]
        cells.append({'size': size, 'rows': len(group),
            'wall_pass_blocks': sum(b['original_wall_qualified'] for b in cell_blocks),
            'thread_pass_blocks_diagnostic_only': sum(b['diagnostic_thread_within_1pct'] for b in cell_blocks),
            'residual_min_ns': min(r['residual_ns'] for r in group),
            'residual_max_ns': max(r['residual_ns'] for r in group),
            'residual_median_ns': median(r['residual_ns'] for r in group),
            'cpu_endpoint_pairs': sorted({(r['cpu_start'], r['cpu_end']) for r in group}),
            'different_cpu_endpoints_rows': sum(r['cpu_start'] != r['cpu_end'] for r in group)})
    assert [c['wall_pass_blocks'] for c in cells] == [6, 3]
    assert [c['thread_pass_blocks_diagnostic_only'] for c in cells] == [6, 3]
    result = {'status': 'OFFLINE_DIAGNOSTIC_COMPLETE',
        'interpretation': 'Observed wall/thread differences alone do not account for all three failed 1M contrasts; exact off-CPU attribution and mechanism remain unresolved.',
        'limits': ['Thread clock brackets wall clock rather than the exact same interval; wrapper cost has no measured bound.',
            'Residual is not exact off-CPU time. Thread CPU time is not cycles or fixed-frequency work.',
            'CPU endpoints are snapshots, not continuous migration or core-class observations.',
            'Thread contrasts are diagnostic and never substitute the frozen wall acceptance clock.',
            'No native experiment, source optimization, acceptance or cross-host inference.'],
        'input_sha256': inputs, 'preserved_frozen_seals': seals, 'script_sha256': sha(Path(__file__)),
        'cells': cells, 'blocks': blocks, 'rows': rows}
    (HERE / 'analysis.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'verified_streams': len(streams), 'cells': cells}))


if __name__ == '__main__':
    main()
