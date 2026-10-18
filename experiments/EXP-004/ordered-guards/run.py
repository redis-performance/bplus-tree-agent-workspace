from pathlib import Path
import json,hashlib,subprocess,datetime,time,os,sys
P=Path(__file__).resolve().parent;R=P.parents[2];phase=sys.argv[1];assert phase in ['screen','confirm'];D=P/phase;D.mkdir();(D/'raw').mkdir();F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];Q=R/'experiments/OVERNIGHT-2026-10-17/AA-010';CELLS=json.loads((Q/'eligible.json').read_text());assert len(CELLS)==6
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();seeds=[31031,31043] if phase=='screen' else [31051,31063]
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 assert sha(S/v/'build/release/iterator-modes')==json.loads((P/v/'binaries.json').read_text())['release']
M=dict(status='running',phase=phase,started_utc=utc(),plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),freeze_sha256=sha(P/'freeze.json'),qualification_sha256=sha(Q/'summary.json'),cells=CELLS,seeds=seeds,blocks=3,binaries={v:sha(S/v/'build/release/iterator-modes') for v in F['files']},warmup=[],runs=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(v,c,seed,block,step,label,warmup=False):
 arm=v if label=='B' else 'control';binary=S/arm/'build/release/iterator-modes'
 name=f'{v}-{c["name"]}-s{seed}-b{block}-p{step}-{label}'
 cmd=[str(binary.relative_to(R)),'--size','100000','--ops',str(1000000 if warmup else 20000000),'--seed',str(seed),'--warmup-passes','3','--direction',c['direction'],'--encoding',c['encoding'],'--construction',c['construction'],'--member-bytes',str(c['bytes']),'--mask',str(c['mask'])]
 out=D/'raw'/(name+'.csv');err=D/'raw'/(name+'.stderr');started=utc();t=time.monotonic();row=dict(variant=v,arm=arm,cell=c['name'],seed=seed,block=block,step=step,label=label,command=cmd,started_utc=started,load_before=os.getloadavg())
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),seconds=time.monotonic()-t,load_after=os.getloadavg(),csv=str(out.relative_to(D)),stderr=str(err.relative_to(D)),csv_sha256=sha(out),stderr_sha256=sha(err));M['warmup' if warmup else 'runs'].append(row);save();return rc==0
save();ok=True
if phase=='screen':
 for v in ['control','A','B','C']:
  ok=run(v,CELLS[0],seeds[0],0,0,'B',True)
  if not ok:break
t=time.monotonic()
for block in range(1,4):
 if not ok:break
 variants=['A','B','C'];i=(block-1)%3;variants=variants[i:]+variants[:i];j=(block-1)%len(CELLS)
 for seed in (seeds if block%2 else list(reversed(seeds))):
  if not ok:break
  for v in variants:
   if not ok:break
   for c in CELLS[j:]+CELLS[:j]:
    for step,label in enumerate('ABBA',1):
     if time.monotonic()-t>480:ok=False;M['status']='budget-exhausted';break
     ok=run(v,c,seed,block,step,label)
     if not ok:M['status']='failed';break
    if not ok:break
   print(phase,block,seed,v,len(M['runs']),ok,flush=True)
if ok:M['status']='complete'
M.update(ended_utc=utc(),seconds=time.monotonic()-t)
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 assert sha(S/v/'build/release/iterator-modes')==M['binaries'][v]
save()
