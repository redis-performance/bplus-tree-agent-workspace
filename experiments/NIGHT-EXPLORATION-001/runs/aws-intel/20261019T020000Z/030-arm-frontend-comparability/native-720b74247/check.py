"""Independent immutable native-freeze/fixture metadata check, no producer imports."""
import collections, hashlib, json, struct, subprocess
from pathlib import Path
REV='720b74247906a4b760b431e2493db3befba1e11f'
BASE='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/'
hashes={}
def read(name):
    data=subprocess.check_output(['git','show',REV+':'+BASE+name]);hashes[name]=hashlib.sha256(data).hexdigest();return data
def js(name):return json.loads(read(name))
freeze=js('native-execution-freeze.json');seal=js('preparation-seal-v2.json')
for names in [freeze['files'],seal]:
    for name,expected in names.items():assert hashlib.sha256(read(name)).hexdigest()==expected,name
old=js('preparation-seal.json');missing='inputs/__pycache__/arm_asm.cpython-312.pyc'
assert set(old)-set(seal)=={missing} and all(old[k]==v for k,v in seal.items())
ids=js('identities.json'); original=js('original-identity-import.json'); artifact=js('artifact-retrieval/manifest.json')
for key in ['source_hashes','candidate_source_sha256','candidate_patch_sha256']:assert ids[key]==original[key]
for name,identity in ids['binaries'].items():
    assert identity==dict(path=artifact['binaries'][name]['relative_path'],sha256=artifact['binaries'][name]['expected_sha256'])
for name,expected in ids['source_hashes'].items():
    actual=subprocess.check_output(['git','show',ids['source_commit']+':'+name]);assert hashlib.sha256(actual).hexdigest()==expected,name
cells={c['id']:c for c in js('cells.json')};schedules=js('schedules.json')
for phase in ['native-AA','native-comparison']:
    runs=schedules[phase];assert len(runs)==144;groups=collections.defaultdict(list)
    for index,r in enumerate(runs):
        assert r['index']==index;assert r['seed']==1601+r['block']%3;assert r['binary']=='actual'
        assert r['source']==('control' if phase=='native-AA' or r['position'] in [0,3] else 'A')
        assert r['label']==('control' if r['position'] in [0,3] else 'A')
        c=cells[r['cell']];expected=['--size',str(c['size']),'--ops',str(c['requested_ops']),'--member-bytes','16','--seed',str(r['seed']),'--warmup-passes',str(c['warmup_passes'])]
        expected+=['--case','iterate'] if c['frontend']=='primary' else ['--direction',c['direction'],'--mask','4','--encoding','integer']
        assert r['args']==expected;groups[(r['cell'],r['block'])].append(r)
    assert len(groups)==36 and all([r['position'] for r in g]==[0,1,2,3] for g in groups.values())

oracle=js('fixture-oracle.json');mod=1<<64;checked=[]
def stream(seed):
    state=seed
    while True:
        state=(state+0x9e3779b97f4a7c15)%mod
        x=(state^(state>>30))*0xbf58476d1ce4e5b9%mod
        x=(x^(x>>27))*0x94d049bb133111eb%mod
        yield x^(x>>31)
for n in [129,100000,1000000]:
    bit_sum=sum(struct.unpack('<Q',struct.pack('<d',i-n//2))[0] for i in range(n))%mod
    for seed in ([1801] if n==129 else [1601,1602,1603,1701,1702,1703]):
        generator=stream(seed)
        for _ in range(16):next(generator)
        order=list(range(n))
        for position in range(n-1,0,-1):
            other=next(generator)%(position+1)
            order[position],order[other]=order[other],order[position]
        fingerprint=14695981039346656037
        for element in order:fingerprint=(fingerprint^element)*1099511628211%mod
        expect=dict(primary_one_traversal_checksum=n*(n-1)//2,h4_one_traversal_checksum=(n+bit_sum)%mod,h4_construction_fingerprint=fingerprint)
        key=f'{n}/{seed}';assert oracle[key]==expect,key;checked.append(key)
assert set(oracle)==set(checked)
out=Path(__file__).parent
(out/'CHECKS.json').write_text(json.dumps(dict(revision=REV,metadata_checks='PASS',execution_grant='BLOCKED_PENDING_STATIC_FINDINGS',native_freeze_files=len(freeze['files']),corrected_preparation_files=len(seal),preserved_missing_cache_entry=missing,native_schedule_processes=288,independently_reconstructed_fixture_models=checked,source_bindings='PASS',scope='Immutable local arithmetic and metadata only; no benchmarks/builds/SSH.'),indent=2)+'\n')
(out/'input-hashes.json').write_text(json.dumps(hashes,indent=2,sort_keys=True)+'\n')
print('PASS:15 native inputs,63 corrected prep inputs,288 scheduled processes,13 independent fixture models; static findings remain blocking')
