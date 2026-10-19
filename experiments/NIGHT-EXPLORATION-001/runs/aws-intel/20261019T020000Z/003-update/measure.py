import csv,datetime,json,math,subprocess,sys,time
from pathlib import Path
P=Path(__file__).resolve().parent;phase=sys.argv[1]
CELLS=[(n,pattern) for n in [100,1000,10000,100000,1000000] for pattern in ['same','position','nearby','distant','original']]
M={'phase':phase,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':[],'status':'running'};start=time.monotonic();out=P/(phase+'.json');assert not out.exists()
def stat():
 lines=Path('/proc/stat').read_text().splitlines()
 return {key:list(map(int,next(l for l in lines if l.startswith(key+' ')).split()[1:])) for key in ['cpu','cpu2','cpu50','ctxt']}
def save():out.write_text(json.dumps(M,indent=2)+'\n')
def run(n,pattern,ops,seed,block,pos):
 assert time.monotonic()-start<300
 cmd=[str(P/'build/release'),'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed),'--query-seed',str(seed+100),'--query-order','independent','--pattern',pattern]
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();before=stat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120);after=stat();tag=f'{phase}-{len(M["rows"]):04d}'
 (P/'raw'/(tag+'.stdout')).write_text(r.stdout);(P/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
 row=list(csv.DictReader(r.stdout.splitlines()))[0];assert int(row['cpu_start'])==int(row['cpu_end'])==2
 M['rows'].append(dict(cell=f'{pattern}-{n}',block=block,position=pos,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),proc_stat_before=before,proc_stat_after=after,row=row));save();return row
if phase=='calibration':
 M['counts']={}
 for n,pattern in CELLS:
  values=[run(n,pattern,100000,1,0,i) for i in range(3)]
  M['counts'][f'{pattern}-{n}']=min(100000000,math.ceil(50000000/min(float(v['ns_per_op']) for v in values)));save()
else:
 counts=json.loads((P/'calibration.json').read_text())['counts']
 for block in range(6):
  for n,pattern in CELLS[block:]+CELLS[:block]:
   for pos in range(4):run(n,pattern,counts[f'{pattern}-{n}'],1+block%3,block,pos)
 M['effects']=[]
 for i in range(0,len(M['rows']),4):
  r=M['rows'][i:i+4];v=[float(x['row']['ns_per_op']) for x in r]
  M['effects'].append(dict(cell=r[0]['cell'],block=r[0]['block'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),min_elapsed_ns=min(int(x['row']['elapsed_ns']) for x in r),memory_equal=len({x['row']['tree_bytes'] for x in r})==1))
M.update(status='complete',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print(phase,len(M['rows']),'rows complete')
