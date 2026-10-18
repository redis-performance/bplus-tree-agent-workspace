from pathlib import Path
import ast,csv,datetime,hashlib,json,math,re,statistics
P=Path(__file__).resolve().parent;R=P.parents[1];E=R/'experiments/EXP-006';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checked=0;windows=[];patches=0
T=ast.parse((P/'verify-round016.py').read_text());node=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name=='apply_unified');scope={'re':re};exec(compile(ast.Module(body=[node],type_ignores=[]),'<patch-reconstruct>','exec'),scope);apply=scope['apply_unified']
def check(p,h):
 global checked
 assert sha(p)==h,str(p.relative_to(R));checked+=1
def row(r,root,mode='name'):
 if mode=='paths':
  check(R/r['stdout'],r['stdout_sha256']);check(R/r['stderr'],r['stderr_sha256'])
 elif mode=='csv':
  check(root/r['csv'],r['csv_sha256']);check(root/r['stderr'],r['stderr_sha256'])
 else:
  check(root/(r['name']+'.stdout'),r['stdout_sha256']);check(root/(r['name']+'.stderr'),r['stderr_sha256'])
 if 'started_utc' in r:
  a=datetime.datetime.fromisoformat(r['started_utc']);b=datetime.datetime.fromisoformat(r['ended_utc']);assert b>=a and (b-a).total_seconds()<121;windows.append((a,b,r.get('name',r.get('stage','?'))))
def snapshots(m):
 for d in m['snapshots'].values():
  for n,h in d['files'].items():check(R/d['path']/n,h)
# Prior immutable evidence, shared ledgers excluded because this round updates them.
prior=json.loads((P/'ROUND-018-PRIOR-AUDIT.json').read_text())
for n,h in prior['sha256'].items():
 if n not in {'experiments/NEXT-STEPS.md','experiments/token-ledger.tsv'}:check(R/n,h)
# These two shared ledgers were intentionally updated at handoff; initial hashes
# remain in PRIOR-AUDIT, and final hashes belong to ROUND-018-SHA256.
for rel in ['BOUNDARY-025','BOUNDARY-025/confirmation']:
 D=P/rel;m=json.loads((D/'manifest.json').read_text());assert m['status']=='complete';check(D/'PLAN.md',m['plan_sha256']);snapshots(m)
 for r in m['runs']:assert r['returncode']==0;row(r,D)
 for v,h in m['binaries'].items():a,b=v.rsplit('-',1);check(R/m['snapshots'][a]['path']/'build'/b,h)
 for v,d in m['snapshots'].items():assert apply('',(D/'oracle.patch').read_text())==(R/d['path']/'tests/partial_batch_promotion_oracle.c').read_text();patches+=1
 for r in m['runs']:
  if not r['stage'].startswith('seed'):continue
  s=(D/(r['name']+'.stdout')).read_text();lines=[x for x in s.splitlines() if x.startswith('MATRIX ')];assert len(lines)==18
  seen=set()
  for line in lines:
   v=dict(x.split('=') for x in line.split()[1:]);n=int(v['lanes']);mode=int(v['mode']);expected=sum(1<<j for j in range(n) if mode==0 or (mode==2 and j%2==0));assert int(v['mask'],16)==expected and int(v['remaining'])==n-1 and v['promoted']=='1';seen.add((n,mode))
  assert seen=={(n,mode) for n in [1,2,3,7,15,16] for mode in range(3)}
D=P/'BOUNDARY-025/faults';m=json.loads((D/'manifest.json').read_text())
base=json.loads((P/'BOUNDARY-025/manifest.json').read_text());old=(R/base['snapshots']['control']['path']/'src/zset_btree.c').read_text()
for f in m:
 assert f['detected'];check(R/f['snapshot']/'src/zset_btree.c',f['source_sha256']);assert apply(old,(D/(f['name']+'.patch')).read_text())==(R/f['snapshot']/'src/zset_btree.c').read_text();patches+=1
 for r in f['runs']:row(dict(r,name=f['name']+'-'+r['stage']),D)
for rel in ['HARNESS-007','HARNESS-007/attempt-002']:
 D=P/rel;f=json.loads((D/'freeze.json').read_text());m=json.loads((D/'validation.json').read_text());check(D/'PLAN.md',m['plan_sha256']);check(D/'freeze.json',m['freeze_sha256'])
 for n,h in f['files'].items():check(R/f['snapshot']/n,h)
 assert apply('',(D/'harness.patch').read_text())==(R/f['snapshot']/'bench/batch_lookup.c').read_text();patches+=1
 for r in m['runs']:row(r,D/'raw')
 if rel.endswith('attempt-002'):assert m['status']=='complete' and m['cells']==dict(release=540,sanitize=540)
 else:assert m['runs'][-1]['name']=='release-0000';v=next(csv.DictReader((D/'raw/release-0000.stdout').open()));assert v['elapsed_ns']=='0'
D=P/'HARNESS-007/attempt-002/faults';m=json.loads((D/'manifest.json').read_text());base=json.loads((D.parent/'freeze.json').read_text());old=(R/base['snapshot']/'bench/batch_lookup.c').read_text()
for f in m:
 assert f['detected'];assert apply(old,(D/(f['name']+'.patch')).read_text())==(R/f['snapshot']/'bench/batch_lookup.c').read_text();patches+=1
 for r in f['runs']:row(r,D)
# Qualification and both fixed comparison schedules, including independent raw effects.
intervals=0;timings=0
for D in [P/'AA-012',E/'bench-results/screen',E/'bench-results/confirm']:
 m=json.loads((D/'manifest.json').read_text());assert m['status']=='complete';summary=json.loads((D/'summary.json').read_text());rs=m['runs'];timings+=len(rs)+len(m.get('warmup',[]))
 for r in rs+m.get('warmup',[]):row(r,D,'csv');assert r['returncode']==0
 for item in summary['results']:
  subset=[r for r in rs if r['cell']==item['cell'] and r['seed']==item['seed'] and ('variant' not in item or r['variant']==item['variant'])]
  for key,target in [('elapsed_ns','wall_percent'),('thread_elapsed_ns','thread_percent')]:
   values=[]
   for block in range(1,m['blocks']+1):
    group=[r for r in subset if r['block']==block];assert ''.join(r['label'] for r in group)=='ABBA';v=[int(next(csv.DictReader((D/r['csv']).open()))[key]) for r in group];values.append(100*((v[1]+v[2])/(v[0]+v[3])-1))
   avg=statistics.mean(values);half=(4.302652729911275 if m['blocks']==3 else 2.570581835636305)*statistics.stdev(values)/math.sqrt(len(values));assert values==item[target]['effects']
   for k,x in [('mean',avg),('low',avg-half),('high',avg+half)]:assert abs(item[target][k]-x)<1e-10
   intervals+=1
# Diagnostic profile calibration/capture command windows and symbols.
profiles=0;calibrations=0
for D in [P/'PROFILE-004',E/'profile-results']:
 m=json.loads((D/'manifest.json').read_text());assert m['status']=='complete';check(D/'PLAN.md',m['plan_sha256'])
 for n,h in m['files'].items():check(R/m['snapshot']/n,h)
 for r in m['runs']:row(r,D,'paths');assert r['returncode']==0
 assert len(m['calibrations'])==2 and all(z['pass'] for z in m['calibrations']);assert len(m['captures'])==8 and all(z['sufficient'] and z['unknown']==0 for z in m['captures']);profiles+=8;calibrations+=2
# Every candidate frozen source and patch, including earlier populations.
for id in ['EXP-002','EXP-003','EXP-004','EXP-005','EXP-006']:
 D=R/'experiments'/id;f=json.loads((D/'freeze.json').read_text());root=R/f['snapshot_root'];old=(root/'control/src/zset_btree.c').read_text()
 for v,files in f['files'].items():
  for n,h in files.items():check(root/v/n,h)
 for v in ['A','B','C']:assert apply(old,(D/'variants'/v/'candidate.patch').read_text())==(root/v/'src/zset_btree.c').read_text();patches+=1
 assert (R/'src/zset_btree.c').read_text()==old
m=json.loads((E/'validation.json').read_text());assert m['status']=='complete';check(E/'PLAN.md',m['plan_sha256'])
for r in m['runs']:row(r,E/'validation');assert r['returncode']==0
D=E/'tag-guard';m=json.loads((D/'manifest.json').read_text());assert m['status']=='complete' and m['fault_detected'];snapshots(m)
for r in m['runs']:row(r,D)
old=(R/m['snapshots']['C']['path']/'src/zset_btree.c').read_text();assert apply(old,(D/'overread.patch').read_text())==(R/m['snapshots']['fault']['path']/'src/zset_btree.c').read_text();patches+=1
for r in json.loads((E/'profile-results/codegen.json').read_text()):
 row(dict(r,name=r['variant']+'-assembly-build'),E/'profile-results');check(R/r['assembly'],r['assembly_sha256']);assert r['memchr_calls']==(1 if r['variant']=='control' else 0)
windows.sort()
for x,y in zip(windows,windows[1:]):assert x[1]<=y[0],(x,y)
result=dict(status='pass',sha256_checks=checked,serial_command_windows=len(windows),timing_windows=timings,profile_captures=profiles,calibrations=calibrations,raw_derived_intervals=intervals,patch_reconstructions=patches,all_prior_optimization_patches=12,new_optimization_patches=3,source_selection='NONE',experiment006='C/PARK')
(P/'ROUND-018-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
