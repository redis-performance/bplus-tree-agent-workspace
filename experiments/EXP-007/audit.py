#!/usr/bin/env python3
"""Independently reconstruct process statistics and block effects from retained CSVs."""
import csv
import hashlib
import json
from pathlib import Path
import statistics
import sys, math

root = Path(__file__).resolve().parent
runroot = root / sys.argv[1]
assert sys.argv[1] in ('discovery','confirmation')
expected_runs=2880 if sys.argv[1]=='discovery' else 1440
manifest = json.loads((runroot/'manifest.json').read_text())
saved = json.loads((runroot/'process-summary.json').read_text())
assert manifest['status'] == 'complete'
assert len(manifest['runs']) == len(manifest['schedule']) == len(saved) == expected_runs
fixtures, derived = {}, []
row_count = 0
previous_end = ''
for run, scheduled, summary in zip(manifest['runs'], manifest['schedule'], saved):
    assert all(run[k] == v for k, v in scheduled.items())
    assert run['returncode'] == 0
    assert previous_end <= run['started_utc'] <= run['ended_utc']
    previous_end = run['ended_utc']
    for name in ('csv', 'stderr'):
        assert hashlib.sha256((runroot/run[name]).read_bytes()).hexdigest() == run[name+'_sha256']
    rows = list(csv.DictReader((runroot/run['csv']).read_text().splitlines()))
    assert len(rows) == 129
    row_count += len(rows)
    for i, row in enumerate(rows):
        assert row['kind'] == 'time' and int(row['sample']) == i
        for field in ('width', 'reversed', 'count', 'seed'):
            assert int(row[field]) == run[field]
        operations=run['count']*8*math.ceil(49152/(run['count']*8))
        assert int(row['operations']) == operations
        assert abs(float(row['elapsed_ns'])/operations-float(row['ns_per_decode'])) < 2e-8
        offsets = {(j*run['width']) % 8 for j in range(run['count'])}
        assert int(row['offset_mask']) == sum(1 << o for o in offsets)
        assert int(row['crossings_per_round']) == 8*sum(run['width']+(j*run['width']) % 8 > 64 for j in range(run['count']))
        identity = (run['width'], run['reversed'], run['count'], run['seed'])
        invariant = tuple(row[k] for k in ('operations','leaf_bytes','offset_mask','crossings_per_round','fixture_hash','checksum'))
        assert fixtures.setdefault(identity,invariant) == invariant
        assert row['cycles'] == row['instructions'] == ''
    values = sorted(float(r['ns_per_decode']) for r in rows)
    stats = dict(min_ns=values[0],median_ns=statistics.median(values),p90_ns=values[int(.9*(len(values)-1))],max_ns=values[-1],min_batch_ns=min(float(r['elapsed_ns']) for r in rows),endpoint_migrations=sum(r['cpu_start'] != r['cpu_end'] for r in rows))
    assert all(summary[k] == v for k,v in stats.items())
    derived.append(dict(scheduled,**stats))
summary = json.loads((runroot/'summary.json').read_text())
assert len(summary) == (120 if sys.argv[1]=='discovery' else 60)
for cell in summary:
    group = [r for r in derived if all(r[k] == cell[k] for k in ('phase','width','reversed','count'))]
    assert len(group) == 24
    for stat in ('min_ns','median_ns'):
        effects=[]
        for block in range(6):
            pair = [r for r in group if r['block']==block]
            assert ''.join(r['label'] for r in pair)=='ABBA'
            if cell['phase']=='aa': assert {r['variant'] for r in pair} == {'base'}
            a=statistics.mean(r[stat] for r in pair if r['label']=='A')
            b=statistics.mean(r[stat] for r in pair if r['label']=='B')
            effect=100*(b/a-1); effects.append(effect)
            assert cell[stat]['block_effects'][block]['percent']==effect
        assert cell[stat]['median_effect_pct']==statistics.median(effects)
assert sum(int(r['samples']) for r in csv.DictReader((runroot/'histogram.csv').read_text().splitlines()))==row_count
build=json.loads((runroot/'build.json').read_text())
assert all(manifest['binary_hashes_after'][v]==build['variants'][v]['binary_sha256'] for v in ('base','A','B','C'))
result=dict(status='PASS',processes=len(derived),raw_sha256_checks=2*expected_runs,measured_batches=row_count,fixture_identities=len(fixtures),cell_summaries=len(summary),paired_block_effects=len(summary)*12,serial_windows=True,scope='Read-only raw evidence audit; not independent experimental confirmation')
freeze=json.loads((root/'freeze.json').read_text())
workspace=root.parents[1]
for name,digest in freeze['files'].items():
    assert hashlib.sha256((workspace/name).read_bytes()).hexdigest()==digest
for name,digest in build['files'].items():
    assert hashlib.sha256((workspace/name).read_bytes()).hexdigest()==digest
assert hashlib.sha256((workspace/'src/zset_btree.c').read_bytes()).hexdigest()==freeze['production_source_sha256']
for v in ('base','A','B','C'):
    binary=workspace/build['variants'][v]['binary']
    assert hashlib.sha256(binary.read_bytes()).hexdigest()==build['variants'][v]['binary_sha256']
result['frozen_files_and_binaries']='PASS'
(runroot/'AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
