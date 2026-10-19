import subprocess,pathlib,time,datetime,json,csv,math,hashlib
out=pathlib.Path('scratch/amd-lowerbound-aa');out.mkdir(parents=True,exist_ok=False)
binary='build/size-matrix/btree-bench'; rows=[]; records=[]
def run(n,ops,seed,label):
 cmd=[binary,'--case','update','--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed)]
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
 (out/(label+'.csv')).write_text(r.stdout);(out/(label+'.stderr')).write_text(r.stderr)
 records.append(dict(label=label,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode))
 (out/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
 row=list(csv.DictReader(r.stdout.splitlines()))[0];rows.append(dict(label=label,**row));return row
counts={}
for n in [100000,1000000]:
 cal=[run(n,100000,1,f'cal-n{n}-r{i}') for i in range(3)]
 counts[n]=min(100000000,math.ceil(50000000/min(float(r['ns_per_op']) for r in cal)))
(out/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
started=time.monotonic()
for b in range(6):
 for n in ([100000,1000000] if b%2==0 else [1000000,100000]):
  for j,letter in enumerate('ABBA'):
   if time.monotonic()-started>300:raise RuntimeError('timing budget exhausted')
   run(n,counts[n],1+b//2,f'aa-b{b}-n{n}-s{j}-{letter}')
summary={}
for n in counts:
 cells=[]
 for b in range(6):
  rr=[r for r in rows if r['label'].startswith(f'aa-b{b}-n{n}-')]
  a=sum(float(r['ns_per_op']) for r in rr if r['label'].endswith('A'))/2;btime=sum(float(r['ns_per_op']) for r in rr if r['label'].endswith('B'))/2
  cells.append(dict(effect_pct=100*(btime/a-1),minimum_ns=min(int(r['elapsed_ns']) for r in rr)))
 summary[n]=dict(blocks=cells,qualified=all(abs(x['effect_pct'])<=1 and x['minimum_ns']>=10000000 for x in cells))
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'rows.json').write_text(json.dumps(rows,indent=2)+'\n')
