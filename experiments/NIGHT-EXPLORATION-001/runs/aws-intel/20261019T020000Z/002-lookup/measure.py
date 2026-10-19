import csv,datetime,hashlib,json,math,subprocess,sys,time
from pathlib import Path
P=Path(__file__).resolve().parent
phase=sys.argv[1]
CELLS=[(n,c,16) for n in [10000,100000,1000000] for c in ['lookup-hit','lookup-miss']]
M={'phase':phase,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':[],'status':'running'}
start=time.monotonic();out=P/(phase+'.json');assert not out.exists()
def save():out.write_text(json.dumps(M,indent=2)+'\n')
def run(n,c,b,ops,seed,block,position,variant='base'):
 assert time.monotonic()-start<300
 binary=P/'build'/variant
 cmd=[str(binary),'--size',str(n),'--case',c,'--member-bytes',str(b),'--ops',str(ops),'--seed',str(seed),'--query-seed',str(seed+100),'--query-order','independent']
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();stats=Path('/proc/stat').read_text().splitlines();r=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
 tag=f'{phase}-{len(M["rows"]):04d}';(P/'raw'/(tag+'.stdout')).write_text(r.stdout);(P/'raw'/(tag+'.stderr')).write_text(r.stderr)
 assert r.returncode==0,(cmd,r.stderr)
 row=list(csv.DictReader(r.stdout.splitlines()))[0]
 assert int(row['cpu_start'])==2 and int(row['cpu_end'])==2
 M['rows'].append(dict(cell=f'{c}-{n}-{b}',variant=variant,block=block,position=position,started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),row=row,sibling50_before=next(x for x in stats if x.startswith('cpu50 ')),sibling50_after=next(x for x in Path('/proc/stat').read_text().splitlines() if x.startswith('cpu50 '))))
 save();return row
if phase=='calibration':
 M['counts']={}
 for n,c,b in CELLS:
  values=[run(n,c,b,1000000,1,0,i) for i in range(3)]
  count=min(100000000,max(1,math.ceil(50000000/min(float(v['ns_per_op']) for v in values))))
  M['counts'][f'{c}-{n}-{b}']=count;save()
else:
 counts=json.loads((P/'calibration.json').read_text())['counts']
 variants=['base'] if phase=='aa' else ['A','B','C']
 for block in range(6):
  seed=1+block%3
  cells=CELLS[block%len(CELLS):]+CELLS[:block%len(CELLS)]
  for n,c,b in cells:
   for variant in variants[block%len(variants):]+variants[:block%len(variants)]:
    for pos,v in enumerate(['base',variant,variant,'base']):run(n,c,b,counts[f'{c}-{n}-{b}'],seed,block,pos,v)
 M['effects']=[]
 for i in range(0,len(M['rows']),4):
  r=M['rows'][i:i+4];a=(float(r[0]['row']['ns_per_op'])+float(r[3]['row']['ns_per_op']))/2;b=(float(r[1]['row']['ns_per_op'])+float(r[2]['row']['ns_per_op']))/2
  M['effects'].append(dict(cell=r[0]['cell'],block=r[0]['block'],variant=r[1]['variant'],percent=100*(b/a-1),min_elapsed_ns=min(int(x['row']['elapsed_ns']) for x in r),memory_equal=len({x['row']['tree_bytes'] for x in r})==1))
M.update(status='complete',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print(phase,len(M['rows']),'rows complete')
