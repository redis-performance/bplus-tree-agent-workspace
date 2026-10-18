from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,time
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'manifest.json').read_text());G=json.loads((R/'experiments/EXP-004/freeze.json').read_text());S=R/'scratch/overnight-counters-006-fresh';assert not S.exists();S.mkdir();D=P/'fresh';D.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='preparing',base_commit=F['base_commit'],plan_sha256=sha(P/'FRESH-PLAN.md'),snapshots={},runs=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for policy in ['exact','round16']:
 desc=F['snapshots'][policy]
 for v in ['control','A','B','C']:
  name=policy+'-'+v;B=S/name;B.mkdir()
  for n,h in desc['files'].items():
   src=R/desc['path']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
  if v!='control':
   src=R/G['snapshot_root']/v/'src/zset_btree.c';assert sha(src)==G['files'][v]['src/zset_btree.c'];shutil.copy2(src,B/'src/zset_btree.c')
  p=B/'tests/diagnostic.c';s=p.read_text();s=s.replace('31121,31123','31133,31139').replace('n<=96','n<=98').replace('exercise(n,lengths[l],d,seeds[s])','exercise(n<=96?n:n==97?97:513,lengths[l],d,seeds[s])').replace('289060','325860').replace('86570560','163246200');p.write_text(s)
  M['snapshots'][name]=dict(path=str(B.relative_to(R)),policy=policy,variant=v,quantum=desc['quantum'],files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M['status']='frozen';M['frozen_utc']=utc();save();start=time.monotonic()
for name,desc in M['snapshots'].items():
 B=R/desc['path']
 for kind in ['release','sanitize']:
  if time.monotonic()-start>480:M['status']='budget-exhausted';save();raise SystemExit(3)
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];label=name+'-'+kind
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',f'-DCAPACITY_QUANTUM={desc["quantum"]}',*flags,'tests/diagnostic.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+kind]
  for stage,args in [('build',cmd),('run',['build/'+kind])]:
   tag=label+'-'+stage;row=dict(name=tag,policy=desc['policy'],variant=desc['variant'],kind=kind,stage=stage,command=args,cwd=desc['path'],started_utc=utc())
   with (D/(tag+'.stdout')).open('w') as out,(D/(tag+'.stderr')).open('w') as err:
    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(D/(tag+'.stdout')),stderr_sha256=sha(D/(tag+'.stderr')));M['runs'].append(row);save();assert rc==0,tag
  M.setdefault('binaries',{})[label]=sha(B/'build'/kind);save();print(label,'PASS',flush=True)
for desc in M['snapshots'].values():
 for n,h in desc['files'].items():assert sha(R/desc['path']/n)==h
M['status']='complete';save()
summary=dict(status='pass',cells=16,fixtures_per_cell=1980,modelchecks_per_cell=325860,exact_results_per_cell=163246200,policy_equal={})
for policy in ['exact','round16']:
 outputs=[(D/(r['name']+'.stdout')).read_bytes() for r in M['runs'] if r['stage']=='run' and r['policy']==policy]
 assert len(outputs)==8;summary['policy_equal'][policy]=len(set(outputs))==1
 if not summary['policy_equal'][policy]:summary['status']='physical_equality_unsupported'
(D/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
