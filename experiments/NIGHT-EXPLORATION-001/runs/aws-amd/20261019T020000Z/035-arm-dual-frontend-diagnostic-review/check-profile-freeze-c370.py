import subprocess,json,hashlib,collections,ast,struct,pathlib
rev='c370e444f513620dacaf854637a328d4c69d9040';prefix='experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis/';get=lambda n:subprocess.check_output(['git','show',rev+':'+prefix+n]);j=lambda n:json.loads(get(n));sha=lambda b:hashlib.sha256(b).hexdigest()
f=j('profile-execution-freeze.json');assert len(f['files'])==35
for n,h in f['files'].items():
 assert sha(get(n))==h,n
 if n.endswith('.py'):ast.parse(get(n))
c=j('profile-commands.json');s=j('schedules.json');cells={x['id']:x for x in j('cells.json')};assert len(c)==642 and len({x['name'] for x in c})==642
counts=collections.Counter(x['kind'] for x in c);assert counts==dict(archive=1,compiler=1,build=26,original43=4,tree=132,census=56,**{'disabled-stat':4,'known':3,'known-stat':2,'plain':87,'known-gate':1,'fault-scope':1,'instrument':288,'tree-stat':36}),counts
for row in c:
 assert set(row['profile_env'])=={'PROFILE_DISABLE','BPLUS_PERF_CTL','BPLUS_PERF_ACK'}
 if row['fixture']:
  z=row['fixture'];args=row['command'];assert args[args.index('--size')+1]==str(z['size']) and args[args.index('--ops')+1]==str(z['requested_ops']);assert args[args.index('--seed')+1]==str(z['seed']) and args[args.index('--warmup-passes')+1]==str(z['warmup_passes'])
  if z['frontend']=='h4':assert args[args.index('--mask')+1]=='4' and args[args.index('--encoding')+1]=='integer' and args[args.index('--direction')+1]==z['direction']
for phase in ['instrument-AA','instrument-perturbation']:
 rows=[x for x in c if x.get('instrument_phase')==phase];assert len(rows)==144
 for x,y in zip(rows,s[phase]):assert x['instrument_contract']==y and x['variant']==y['source'] and x['fixture']['seed']==y['seed']
for phase,rows in [('cycle-captures',[x for x in c if 'capture_file' in x]),('scoped-stats',[x for x in c if x['kind']=='tree-stat'])]:
 assert len(rows)==36
 for x,y in zip(rows,s[phase]):
  assert x['variant']==y['source'] and x['fixture']['id']==y['cell'] and x['fixture']['seed']==y['seed'];cmd=x['command'];assert cmd[cmd.index('--')+2:]==y['args'];assert x['profile_env']['PROFILE_DISABLE'] is None and cmd[cmd.index('-D')+1]=='-1' and any(v.startswith('--control=fifo:') for v in cmd)
 assert len({(x['variant'],x['fixture']['id'],x['fixture']['seed']) for x in rows})==36
assert next(i for i,x in enumerate(c) if x['kind']=='fault-scope')<next(i for i,x in enumerate(c) if 'capture_file' in x)
base=get('inputs/known-control.c').decode();fault=get('inputs/known-missing-disable.c').decode();assert base.replace('if (enabled) profile_control("disable\\n");','/* Deliberate scope fault: omitted disable before outside_work. */')==fault
# Independently reconstruct every census digest from the literal finite score sequence.
oracle=j('census-score-oracle.json');digests={}
for front in ['primary','h4']:
 for n in [129,100000,1000000]:
  value=14695981039346656037
  for i in range(n):value=((value^int.from_bytes(struct.pack('<d',i-(n//2 if front=='h4' else 0)),'little'))*1099511628211)&((1<<64)-1)
  assert oracle[f'{front}/{n}']==value;digests[f'{front}/{n}']=value
print(json.dumps(dict(revision=rev,freeze_sha256=sha(get('profile-execution-freeze.json')),frozen_files=35,commands=642,kind_counts=dict(counts),instrumentation_processes=288,scientific_captures=36,scientific_counter_runs=36,matched_counter_pairs=18,census_score_digests=digests,scope_fault='exact single missing-disable line verified before scientific captures',local_metadata_only=True,runner_access=False),indent=2))
