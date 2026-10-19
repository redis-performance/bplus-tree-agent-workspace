import csv,datetime,hashlib,json,math,subprocess,sys,time
from pathlib import Path
P=Path(__file__).resolve().parent;phase=sys.argv[1];assert phase in ['calibration','aa','screen-A','screen-B','fresh-A','fresh-B']
CELLS=[(n,e,d,m) for n in [100000,1000000] for e,d,m in [('integer','forward',7),('integer','reverse',7),('integer','forward',4),('fraction','forward',7)]]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
out=P/phase;out.mkdir(exist_ok=False);(out/'raw').mkdir();M={'phase':phase,'started_utc':utc(),'rows':[],'status':'running','budget_seconds':600};start=time.monotonic()
def save(status=None):
 if status:M['status']=status
 M['finished_utc']=utc();M['elapsed_seconds']=time.monotonic()-start;(out/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(cell,ops,seed,block,pos,variant='base'):
 if time.monotonic()-start>600:save('budget-exhausted');raise SystemExit('fixed phase budget exhausted')
 n,e,d,m=cell;cmd=[str(P/'build'/variant),'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed),'--encoding',e,'--direction',d,'--mask',str(m)];begun=utc()
 try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
 except subprocess.TimeoutExpired as exc:
  save('child-timeout');raise
 tag=f'{len(M["rows"]):04d}-{variant}-'+ '-'.join(map(str,cell))+f'-s{seed}-b{block}-{pos}';raw=r.stdout.encode();(out/'raw'/(tag+'.csv')).write_bytes(raw);(out/'raw'/(tag+'.stderr')).write_text(r.stderr)
 row=dict(name=tag,cell='-'.join(map(str,cell)),variant=variant,block=block,position=pos,seed=seed,requested_ops=ops,started_utc=begun,finished_utc=utc(),command=cmd,returncode=r.returncode,csv_sha256=hashlib.sha256(raw).hexdigest())
 if r.returncode==0:
  rr=list(csv.DictReader(r.stdout.splitlines()));assert len(rr)==1;row['result']=rr[0]
 M['rows'].append(row);save()
 if r.returncode:save('failed');raise SystemExit(tag+' failed')
 v=row['result'];assert int(v['cpu_start'])==int(v['cpu_end'])==2 and v['checksum']==v['expected_checksum'];return v
if phase=='calibration':
 counts={}
 for cell in CELLS:
  rows=[run(cell,1000000,1,-1,i) for i in range(3)];ns=min(int(r['elapsed_ns'])/int(r['operations']) for r in rows);counts['-'.join(map(str,cell))]=min(100000000,math.ceil(100000000/ns))
 (P/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
else:
 counts=json.load(open(P/'counts.json'));variant='base' if phase=='aa' else phase.split('-')[1]
 for block in range(6):
  seed=(101 if phase.startswith('fresh') else 1)+block%3
  for cell in CELLS[block%len(CELLS):]+CELLS[:block%len(CELLS)]:
   for pos,v in enumerate(['base',variant,variant,'base']):run(cell,counts['-'.join(map(str,cell))],seed,block,pos,v)
save('complete');print(phase,len(M['rows']),'processes complete')
