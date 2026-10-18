from pathlib import Path
import json,hashlib,subprocess,time,datetime,os
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'attempt-002/freeze.json').read_text());S=R/F['snapshot_root'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();V=json.loads((P/'validation.json').read_text());assert len(V)==1028 and all(r['returncode']==0 for r in V);assert json.loads((P/'codegen-audit.json').read_text())['pass_all'];assert not (P/'manifest.json').exists();(P/'raw').mkdir()
for pad,files in F['files'].items():
 for n,h in files.items():assert sha(S/pad/n)==h
bins={pad:str((S/str(pad)/'build/release').relative_to(R)) for pad in [0,16,32,48]};hashes={pad:sha(R/b) for pad,b in bins.items()};assert all(hashes[pad]==F['binaries'][f'{pad}-release'] for pad in bins)
M=dict(status='running',plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'attempt-002/freeze.json'),codegen_sha256=sha(P/'codegen-audit.json'),binaries=bins,binary_hashes=hashes,runs=[],warmups=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def one(name,pad,mask,seed,ops,meta,section):
 cmd=[bins[pad],'--mask',str(mask),'--size','100000','--ops',str(ops),'--seed',str(seed),'--direction','forward','--encoding','integer','--member-bytes','16','--warmup-passes','3'];out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr');row=dict(**meta,pad=pad,command=cmd,started_utc=utc(),load_before=os.getloadavg())
 with out.open('w') as so,err.open('w') as se:
  try:rc=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M[section].append(row);save();assert rc==0,name
save();start=time.monotonic();cells=[(0,6)]+[(p,m) for p in [16,32,48] for m in [4,6,7]]
for pad in bins:one(f'warmup-{pad}',pad,6,19103,1000000,dict(prospective=True),'warmups')
for seed in [19103,19139]:
 for block in range(1,7):
  off=block-1
  for target,mask in cells[off:]+cells[:off]:
   for step,label in enumerate('ABBA',1):
    assert time.monotonic()-start<600
    pad=0 if label=='A' else target;name=f's{seed}-b{block}-p{target}-m{mask}-{step}-{label}';one(name,pad,mask,seed,20000000,dict(seed=seed,block=block,target=target,mask=mask,step=step,label=label),'runs')
  print(seed,block,len(M['runs']),flush=True)
for pad,b in bins.items():assert sha(R/b)==hashes[pad]
M['status']='complete';save()
