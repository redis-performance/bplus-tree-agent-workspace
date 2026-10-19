import json,pathlib,hashlib,subprocess,struct,collections,sys,ast
p=pathlib.Path(sys.argv[1]);j=lambda n:json.loads((p/n).read_text());sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();f=j('native-execution-freeze.json');ids=j('identities.json');cells={x['id']:x for x in j('cells.json')};schedules=j('schedules.json');oracle=j('fixture-oracle.json')
for name,value in f['files'].items():assert sha(p/name)==value,name
for name,value in j('preparation-seal-v2.json').items():assert sha(p/name)==value,name
for name,value in ids['source_hashes'].items():assert hashlib.sha256(subprocess.check_output(['git','show',ids['source_commit']+':'+name])).hexdigest()==value
assert len(f['files'])==15 and len(cells)==6
for name in ['run-native.py','native_common.py','audit-native.py','fixture-oracle-generator.py']:ast.parse((p/name).read_text())
assert ids['candidate_source_sha256']=='aa834a771284bed367400a8f54538cd366b2791666d9711a8e160aaa93f62fc4'
counts={}
for phase in ['native-AA','native-comparison']:
 rows=schedules[phase];assert len(rows)==144 and [x['index'] for x in rows]==list(range(144));counts[phase]=len(rows);groups=collections.defaultdict(list)
 for row in rows:
  c=cells[row['cell']];assert row['seed']==1601+row['block']%3 and row['position'] in range(4);assert row['label']==['control','A','A','control'][row['position']]
  assert row['source']==('control' if phase=='native-AA' or row['position'] in [0,3] else 'A') and row['binary']=='actual'
  expected=['--size',str(c['size']),'--ops',str(c['requested_ops']),'--member-bytes','16','--seed',str(row['seed']),'--warmup-passes',str(c['warmup_passes'])]
  expected+=['--case','iterate'] if c['frontend']=='primary' else ['--direction',c['direction'],'--mask','4','--encoding','integer']
  assert row['args']==expected;groups[(row['cell'],row['block'])].append(row['position'])
 assert len(groups)==36 and all(x==[0,1,2,3] for x in groups.values())
# Independently reconstruct oracle integers using the source's literal PRNG/permutation contract.
mask=2**64-1
def random_stream(seed):
 state=seed
 while True:
  state=(state+0x9e3779b97f4a7c15)&mask;x=state;x=((x^(x>>30))*0xbf58476d1ce4e5b9)&mask;x=((x^(x>>27))*0x94d049bb133111eb)&mask;yield x^(x>>31)
checks=[]
for n in [129,100000,1000000]:
 bit_total=sum(int.from_bytes(struct.pack('<d',i-n//2),'little') for i in range(n))&mask
 for seed in ([1801] if n==129 else [1601,1602,1603,1701,1702,1703]):
  ref=oracle[f'{n}/{seed}'];assert ref['primary_one_traversal_checksum']==n*(n-1)//2 and ref['h4_one_traversal_checksum']==(n+bit_total)&mask
  stream=random_stream(seed)
  for _ in range(16):next(stream)
  order=list(range(n))
  for index in range(n-1,0,-1):other=next(stream)%(index+1);order[index],order[other]=order[other],order[index]
  fingerprint=0xcbf29ce484222325
  for item in order:fingerprint=((fingerprint^item)*0x100000001b3)&mask
  assert ref['h4_construction_fingerprint']==fingerprint;checks.append(f'{n}/{seed}')
print(json.dumps(dict(revision='720b74247',status='SOURCE_SCHEDULE_ORACLE_CHECKS_PASS_WITH_REVIEW_FINDINGS',native_freeze_sha256=sha(p/'native-execution-freeze.json'),frozen_inputs=len(f['files']),preparation_seal_v2_entries=len(j('preparation-seal-v2.json')),source_hashes=len(ids['source_hashes']),schedule_processes=counts,oracle_fixtures_reconstructed=checks,findings=['AA audit result hash join missing','Comparison window floor absent from qualification','Explicit lease deadline/slice/CPU binding requested'],runner_access=False,scientific_execution=False),indent=2))
