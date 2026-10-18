from pathlib import Path
from datetime import datetime,timezone
import subprocess,shutil,json,hashlib,os,time
P=Path(__file__).resolve().parent;R=P.parents[1];S=R/'scratch/exp-002-profiles';assert not S.exists();S.mkdir()
F=json.loads((R/'experiments/OVERNIGHT-2026-10-17/PROFILE-003/freeze.json').read_text());E=json.loads((P/'freeze.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat();m=dict(status='preparing',plan_sha256=sha(P/'CONFIRMATION-PLAN.md'),runs=[],preparation=[],sources={})
def save():(P/'profile-results/manifest.json').write_text(json.dumps(m,indent=2)+'\n')
for v in ['control','C']:
 B=S/v;B.mkdir()
 for name,h in F['files'].items():
  src=R/F['snapshot']/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 src=R/E['snapshot_root']/v/'src/zset_btree.c';assert sha(src)==E['files'][v]['src/zset_btree.c'];shutil.copy2(src,B/'src/zset_btree.c')
 m['sources'][v]={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()};(B/'build/release').mkdir(parents=True)
 for step,cmd in [('build',['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3','bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/release/btree-bench']),('dsym',['dsymutil','build/release/btree-bench']),('assembly',['otool','-tvV','build/release/btree-bench'])]:
  out=S/f'{v}-{step}.stdout';err=S/f'{v}-{step}.stderr'
  with out.open('w') as so,err.open('w') as se:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120)
  row=dict(variant=v,step=step,command=cmd,cwd=str(B.relative_to(R)),returncode=q.returncode,stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));m['preparation'].append(row);save();assert q.returncode==0
m['status']='running';save();begin=time.monotonic()
for seed,qseed in [(4507,4603),(4801,4903)]:
 for v in ['control','C']:
  B=S/v;binary=B/'build/release/btree-bench';name=f'{v}-{seed}';out=S/(name+'.csv');err=S/(name+'.stderr')
  cmd=[str(binary.relative_to(R)),'--case','iterate','--size','100000','--ops','100000000','--member-bytes','16','--seed',str(seed),'--query-seed',str(qseed),'--query-order','independent','--warmup-passes','10']
  row=dict(name=name,variant=v,seed=seed,query_seed=qseed,case='iterate',member_bytes=16,interval_usec=1000,command=cmd,environment_overrides={'PROFILE_USEC':'1000'},started_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),binary=str(binary.relative_to(R)),binary_sha256=sha(binary))
  with out.open('w') as so,err.open('w') as se:q=subprocess.run(cmd,cwd=R,env=dict(os.environ,PROFILE_USEC='1000'),stdout=so,stderr=se,timeout=min(120,max(.01,120-(time.monotonic()-begin))))
  row.update(returncode=q.returncode,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save();assert q.returncode==0
m['status']='complete';save();print('PASS four matched descriptive captures')
