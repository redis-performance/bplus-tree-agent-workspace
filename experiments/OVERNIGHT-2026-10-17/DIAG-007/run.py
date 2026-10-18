from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os,time
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-007/base'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
binary=B/'build/release/btree-bench';m=dict(started_utc=utc(),status='running',binary=str(binary.relative_to(R)),binary_sha256=sha(binary),plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),runs=[])
def save():(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();begin=time.monotonic();cells=[(16,0),(16,1),(320,0),(320,1)]
for block in range(1,7):
 rotate=(block-1)%4
 for size,miss in cells[rotate:]+cells[:rotate]:
  name=f'b{block}-{size}-{miss}';out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr')
  cmd=[str(binary.relative_to(R)),'100000','500000',str(size),'16',str(miss+1),'1409','10']
  row=dict(block=block,member_bytes=size,miss=miss,command=cmd,started_utc=utc(),load_before=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)))
  with out.open('w') as so,err.open('w') as se:
   try:r=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=min(120,max(.01,240-(time.monotonic()-begin))));code=r.returncode
   except subprocess.TimeoutExpired:code='timeout'
  row.update(returncode=code,ended_utc=utc(),load_after=os.getloadavg(),csv_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save()
  if code!=0:m['status']='failed';save();raise SystemExit(1)
 print('block',block,'processes',len(m['runs']),flush=True)
m.update(status='complete',ended_utc=utc(),elapsed_seconds=time.monotonic()-begin,binary_sha256_after=sha(binary));assert m['binary_sha256_after']==m['binary_sha256']
for name,h in F['files'].items():assert sha(B/name)==h
save()
