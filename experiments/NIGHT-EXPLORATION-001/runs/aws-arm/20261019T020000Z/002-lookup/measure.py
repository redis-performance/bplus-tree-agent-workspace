import argparse,csv,hashlib,json,math,subprocess,time
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['calibration','aa','screen','confirmation']);ap.add_argument('--variants',default='A,B,C');a=ap.parse_args()
cells=[dict(name=f'hit-n{n}-k16',n=n,k=16,case='lookup-hit') for n in (100,1000,10000,100000,1000000)]+[dict(name=f'miss-n{n}-k16',n=n,k=16,case='lookup-miss') for n in (100000,1000000)]+[dict(name=f'hit-n100000-k{k}',n=100000,k=k,case='lookup-hit') for k in (8,319,320,321,1024)]
out=p/a.phase;out.mkdir(exist_ok=False);rows=[];start=time.time()
def run(c,variant,seed,ops,block,step,label):
 name=f'{len(rows):04d}-{variant}-{c["name"]}-s{seed}-b{block}-s{step}-{label}'
 cmd=[str(p/'build'/variant),'--size',str(c['n']),'--ops',str(ops),'--member-bytes',str(c['k']),'--seed',str(seed),'--case',c['case']]
 begin=time.time();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120);end=time.time()
 (out/(name+'.csv')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr)
 row=dict(name=name,cell=c,variant=variant,seed=seed,ops=ops,block=block,step=step,label=label,started=begin,finished=end,returncode=r.returncode,csv_sha256=hashlib.sha256(r.stdout.encode()).hexdigest(),command=cmd)
 if r.returncode==0:
  parsed=list(csv.DictReader(r.stdout.splitlines()));assert len(parsed)==1;row['result']=parsed[0]
 rows.append(row);(out/'manifest.json').write_text(json.dumps(dict(status='running',started=start,rows=rows),indent=2)+'\n')
 assert r.returncode==0,(name,r.returncode)
 assert row['result']['cpu_start']=='2' and row['result']['cpu_end']=='2'
 return row
if a.phase=='calibration':
 counts={}
 for c in cells:
  ns=[]
  for step in range(3):ns.append(float(run(c,'base',1,1000000,-1,step,'calibration')['result']['ns_per_op']))
  counts[c['name']]=min(100000000,math.ceil(50000000/min(ns)))
 (p/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
else:
 counts=json.load(open(p/'counts.json'));variants=['base'] if a.phase=='aa' else a.variants.split(',')
 # Screen is explicitly bounded to both hit primaries and one large miss guard.
 selected=cells if a.phase=='aa' else [c for c in cells if (c['n'] in (100000,1000000) and c['k']==16)]
 for block in range(6):
  seed=(101 if a.phase=='confirmation' else 1)+block//2
  rotated=selected[block%len(selected):]+selected[:block%len(selected)]
  for c in rotated:
   for v in variants[block%len(variants):]+variants[:block%len(variants)]:
    for step,(binary,label) in enumerate([('base','A'),(v,'B'),(v,'B'),('base','A')]):
     if time.time()-start>300:raise SystemExit('phase budget exhausted; preserve partial data')
     run(c,binary,seed,counts[c['name']],block,step,label)
(out/'manifest.json').write_text(json.dumps(dict(status='complete',started=start,finished=time.time(),rows=rows),indent=2)+'\n')
print(a.phase,'complete',len(rows))
