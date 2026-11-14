#!/usr/bin/env python3
import argparse,pathlib,json,subprocess,time,hashlib
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--output',required=True);p.add_argument('--binary',required=True);a=p.parse_args();root=pathlib.Path(a.root);out=root/a.output;out.mkdir();binary=str(root/a.binary)
lease=json.loads((root/'reservation.json').read_text());assert lease['state']=='RESERVED' and time.time()<lease['deadline']-300
assert subprocess.check_output(['systemctl','is-active',root.name+'-release.timer'],text=True).strip()=='active'
def run(cmd,stem):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=180);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'argv':cmd,'stem':stem,'returncode':q.returncode})+'\n')
 assert q.returncode==0,(stem,q.stderr[-1600:])
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity-zero-work')
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
perf='/usr/lib/linux-tools/6.14.0-1010-aws/perf';work=['--','taskset','-c','2',binary,'measure','hit','17','400000']
for i in range(3):run([perf,'stat','-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u']+work,'stat-'+str(i))
run([perf,'record','-o',str(out/'hit.data'),'-F','999','-e','cycles:u']+work,'record');run([perf,'report','--stdio','--no-children','--percent-limit','0','-i',str(out/'hit.data'),'-s','dso,symbol'],'report')
from topdown.collector.perf_stat import PerfStatRunner,PerfStatOptions
cmd=PerfStatRunner(PerfStatOptions(interval_ms=1000,extra_args=['-C','2'])).build_command();cmd[0]=perf;run(cmd+work,'topdown')
run(['objdump','-d',binary],'assembly');run(['size',binary],'size');run([perf,'--version'],'perf-version')
(out/'COMPLETE.json').write_text(json.dumps({'finished':time.time(),'binary_sha256':hashlib.sha256(pathlib.Path(binary).read_bytes()).hexdigest(),'scope':'process-user counters/samples; CPU2-wide topdown exploratory; setup/warmup included'}))
