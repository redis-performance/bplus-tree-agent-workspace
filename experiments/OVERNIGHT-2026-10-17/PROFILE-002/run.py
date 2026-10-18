from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os,time,csv
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-profile-002/base';S=B.parent/'captures'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
F=json.loads((P/'freeze.json').read_text());v=json.loads((P/'validation.json').read_text())
assert len([r for r in v if r.get('criterion_met')])==2
for name,h in F['files'].items():assert sha(B/name)==h
assert not S.exists() and not (P/'manifest.json').exists();S.mkdir()
binary=B/'build/release/btree-bench';m=dict(started_utc=utc(),status='running',binary=str(binary.relative_to(R)),binary_sha256=sha(binary),plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),runs=[])
def save():(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();begin=time.monotonic()
for seed,qseed in [(503,701),(809,907)]:
 for interval in [1000,3001]:
  for case,size,ops in [('lookup-hit',16,50000000),('lookup-hit',320,10000000),('rank',16,10000000)]:
   name=f'{seed}-{interval}-{case}-{size}';out=S/(name+'.csv');err=S/(name+'.stderr')
   cmd=[str(binary.relative_to(R)),'--case',case,'--member-bytes',str(size),'--ops',str(ops),'--size','100000','--seed',str(seed),'--query-seed',str(qseed),'--query-order','independent','--warmup-passes','10']
   row=dict(name=name,seed=seed,query_seed=qseed,interval_usec=interval,case=case,member_bytes=size,operations=ops,command=cmd,environment_overrides={'PROFILE_USEC':str(interval)},started_utc=utc(),load_before=os.getloadavg(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)))
   with out.open('w') as so,err.open('w') as se:
    try:p=subprocess.run(cmd,cwd=R,env=dict(os.environ,PROFILE_USEC=str(interval)),stdout=so,stderr=se,timeout=min(120,max(.01,240-(time.monotonic()-begin))));code=p.returncode
    except subprocess.TimeoutExpired:code='timeout'
   row.update(returncode=code,ended_utc=utc(),load_after=os.getloadavg(),stdout_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save()
   print(name,code,flush=True)
   if code!=0:m['status']='failed';save();raise SystemExit(1)
   rs=list(csv.DictReader(out.open()));assert len(rs)==1
   assert int(rs[0]['operations'])==ops and int(rs[0]['checksum'])==ops*99999//2
m.update(status='complete',ended_utc=utc(),elapsed_seconds=time.monotonic()-begin,binary_sha256_after=sha(binary));assert m['binary_sha256']==m['binary_sha256_after']
for name,h in F['files'].items():assert sha(B/name)==h
save()
