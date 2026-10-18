from pathlib import Path
import csv,hashlib,json,subprocess,time,os,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'HARNESS-004/freeze.json').read_text());S=R/F['snapshot'];B=S/'build/release/iterator-modes'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
CELLS=[dict(name=f'f-int16-m{m}',direction='forward',encoding='integer',bytes=16,mask=m) for m in range(8)]+[dict(name=f'r-int16-m{m}',direction='reverse',encoding='integer',bytes=16,mask=m) for m in [4,7]]+[dict(name='f-frac320-m7',direction='forward',encoding='fraction',bytes=320,mask=7),dict(name='r-wide320-m7',direction='reverse',encoding='wide',bytes=320,mask=7),dict(name='f-frac320-m4',direction='forward',encoding='fraction',bytes=320,mask=4),dict(name='f-wide320-m4',direction='forward',encoding='wide',bytes=320,mask=4)]
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(B)==json.loads((P.parent/'HARNESS-004/binaries.json').read_text())['release']
M=dict(started_utc=utc(),status='running',freeze_sha256=sha(P.parent/'HARNESS-004/freeze.json'),plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),binary=str(B.relative_to(R)),binary_sha256=sha(B),cells=CELLS,blocks=6,warmup=[],runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(cell,block,step,label,warmup=False):
 name='warmup' if warmup else f'{cell["name"]}-b{block}-s{step}-{label}'
 cmd=[str(B.relative_to(R)),'--size','100000','--ops',str(1000000 if warmup else 20000000),'--seed','7103','--warmup-passes','3','--direction',cell['direction'],'--encoding',cell['encoding'],'--member-bytes',str(cell['bytes']),'--mask',str(cell['mask'])]
 out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr');start=time.monotonic();row=dict(cell=cell['name'],block=block,step=step,label=label,command=cmd,started_utc=utc(),load_before=os.getloadavg())
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,elapsed_seconds=time.monotonic()-start,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['warmup' if warmup else 'runs'].append(row);save();return rc==0
save();ok=run(CELLS[4],0,0,'warmup',True);start=time.monotonic()
for block in range(1,7):
 if not ok:break
 offset=(block-1)%len(CELLS)
 for cell in CELLS[offset:]+CELLS[:offset]:
  for step,label in enumerate('ABBA',1):
   if time.monotonic()-start>600:ok=False;M['status']='budget-exhausted';break
   ok=run(cell,block,step,label)
   if not ok:M['status']='failed';break
  print(block,cell['name'],len(M['runs']),ok,flush=True)
  if not ok:break
M.update(ended_utc=utc(),seconds=time.monotonic()-start,binary_sha256_after=sha(B))
if ok:M['status']='complete'
assert M['binary_sha256']==M['binary_sha256_after']
for n,h in F['files'].items():assert sha(S/n)==h
save()
