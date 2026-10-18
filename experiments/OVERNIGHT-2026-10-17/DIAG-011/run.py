from pathlib import Path
import json,hashlib,subprocess,time,datetime,os
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();V=json.loads((P/'validation.json').read_text());assert len(V)==388 and all(r['returncode']==0 for r in V);assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
bins={v:str((S/v/'build/release').relative_to(R)) for v in ['control','A']};hashes={v:sha(R/b) for v,b in bins.items()};old=json.loads((P/'binaries.json').read_text());assert all(hashes[v]==old[v+'-release'] for v in bins)
M=dict(status='running',plan_sha256=sha(P/'PLAN.md'),erratum_sha256=sha(P/'VALIDATION-ERRATUM.md'),freeze_sha256=sha(P/'freeze.json'),binaries=bins,binary_hashes=hashes,runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
save();start=time.monotonic();cells=[(caller,mask) for caller in ['dynamic','fixed'] for mask in [4,6,7]]
for seed in [14107,14143]:
 for block in range(1,4):
  off=block-1
  for caller,mask in cells[off:]+cells[:off]:
   for step,label in enumerate('ABBA',1):
    assert time.monotonic()-start<300
    v='control' if label=='A' else 'A';name=f's{seed}-b{block}-{caller}-m{mask}-{step}-{label}';cmd=[bins[v],'--caller',caller,'--mask',str(mask),'--size','100000','--ops','100000000','--seed',str(seed),'--direction','forward','--encoding','integer','--member-bytes','16','--warmup-passes','3'];out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr');row=dict(seed=seed,block=block,caller=caller,mask=mask,step=step,label=label,variant=v,command=cmd,started_utc=utc(),load_before=os.getloadavg())
    with out.open('w') as so,err.open('w') as se:
     try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
     except subprocess.TimeoutExpired:rc='timeout'
    row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(row);save();assert rc==0,name
  print(seed,block,len(M['runs']),flush=True)
for v,b in bins.items():assert sha(R/b)==hashes[v]
M['status']='complete';save()
