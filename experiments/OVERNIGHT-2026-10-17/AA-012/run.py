from pathlib import Path
import datetime,hashlib,json,os,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];H=P.parent/'HARNESS-007/attempt-002';F=json.loads((H/'freeze.json').read_text());V=json.loads((H/'validation.json').read_text());assert V['status']=='complete'
assert json.loads((H/'faults/summary.json').read_text())['status']=='pass'
B=R/F['snapshot'];binary=B/'build/batch/release';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
for n,h in F['files'].items():assert sha(B/n)==h
assert sha(binary)==V['binaries']['release'];assert not (P/'manifest.json').exists();(P/'raw').mkdir()
C=[dict(name=n,layout=l,bytes=b,batch=k) for n,l,b,k in [('hit16-b16','hit',16,16),('hit16-b1','hit',16,1),('hit320-b16','hit',320,16),('miss16-b16','miss',16,16),('mixed16-b16','mixed',16,16)]]
M=dict(status='running',base_commit=F['base_commit'],freeze_sha256=sha(H/'freeze.json'),plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),binary=str(binary.relative_to(R)),binary_sha256=sha(binary),cells=C,seeds=[[80703,80719],[80711,80723]],blocks=6,warmup=[],runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(c,seed,qseed,block,step,label,warm=False):
 tag='warmup' if warm else f'{c["name"]}-s{seed}-b{block}-{step}{label}'
 cmd=[str(binary.relative_to(R)),'--size','8192','--ops',str(100000 if warm else 2000000),'--member-bytes',str(c['bytes']),'--seed',str(seed),'--query-seed',str(qseed),'--batch-size',str(c['batch']),'--layout',c['layout'],'--warmup-passes','3']
 row=dict(name=tag,cell=c['name'],seed=seed,query_seed=qseed,block=block,step=step,label=label,command=cmd,started_utc=utc(),load_before=os.getloadavg())
 out=P/'raw'/(tag+'.csv');err=P/'raw'/(tag+'.stderr')
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['warmup' if warm else 'runs'].append(row);save();return rc==0
save();ok=run(C[0],80703,80719,0,0,'warmup',True);start=time.monotonic()
for block in range(1,7):
 if not ok:break
 offset=(block-1)%len(C)
 for seed,qseed in (M['seeds'] if block%2 else M['seeds'][::-1]):
  if not ok:break
  for c in C[offset:]+C[:offset]:
   for step,label in enumerate('ABBA',1):
    if time.monotonic()-start>360:ok=False;M['status']='budget-exhausted';break
    ok=run(c,seed,qseed,block,step,label)
    if not ok:M['status']='failed';break
   if not ok:break
  print(block,seed,len(M['runs']),ok,flush=True)
M['ended_utc']=utc();M['binary_sha256_after']=sha(binary);assert sha(binary)==M['binary_sha256']
for n,h in F['files'].items():assert sha(B/n)==h
if ok:M['status']='complete'
save()
