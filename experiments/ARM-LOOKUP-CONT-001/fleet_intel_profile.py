#!/usr/bin/env python3
"""Owned Intel steady-workload profiles; timing acceptance is separate."""
import argparse,collections,csv,hashlib,importlib.metadata,json,math,os,pathlib,signal,subprocess,time
from topdown.collector.toplev import ToplevRunner,ToplevOptions
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--label',required=True);p.add_argument('--binary',required=True);a=p.parse_args();root=pathlib.Path(a.root);out=root/a.label;out.mkdir();binary=root/a.binary
lease=json.loads((root/'reservation.json').read_text());assert lease['state']=='RESERVED' and time.time()<lease['deadline']-300
assert subprocess.check_output(['systemctl','is-active',root.name+'-release.timer'],text=True).strip()=='active';assert os.sched_getaffinity(0)=={0}
perf='/usr/lib/linux-tools/'+subprocess.check_output(['uname','-r'],text=True).strip()+'/perf';assert pathlib.Path(perf).exists();os.environ['PERF']=perf;os.environ['CACHEDIR']=str(root/'pmu-events')
roots={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def save(n,d):(out/n).write_text(json.dumps(d,indent=2)+'\n')
def run(cmd,stem,timeout=90):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr);save(stem+'.command.json',{'argv':cmd,'returncode':q.returncode});return q

def snap(pid):
 assert pathlib.Path('/sys/devices/system/cpu/cpu50/online').read_text().strip()=='0'
 assert subprocess.run(['systemctl','is-active','--quiet','snap.parca-agent.parca-agent-svc.service']).returncode!=0
 assert os.sched_getaffinity(pid)=={2}
 proc=pathlib.Path(f'/proc/{pid}/stat').read_text();assert proc.rsplit(')',1)[1].split()[0]!='Z'
 cpu=next(l for l in pathlib.Path('/proc/stat').read_text().splitlines() if l.startswith('cpu2 '));return {'time':time.time(),'cpu2':list(map(int,cpu.split()[1:9])),'proc':proc,'affinity':[2],'sibling_offline':True,'parca_inactive':True}
def scope(x,y):
 delta=[b-a for a,b in zip(x['cpu2'],y['cpu2'])];busy=sum(delta)-delta[3]-delta[4]
 ticks=lambda s:sum(int(s.rsplit(')',1)[1].split()[i]) for i in [11,12]);work=ticks(y['proc'])-ticks(x['proc']);error=100*abs(busy-work)/max(1,busy)
 return {'before':x,'after':y,'cpu_busy_ticks':busy,'workload_ticks':work,'accounting_error_percent':error,'pass':busy>0 and error<=1}
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
assert run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity').returncode==0
assert run(['taskset','-c','2',str(binary),'verify','hit','17','1'],'verify').returncode==0
meta={'started':time.time(),'binary_sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),'topdown_version':importlib.metadata.version('topdown-profiler'),'pmu_revision':(root/'pmu-revision.txt').read_text().strip(),'controller_affinity':[0],'workload_affinity':[2],'kernel':subprocess.check_output(['uname','-r'],text=True).strip(),'nmi_watchdog':pathlib.Path('/proc/sys/kernel/nmi_watchdog').read_text().strip(),'perf_event_paranoid':pathlib.Path('/proc/sys/kernel/perf_event_paranoid').read_text().strip()};save('metadata.json',meta)
run([perf,'--version'],'perf-version');run(['size',str(binary)],'size');run(['objdump','-d',str(binary)],'assembly')
f=(out/'workload.stdout').open('w');e=(out/'workload.stderr').open('w');cmd=['taskset','-c','2',str(binary),'measure','hit','17','40000000'];child=subprocess.Popen(cmd,stdout=f,stderr=e);save('workload-command.json',cmd);quality=[]
try:
 time.sleep(.5);snap(child.pid)
 runner=ToplevRunner(str(root/'pmu-tools/toplev.py'),ToplevOptions(level=2,extra_args=['-C','2']))
 for i in range(3):
  stem='tma-'+str(i);x=snap(child.pid);q=run(runner.build_command()+['--','sleep','5'],stem);sc=scope(x,snap(child.pid));save(stem+'.scope.json',sc)
  lines=(q.stderr+'\n'+q.stdout).splitlines();heads=[j for j,l in enumerate(lines) if 'Timestamp' in l and 'Area' in l and 'Value' in l and 'Unit' in l];rows=list(csv.DictReader(lines[heads[0]:])) if len(heads)==1 else [];rows=[r for r in rows if r.get('Area')];groups=collections.defaultdict(list)
  for r in rows:
   if r['Area'] in roots:groups[r['Timestamp']].append(r)
  try:
   partition=len(groups)==5 and all(len(v)==4 and {r['Area'] for r in v}==roots and all(r['Unit'] in ['% Slots','% Slots <'] and math.isfinite(float(r['Value'])) and 0<=float(r['Value'])<=100 for r in v) and abs(sum(float(r['Value']) for r in v)-100)<=.3 for v in groups.values());mux=[float(r['Multiplex']) for r in rows];muxok=bool(rows) and len(mux)==len(rows) and all(v==100 for v in mux)
  except (KeyError,ValueError):partition=False;muxok=False;mux=[]
  rec={'capture':stem,'scope_pass':sc['pass'],'partition_pass':partition,'multiplex_all_100':muxok,'qualified':q.returncode==0 and sc['pass'] and partition and muxok,'rows':len(rows),'multiplex_min':min(mux) if mux else None};quality.append(rec);save(stem+'.quality.json',rec)
 x=snap(child.pid);q=run([perf,'stat','-p',str(child.pid),'-x,','-e','{cycles:u,instructions:u,branches:u,branch-misses:u}','--','sleep','3'],'counters');save('counters.scope.json',scope(x,snap(child.pid)))
 x=snap(child.pid);q=run([perf,'record','-p',str(child.pid),'-F','999','-e','cycles:u','-o',str(out/'hit.data'),'--','sleep','3'],'samples');save('samples.scope.json',scope(x,snap(child.pid)))
 if (out/'hit.data').exists():run([perf,'report','--stdio','--no-children','--percent-limit','0','-i',str(out/'hit.data'),'-s','dso,symbol'],'report')
 save('COMPLETE.json',{'finished':time.time(),'tma':quality,'all_tma_qualified':all(x['qualified'] for x in quality),'timing_acceptance':False})
finally:
 if child.poll() is None:child.terminate()
 try:child.wait(timeout=5)
 except subprocess.TimeoutExpired:child.kill();child.wait()
 f.close();e.close();save('workload-end.json',{'returncode':child.returncode,'intentionally_terminated':True})
