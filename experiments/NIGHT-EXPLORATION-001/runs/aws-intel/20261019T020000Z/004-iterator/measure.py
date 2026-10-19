import csv,datetime,json,math,subprocess,sys,time
from pathlib import Path
P=Path(__file__).resolve().parent;phase=sys.argv[1]
CELLS=[(n,e,d,m) for n in [100000,1000000] for e,d,m in [('integer','forward',7),('integer','reverse',7),('integer','forward',4),('fraction','forward',7)]]
M={'phase':phase,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':[],'status':'running'};start=time.monotonic();out=P/(phase+'.json');assert not out.exists()
def save():out.write_text(json.dumps(M,indent=2)+'\n')
def run(cell,ops,seed,block,pos,variant='release'):
 assert time.monotonic()-start<300
 n,e,d,m=cell;cmd=[str(P/'build'/variant),'--size',str(n),'--ops',str(ops),'--member-bytes','16','--seed',str(seed),'--encoding',e,'--direction',d,'--mask',str(m)]
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120);tag=f'{phase}-{len(M["rows"]):04d}'
 (P/'raw'/(tag+'.stdout')).write_text(r.stdout);(P/'raw'/(tag+'.stderr')).write_text(r.stderr);assert r.returncode==0,r.stderr
 row=list(csv.DictReader(r.stdout.splitlines()))[0];assert int(row['cpu_start'])==int(row['cpu_end'])==2 and row['checksum']==row['expected_checksum']
 M['rows'].append(dict(cell='-'.join(map(str,cell)),variant=variant,block=block,position=pos,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row));save();return row
if phase=='calibration':
 M['counts']={}
 for cell in CELLS:
  values=[run(cell,1000000,1,0,i) for i in range(3)]
  ns=min(int(v['elapsed_ns'])/int(v['operations']) for v in values);M['counts']['-'.join(map(str,cell))]=min(100000000,math.ceil(50000000/ns));save()
else:
 counts=json.loads((P/'calibration.json').read_text())['counts'];variants=['release'] if phase=='aa' else ['A','B','C']
 for block in range(6):
  for cell in CELLS[block:]+CELLS[:block]:
   for variant in variants[block%len(variants):]+variants[:block%len(variants)]:
    for pos,v in enumerate(['release',variant,variant,'release']):run(cell,counts['-'.join(map(str,cell))],1+block%3,block,pos,v)
 M['effects']=[]
 for i in range(0,len(M['rows']),4):
  r=M['rows'][i:i+4];v=[int(x['row']['elapsed_ns'])/int(x['row']['operations']) for x in r]
  M['effects'].append(dict(cell=r[0]['cell'],variant=r[1]['variant'],block=r[0]['block'],percent=100*((v[1]+v[2])/(v[0]+v[3])-1),min_elapsed_ns=min(int(x['row']['elapsed_ns']) for x in r),memory_equal=len({x['row']['tree_bytes'] for x in r})==1))
M.update(status='complete',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print(phase,len(M['rows']),'rows complete')
