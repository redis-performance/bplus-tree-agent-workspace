#!/usr/bin/env python3
"""Read-only audit of the immutable 2ab283daa focused scan referee evidence."""
import argparse, hashlib, itertools, json, pathlib
p = argparse.ArgumentParser()
p.add_argument('referee', type=pathlib.Path)
p.add_argument('--out', required=True, type=pathlib.Path)
a = p.parse_args(); root = a.referee; data = root / 'local-baseline-validation'
freeze = json.loads((root / 'referee-freeze.json').read_text())
for name, digest in freeze['referee_sha256'].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
assert hashlib.sha256((data / 'fixture-manifest.json').read_bytes()).hexdigest() == freeze['fixture_manifest_sha256']
commands = json.loads((data / 'commands.json').read_text())
assert len(commands) == 368 and len({x['name'] for x in commands}) == 368
for i, row in enumerate(commands):
    assert row['returncode'] == row['expected_returncode']
    assert row['start_utc'] <= row['end_utc']
    if i: assert commands[i-1]['end_utc'] <= row['start_utc']
    if 'run' in row['argv']: assert row['argv'][-2] == '0', row['name']
    if not row['name'].startswith('fault-'):
        assert not (data / (row['name'] + '.stderr')).read_text()
faults = [x for x in commands if x['name'].startswith('fault-')]
assert {x['name'] for x in faults} == {f'fault-{mode}-{f}' for mode in ['native','sanitize'] for f in range(1,5)}
assert all(x['returncode'] == 2 for x in faults)
rows = [json.loads(x) for x in (data / 'census.jsonl').read_text().splitlines()]
expected = {f's{s}-n{n}-b{b}-d{d}-o{o}' for s,n,b,d,o in itertools.product([101,102,103],[4096,100000],[16,321],range(3),range(3))}
assert {x['cell'] for x in rows} == expected and len(rows) == 108
folded = []; descending = []
for x in rows:
    cell,c,r = x['cell'], x['census'], x['run']; n = r['n']
    assert c['members'] == n == sum(c['tag_histogram'])
    assert sum(c['leaf_count_histogram']) == c['leaves']
    assert sum(i*v for i,v in enumerate(c['leaf_count_histogram'])) == n
    assert not c['active_rehash'] and c['wide_ids'] == 0
    assert c['external_members'] == (n if r['bytes'] == 321 else 0)
    if r['distribution'] == 1: assert c['tag_histogram'][17] == n
    if r['distribution'] == 2:
        assert sum(c['tag_histogram'][:2]) == n and min(c['tag_histogram'][:2]) > 0
        folded.append(c['tag_histogram'][0] / n)
    if r['order'] == 1:
        assert c['reversed_leaves'] == 1 and c['reversed_members'] == 64
        descending.append(64/n)
    for mode in ['native', 'sanitize']:
        actual = json.loads((data / (cell+'-'+mode+'.stdout')).read_text())
        for k in ['n','bytes','seed','distribution','order']:
            assert actual[k] == r[k]
        if mode == 'native':
            for k in ['callbacks_per_pass','checksum_per_pass','tree_bytes']:
                assert actual[k] == r[k]
manifest = json.loads((data / 'fixture-manifest.json').read_text())
assert len(manifest) == 36
for f in manifest:
    assert f['bytes'] == 40 + 4*f['generator']['n']
a.out.write_text(json.dumps({'status':'pass','immutable_commit':'2ab283daa','commands':len(commands),'cells':len(rows),'fixture_manifests':len(manifest),'referee_hashes_verified':len(freeze['referee_sha256']),'fault_controls':len(faults),'descending_cells':len(descending),'descending_reversed_members_each':64,'descending_reversed_member_fraction_min_max':[min(descending),max(descending)],'folded_tag_zero_fraction_min_max':[min(folded),max(folded)],'active_rehash_cells':0,'wide_id_cells':0,'timing_windows':0,'fixture_binary_hashes_recomputed':False,'fixture_binary_note':'Only manifest is published; generation bytes were not reexecuted or independently reconstructed in this read-only audit.','reviewer':'one AMD native agent; exact model and costs unknown'},indent=2)+'\n')
