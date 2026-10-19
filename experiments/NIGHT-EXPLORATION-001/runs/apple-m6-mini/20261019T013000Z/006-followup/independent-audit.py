#!/usr/bin/env python3
"""Read retained evidence; independently reconstruct exact paired effects.

Does not import the campaign driver, execute binaries, or collect measurements.
"""
from collections import Counter
import csv
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path

ROOT = Path.cwd()
OUT = Path(__file__).resolve().parent
PLAN = json.loads((OUT / 'PLAN.json').read_text())
CELLS = {c['id']: c for c in PLAN['cells']}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def ceil(value):
    return -(-value.numerator // value.denominator)

def close(a, b):
    assert abs(float(a) - float(b)) < 1e-9, (a, b)

def median(values):
    ordered = sorted(values)
    return (ordered[2] + ordered[3]) / 2

def timestamp(value):
    return datetime.fromisoformat(value)

def reconstruct(run):
    cell = CELLS[run['cell']]
    path = OUT / run['file']
    assert sha(path) == run['sha256'], ('CSV hash', run['name'])
    rows = list(csv.DictReader(io.StringIO(path.read_text())))
    assert len(rows) == 1
    raw = rows[0]
    assert raw == run['csv'], ('CSV metadata', run['name'])
    count = int(raw.get('operations', raw.get('ops', 0)))
    elapsed = int(raw['elapsed_ns'])
    assert count == run['operations'] and elapsed == run['elapsed_ns']
    assert count > 0 and elapsed > 0
    assert int(raw['size']) == cell['size'] and raw['case'] == cell['case']
    assert int(raw['seed']) == run['seed'] and raw['checksum'] == run['checksum']
    if 'member_bytes' in raw:
        assert int(raw['member_bytes']) == cell['member_bytes']
    requested = run['requested_ops']
    if 'requested_ops' in raw:
        assert int(raw['requested_ops']) == requested
    if cell['referee'] == 'standard':
        if cell['case'] in ('insert', 'delete'):
            assert int(raw['replicas']) == run['replicas']
            assert count == cell['size'] * run['replicas']
            assert int(raw['total_operations']) == count
            assert 1 <= run['replicas'] <= 4096
            if run['replicas'] > 1:
                assert int(raw['working_set_tree_bytes']) <= 64 * 1024 * 1024
                assert int(raw['estimated_working_set_tree_bytes']) <= 64 * 1024 * 1024
        elif cell['case'] in ('iterate', 'scan'):
            traversals = ceil(Fraction(requested, cell['size']))
            assert int(raw['traversals']) == traversals
            assert count >= traversals * cell['size']
            if cell['case'] == 'iterate':
                assert count == traversals * cell['size']
        else:
            assert count == requested
    else:
        assert count == requested
    if cell['referee'] == 'batch':
        assert int(raw['batch_size']) == cell['batch']
        assert int(raw['query_seed']) == run['seed'] + 1000
        assert int(raw['api_calls']) == ceil(Fraction(requested, cell['batch']))
    memory = Fraction(raw.get('mean_tree_bytes', raw['tree_bytes']))
    assert memory > 0
    close(memory, run['tree_bytes'])
    close(Fraction(elapsed, count), run['ns_op'])
    return dict(run=run, raw=raw, count=count, elapsed=elapsed, memory=memory)

def effects(reconstructed, cell_ids, reported, aa=False):
    computed = []
    lookup = {entry['cell']: entry for entry in reported}
    for cell_id in cell_ids:
        rows = [r for r in reconstructed if r['run']['cell'] == cell_id]
        assert len(rows) == 24
        time_effects, memory_effects = [], []
        for block in range(6):
            paired = sorted([r for r in rows if r['run']['block'] == block],
                            key=lambda r: r['run']['step'])
            assert len(paired) == 4
            assert ''.join(r['run']['label'] for r in paired) == 'ABBA'
            assert [r['run']['step'] for r in paired] == [0, 1, 2, 3]
            assert len({r['count'] for r in paired}) == 1
            assert len({r['raw']['checksum'] for r in paired}) == 1
            assert all(r['run']['seed'] == PLAN['discovery_seeds'][block] for r in paired)
            outside = paired[0]['elapsed'] + paired[3]['elapsed']
            inside = paired[1]['elapsed'] + paired[2]['elapsed']
            # Counts match within the block, so this exact integer-total ratio
            # equals the ratio of means of per-process ns/op without floats.
            time_effects.append(100 * (Fraction(inside, outside) - 1))
            outer_memory = paired[0]['memory'] + paired[3]['memory']
            inner_memory = paired[1]['memory'] + paired[2]['memory']
            memory_effects.append(100 * (inner_memory / outer_memory - 1))
        shortest = Fraction(min(r['elapsed'] for r in rows), 1000000)
        gate = dict(qualified=(all(abs(e) <= 1 for e in time_effects) and shortest >= 10) if aa else None,
                    primary_pass=all(e <= -2 for e in time_effects) and shortest >= 10,
                    guard_pass=all(e <= 1 for e in time_effects) and shortest >= 10,
                    memory_pass=all(e <= 1 for e in memory_effects),
                    consistent_regression=all(e > 1 for e in time_effects))
        record = lookup[cell_id]
        for key, value in gate.items():
            assert record[key] == value, (cell_id, key, record[key], value)
        for values, key in ((time_effects, 'effects_pct'), (memory_effects, 'memory_pct')):
            assert len(record[key]) == 6
            for exact, saved in zip(values, record[key]):
                close(exact, saved)
        close(median(time_effects), record['median_pct'])
        close(shortest, record['shortest_ms'])
        computed.append(dict(cell=cell_id, effects_pct=list(map(float, time_effects)),
                             exact_effect_fractions=[str(x) for x in time_effects],
                             median_pct=float(median(time_effects)),
                             min_pct=float(min(time_effects)), max_pct=float(max(time_effects)),
                             max_abs_pct=float(max(map(abs, time_effects))),
                             memory_pct=list(map(float, memory_effects)),
                             shortest_ms=float(shortest), **gate))
    return computed

def audit():
    calibration = json.loads((OUT / 'calibration.json').read_text())
    aa = json.loads((OUT / 'aa.json').read_text())
    screens = {v: json.loads((OUT / f'screen-{v}.json').read_text()) for v in 'ABC'}
    assert len(CELLS) == 101 and len(calibration['observations']) == 303
    assert len(aa['runs']) == 2424
    assert all(len(s['runs']) == 48 for s in screens.values())
    assert all(p['status'] == 'complete' for p in [calibration, aa, *screens.values()])
    cal_rows = list(map(reconstruct, calibration['observations']))
    aa_rows = list(map(reconstruct, aa['runs']))
    screen_rows = {v: list(map(reconstruct, d['runs'])) for v, d in screens.items()}
    all_rows = cal_rows + aa_rows + [r for rows in screen_rows.values() for r in rows]
    assert len({r['run']['file'] for r in all_rows}) == len(all_rows) == 2871
    for cell_id, cell in CELLS.items():
        rows = [r for r in cal_rows if r['run']['cell'] == cell_id]
        assert len(rows) == 3
        assert all(r['run']['variant'] == '0' and r['run']['seed'] == 1 and
                   r['run']['requested_ops'] == 200000 for r in rows)
        fastest = min(Fraction(r['elapsed'], r['count']) for r in rows)
        operations = min(100000000, ceil(Fraction(100000000) / fastest))
        replicas, capped = 1, False
        if cell['referee'] == 'standard' and cell['case'] in ('insert', 'delete'):
            per_tree = max(Fraction(r['raw'].get('estimated_working_set_tree_bytes',
                                               r['raw']['tree_bytes'])) for r in rows)
            limit = max(1, min(4096, (64 * 1024 * 1024) // per_tree))
            desired = ceil(Fraction(100000000) / (fastest * cell['size']))
            replicas, capped, operations = min(limit, desired), desired > limit, cell['size']
        fixed = calibration['fixed'][cell_id]
        assert fixed['ops'] == operations and fixed['replicas'] == replicas
        assert fixed['capped'] == (capped or operations == 100000000)
        close(fastest, fixed['calibrated_ns_op'])
    for r in aa_rows + [r for rows in screen_rows.values() for r in rows]:
        fixed = calibration['fixed'][r['run']['cell']]
        assert r['run']['requested_ops'] == fixed['ops']
        assert r['run']['replicas'] == fixed['replicas']
    assert all(r['run']['variant'] == '0' for r in aa_rows)
    for variant, rows in screen_rows.items():
        for r in rows:
            assert r['run']['variant'] == ('0' if r['run']['label'] == 'A' else variant)
    aa_effects = effects(aa_rows, list(CELLS), aa['results'], aa=True)
    screen_effects = {v: effects(rows, PLAN['primaries'], screens[v]['results'])
                      for v, rows in screen_rows.items()}
    commands = [json.loads(line) for line in (OUT / 'driver-commands.jsonl').read_text().splitlines()]
    names = [r['run']['name'] for r in all_rows]
    assert len(set(names)) == len(names)
    measured = [c for c in commands if c['name'] in set(names)]
    assert len(measured) == len(names)
    assert all(c['returncode'] == 0 for c in measured)
    assert all(timestamp(a['finish_utc']) <= timestamp(b['start_utc'])
               for a, b in zip(measured, measured[1:]))
    lookup = {r['run']['name']: r['run'] for r in all_rows}
    actual = [lookup[c['name']] for c in measured if c['name'].startswith('screen-')]
    expected = []
    for block in range(6):
        order = 'ABC'[block % 3:] + 'ABC'[:block % 3]
        cells = PLAN['primaries'] if block % 2 == 0 else list(reversed(PLAN['primaries']))
        for v in order:
            for cell in cells:
                for step, label in enumerate('ABBA'):
                    expected.append((v, cell, block, step, label))
    observed = [(r['name'].split('-')[1], r['cell'], r['block'], r['step'], r['label']) for r in actual]
    assert observed == expected, 'screen variant/cell rotation'
    observed = [(r['cell'], r['block'], r['step'], r['label']) for r in aa['runs']]
    expected = []
    cells = list(CELLS)
    for block in range(6):
        order = cells[block % len(cells):] + cells[:block % len(cells)]
        if block % 2:
            order.reverse()
        expected.extend((cell, block, step, label) for cell in order
                        for step, label in enumerate('ABBA'))
    assert observed == expected, 'A/A cell rotation'
    totals = dict(aa=sum(r['elapsed'] for r in aa_rows) / 1e9,
                  screens=sum(r['elapsed'] for rows in screen_rows.values() for r in rows) / 1e9)
    close(totals['aa'], aa['timing_seconds'])
    for v, rows in screen_rows.items():
        close(sum(r['elapsed'] for r in rows) / 1e9, screens[v]['timing_seconds'])
    assert totals['aa'] <= 300 and totals['screens'] <= 300
    assert aa['wall_seconds'] <= 900
    assert all(s['phase_wall_seconds'] <= 900 for s in screens.values())
    deadline = timestamp(PLAN['deadline_utc'])
    assert all(timestamp(c['finish_utc']) <= deadline for c in measured)
    freeze = json.loads((OUT / 'freeze.json').read_text())
    frozen = {**freeze['files'], **freeze['binaries']}
    assert all(sha(ROOT / name) == digest for name, digest in frozen.items())
    winners = [v for v, rows in screen_effects.items()
               if all(r['primary_pass'] and r['memory_pass'] for r in rows)]
    assert winners == []
    return dict(status='PASS', participant='/root/followup_proposal_c',
                backend='GPT-6/Codex family', exact_model=None, token_usage=None,
                monetary_cost=None, authored_variant='C',
                independence='Independent arithmetic/raw-data reconstruction from root driver; author of C, not independent semantic review of C and not new timing confirmation.',
                method='No driver import: exact Fraction arithmetic from integer elapsed totals and CSV owned bytes; paired outer-A versus inner-B sums, manual preregistered gates.',
                row_counts=dict(calibration=303, aa=2424, screens=144, total=2871),
                csv_hashes_verified=2871, frozen_files_and_binaries_verified=len(frozen),
                serial_measured_command_windows_verified=len(measured),
                calibration_cells_recomputed=101, qualified_aa_cells=sum(r['qualified'] for r in aa_effects),
                aa=aa_effects, screens=screen_effects, eligible_variants=winners,
                timing_seconds=totals, decision='REJECT dual-primary screen / source NONE',
                missing_adoption_gates=['full candidate guards', 'fresh confirmation',
                                       'matched candidate profiles', 'adoption review'],
                incidental_metadata=dict(observed_different_cpu_endpoints=sum(r['raw'].get('cpu_start') != r['raw'].get('cpu_end') for r in all_rows if 'cpu_start' in r['raw']),
                                         qos_effective_values=sorted({r['raw']['qos_effective'] for r in all_rows if 'qos_effective' in r['raw']}),
                                         caveat='Endpoint CPU observations do not establish residency or within-window migration; frequency/DVFS/PMU remain unknown.'),
                evidence_sha256={name: sha(OUT / name) for name in ['PLAN.json', 'freeze.json', 'driver.py', 'calibration.json', 'aa.json', 'screen-A.json', 'screen-B.json', 'screen-C.json', 'driver-commands.jsonl']},
                audit_script_sha256=sha(Path(__file__)), finished_utc=datetime.now(timezone.utc).isoformat())

if __name__ == '__main__':
    result = audit()
    (OUT / 'INDEPENDENT-AUDIT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'row_counts', 'qualified_aa_cells',
                                           'eligible_variants', 'timing_seconds', 'decision')}, indent=2))
