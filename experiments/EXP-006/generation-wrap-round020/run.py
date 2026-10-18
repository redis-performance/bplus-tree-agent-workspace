from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];S=R/'scratch/experiment006-generation-wrap-round020';F=json.loads((P.parent/'freeze.json').read_text())
assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
parent=json.loads((P/'parent.json').read_text());assert sha(R/parent['oracle'])==parent['oracle_sha256'];assert sha(R/parent['manifest'])==parent['manifest_sha256']
M=dict(status='preparing',base_commit=F['base_commit'],provenance='uncommitted isolated exact source snapshots',parent=parent,plan_sha256=sha(P/'PLAN.md'),driver_sha256=sha(Path(__file__)),oracle_sha256=sha(P/'batch_generation_oracle.c'),patch_sha256=sha(P/'oracle.patch'),snapshots={},runs=[],binaries={})
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'][v].items():
  src=R/F['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(P/'batch_generation_oracle.c',B/'tests/batch_generation_oracle.c')
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir()
M.update(status='frozen',frozen_utc=utc());save();start=time.monotonic()
for v,d in M['snapshots'].items():
 B=R/d['path']
 for kind in ['native','sanitize']:
  flags=['-O3'] if kind=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];binary='build/'+kind
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG']+flags+['tests/batch_generation_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  for stage,args in [('build',cmd),('run',[binary])]:
   if time.monotonic()-start>300 or datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime.fromisoformat('2026-10-18T06:27:00+00:00'):M.update(status='budget-exhausted',ended_utc=utc());save();raise SystemExit(3)
   tag='-'.join([v,kind,stage]);row=dict(name=tag,variant=v,kind=kind,stage=stage,command=args,cwd=d['path'],started_utc=utc());M['active_command']=row;save();raw=B/(tag+'.raw.stderr')
   with (P/(tag+'.stdout')).open('w') as out,raw.open('w') as err:
    try:rc=subprocess.run(args,cwd=B,stdout=out,stderr=err,timeout=120).returncode
    except subprocess.TimeoutExpired:rc='timeout'
   (P/(tag+'.stderr')).write_text(raw.read_text().replace(str(R),'<workspace>'))
   row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(P/(tag+'.stdout')),stderr_sha256=sha(P/(tag+'.stderr')),raw_stderr=str(raw.relative_to(R)),raw_stderr_sha256=sha(raw));M['runs'].append(row);M.pop('active_command');save()
   if rc!=0:M.update(status='failed',ended_utc=utc());save();raise SystemExit(tag+' failed '+str(rc))
   if stage=='run':
    text=(P/(tag+'.stdout')).read_text();last=text.splitlines()[-1];assert last.startswith('PASS fixtures=4 checks=262188 results=24254190 resizes=262160 wraps=4 digest=')
    assert text.count('WRAP seed=')==4 and text.count('FIXTURE seed=')==4
   else:M['binaries'][str((B/binary).relative_to(R))]=sha(B/binary);save()
   print(tag,'PASS',flush=True)
rows=[r for r in M['runs'] if r['stage']=='run'];assert len(rows)==8
assert len({(P/(r['name']+'.stdout')).read_text().split('digest=')[-1].strip() for r in rows})==1
for d in M['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
M.update(status='complete',ended_utc=utc(),semantic_cells=8,builds=8);save();print('COMPLETE 8 cells; no timing claim',flush=True)
