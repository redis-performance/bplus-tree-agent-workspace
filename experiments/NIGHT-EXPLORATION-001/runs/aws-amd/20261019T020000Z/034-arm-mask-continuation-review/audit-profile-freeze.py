import pathlib,json,hashlib,subprocess,ast,collections,sys
p=pathlib.Path(sys.argv[1]);j=lambda n:json.loads((p/n).read_text());sha=lambda q:hashlib.sha256(q.read_bytes()).hexdigest();f=j('execution-freeze.json');e=j('expected.json');imports=j('IMPORTS.json');c=j('commands.json');fixtures=j('fixtures.json')
for n,h in f['files'].items():assert sha(p/n)==h,n
for n,h in imports['unchanged'].items():
 assert sha(p/n)==h
 origin='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/024-corrected-iterator/'+n
 assert hashlib.sha256(subprocess.check_output(['git','show',imports['immutable_frontend_origin']+':'+origin])).hexdigest()==h
for n,h in e['source_hashes'].items():assert hashlib.sha256(subprocess.check_output(['git','show',e['commit']+':'+n])).hexdigest()==h,n
assert sha(p/'candidate.patch')==e['candidate_patch_sha256']=='ca14579cbf4325816d5511697cb0bec5ab0e618ef661830acbc4bfe72a5cc88f'
for name in ['run-profile.py','audit-profile.py','map-code.py','arm_asm.py','profile_helpers.py']:ast.parse((p/name).read_text())
assert len(c)==104 and len({x['name'] for x in c})==104 and len(fixtures)==6
assert {(x['size'],x['seed'],x['requested_ops'],x['member_bytes'],x['case']) for x in fixtures}=={(n,s,50000000,16,'iterate') for n in [100000,1000000] for s in [1401,1402,1403]}
byname={x['name']:x for x in c}
for suffix in ['original-build','profile-build','original-san-build','profile-san-build','original43']:
 assert byname['control-'+suffix]['command']==byname['A-'+suffix]['command']
for x in c:assert set(x['profile_env'])=={'PROFILE_DISABLE','BPLUS_PERF_CTL','BPLUS_PERF_ACK'}
assert next(i for i,x in enumerate(c) if x['kind']=='known-gate')<min(i for i,x in enumerate(c) if '-iterate-' in x['name'] and x['name'].endswith('-record'))
for fixture in fixtures:
 for variant in ['control','A']:
  label=f'{variant}-iterate-n{fixture["size"]}-s{fixture["seed"]}'
  for suffix in ['original','disabled','record','stat']:assert byname[label+'-'+suffix]['fixture']==fixture
  for suffix in ['record','stat']:
   x=byname[label+'-'+suffix];assert x['profile_env']=={'PROFILE_DISABLE':None,'BPLUS_PERF_CTL':'<job>/control.fifo','BPLUS_PERF_ACK':'<job>/ack.fifo'}
assert collections.Counter(x['kind'] for x in c)['tree-stat']==12
assert len([x for x in c if '-iterate-' in x['name'] and x['name'].endswith('-record')])==12
assert len([x for x in c if x['name'].endswith('-full-asm') and x['name']!='known-full-asm'])==6
for v in ['control','A']:assert e['timing_binaries'][v]['sha256']==e['protected_binaries'][e['timing_binaries'][v]['path']]
print(json.dumps(dict(revision='acbd0cbe9',status='STATIC_REVIEW_NO_DIAGNOSTIC_BLOCKER',frozen_inputs=len(f['files']),freeze_sha256=sha(p/'execution-freeze.json'),unchanged_imports=len(imports['unchanged']),source_hashes=len(e['source_hashes']),commands=len(c),command_kinds=dict(collections.Counter(x['kind'] for x in c)),fixtures=6,captures=12,counter_runs=12,actual_timing_binaries=e['timing_binaries'],no_workload=True,mechanism_gate_is_manual=True,required_result_assessment=['known and scientific losses zero','all six instruction directions pass','all sampled tree bytes map to each own actual timing binary','unknowns and full-body/caller differences assessed','No speed/acceptance inference from diagnostic status pass']),indent=2))
