import csv,hashlib,json,os,subprocess,time
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;ROOT=P.parents[2];B=ROOT/'scratch/overnight-diag-005/base'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'manifest.json').exists()
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
binary=B/'build/release/btree-bench';(P/'raw').mkdir()
m={'started_utc':utc(),'binary':str(binary.relative_to(ROOT)),'binary_sha256':sha(binary),'freeze_sha256':sha(P/'freeze.json'),'plan_sha256':sha(P/'PLAN.md'),'runner_sha256':sha(Path(__file__)),'runs':[],'status':'running'}
def save(): (P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();start=time.monotonic();schedule=[]
for b in range(1,7):
 first=['AS','BS','BI','AI'] if b%2 else ['AI','BI','BS','AS']
 for slot,cell in enumerate(first+list(reversed(first))):
  seed=[211,211,307,307,401,401][b-1]
  schedule.append((b,slot,cell,seed))
for b,slot,cell,seed in schedule:
 size=320;a=cell[0];order='ascending' if a=='A' else 'shuffled';query='coupled' if cell[1]=='S' else 'independent'
 name=f'b{b}-s{slot}-{cell}'
 cmd=[str(binary.relative_to(ROOT)),'--case','lookup-hit','--size','100000','--ops','5000000','--member-bytes',str(size),'--seed',str(seed),'--warmup-passes','10','--fixture-order',order,'--query-order',query]
 row={'block':b,'member_bytes':size,'slot':slot,'arm':a,'cell':cell,'query_order':query,'seed':seed,'command':cmd,'started_utc':utc(),'load_before':os.getloadavg(),'csv':f'raw/{name}.csv','stderr':f'raw/{name}.stderr'}
 if time.monotonic()-start>240:m['status']='budget-exhausted';break
 t=time.monotonic()
 with (P/row['csv']).open('w') as so,(P/row['stderr']).open('w') as se:
  try:r=subprocess.run(cmd,cwd=ROOT,stdout=so,stderr=se,timeout=min(120,240-(time.monotonic()-start)));code=r.returncode
  except subprocess.TimeoutExpired:code='timeout'
 row.update(returncode=code,elapsed_seconds=time.monotonic()-t,ended_utc=utc(),load_after=os.getloadavg())
 for f in ['csv','stderr']:row[f+'_sha256']=sha(P/row[f])
 if code==0:
  rows=list(csv.DictReader((P/row['csv']).open()))
  if len(rows)!=1 or rows[0]['fixture_order']!=order or rows[0]['query_order']!=query:row['returncode']='invalid-output'
 m['runs'].append(row);save();print(name,row['returncode'],flush=True)
 if row['returncode']!=0:m['status']='failed';break
else:m['status']='complete'
m.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-start,binary_sha256_after=sha(binary))
assert m['binary_sha256']==m['binary_sha256_after']
for name,h in F['files'].items():assert sha(B/name)==h
save();print(m['status'],flush=True)
