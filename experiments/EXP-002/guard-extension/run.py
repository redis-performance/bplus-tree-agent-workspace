from pathlib import Path
import json,hashlib,subprocess,time,os,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];AA=R/'experiments/OVERNIGHT-2026-10-17/AA-006';CELLS=json.loads((AA/'manifest.json').read_text())['cells'];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert not (P/'manifest.json').exists();(P/'raw').mkdir()
bins={v:str((S/v/'build/release/iterator-modes').relative_to(R)) for v in F['files']};hashes={v:sha(R/b) for v,b in bins.items()}
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 val=json.loads((P/v/'validation.json').read_text());assert len(val)==1286 and all(r['returncode']==0 for r in val)
 assert hashes[v]==json.loads((P/v/'binaries.json').read_text())['release']
M=dict(status='running',started_utc=utc(),plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),aa_summary_sha256=sha(AA/'summary.json'),runner_sha256=sha(Path(__file__)),binaries=bins,binary_hashes=hashes,cells=CELLS,blocks=3,runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
save();start=time.monotonic();ok=True
for block in range(1,4):
 vs=['A','B','C'];off=block-1
 for v in vs[off:]+vs[:off]:
  for cell in CELLS[off:]+CELLS[:off]:
   for step,label in enumerate('ABBA',1):
    if time.monotonic()-start>600:M['status']='budget-exhausted';save();raise SystemExit(1)
    which='control' if label=='A' else v;name=f'b{block}-{v}-{cell["name"]}-s{step}-{label}'
    cmd=[bins[which],'--size','100000','--ops','20000000','--seed','7103','--warmup-passes','3','--direction',cell['direction'],'--encoding',cell['encoding'],'--member-bytes',str(cell['bytes']),'--mask',str(cell['mask'])]
    out=P/'raw'/(name+'.csv');err=P/'raw'/(name+'.stderr');row=dict(variant=v,cell=cell['name'],block=block,step=step,label=label,binary_variant=which,command=cmd,started_utc=utc(),load_before=os.getloadavg())
    with out.open('w') as so,err.open('w') as se:
     try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
     except subprocess.TimeoutExpired:rc='timeout'
    row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(row);save()
    if rc!=0:M['status']='failed';save();raise SystemExit(1)
  print('block',block,'variant',v,'rows',len(M['runs']),flush=True)
for v,b in bins.items():assert sha(R/b)==hashes[v]
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
M.update(status='complete',ended_utc=utc(),seconds=time.monotonic()-start);save()
