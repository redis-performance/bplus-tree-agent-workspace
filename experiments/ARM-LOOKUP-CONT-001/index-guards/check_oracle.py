#!/usr/bin/env python3
"""Independent integer/byte model; baseline/candidate joins include both endpoints."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
manifest = json.loads((HERE / 'correctness' / 'build-manifest.json').read_text())
assert manifest['measurement_calls'] == 0 and len(manifest['binaries']) == 12
assert all(v['clock_symbol_wrapped'] and v['cells'] == 24 for v in manifest['binaries'].values())
fixtures = {}
for seed in (17, 29, 43):
    f = json.loads((HERE / 'correctness' / f'fixture-{seed}.json').read_text())
    assert f['seed'] == seed and len(f['nonces']) == len(f['hashes']) == 544
    keys, digest = [], 1469598103934665603
    for i, nonce in enumerate(f['nonces']):
        b = bytearray((i*17+j*29) % 256 if j % 7 else 0 for j in range(128))
        b[:4] = i.to_bytes(4, 'little')
        b[4:8] = nonce.to_bytes(4, 'little')
        assert nonce < 10000000
        assert f['hashes'][i] & 63 == 63 and f['hashes'][i] >> 24 == i % 2
        for byte in b:
            digest = ((digest ^ byte)*1099511628211) % 2**64
        keys.append(bytes(b))
    assert len(set(keys)) == 544 and f'{digest:016x}' == f['digest']
    fixtures[seed] = f, keys

IGNORE = {'diagnostic', 'home_hits', 'displaced_hits', 'max_displacement',
          'active_before', 'active_after', 'growth_states', 'shrink_states',
          'completions', 'leaf_reassignments', 'mixed_active_before', 'reassigned_during_active'}
rows, diagnostics = {}, []
for path in sorted((HERE / 'correctness').glob('*.jsonl')):
    variant, mode, scope = path.stem.split('-')
    cells = list(map(json.loads, path.read_text().splitlines()))
    assert len(cells) == 24
    for r in cells:
        assert r['verified'] and r['mode'] == 'verify' and 'elapsed_ns' not in r
        assert r['sweeps'] in (1, 2) and r['seed'] in fixtures
        f, keys = fixtures[r['seed']]
        assert r['fixture_digest'] == f['digest']
        n, case = r['sweeps'], r['case']
        if case == 'collision-hit':
            assert r['calls'] == r['hits'] == 256*n and r['score_sum'] == sum(range(1, 257))*n
        elif case == 'collision-miss':
            assert r['calls'] == 32*n and r['hits'] == r['score_sum'] == 0
        elif case == 'repair-churn':
            assert r['calls'] == 1792*n and r['hits'] == 384*n
            assert r['score_sum'] == sum(range(513, 1025))*n
        else:
            assert case == 'scan-members' and len(r['seen']) == 256
            assert min(r['seen']) >= n and r['callbacks'] == sum(r['seen'])
            assert r['score_sum'] == sum((i+1)*v for i,v in enumerate(r['seen']))
            assert r['byte_sum'] == sum((keys[i][0]+3*keys[i][64]+7*keys[i][-1]+128)*v
                                        for i,v in enumerate(r['seen']))
            assert r['calls'] == r['scan_calls'] and r['hits'] == 0
        if case != 'scan-members':
            assert r['callbacks'] == r['scan_calls'] == r['byte_sum'] == 0 and not any(r['seen'])
        if r['diagnostic']:
            if case != 'repair-churn':
                assert r['home_hits'] + r['displaced_hits'] == 256
                assert r['home_hits'] > 0 and r['displaced_hits'] > 0 and r['max_displacement'] > 1
            else:
                for name in ('active_before', 'active_after', 'growth_states', 'shrink_states',
                             'mixed_active_before', 'completions', 'leaf_reassignments'):
                    assert r[name] > 0, (path, name)
            diagnostics.append({k:v for k,v in r.items() if k in IGNORE or k in ('case','seed','sweeps')})
        key = (variant, mode, scope, r['seed'], n, case)
        assert key not in rows
        rows[key] = r
assert len(rows) == 288
for (variant, mode, scope, seed, n, case), row in rows.items():
    base = rows['base', mode, 'public', seed, n, case]
    assert {k:v for k,v in row.items() if k not in IGNORE} == \
           {k:v for k,v in base.items() if k not in IGNORE}, (variant,mode,scope,seed,n,case)
print(json.dumps({'verified': True, 'independent_model_rows':len(rows),
                  'baseline_candidate_exact_joins':len(rows),
                  'memory_endpoints_included': True, 'clock_denied': True,
                  'measurement_calls':0}, indent=2))
