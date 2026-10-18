from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,time
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((P/'freeze.json').read_text());V=json.loads((P/'validation.json').read_text());assert V['status']=='complete';phase=sys.argv[1];assert phase in ['screen','confirm'];S=R/F['snapshot_root'];D=P/'bench-results'/phase;D.mkdir();(D/'raw').mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
allcells=[dict(name=n,layout=l,bytes=b,batch=k) for n,l,b,k in [('mixed16-b16','mixed',16,16),('hit320-b16','hit',320,16),('hit16-b16','hit',16,16),('hit16-b1','hit',16,1),('miss16-b16','miss',16,16)]]
variants=['A','B','C'];seeds=[[80703,80719],[80711,80723]];blocks=3;cells=allcells
if phase=='confirm':
 select=json.loads((P/'bench-results/screen/summary.json').read_text())['confirmation_choice'];variants=variants if select=='NONE' else [select];seeds=[[80803,80819],[80811,80823]];blocks=6;cells=allcells[:2]
for v in ['control',*variants]:
 for n,h in F['files'][v].items():assert sha(S/v/n)==h
 assert sha(S/v/'build/release-batch')==V['binaries'][v+'-release-batch']
M=dict(status='running',phase=phase,plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),variants=variants,cells=cells,seeds=seeds,blocks=blocks,runs=[],binaries={v:V['binaries'][v+'-release-batch'] for v in ['control',*variants]})
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
start=time.monotonic();save()
for block in range(1,blocks+1):
 offset=(block-1)%len(cells);vshift=(block-1)%len(variants)
 for seed,qseed in (seeds if block%2 else seeds[::-1]):
  for c in cells[offset:]+cells[:offset]:
   for v in variants[vshift:]+variants[:vshift]:
    for step,label in enumerate('ABBA',1):
     if time.monotonic()-start>360 or datetime.datetime.now(datetime.timezone.utc)>=datetime.datetime(2026,10,18,5,33,tzinfo=datetime.timezone.utc):M['status']='budget-exhausted';save();raise SystemExit(3)
     source='control' if label=='A' else v;binary=S/source/'build/release-batch';tag=f'{v}-{c["name"]}-s{seed}-b{block}-{step}{label}';args=[str(binary.relative_to(R)),'--size','8192','--ops','2000000','--member-bytes',str(c['bytes']),'--batch-size',str(c['batch']),'--layout',c['layout'],'--seed',str(seed),'--query-seed',str(qseed),'--warmup-passes','3'];out=D/'raw'/(tag+'.csv');err=D/'raw'/(tag+'.stderr');r=dict(name=tag,variant=v,source=source,cell=c['name'],seed=seed,query_seed=qseed,block=block,step=step,label=label,command=args,started_utc=utc(),load_before=os.getloadavg())
     with out.open('w') as o,err.open('w') as e:
      try:rc=subprocess.run(args,cwd=R,stdout=o,stderr=e,timeout=120).returncode
      except subprocess.TimeoutExpired:rc='timeout'
     r.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(D)),stderr=str(err.relative_to(D)),csv_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save()
     if rc!=0:M['status']='failed';save();raise SystemExit(1)
  print(phase,block,seed,len(M['runs']),flush=True)
for v in ['control',*variants]:
 for n,h in F['files'][v].items():assert sha(S/v/n)==h
 assert sha(S/v/'build/release-batch')==M['binaries'][v]
M['status']='complete';M['ended_utc']=utc();save()
