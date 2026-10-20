"""Serial profile-only sweep. No acceptance timing or retry of invalid captures."""
import collections,csv,dataclasses,hashlib,json,math,os,signal,subprocess,time,traceback
from pathlib import Path
from topdown.collector.toplev import ToplevRunner,ToplevOptions
from topdown.collector.csv_parser import parse_output
P=json.loads(Path('protocol-v2.json').read_text());O=Path('results');RAW=Path('raw');RAW.mkdir(exist_ok=True)
PERF='/usr/lib/linux-tools/7.0.0-1014-aws/perf';os.environ['PERF']=PERF
ROOTS={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def save(name,data):(O/name).write_text(json.dumps(data,indent=2)+'\n')
def snapshot(pid):
 assert os.sched_getaffinity(pid)=={2},'workload affinity changed'
 assert Path(f'/proc/{pid}/stat').read_text().rsplit(')',1)[1].split()[0]!='Z','workload exited'
 stat=Path('/proc/stat').read_text()
 return {'time':time.time(),'cpu':{str(c):list(map(int,next(l for l in stat.splitlines() if l.startswith(f'cpu{c} ')).split()[1:9])) for c in [2,50]},
  'proc':Path(f'/proc/{pid}/stat').read_text(),'schedstat':Path(f'/proc/{pid}/schedstat').read_text(),
  'frequency_khz':Path('/sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq').read_text().strip(),'affinity':sorted(os.sched_getaffinity(pid))}
def scope(a,b):
 def busy(c):
  delta=[y-x for x,y in zip(a['cpu'][str(c)],b['cpu'][str(c)])];total=sum(delta);work=total-delta[3]-delta[4]
  return total,work
 def ticks(s):f=s.rsplit(')',1)[1].split();return int(f[11])+int(f[12])
 total,cpu=busy(2);stotal,sbusy=busy(50);work=ticks(b['proc'])-ticks(a['proc'])
 smt=100*sbusy/stotal;err=100*abs(cpu-work)/max(1,cpu)
 return {'before':a,'after':b,'cpu_busy_ticks':cpu,'workload_ticks':work,'sibling_busy_percent':smt,'accounting_error_percent':err,'pass':a['affinity']==b['affinity']==[2] and smt<=1 and err<=1}
def execute(tag,args,seconds=3):
 try:r=subprocess.run(args,capture_output=True,text=True,timeout=seconds+120)
 except subprocess.TimeoutExpired as e:
  txt=lambda x:x.decode(errors='replace') if isinstance(x,bytes) else (x or '')
  r=subprocess.CompletedProcess(args,124,txt(e.stdout),txt(e.stderr)+'\nTIMEOUT\n')
 (O/(tag+'.stdout')).write_text(r.stdout);(O/(tag+'.stderr')).write_text(r.stderr)
 save(tag+'.command.json',{'args':args,'returncode':r.returncode})
 return r
schedule=[]
for i,c in enumerate(P['cells']):
 variants=c['variants'] if i%2==0 else list(reversed(c['variants']))
 for v in variants:schedule.append({'index':len(schedule),'cell':c,'variant':v})
save('schedule.json',schedule)
summary=[]
for item in schedule:
 if subprocess.check_output(["docker","ps","-q"],text=True).strip():raise RuntimeError("isolation lost: active container; abort sweep")
 c=item['cell'];v=item['variant'];tag=c['id']+'-'+v;binary=str(Path('build')/v/c['driver'])
 args=['numactl','--all','--physcpubind=2','--membind=0',binary]+c['args']
 record={'index':item['index'],'cell':c['id'],'variant':v,'workload_command':args,'binary_sha256':hashlib.sha256(Path(binary).read_bytes()).hexdigest(),'captures':[]}
 out=(O/(tag+'-workload.stdout')).open('w');err=(O/(tag+'-workload.stderr')).open('w')
 proc=subprocess.Popen(args,stdout=out,stderr=err,env=dict(os.environ,BPLUS_PROFILE_STOP='1'))
 try:
  deadline=time.monotonic()+90
  while time.monotonic()<deadline:
   assert proc.poll() is None,'workload exited before readiness'
   if '\nState:\tT' in Path(f'/proc/{proc.pid}/status').read_text():break
   time.sleep(.05)
  else:raise RuntimeError('readiness timeout')
  assert os.sched_getaffinity(proc.pid)=={2}
  (O/(tag+'-numa.txt')).write_text(Path(f'/proc/{proc.pid}/numa_maps').read_text())
  os.kill(proc.pid,signal.SIGCONT)
  for level,reps in [(2,3),(3,1)]:
   runner=ToplevRunner(str(Path('pmu/toplev.py').resolve()),ToplevOptions(level=level,extra_args=['-C','2']))
   for rep in range(reps):
    name=f'{tag}-L{level}-{rep+1}';a=snapshot(proc.pid);stdout,stderr=runner.run(5)
    (O/(name+'.stdout')).write_text(stdout);(O/(name+'.stderr')).write_text(stderr)
    b=snapshot(proc.pid);sc=scope(a,b);save(name+'.scope.json',sc)
    samples=parse_output(stderr) or parse_output(stdout);save(name+'.samples.json',[dataclasses.asdict(x) for x in samples])
    lines=stderr.splitlines();headers=[i for i,l in enumerate(lines) if l.startswith('Timestamp,Area,Value,Unit,')]
    rows=[r for r in csv.DictReader(lines[headers[0]:]) if r.get('Area')] if len(headers)==1 else []
    bytime=collections.defaultdict(list)
    for r in rows:
     if r['Area'] in ROOTS:bytime[r['Timestamp']].append(r)
    rootok=len(bytime)==5 and all(len(rs)==4 and {r['Area'] for r in rs}==ROOTS and all(r['Unit'] in ('% Slots','% Slots <') and math.isfinite(float(r['Value'])) and 0<=float(r['Value'])<=100 for r in rs) and abs(sum(float(r['Value']) for r in rs)-100)<=.3 for rs in bytime.values())
    mux=[float(r['Multiplex']) for r in rows if r.get('Multiplex')]
    rec={'tag':name,'level':level,'rep':rep+1,'command':runner.build_command()+['--','sleep','5'],'raw_sha256':hashlib.sha256(stderr.encode()).hexdigest(),'roots_pass':rootok,'scope_pass':sc['pass'],'multiplex_min':min(mux) if mux else None,'l2_qualified':level==2 and bool(mux) and len(mux)==len(rows) and all(x==100 for x in mux) and rootok and sc['pass'],'preamble':lines[:headers[0]] if headers else lines}
    record['captures'].append(rec);save(tag+'.record.json',record)
  name=tag+'-counters';a=snapshot(proc.pid)
  counter_result=execute(name,[PERF,'stat','-a','-C','2','-x,','-e','{cycles,instructions,ref-cycles,branches,branch-misses}','--','sleep','3'])
  save(name+'.scope.json',scope(a,snapshot(proc.pid)))
  name=tag+'-samples';raw=RAW/(tag+'.perf.data');a=snapshot(proc.pid)
  sample_result=execute(name,[PERF,'record','-e','cycles:u','-F','199','-p',str(proc.pid),'-o',str(raw),'--','sleep','3'])
  save(name+'.scope.json',scope(a,snapshot(proc.pid)))
  record['counter_returncode']=counter_result.returncode;record['sample_returncode']=sample_result.returncode
  record['sample_report_returncodes']=[]
  if raw.exists():
   record['raw_perf_sha256']=hashlib.sha256(raw.read_bytes()).hexdigest();record['raw_perf_bytes']=raw.stat().st_size
   report=execute(tag+'-symbols',[PERF,'report','--stdio','--no-children','--percent-limit','0','--sort','symbol,dso','-i',str(raw)])
   events=execute(tag+'-sample-events',[PERF,'script','-i',str(raw),'-F','event,ip,sym,dso'])
   record['sample_report_returncodes']=[report.returncode,events.returncode]
  record['status']='COLLECTED' if counter_result.returncode==sample_result.returncode==0 and raw.exists() and record['sample_report_returncodes']==[0,0] else 'PARTIAL'
 except Exception as e:
  record['status']='INCOMPLETE';record['error']=str(e);record['traceback']=traceback.format_exc()
 finally:
  if proc.poll() is None:
   proc.terminate();os.kill(proc.pid,signal.SIGCONT)
   try:proc.wait(timeout=5)
   except subprocess.TimeoutExpired:proc.kill();proc.wait()
  record['workload_returncode']=proc.returncode;out.close();err.close()
 save(tag+'.record.json',record);summary.append(record);save('summary.json',summary)
 print(json.dumps({'done':len(summary),'total':len(schedule),'cell':c['id'],'variant':v,'status':record['status'],'l2_pass':sum(x['l2_qualified'] for x in record['captures'])}),flush=True)
save('RESULT.json',{'decision':'DIAGNOSTIC_ONLY','configurations':len(summary),'collected':sum(x['status']=='COLLECTED' for x in summary),'qualified_l2_windows':sum(c['l2_qualified'] for x in summary for c in x['captures']),'source_adoption':'NONE','timing_acceptance':False})
