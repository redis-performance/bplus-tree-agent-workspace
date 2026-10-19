"""Independent metadata/assembly review; no producer imports or runner execution."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

REV = 'a3db7053af779f7ee2572963cf4d79d3629b650f'
BASE = 'experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/'
INPUTS = {}

def raw(path):
    b = subprocess.check_output(['git', 'show', REV + ':' + BASE + path])
    INPUTS[path] = hashlib.sha256(b).hexdigest()
    return b

def js(path):
    return json.loads(raw(path))

def functions(path):
    result = {}; current = None
    for line in raw(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]+) <([^>]+)>:', line)
        if match:
            current = match[2]
            assert current not in result
            result[current] = dict(start=int(match[1], 16), words=[])
        match = re.match(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.+)$', line)
        if match:
            assert current is not None
            result[current]['words'].append(dict(pc=int(match[1],16),word=match[2],asm=match[3]))
    return result

seal = js('preparation-seal.json')
missing = []
for path, sha in seal.items():
    exists = subprocess.run(['git','cat-file','-e',REV+':'+BASE+path],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if exists.returncode:
        missing.append(path)
        continue
    assert hashlib.sha256(raw(path)).hexdigest() == sha, path
manifest = js('artifact-retrieval/manifest.json')
assert len(manifest['commands']) == 20
for command in manifest['commands']:
    assert command['returncode'] == 0
    stem = 'artifact-retrieval/' + command['name'] + '-' + command['kind']
    for stream in ['stdout', 'stderr']:
        key = stream + '_public_sha256'
        if key in command:
            assert hashlib.sha256(raw(stem + '.' + stream)).hexdigest() == command[key]
for name, binding in manifest['binaries'].items():
    before = raw('artifact-retrieval/'+name+'-hash-before.stdout').decode().split()[0]
    after = raw('artifact-retrieval/'+name+'-hash-after.stdout').decode().split()[0]
    binary = next(c for c in manifest['commands'] if c['name']==name and c['kind']=='binary')
    assert before == after == binding['expected_sha256'] == binding['local_binary_sha256'] == binary['stdout_raw_sha256']

assemblies = {name:functions('artifact-retrieval/'+name+'-assembly.stdout') for name in manifest['binaries']}
actual_map = {}
for source, expected in [('control',114),('A',113)]:
    p = assemblies['primary-'+source]['zbtreeIteratorNext']
    h = assemblies['h4-'+source]['zbtreeIteratorNext']
    assert len(p['words']) == len(h['words']) == expected
    delta = [i*4 for i,(a,b) in enumerate(zip(p['words'],h['words'])) if a['word']!=b['word']]
    assert delta == ([432,436,440,444] if source=='control' else [428,432,436,440])
    published = js('exact-cross-frontend-iterator-map.json')[source]
    assert delta == [int(d['offset'],16) for d in published['exact_encoded_differences']]
    t = assemblies['h4-'+source]['traverse']; assert len(t['words']) == 282
    loop = [w for w in t['words'] if 0xd4 <= w['pc']-t['start'] <= 0xfc]
    assert len(loop) == 11
    assert not any(re.match(r'(tb[n]?z|cbz|b\.)\b',w['asm']) for w in loop)
    assert loop[-1]['asm'].startswith('cbnz')
    assert sum('zbtreeIteratorNext>' in w['asm'] and w['asm'].startswith('bl') for w in t['words']) == 13
    actual_map[source] = dict(iterator_instructions=expected,primary_start=hex(p['start']),h4_start=hex(h['start']),different_offsets=[hex(i) for i in delta],h4_traverse_instructions=282,mask4_loop=loop)

cells = {c['id']:c for c in js('cells.json')}; schedules = js('schedules.json')
assert len(cells)==6
counts={}
for phase, rows in schedules.items():
    assert len(rows)==(36 if phase in ['cycle-captures','scoped-stats'] else 144)
    assert [r['index'] for r in rows]==list(range(len(rows)))
    groups=collections.defaultdict(list)
    for r in rows:
        c=cells[r['cell']]; a=dict(zip(r['args'][::2],r['args'][1::2]))
        expected={'--size':str(c['size']),'--ops':str(c['requested_ops']),'--member-bytes':'16','--seed':str(r['seed']),'--warmup-passes':str(c['warmup_passes'])}
        expected.update({'--case':'iterate'} if c['frontend']=='primary' else {'--encoding':'integer','--direction':c['direction'],'--mask':'4'})
        assert a==expected
        assert r['seed'] in ([1601,1602,1603] if phase.startswith('native') else [1701,1702,1703])
        if phase in ['cycle-captures','scoped-stats']:
            assert r['binary']=='diagnostic-enabled'
            groups[(r['cell'],r['seed'])].append(r)
        else:
            key=(r['cell'],r['block']) if phase.startswith('native') else (r['cell'],r['block'],r['source'])
            groups[key].append(r)
    for key, block in groups.items():
        if phase in ['cycle-captures','scoped-stats']:
            assert len(block)==2 and {r['source'] for r in block}=={'control','A'}
        else:
            assert [r['position'] for r in block]==[0,1,2,3]
            assert block[0]['label']==block[3]['label'] and block[1]['label']==block[2]['label'] and block[0]['label']!=block[1]['label']
            if phase=='native-AA': assert all(r['source']=='control' and r['binary']=='actual' for r in block)
            if phase=='native-comparison': assert [r['source'] for r in block]==['control','A','A','control'] and all(r['binary']=='actual' for r in block)
            if phase=='instrument-AA': assert all(r['binary']=='actual' for r in block)
            if phase=='instrument-perturbation': assert [r['binary'] for r in block]==['actual','diagnostic-disabled','diagnostic-disabled','actual']
    counts[phase]=len(rows)

out=Path(__file__).parent
(out/'CHECKS.json').write_text(json.dumps(dict(revision=REV,integrity='BLOCKED_MISSING_SEALED_FILE' if missing else 'PASS',sealed_files=len(seal),missing_sealed_files=missing,read_only_retrieval_commands=20,binary_bindings=manifest['binaries'],actual_maps=actual_map,schedule_counts=counts,limitations=['Public assembly and recorded binary hashes verified; raw ELF bytes not rehashed by this reviewer.','No executable driver/profile mapping implementation reviewed; preparation is not launch approval.']),indent=2)+'\n')
(out/'input-hashes.json').write_text(json.dumps(INPUTS,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(seal_files=len(seal),input_files=len(INPUTS),schedule_counts=counts,missing_sealed_files=missing,status='BLOCKED' if missing else 'PASS')))
