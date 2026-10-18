from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,csv,os,time
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-006/base';S=B.parent/'raw'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'manifest.json').exists() and not S.exists();S.mkdir();(P/'raw').mkdir()
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
binary=B/'build/release/btree-bench';m=dict(started_utc=utc(),status='running',binary=str(binary.relative_to(R)),binary_sha256=sha(binary),plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),runs=[])
def save():(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();begin=time.monotonic();cells=[(16,10000000),(320,5000000)]
for block in range(1,7):
 for size,ops in (cells if block%2 else cells[::-1]):
  for slot,label in enumerate('ABBA'):
   mode='0' if label=='A' else '1000';name=f'b{block}-{size}-s{slot}-{label}';out=P/'raw'/(name+'.csv');err=S/(name+'.stderr')
   cmd=[str(binary.relative_to(R)),'--case','lookup-hit','--size','100000','--ops',str(ops),'--member-bytes',str(size),'--seed','1103','--query-seed','1201','--query-order','independent','--warmup-passes','10']
   row=dict(block=block,slot=slot,label=label,member_bytes=size,operations=ops,command=cmd,profile_usec=mode,started_utc=utc(),load_before=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(R)))
   with out.open('w') as so,err.open('w') as se:
    try:r=subprocess.run(cmd,cwd=R,env=dict(os.environ,PROFILE_USEC=mode),stdout=so,stderr=se,timeout=min(120,max(.01,240-(time.monotonic()-begin))));code=r.returncode
    except subprocess.TimeoutExpired:code='timeout'
   row.update(returncode=code,ended_utc=utc(),load_after=os.getloadavg(),csv_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save()
   if code!=0:m['status']='failed';save();raise SystemExit(1)
  print(block,size,len(m['runs']),flush=True)
m.update(status='complete',ended_utc=utc(),elapsed_seconds=time.monotonic()-begin,binary_sha256_after=sha(binary));assert m['binary_sha256_after']==m['binary_sha256']
for name,h in F['files'].items():assert sha(B/name)==h
save()
