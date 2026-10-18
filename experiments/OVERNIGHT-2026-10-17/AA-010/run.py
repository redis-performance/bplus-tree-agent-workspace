from pathlib import Path
import csv,hashlib,json,subprocess,time,os,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'HARNESS-005/freeze.json').read_text());S=R/F['snapshot'];B=S/'build/release/iterator-modes'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
CELLS=[dict(name=name,direction=d,encoding=e,construction=c,bytes=16,mask=m) for name,e,c,d,m in [('int-asc-f4','integer','ascending','forward',4),('int-desc-f4','integer','descending','forward',4),('int-desc-r4','integer','descending','reverse',4),('zero-asc-f4','alternating-zero','ascending','forward',4),('zero-desc-f4','alternating-zero','descending','forward',4),('zero-desc-r4','alternating-zero','descending','reverse',4),('zero-desc-f6','alternating-zero','descending','forward',6),('zero-desc-f7','alternating-zero','descending','forward',7)]]
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for n,h in F['files'].items():assert sha(S/n)==h
assert sha(B)==json.loads((P.parent/'HARNESS-005/binaries.json').read_text())['release']
M=dict(started_utc=utc(),status='running',freeze_sha256=sha(P.parent/'HARNESS-005/freeze.json'),plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),binary=str(B.relative_to(R)),binary_sha256=sha(B),cells=CELLS,seeds=[31031,31043],blocks=6,warmup=[],runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(cell,seed,block,step,label,warmup=False):
 name='warmup' if warmup else f'{cell["name"]}-seed{seed}-b{block}-s{step}-{label}'
 cmd=[str(B.relative_to(R)),'--size','100000','--ops',str(1000000 if warmup else 20000000),'--seed',str(seed),'--warmup-passes','3','--direction',cell['direction'],'--encoding',cell['encoding'],'--construction',cell['construction'],'--member-bytes',str(cell['bytes']),'--mask',str(cell['mask'])]
 out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr');start=time.monotonic();row=dict(cell=cell['name'],seed=seed,block=block,step=step,label=label,command=cmd,started_utc=utc(),load_before=os.getloadavg())
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,elapsed_seconds=time.monotonic()-start,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['warmup' if warmup else 'runs'].append(row);save();return rc==0
save();ok=run(CELLS[0],31031,0,0,'warmup',True);start=time.monotonic()
for block in range(1,7):
 if not ok:break
 offset=(block-1)%len(CELLS)
 for seed in ([31031,31043] if block%2 else [31043,31031]):
  if not ok:break
  for cell in CELLS[offset:]+CELLS[:offset]:
   for step,label in enumerate('ABBA',1):
    if time.monotonic()-start>600:ok=False;M['status']='budget-exhausted';break
    ok=run(cell,seed,block,step,label)
    if not ok:M['status']='failed';break
   if not ok:break
  print(block,seed,len(M['runs']),ok,flush=True)
M.update(ended_utc=utc(),seconds=time.monotonic()-start,binary_sha256_after=sha(B))
if ok:M['status']='complete'
assert M['binary_sha256']==M['binary_sha256_after']
for n,h in F['files'].items():assert sha(S/n)==h
save()
