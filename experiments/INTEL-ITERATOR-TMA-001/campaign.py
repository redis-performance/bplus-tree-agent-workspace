"""Fixed, serial baseline qualification. No candidate performance comparisons."""
import csv,dataclasses,hashlib,json,math,os,signal,subprocess,time
from pathlib import Path
from topdown.collector.toplev import ToplevRunner,ToplevOptions
from topdown.collector.csv_parser import parse_output
P=json.loads(Path('protocol.json').read_text());OUT=Path('results');OUT.mkdir(exist_ok=True)
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
def snap():
 text=Path('/proc/stat').read_text()
 return {str(cpu):list(map(int,next(l for l in text.splitlines() if l.startswith(f'cpu{cpu} ')).split()[1:9])) for cpu in [2,50]}
def occupancy(a,b,cpu):
 d=[y-x for x,y in zip(a[str(cpu)],b[str(cpu)])];total=sum(d)
 return 100*(total-d[3]-d[4])/total if total else None
def command(cell,ops,seed,binary='build/base/iterator'):
 return ['numactl','--physcpubind=2','--membind=0',binary,'--size',str(cell['size']),'--ops',str(ops),
 '--member-bytes','16','--seed',str(seed),'--mask',str(cell['output_mask']),'--encoding',cell['layout'],'--direction',cell['direction']]
def runrow(tag,cell,ops,seed,binary='build/base/iterator',strict=True):
 args=command(cell,ops,seed,binary);before=snap();start=time.time()
 try:
  r=subprocess.run(args,capture_output=True,text=True,timeout=60)
 except subprocess.TimeoutExpired as e:
  def text(v): return v.decode(errors='replace') if isinstance(v,bytes) else (v or '')
  r=subprocess.CompletedProcess(args,124,text(e.stdout),text(e.stderr)+'\nPROCESS TIMEOUT\n')
 after=snap()
 (OUT/f'{tag}.stdout').write_text(r.stdout);(OUT/f'{tag}.stderr').write_text(r.stderr)
 meta={'args':args,'started':start,'ended':time.time(),'returncode':r.returncode,'cpu_before':before,'cpu_after':after,'sibling_busy_pct':occupancy(before,after,50)}
 save(f'{tag}.process.json',meta)
 rows=list(csv.DictReader(r.stdout.splitlines())) if r.returncode==0 else []
 row=rows[0] if len(rows)==1 else {}
 good=r.returncode==0 and bool(row) and row.get('checksum')==row.get('expected_checksum') and row.get('cpu_start')==row.get('cpu_end')=='2'
 record={'row':row,'meta':meta,'valid':good}
 if strict and not good: raise RuntimeError('Invalid process '+tag+'; stdout/stderr/meta retained')
 return record
# Timing referee equivalence over supported score modes, all masks and directions.
parity=[]
for encoding in ['integer','fraction','wide','zero']:
 for direction in ['forward','reverse']:
  for mask in range(8):
   c={'size':257,'layout':encoding,'direction':direction,'output_mask':mask}
   tag=f'parity-{encoding}-{direction}-{mask}'
   a=runrow(tag+'-original',c,1000,71,'build/base/original')['row'];b=runrow(tag+'-long',c,1000,71)['row']
   keys=['case','size','operations','member_bytes','seed','direction','mask','encoding','traversals','checksum','expected_checksum','tree_bytes','construction_fingerprint']
   assert all(a[k]==b[k] for k in keys),tag
   parity.append(tag)
save('parity.json',{'pairs':len(parity),'pass':True,'cases':parity})
# Completed >100M boundary exercises the widened path and all end-of-run checks.
runrow('long-ops-boundary',P['cells'][0],100000001,71)
# Baseline TMA on exactly the binary used for controls, steady loop only.
os.environ['PERF']='/usr/lib/linux-tools/7.0.0-1014-aws/perf'
runner=ToplevRunner(str(Path('pmu/toplev.py').resolve()),ToplevOptions(level=2,extra_args=['-C','2']))
profile_ok=True
for size in P['profile']['sizes']:
 c={'size':size,'layout':'integer','direction':'forward','output_mask':7};args=command(c,20000000000,7103)
 out=(OUT/f'profile-{size}-workload.stdout').open('w');err=(OUT/f'profile-{size}-workload.stderr').open('w')
 proc=subprocess.Popen(args,env=dict(os.environ,BPLUS_PROFILE_STOP='1'),stdout=out,stderr=err)
 try:
  deadline=time.monotonic()+60
  while time.monotonic()<deadline:
   assert proc.poll() is None
   if '\nState:\tT' in Path(f'/proc/{proc.pid}/status').read_text():break
   time.sleep(.05)
  else:raise RuntimeError('readiness timeout')
  assert os.sched_getaffinity(proc.pid)=={2}
  (OUT/f'profile-{size}-numa-maps.txt').write_text(Path(f'/proc/{proc.pid}/numa_maps').read_text())
  os.kill(proc.pid,signal.SIGCONT)
  for rep in range(3):
   before=snap();wt0=Path(f'/proc/{proc.pid}/stat').read_text();begin=time.time();stdout,stderr=runner.run(10);after=snap()
   tag=f'profile-{size}-{rep+1}'
   (OUT/f'{tag}.stdout').write_text(stdout);(OUT/f'{tag}.stderr').write_text(stderr)
   try:
    wt1=Path(f'/proc/{proc.pid}/stat').read_text();affinity=sorted(os.sched_getaffinity(proc.pid))
   except (FileNotFoundError,ProcessLookupError):
    wt1=None;affinity=[]
   samples=parse_output(stderr) or parse_output(stdout)
   save(f'{tag}.json',[dataclasses.asdict(s) for s in samples])
   meta={'start':begin,'end':time.time(),'pid':proc.pid,'command':runner.build_command()+['--','sleep','10'],
    'alive':proc.poll() is None,'affinity':affinity,'cpu_before':before,'cpu_after':after,'sibling_busy_pct':occupancy(before,after,50)}
   def workload_ticks(text):
    fields=text.rsplit(')',1)[1].split();return int(fields[11])+int(fields[12])
   cpu_delta=[b-a for a,b in zip(before['2'],after['2'])]
   cpu_busy=sum(cpu_delta)-cpu_delta[3]-cpu_delta[4]
   workload_delta=workload_ticks(wt1)-workload_ticks(wt0) if wt1 else None
   meta.update(workload_before=wt0,workload_after=wt1,cpu_busy_ticks=cpu_busy,workload_ticks=workload_delta,
     workload_accounting_error_pct=100*abs(cpu_busy-workload_delta)/max(cpu_busy,1) if workload_delta is not None else None)
   save(f'{tag}.scope.json',meta)
   assert meta['alive'] and meta['affinity']==[2]
   rows=[r for r in csv.DictReader(stderr.splitlines()) if r.get('Area')]
   roots=['Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring']
   bytime={}
   for r in rows:
    if r['Area'] in roots:bytime.setdefault(r['Timestamp'],[]).append(r)
   root_quality=len(bytime)==10 and all(len(rs)==4 and {r['Area'] for r in rs}==set(roots)
    and all(r['Unit'] in ('% Slots','% Slots <') and math.isfinite(float(r['Value'])) and 0<=float(r['Value'])<=100 for r in rs)
    and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in bytime.values())
   good=bool(samples) and root_quality and all(float(r['Multiplex'])==100 for r in rows) and meta['sibling_busy_pct']<=1 and meta['workload_accounting_error_pct']<=1
   profile_ok &= good
   print(json.dumps({'phase':'profile','size':size,'rep':rep+1,'samples':len(samples),'quality':good}),flush=True)
 finally:
  if proc.poll() is None: proc.terminate();os.kill(proc.pid,signal.SIGCONT);proc.wait(timeout=5)
  out.close();err.close()
save('profile-quality.json',{'pass':profile_ok})
# Baseline-only calibration: fixed three seeds; no favorable-count reruns.
counts=[]
for idx,c in enumerate(P['cells']):
 runs=[runrow(f'calibration-{idx}-{seed}',c,10000000,seed) for seed in [1,2,3]]
 fastest=min(int(r['row']['elapsed_ns']) for r in runs)
 denominator=fastest*c['size']
 ops=((10000000*600000000+denominator-1)//denominator)*c['size']
 assert ops<=2000000000,'calibration exceeds preregistered cap'
 counts.append(ops)
save('frozen-counts.json',{'counts':counts,'binary_sha256':hashlib.sha256(Path('build/base/iterator').read_bytes()).hexdigest(),
 'protocol_sha256':hashlib.sha256(Path('protocol.json').read_bytes()).hexdigest(),'frozen_before_aa':time.time()})
# Seal one deterministic schedule before first A/A row.
schedule=[]
for block,seed in enumerate(P['seeds']):
 for cell in range(8):
  for position in range(4):schedule.append({'index':len(schedule),'block':block,'seed':seed,'cell':cell,'position':position,'ops':counts[cell]})
save('schedule.json',schedule)
rows=[];deadline=time.monotonic()+900
for item in schedule:
 if time.monotonic()>deadline:break
 idx=item['index'];r=runrow(f'aa-{idx:03}',P['cells'][item['cell']],item['ops'],item['seed'],strict=False);rows.append(dict(item,**r))
 save('aa-rows.json',rows)
 if not r['valid']:break
 if (idx+1)%32==0:print(json.dumps({'phase':'aa','rows':idx+1,'total':192}),flush=True)
save('aa-rows.json',rows)
blocks=[]
for i in range(0,len(rows)-3,4):
 rs=rows[i:i+4]
 if not all(r['valid'] for r in rs):break
 ns=[int(r['row']['elapsed_ns']) for r in rs];outer=ns[0]+ns[3];inner=ns[1]+ns[2]
 invariants=['size','operations','traversals','checksum','expected_checksum','tree_bytes','construction_fingerprint','seed','mask','direction','encoding']
 same=all(len({r['row'][k] for r in rs})==1 for k in invariants)
 duration=min(ns)>=500000000;precision=abs(inner-outer)*100<=outer
 smt=all(r['meta']['sibling_busy_pct'] is not None and r['meta']['sibling_busy_pct']<=1 for r in rs)
 blocks.append({'cell':rs[0]['cell'],'block':rs[0]['block'],'seed':rs[0]['seed'],'effect_pct':100*(inner/outer-1),
  'minimum_ns':min(ns),'precision':precision,'duration':duration,'smt':smt,'invariants':same,'pass':precision and duration and smt and same})
qualified=len(rows)==192 and len(blocks)==48 and all(b['pass'] for b in blocks) and profile_ok
save('RESULT.json',{'decision':'BASELINE_QUALIFIED' if qualified else 'PARK','candidate_timing_runs':0,'rows':len(rows),
 'profile_pass':profile_ok,'qualified_blocks':sum(b['pass'] for b in blocks),'blocks':blocks,'source_adoption':'NONE'})
print(json.dumps({'decision':'BASELINE_QUALIFIED' if qualified else 'PARK','rows':len(rows),'qualified_blocks':sum(b['pass'] for b in blocks)}),flush=True)
