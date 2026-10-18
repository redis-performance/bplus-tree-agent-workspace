from pathlib import Path
import json,hashlib,subprocess,time,os,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];old=json.loads((P/'manifest.json').read_text());CELLS=[c for c in old['cells'] if c['name'] in ['f-int16-m0','f-int16-m4','f-int16-m7']];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();assert not (P/'confirmation.json').exists();(P/'fresh').mkdir()
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
for v,b in old['binaries'].items():assert sha(R/b)==old['binary_hashes'][v]
M=dict(status='running',started_utc=utc(),plan_sha256=sha(P/'CONFIRMATION-PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runner_sha256=sha(Path(__file__)),binaries=old['binaries'],binary_hashes=old['binary_hashes'],cells=CELLS,seeds=[9103,9151],blocks=3,runs=[])
def save():(P/'confirmation.json').write_text(json.dumps(M,indent=2)+'\n')
save();start=time.monotonic()
for seed in M['seeds']:
 for block in range(1,4):
  vs=['A','B','C'];off=block-1
  for v in vs[off:]+vs[:off]:
   for cell in CELLS[off:]+CELLS[:off]:
    for step,label in enumerate('ABBA',1):
     if time.monotonic()-start>420:M['status']='budget-exhausted';save();raise SystemExit(1)
     which='control' if label=='A' else v;name=f'{seed}-b{block}-{v}-{cell["name"]}-s{step}-{label}';cmd=[M['binaries'][which],'--size','100000','--ops','20000000','--seed',str(seed),'--warmup-passes','3','--direction',cell['direction'],'--encoding',cell['encoding'],'--member-bytes',str(cell['bytes']),'--mask',str(cell['mask'])]
     out=P/'fresh'/(name+'.csv');err=P/'fresh'/(name+'.stderr');row=dict(variant=v,cell=cell['name'],seed=seed,block=block,step=step,label=label,binary_variant=which,command=cmd,started_utc=utc(),load_before=os.getloadavg())
     with out.open('w') as so,err.open('w') as se:
      try:q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120);rc=q.returncode
      except subprocess.TimeoutExpired:rc='timeout'
     row.update(returncode=rc,ended_utc=utc(),load_after=os.getloadavg(),csv=str(out.relative_to(P)),stderr=str(err.relative_to(P)),csv_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(row);save()
     if rc!=0:M['status']='failed';save();raise SystemExit(1)
   print('seed',seed,'block',block,'variant',v,'rows',len(M['runs']),flush=True)
for v,b in M['binaries'].items():assert sha(R/b)==M['binary_hashes'][v]
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
M.update(status='complete',ended_utc=utc(),seconds=time.monotonic()-start);save()
