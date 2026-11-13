#!/usr/bin/env python3
"""Fleet-only frozen qualification. Invoke inside an owned bounded unit."""
import argparse,hashlib,json,os,pathlib,shutil,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--perf',required=True);args=p.parse_args()
root=pathlib.Path(args.root);os.chdir(root);out=root/'evidence';out.mkdir(exist_ok=True)
assert not (out/'aa.jsonl').exists(),'Never overwrite or retry a completed/partial cohort'
lease=json.loads((root/'reservation.json').read_text());assert lease['owner']=='bplus ARM-LOOKUP-GAP-001' and lease['state']=='RESERVED' and time.time()<lease['deadline']-600
assert subprocess.check_output(['systemctl','is-active','bplus-arm-lookup-gap-20261113-release.timer'],text=True).strip()=='active'
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
def run(cmd,stem,timeout=180,check=True):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)
 (out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'stem':stem,'argv':cmd,'returncode':q.returncode})+'\n')
 if check:assert q.returncode==0,(stem,q.stderr[-1000:])
 return q
run(['sh','experiments/ARM-LOOKUP-GAP-001/build.sh','bin'],'build')
for label in ['A','B']:shutil.copy2(root/'bin/lookup',root/('bin/'+label))
sha=lambda f:hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()
run(['taskset','-c','2','python3','-c','import os,json; a=sorted(os.sched_getaffinity(0));assert a==[2];print(json.dumps(a))'],'affinity-zero-work')
meta={'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'cpu':2,'sibling_list':pathlib.Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip(),'binary_sha256':{l:sha(root/('bin/'+l)) for l in ['A','B']},'unstable_manifest':json.loads((root/'experiments/ARM-LOOKUP-GAP-001/unstable-manifest.json').read_text()),'scope':'One process, CPU 2; timing loop only. perf stat/record cover process lifetime. Topdown is CPU-wide and separate.','background':'OS services and existing parca-agent left unchanged. Coordinator paused with saved identity. No benchmark containers.','kernel':subprocess.check_output(['uname','-r'],text=True).strip(),'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],'libc':subprocess.check_output(['ldd','--version'],text=True).splitlines()[0],'perf':subprocess.check_output([args.perf,'--version'],text=True).strip(),'cpufreq':{}}
for n in ['scaling_governor','scaling_cur_freq','cpuinfo_max_freq','cpuinfo_min_freq']:
 f=pathlib.Path('/sys/devices/system/cpu/cpu2/cpufreq')/n;meta['cpufreq'][n]=f.read_text().strip() if f.exists() else 'unavailable'
run(['lscpu'],'cpu');(out/'metadata.json').write_text(json.dumps(meta,indent=2))
for case in ['hit','score','miss','long']:
 run(['taskset','-c','2','bin/A','verify',case,'17','1'],'verify-'+case)
 for block in range(3):
  for slot,label in enumerate('ABBA'):
   q=run(['taskset','-c','2','bin/'+label,'measure',case,'17','100000'],f'aa-{case}-{block}-{slot}')
   row=json.loads(q.stdout);row.update(block=block,slot=slot,label=label)
   with (out/'aa.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
   print('AA',case,block,slot,flush=True)
for i in range(3):
 run([args.perf,'stat','-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','--','taskset','-c','2','bin/A','measure','hit','17','400000'],f'stat-hit-{i}')
for case in ['hit','long']:
 run([args.perf,'record','-o',str(out/(case+'.data')),'-F','999','-e','cycles:u','--','taskset','-c','2','bin/A','measure',case,'17','400000'],'record-'+case)
 run([args.perf,'report','--stdio','--no-children','--percent-limit','0','-i',str(out/(case+'.data')),'-s','dso,symbol'],'report-'+case)
from topdown.collector.perf_stat import PerfStatOptions,PerfStatRunner
import importlib.metadata,inspect
runner=PerfStatRunner(PerfStatOptions(interval_ms=1000,pids=None,extra_args=['-C','2']))
cmd=runner.build_command();cmd[0]=args.perf
(out/'topdown-collector.json').write_text(json.dumps({'version':importlib.metadata.version('topdown-profiler'),'source_sha256':sha(inspect.getfile(PerfStatRunner)),'actual_command':cmd,'scope':'CPU-wide CPU 2, not process isolated; background OS work may be included'},indent=2))
run(cmd+['--','taskset','-c','2','bin/A','measure','hit','17','400000'],'topdown-hit',check=False)
run([args.perf,'list','--details'],'perf-list',check=False)
(out/'COMPLETE.json').write_text(json.dumps({'complete':True,'rows':48,'finished':time.time()},indent=2));print('COMPLETE',flush=True)
