#!/usr/bin/env python3
"""Fleet-only held-out controls, confirmation or matched profile stage."""
import argparse,json,os,pathlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--stage',choices=['controls','confirm','profiles'],required=True);p.add_argument('--variant',choices=['A','B','C'],required=True);p.add_argument('--perf',default='/usr/lib/linux-tools/6.14.0-1010-aws/perf');a=p.parse_args()
root=pathlib.Path(a.root);os.chdir(root);out=root/('heldout-'+a.stage);out.mkdir()
lease=json.loads((root/'reservation.json').read_text());assert lease['state']=='RESERVED' and lease['owner']=='bplus ARM-LOOKUP-GAP-001' and time.time()<lease['deadline']-900
assert subprocess.check_output(['systemctl','is-active','bplus-arm-lookup-gap-20261113-release.timer'],text=True).strip()=='active'
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
def run(cmd,stem,check=True):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=180);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'stem':stem,'argv':cmd,'returncode':q.returncode})+'\n')
 if check:assert q.returncode==0,(stem,q.stderr[-1000:])
 return q
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity-zero-work')
if a.stage in ['controls','confirm']:
 for seed in [29,43]:
  for case in ['hit','score','miss','long']:
   for block in range(3):
    for slot,arm in enumerate('ABBA'):
     binary=root/'bin/A' if arm=='A' or a.stage=='controls' else root/'variants'/a.variant/'bin/lookup'
     q=run(['taskset','-c','2',str(binary),'measure',case,str(seed),'100000'],f'{seed}-{case}-{block}-{slot}')
     row=json.loads(q.stdout);row.update(stage=a.stage,variant=a.variant,block=block,slot=slot,arm=arm)
     with (out/'rows.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
     print(seed,case,block,slot,flush=True)
else:
 for arm,binary in [('baseline',root/'bin/A'),('candidate',root/'variants'/a.variant/'bin/lookup')]:
  for i in range(3):run([a.perf,'stat','-x,','-e','cycles:u,instructions:u,branches:u,branch-misses:u','--','taskset','-c','2',str(binary),'measure','hit','29','400000'],f'stat-{arm}-{i}')
  run([a.perf,'record','-o',str(out/(arm+'.data')),'-F','999','-e','cycles:u','--','taskset','-c','2',str(binary),'measure','hit','29','400000'],f'record-{arm}')
  run([a.perf,'report','--stdio','--no-children','--percent-limit','0','-i',str(out/(arm+'.data')),'-s','dso,symbol'],f'report-{arm}')
  from topdown.collector.perf_stat import PerfStatOptions,PerfStatRunner
  cmd=PerfStatRunner(PerfStatOptions(interval_ms=1000,pids=None,extra_args=['-C','2'])).build_command();cmd[0]=a.perf
  run(cmd+['--','taskset','-c','2',str(binary),'measure','hit','29','400000'],'topdown-'+arm,False)
(out/'COMPLETE.json').write_text(json.dumps({'stage':a.stage,'variant':a.variant,'finished':time.time()}));print('COMPLETE',flush=True)
