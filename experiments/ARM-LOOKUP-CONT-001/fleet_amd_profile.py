#!/usr/bin/env python3
"""Owned AMD baseline diagnostic profiles; timing acceptance is separate."""
import argparse,shutil,collections,csv,hashlib,importlib.metadata,json,math,os,pathlib,signal,subprocess,time
from topdown.collector.uprof_pcm import UprofPcmRunner,UprofPcmOptions
import inspect
p=argparse.ArgumentParser();p.add_argument('--perf',required=True);p.add_argument('--case',choices=['hit','update'],default='hit');p.add_argument('--start-rep',type=int,default=0);p.add_argument('--resume-from');p.add_argument('--root',required=True);p.add_argument('--label',required=True);p.add_argument('--binary',required=True);a=p.parse_args();root=pathlib.Path(a.root);out=root/a.label;out.mkdir();binary=root/a.binary
lease=json.loads((root/'reservation.json').read_text());assert lease['state']=='RESERVED' and time.time()<lease['deadline']-300
assert subprocess.check_output(['systemctl','is-active',root.name+'-release.timer'],text=True).strip()=='active';assert os.sched_getaffinity(0)=={0}
perf=str(pathlib.Path(a.perf).resolve(strict=True));assert pathlib.Path(perf).is_file();os.environ['PERF']=perf
roots={'Frontend_Bound','Bad_Speculation','Backend_Bound','Retiring'}
def save(n,d):(out/n).write_text(json.dumps(d,indent=2)+'\n')
def run(cmd,stem,timeout=90):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr);save(stem+'.command.json',{'argv':cmd,'returncode':q.returncode});return q

def snap(pid):
 assert pathlib.Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip()=='2'
 assert subprocess.run(['systemctl','is-active','--quiet','snap.parca-agent.parca-agent-svc.service']).returncode!=0
 assert os.sched_getaffinity(pid)=={2}
 proc=pathlib.Path(f'/proc/{pid}/stat').read_text();assert proc.rsplit(')',1)[1].split()[0]!='Z'
 cpu=next(l for l in pathlib.Path('/proc/stat').read_text().splitlines() if l.startswith('cpu2 '));return {'time':time.time(),'cpu2':list(map(int,cpu.split()[1:9])),'proc':proc,'affinity':[2],'siblings':[2],'parca_inactive':True}
def scope(x,y):
 delta=[b-a for a,b in zip(x['cpu2'],y['cpu2'])];busy=sum(delta)-delta[3]-delta[4]
 ticks=lambda s:sum(int(s.rsplit(')',1)[1].split()[i]) for i in [11,12]);work=ticks(y['proc'])-ticks(x['proc']);error=100*abs(busy-work)/max(1,busy)
 return {'before':x,'after':y,'cpu_busy_ticks':busy,'workload_ticks':work,'accounting_error_percent':error,'pass':busy>0 and error<=1}
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
assert run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity').returncode==0
assert run(['taskset','-c','2',str(binary),'verify',a.case,'17','1'],'verify').returncode==0
meta={'started':time.time(),'perf_path':perf,'perf_sha256':hashlib.sha256(pathlib.Path(perf).read_bytes()).hexdigest(),'binary_sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),'topdown_version':importlib.metadata.version('topdown-profiler'),'uprof_collector_sha256':hashlib.sha256(inspect.getsource(UprofPcmRunner).encode()).hexdigest(),'case':a.case,'tma_scope':'PID user selection with workload pinned to CPU2; scheduling/formulas require offline audit','controller_affinity':[0],'workload_affinity':[2],'kernel':subprocess.check_output(['uname','-r'],text=True).strip(),'nmi_watchdog':pathlib.Path('/proc/sys/kernel/nmi_watchdog').read_text().strip(),'perf_event_paranoid':pathlib.Path('/proc/sys/kernel/perf_event_paranoid').read_text().strip()};save('metadata.json',meta)
run([perf,'--version'],'perf-version');run(['size',str(binary)],'size');run(['objdump','-d',str(binary)],'assembly')
f=(out/'workload.stdout').open('w');e=(out/'workload.stderr').open('w');cmd=['taskset','-c','2',str(binary),'measure',a.case,'17','10000000'];child=subprocess.Popen(cmd,stdout=f,stderr=e);save('workload-command.json',cmd);quality=[]
try:
 if a.start_rep:
  assert a.start_rep==1 and a.resume_from
  prior=root/a.resume_from;assert json.loads((prior/'metadata.json').read_text())['binary_sha256']==meta['binary_sha256']
  for src in prior.glob('tma-0.*'):shutil.copy2(src,out/src.name)
  save('resume.json',{'from':a.resume_from,'kept_capture':'tma-0','raw_sha256':hashlib.sha256((out/'tma-0.stderr').read_bytes()).hexdigest()})
  quality.append({'capture':'tma-0','resumed_raw':True})
 time.sleep(.5);assert (out/'workload.stderr').stat().st_size==0, 'workload startup failed';snap(child.pid)
 runner=UprofPcmRunner(UprofPcmOptions())
 for i in range(a.start_rep,3):
  stem='tma-'+str(i);generated=runner.build_command(str(out/(stem+'.csv')),5);save(stem+'.generated-command.json',generated)
  assert generated.count('-a')==1
  command=[x for x in generated if x!='-a']+['-p',str(child.pid),'-u','1']
  x=snap(child.pid);q=run(command,stem);sc=scope(x,snap(child.pid));save(stem+'.scope.json',sc)
  quality.append({'capture':stem,'scope_pass':sc['pass'],'returncode':q.returncode})
  if q.returncode:break
 x=snap(child.pid);q=run([perf,'stat','-p',str(child.pid),'-x,','-e','{cycles:u,instructions:u,branches:u,branch-misses:u}','--','sleep','3'],'counters');save('counters.scope.json',scope(x,snap(child.pid)))
 x=snap(child.pid);q=run([perf,'record','-p',str(child.pid),'-F','999','-e','cycles:u','-o',str(out/'hit.data'),'--','sleep','3'],'samples');save('samples.scope.json',scope(x,snap(child.pid)))
 if (out/'hit.data').exists():run([perf,'report','--stdio','--no-children','--percent-limit','0','-i',str(out/'hit.data'),'-s','dso,symbol'],'report')
 save('COMPLETE.json',{'finished':time.time(),'tma':quality,'tma_qualification':'offline_pending','timing_acceptance':False})
finally:
 terminated=child.poll() is None
 if terminated:child.terminate()
 try:child.wait(timeout=5)
 except subprocess.TimeoutExpired:child.kill();child.wait()
 f.close();e.close();save('workload-end.json',{'returncode':child.returncode,'intentionally_terminated':terminated})
