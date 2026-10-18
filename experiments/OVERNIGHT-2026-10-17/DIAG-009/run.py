from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os,time
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-009/base';S=B.parent/'raw'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'manifest.json').exists() and not S.exists();S.mkdir()
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
binary=B/'build/release/calibrate';m=dict(started_utc=utc(),status='running',binary=str(binary.relative_to(R)),binary_sha256=sha(binary),plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),runs=[])
def save():(P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();begin=time.monotonic();modes=[1000,3001,17011]
for block in range(1,7):
 offset=(block-1)%3
 for mode in modes[offset:]+modes[:offset]:
  name=f'b{block}-{mode}';out=S/(name+'.csv');err=S/(name+'.stderr');cmd=[str(binary.relative_to(R)),'400000000']
  row=dict(name=name,block=block,profile_usec=mode,command=cmd,started_utc=utc(),load_before=os.getloadavg(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)))
  with out.open('w') as so,err.open('w') as se:
   try:r=subprocess.run(cmd,cwd=R,env=dict(os.environ,PROFILE_USEC=str(mode)),stdout=so,stderr=se,timeout=min(120,max(.01,120-(time.monotonic()-begin))));code=r.returncode
   except subprocess.TimeoutExpired:code='timeout'
  row.update(returncode=code,ended_utc=utc(),load_after=os.getloadavg(),stdout_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save()
  if code!=0:m['status']='failed';save();raise SystemExit(1)
 print('block',block,'processes',len(m['runs']),flush=True)
m.update(status='complete',ended_utc=utc(),elapsed_seconds=time.monotonic()-begin,binary_sha256_after=sha(binary));assert m['binary_sha256_after']==m['binary_sha256']
for name,h in F['files'].items():assert sha(B/name)==h
save()
