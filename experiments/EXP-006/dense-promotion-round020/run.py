from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/experiment006-dense-promotion-round020';F=json.loads((P.parent/'freeze.json').read_text())
assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
parent=R/'scratch/overnight-boundary-025/control/tests/partial_batch_promotion_oracle.c';assert sha(parent)=='15d57ede3f96e8e1f7b53def545153b447ee5a381c0adb51ba185ae6d70c87de'
M=dict(status='preparing',base_commit=F['base_commit'],provenance='uncommitted isolated snapshots; exact EXP-006 source',plan_sha256=sha(P/'PLAN.md'),driver_sha256=sha(Path(__file__)),oracle_sha256=sha(P/'dense_promotion_oracle.c'),patch_sha256=sha(P/'oracle.patch'),parent_oracle=str(parent.relative_to(R)),parent_oracle_sha256=sha(parent),parent_freeze_sha256=sha(P.parent/'freeze.json'),snapshots={},runs=[],binaries={})
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for v in ['control','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'][v].items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(P/'dense_promotion_oracle.c',B/'tests/dense_promotion_oracle.c')
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M.update(status='frozen',frozen_utc=utc());save();start=time.monotonic()
for phase,seed,debug in [('discovery',93503,True),('confirmation',93521,False)]:
 for v,d in M['snapshots'].items():
  B=R/d['path']
  for kind in ['native','sanitize']:
   flags=['-O3'] if kind=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];binary='build/'+phase+'-'+kind
   cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer']+(['-DREDIS_DEBUG'] if debug else [])+flags+['tests/dense_promotion_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
   for stage,args in [('build',cmd),('run',[binary,str(seed)])]:
    if time.monotonic()-start>600 or datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-10-18T06:26:00+00:00'):M.update(status='budget-exhausted',ended_utc=utc());save();raise SystemExit(3)
    tag='-'.join([phase,v,kind,stage]);row=dict(name=tag,phase=phase,variant=v,kind=kind,stage=stage,seed=seed,debug=debug,command=args,cwd=d['path'],started_utc=utc());M['active_command']=row;save();raw=B/(tag+'.raw.stderr')
    with (P/(tag+'.stdout')).open('w') as out,raw.open('w') as err:
     try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
     except subprocess.TimeoutExpired:rc='timeout'
    (P/(tag+'.stderr')).write_text(raw.read_text().replace(str(R),'<workspace>'))
    row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')),raw_stderr=str(raw.relative_to(R)),raw_stderr_sha256=sha(raw));M['runs'].append(row);M.pop('active_command');save()
    if rc!=0:M.update(status='failed',ended_utc=utc());save();raise SystemExit(tag+' failed '+str(rc))
    if stage=='run':
     text=(P/(tag+'.stdout')).read_text();assert text.splitlines()[-1].startswith('PASS seed='+str(seed)+' ')
     lines=[l for l in text.splitlines() if l.startswith('MATRIX ')];assert len(lines)==36 and 'dense_hits=68' in lines[-1]
    else:M['binaries'][str((B/binary).relative_to(R))]=sha(B/binary);save()
    print(tag,'PASS',flush=True)
 rows=[r for r in M['runs'] if r['phase']==phase and r['stage']=='run'];assert len(rows)==4
 assert len({(P/(r['name']+'.stdout')).read_text().split('digest=')[-1].strip() for r in rows})==1
 M[phase+'_complete_utc']=utc();save()
for d in M['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
M.update(status='complete',ended_utc=utc(),semantic_cells=8,builds=8);save();print('COMPLETE 8 semantic cells',flush=True)
