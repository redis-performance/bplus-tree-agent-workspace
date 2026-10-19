import argparse,csv,hashlib,json,math,subprocess,time
from pathlib import Path
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['calibration','aa','screen','full','fresh']);ap.add_argument('--variant',default='base');a=ap.parse_args()
widths=(0,8,31,57,58,59,60,61,62,63,64);counts=(1,2,4,7,8,16,32,96)
cells=[dict(name=f'w{w}-r{rev}-n{n}',w=w,rev=rev,n=n) for w in widths for rev in (0,1) for n in counts]
screen=[c for c in cells if c['n']==1 or (c['w']==60 and c['rev']==0)]
phase='long-'+a.phase+('-'+a.variant if a.phase not in ('calibration','aa') else '')
out=p/phase;out.mkdir(exist_ok=False);(out/'raw').mkdir();rows=[];started=time.time()
def save(status):
 (out/'manifest.json').write_text(json.dumps(dict(status=status,started=started,finished=time.time(),phase=phase,rows=rows),indent=2)+'\n')
def run(c,v,seed,rounds,block,step,label):
 name=f'{len(rows):04d}-{v}-{c["name"]}-s{seed}-b{block}-{step}'
 binary=p/'build-long'/v/'decoder-native';cmd=[str(binary),'--width',str(c['w']),'--reversed',str(c['rev']),'--count',str(c['n']),'--leaves','64','--rounds',str(rounds),'--samples','1','--warmup','1','--seed',str(seed)]
 begin=time.time();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120);end=time.time()
 (out/'raw'/(name+'.csv')).write_text(r.stdout);(out/'raw'/(name+'.stderr')).write_text(r.stderr)
 row=dict(name=name,cell=c,variant=v,seed=seed,rounds=rounds,block=block,step=step,label=label,started=begin,finished=end,returncode=r.returncode,command=cmd,csv_sha256=hashlib.sha256(r.stdout.encode()).hexdigest())
 if r.returncode==0:
  result=list(csv.DictReader(r.stdout.splitlines()));assert len(result)==1;row['result']=result[0]
 rows.append(row)
 if len(rows)%24==0:save('running')
 if r.returncode:save('failed');raise SystemExit(name+' failed')
 assert row['result']['cpu_start']==row['result']['cpu_end']=='2'
 return row
if a.phase=='calibration':
 fixed={};cal={}
 for c in cells:
  ns=[]
  for step in range(3):ns.append(float(run(c,'base',1,max(1,math.ceil(1000000/(64*c['n']))),-1,step,'calibration')['result']['ns_per_decode']))
  if c in screen:
   for step in range(3):ns.append(float(run(c,'root',1,max(1,math.ceil(1000000/(64*c['n']))),-1,step,'calibration')['result']['ns_per_decode']))
  wanted=math.ceil(100000000/(min(ns)*64*c['n']));fixed[c['name']]=min(100000000,wanted);cal[c['name']]=dict(fastest_ns=min(ns),requested_rounds=wanted,capped=wanted>100000000)
 (p/'counts-long.json').write_text(json.dumps(fixed,indent=2)+'\n');(out/'calibration-limits.json').write_text(json.dumps(cal,indent=2)+'\n')
else:
 fixed=json.load(open(p/'counts-long.json'));selected=cells if a.phase in ('full','fresh') else screen
 variants=['base','root'] if a.phase=='aa' else [a.variant]
 for block in range(6):
  seed=(101 if a.phase=='fresh' else 1)+block//2
  rotated=selected[block%len(selected):]+selected[:block%len(selected)]
  for c in rotated:
   for v in variants:
    control=v if a.phase=='aa' else 'base'
    for step,(binary,label) in enumerate([(control,'A'),(v,'B'),(v,'B'),(control,'A')]):
     if time.time()-started>(600 if a.phase in ('full','fresh') else 300):save('budget-exhausted');raise SystemExit('phase budget exhausted')
     run(c,binary,seed,fixed[c['name']],block,step,label)
save('complete');print(phase,'complete',len(rows))
