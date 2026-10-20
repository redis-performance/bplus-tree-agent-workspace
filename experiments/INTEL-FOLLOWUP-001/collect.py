"""Frozen secondary-host diagnostics; no retries or acceptance timing."""
import collections,csv,dataclasses,hashlib,json,math,os,signal,subprocess,time,traceback
from pathlib import Path
from topdown.collector.toplev import ToplevRunner,ToplevOptions
from topdown.collector.csv_parser import parse_output
P=json.loads(Path('protocol.json').read_text());O=Path('results');O.mkdir(exist_ok=True);RAW=Path('raw');RAW.mkdir(exist_ok=True)
PERF='/usr/lib/linux-tools/7.0.0-1014-aws/perf';os.environ['PERF']=PERF
class IsolationError(RuntimeError):pass
class StageTimeout(RuntimeError):pass
ROOTS={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def save(name,data):(O/name).write_text(json.dumps(data,indent=2)+'\n')
def snapshot(pid):
 stat=Path('/proc/stat').read_text();proc=Path(f'/proc/{pid}/stat').read_text()
 assert os.sched_getaffinity(pid)=={2} and proc.rsplit(')',1)[1].split()[0]!='Z'
 assert json.loads(Path('reservation.json').read_text())['original_sibling_topology']=='2,50'
 topology=Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip();assert topology in ['2','2,50']
 offline=Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()=='0';assert offline
 return {'time':time.time(),'cpu2':list(map(int,next(l for l in stat.splitlines() if l.startswith('cpu2 ')).split()[1:9])),'proc':proc,'affinity':sorted(os.sched_getaffinity(pid)),'sibling_offline':offline,'online_sibling_topology':topology,'frequency_khz':Path('/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq').read_text().strip()}
def scope(a,b):
 ds=[y-x for x,y in zip(a['cpu2'],b['cpu2'])];busy=sum(ds)-ds[3]-ds[4]
 ticks=lambda s:sum(int(s.rsplit(')',1)[1].split()[i]) for i in [11,12])
 work=ticks(b['proc'])-ticks(a['proc']);error=100*abs(busy-work)/max(1,busy)
 return {'before':a,'after':b,'cpu_busy_ticks':busy,'workload_ticks':work,'accounting_error_percent':error,'pass':a['sibling_offline'] and b['sibling_offline'] and a['affinity']==b['affinity']==[2] and error<=1}
def execute(tag,args):
 start=time.time()
 try:r=subprocess.run(args,capture_output=True,text=True,timeout=90)
 except subprocess.TimeoutExpired as e:
  txt=lambda x:x.decode(errors='replace') if isinstance(x,bytes) else x or ''
  r=subprocess.CompletedProcess(args,124,txt(e.stdout),txt(e.stderr)+'\nTIMEOUT\n')
 (O/(tag+'.stdout')).write_text(r.stdout);(O/(tag+'.stderr')).write_text(r.stderr);save(tag+'.command.json',{'args':args,'start':start,'end':time.time(),'returncode':r.returncode})
 if r.returncode==124:raise StageTimeout(tag+' timed out; abort entire owned group')
 return r

def deep(tag,kind,pid):
 raw=RAW/(tag+'.perf.data')
 if kind=='pebs':args=[PERF,'mem','record','-t','load','-U','--ldlat','30','-c','1000','-s','--running-time','-o',str(raw),'--pid',str(pid),'--','sleep','5']
 else:args=[PERF,'record','-e','cycles:u','-c','1000000','-j','any,u','-s','--running-time','-o',str(raw),'--pid',str(pid),'--','sleep','5']
 a=snapshot(pid);r=execute(tag,args)
 rec={'tag':tag,'kind':kind,'returncode':r.returncode,'available':False}
 if raw.exists():rec.update(raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),raw_bytes=raw.stat().st_size)
 save(tag+'.deep.json',rec)
 try:sc=scope(a,snapshot(pid))
 except BaseException as e:
  sc={'before':a,'after':None,'pass':False,'error':str(e)}
 save(tag+'.scope.json',sc);rec['scope_pass']=sc['pass'];save(tag+'.deep.json',rec)
 if not sc['pass']:raise IsolationError(tag+' scope failed')
 if raw.exists():
  rec.update(raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),raw_bytes=raw.stat().st_size)
  actions={'attributes':['evlist','-v'],'dump':['script','-D'],'thread-values':['report','--stdio','-T'],'symbols':['report','--stdio','--no-children','--percent-limit','0','--sort','symbol,dso']}
  fields='event,period,ip,sym,symoff,dso,addr,weight,data_src' if kind=='pebs' else 'event,period,ip,sym,symoff,dso,brstack'
  actions['events']=['script','-F',fields]
  for name,opts in actions.items():
   result=execute(tag+'-'+name,[PERF]+opts+['-i',str(raw)]);rec[name+'_returncode']=result.returncode
  # Supportedness only. Statistical/event/scheduling qualification is offline;
  # no adaptive remeasurement based on the profile's mechanism or outcome.
  events=(O/(tag+'-events.stdout')).read_text().splitlines()
  rec['available']=r.returncode==0 and sc['pass'] and all(rec[n+'_returncode']==0 for n in actions) and len(events)>=200
 save(tag+'.deep.json',rec)
 return rec

def launch(c,v,tag):
 assert not subprocess.check_output(['docker','ps','-q'],text=True).strip(),'active container'
 binary=Path('build')/v/c['driver'];args=['numactl','--all','--physcpubind=2','--membind=0',str(binary)]+c['args']
 out=(O/(tag+'-workload.stdout')).open('w');err=(O/(tag+'-workload.stderr')).open('w');proc=subprocess.Popen(args,stdout=out,stderr=err,env=dict(os.environ,BPLUS_PROFILE_STOP='1'))
 try:
  deadline=time.monotonic()+90
  while time.monotonic()<deadline:
   assert proc.poll() is None,'exited before readiness'
   if '\nState:\tT' in Path(f'/proc/{proc.pid}/status').read_text():break
   time.sleep(.05)
  else:raise RuntimeError('readiness timeout')
  snapshot(proc.pid);(O/(tag+'-numa.txt')).write_text(Path(f'/proc/{proc.pid}/numa_maps').read_text());(O/(tag+'-maps.txt')).write_text(Path(f'/proc/{proc.pid}/maps').read_text());os.kill(proc.pid,signal.SIGCONT)
  return proc,out,err,args
 except BaseException:
  finish(proc,out,err);raise

def finish(proc,out,err):
 if proc.poll() is None:
  proc.terminate();os.kill(proc.pid,signal.SIGCONT)
  try:proc.wait(timeout=5)
  except subprocess.TimeoutExpired:proc.kill();proc.wait()
 out.close();err.close()

probes={}
for kind,cell in [('pebs','update-1000000-same'),('lbr','scan-1000000')]:
 c=next(x for x in P['cells'] if x['id']==cell);tag='probe-'+kind;proc=None
 probes[kind]={'tag':tag,'status':'STARTED','available':False};save('probes.json',probes)
 try:
  proc,out,err,args=launch(c,'base',tag);probes[kind].update(workload_command=args,binary_sha256=hashlib.sha256((Path('build')/'base'/c['driver']).read_bytes()).hexdigest());save('probes.json',probes)
  probes[kind].update(deep(tag,kind,proc.pid));probes[kind]['status']='COLLECTED'
 except BaseException as e:
  probes[kind].update(status='INCOMPLETE',error=str(e));save('probes.json',probes);raise
 finally:
  if proc is not None:finish(proc,out,err)
  save('probes.json',probes)
print(json.dumps({'phase':'PROBES_READY','probes':probes}),flush=True)
deadline=time.monotonic()+240
while not Path('probes-reviewed.json').exists() and time.monotonic()<deadline:time.sleep(1)
review={'pebs':False,'lbr':False,'reason':'review deadline or invalid bound approval'}
if Path('probes-reviewed.json').exists():
 try:
  supplied=json.loads(Path('probes-reviewed.json').read_text())
  assert supplied['protocol_sha256']==hashlib.sha256(Path('protocol.json').read_bytes()).hexdigest()
  assert supplied['reviewer_evidence_sha256'] and set(supplied)=={'protocol_sha256','reviewer_evidence_sha256','raw_sha256','pebs','lbr'}
  for kind in ['pebs','lbr']:
   assert type(supplied[kind]) is bool
   assert supplied['raw_sha256'][kind]==probes[kind].get('raw_sha256')
  review=supplied
 except (ValueError,KeyError,AssertionError):pass
save('probes-reviewed.json',review)

records=[]
for ci,c in enumerate(P['cells']):
 for v in c['variants'] if ci%2==0 else list(reversed(c['variants'])):
  tag=c['id']+'-'+v;rec={'cell':c['id'],'variant':v,'binary_sha256':hashlib.sha256((Path('build')/v/c['driver']).read_bytes()).hexdigest(),'captures':[],'deep':[]};proc=None;failure=None
  save(tag+'.record.json',rec)
  try:
   proc,out,err,args=launch(c,v,tag);rec['workload_command']=args
   runner=ToplevRunner(str(Path('pmu/toplev.py').resolve()),ToplevOptions(level=2,extra_args=['-C','2']))
   for rep in range(1,4):
    name=f'{tag}-L2-{rep}';cap={'tag':name,'rep':rep,'level':2,'qualified':False,'status':'STARTED'};rec['captures'].append(cap);save(tag+'.record.json',rec)
    a=snapshot(proc.pid);stdout,stderr=runner.run(5)
    (O/(name+'.stdout')).write_text(stdout);(O/(name+'.stderr')).write_text(stderr)
    cap.update(raw_sha256=hashlib.sha256(stderr.encode()).hexdigest(),command=runner.build_command()+['--','sleep','5']);save(tag+'.record.json',rec)
    try:sc=scope(a,snapshot(proc.pid))
    except BaseException as e:sc={'before':a,'after':None,'pass':False,'error':str(e)}
    save(name+'.scope.json',sc)
    if not sc['pass']:raise IsolationError(name+' scope failed')
    samples=parse_output(stderr) or parse_output(stdout);save(name+'.samples.json',[dataclasses.asdict(x) for x in samples])
    lines=stderr.splitlines();headers=[i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,')]
    rows=[r for r in csv.DictReader(lines[headers[0]:]) if r.get('Area')] if len(headers)==1 else [];bytime=collections.defaultdict(list)
    for r in rows:
     if r['Area'] in ROOTS:bytime[r['Timestamp']].append(r)
    roots=len(bytime)==5 and all(len(rs)==4 and {r['Area'] for r in rs}==ROOTS and all(r['Unit'] in ['% Slots','% Slots <'] and math.isfinite(float(r['Value'])) and 0<=float(r['Value'])<=100 for r in rs) and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in bytime.values())
    mux=[float(r['Multiplex']) for r in rows if r.get('Multiplex')];ok=roots and sc['pass'] and bool(mux) and len(mux)==len(rows) and all(x==100 for x in mux)
    cap.update(roots_pass=roots,scope_pass=sc['pass'],mux_min=min(mux) if mux else None,qualified=ok,status='COLLECTED');save(tag+'.record.json',rec)
   kind=c['deep']
   if kind and probes[kind]['available'] and review.get(kind) is True:
    for rep in range(1,3):
     entry={'tag':f'{tag}-{kind}-{rep}','status':'STARTED'};rec['deep'].append(entry);save(tag+'.record.json',rec);entry.update(deep(entry['tag'],kind,proc.pid));entry['status']='COLLECTED'
   elif kind:rec['deep_skipped']='unsupported or unqualified probe; original retained'
   rec['status']='COLLECTED'
  except BaseException as e:
   rec.update(status='INCOMPLETE',error=str(e),traceback=traceback.format_exc());failure=e
  finally:
   if proc is not None:finish(proc,out,err);rec['workload_returncode']=proc.returncode
   save(tag+'.record.json',rec);records.append(rec);save('summary.json',records)
  print(json.dumps({'done':len(records),'total':16,'tag':tag,'status':rec['status'],'l2_pass':sum(x['qualified'] for x in rec['captures']),'deep_captures':len(rec['deep'])}),flush=True)
  if failure is not None:raise failure
save('RESULT.json',{'configurations':len(records),'qualified_l2_windows':sum(x['qualified'] for r in records for x in r['captures']),'source_adoption':'NONE','timing_acceptance':False})
