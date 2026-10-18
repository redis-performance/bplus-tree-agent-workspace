from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os,time
P=Path(__file__).resolve().parent;R=P.parents[1];S=R/'scratch/exp-002';F=json.loads((P/'freeze.json').read_text())
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'confirmation.json').exists();V=json.loads((P/'validation.json').read_text());assert len(V)==64 and all(r['returncode']==0 for r in V)
for v,files in F['files'].items():
 for name,h in files.items():assert sha(S/v/name)==h
bins={v:str((S/v/'build/release/bench').relative_to(R)) for v in F['files']};hashes={v:sha(R/b) for v,b in bins.items()}
m=dict(status='running',started_utc=utc(),plan_sha256=sha(P/'CONFIRMATION-PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),binaries=bins,binary_hashes=hashes,runs=[])
def save():(P/'confirmation.json').write_text(json.dumps(m,indent=2)+'\n')
save();begin=time.monotonic()
for block in range(1,4):
 vs=['C'];offset=0
 for variant in vs[offset:]+vs[:offset]:
  for size in ([16,320] if block%2 else [320,16]):
   for step,label in enumerate('ABBA'):
    v='control' if label=='A' else variant;name=f'confirm-b{block}-{variant}-{size}-{step}-{label}'
    out=P/'bench-results'/(name+'.csv');err=P/'bench-results'/(name+'.stderr')
    cmd=[bins[v],'--case','iterate','--size','100000','--ops','50000000','--member-bytes',str(size),'--seed','4507','--query-seed','4603','--query-order','independent','--warmup-passes','10']
    row=dict(block=block,variant=variant,member_bytes=size,step=step,label=label,binary_variant=v,command=cmd,started_utc=utc(),load_before=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)))
    with out.open('w') as so,err.open('w') as se:
     try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=min(120,max(.01,120-(time.monotonic()-begin))));rc=q.returncode
     except subprocess.TimeoutExpired:rc='timeout'
    row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv_sha256=sha(out),stderr_sha256=sha(err));m['runs'].append(row);save()
    if rc!=0:m['status']='failed';save();raise SystemExit(1)
  print('block',block,'variant',variant,'rows',len(m['runs']),flush=True)
for v,b in bins.items():assert sha(R/b)==hashes[v]
for v,files in F['files'].items():
 for name,h in files.items():assert sha(S/v/name)==h
m.update(status='complete',ended_utc=utc(),elapsed_seconds=time.monotonic()-begin);save()
