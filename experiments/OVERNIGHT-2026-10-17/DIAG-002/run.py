import csv,hashlib,json,os,re,subprocess,time
from pathlib import Path
from datetime import datetime,timezone
P=Path(__file__).resolve().parent;ROOT=P.parents[2];B=ROOT/'scratch/overnight-diag-002/base'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
assert not (P/'manifest.json').exists()
s=(P/'dependent-adds.s').read_text();registers=re.findall(r'^\s*add\s+(x\d+),\s*\1,\s*#1\s*$',s,re.M)
assert len(registers)==8 and len(set(registers))==1
F=json.loads((P/'freeze.json').read_text())
for name,h in F['files'].items():assert sha(B/name)==h
binary=B/'build/btree-bench';(P/'raw').mkdir()
m={'started_utc':utc(),'binary':str(binary.relative_to(ROOT)),'binary_sha256':sha(binary),'freeze_sha256':sha(P/'freeze.json'),'plan_sha256':sha(P/'PLAN.md'),'runner_sha256':sha(Path(__file__)),'warmup':[],'runs':[],'status':'running'}
def save(): (P/'manifest.json').write_text(json.dumps(m,indent=2)+'\n')
save();start=time.monotonic()
for i in range(7):
 name='warmup' if i==0 else f'process{i}'
 row={'process':i,'command':[str(binary.relative_to(ROOT))],'started_utc':utc(),'load_before':os.getloadavg(),'csv':f'raw/{name}.csv','stderr':f'raw/{name}.stderr'}
 if time.monotonic()-start>300:m['status']='budget-exhausted';break
 t=time.monotonic()
 with (P/row['csv']).open('w') as so,(P/row['stderr']).open('w') as se:
  try:r=subprocess.run([str(binary)],stdout=so,stderr=se,timeout=120);code=r.returncode
  except subprocess.TimeoutExpired:code='timeout'
 row.update(returncode=code,elapsed_seconds=time.monotonic()-t,ended_utc=utc(),load_after=os.getloadavg())
 for f in ['csv','stderr']:row[f+'_sha256']=sha(P/row[f])
 if code==0:
  rows=list(csv.DictReader((P/row['csv']).open()))
  if len(rows)!=4 or [r['sample'] for r in rows]!=['0','1','2','3']:row['returncode']='invalid-output'
 m['warmup' if i==0 else 'runs'].append(row);save();print(name,row['returncode'],flush=True)
 if row['returncode']!=0:m['status']='failed';break
else:m['status']='complete'
m.update(ended_utc=utc(),elapsed_seconds=time.monotonic()-start,binary_sha256_after=sha(binary))
assert m['binary_sha256']==m['binary_sha256_after']
for name,h in F['files'].items():assert sha(B/name)==h
save();print(m['status'],flush=True)
