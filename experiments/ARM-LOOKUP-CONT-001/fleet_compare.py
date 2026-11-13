#!/usr/bin/env python3
"""Serial fleet-only comparisons after full cohort qualification."""
import argparse,os,pathlib,json,hashlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--phase',required=True);p.add_argument('--variants',default='ABC');p.add_argument('--cohort',default='gcc15-lto');p.add_argument('--seed',default='17');a=p.parse_args();root=pathlib.Path(a.root);os.chdir(root)
out=root/a.phase;out.mkdir();exp='experiments/ARM-LOOKUP-CONT-001'
lease=json.loads((root/'reservation.json').read_text());assert lease['owner']=='bplus ARM-LOOKUP-CONT-001' and lease['state']=='RESERVED' and time.time()<lease['deadline']-900
assert subprocess.check_output(['systemctl','is-active','bplus-arm-lookup-cont-20261113-release.timer'],text=True).strip()=='active'
def run(cmd,stem):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=240);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'argv':cmd,'stem':stem,'returncode':q.returncode})+'\n')
 assert q.returncode==0,(stem,q.stderr[-1600:]);return q
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
prior=json.loads((root/'baseline/metadata.json').read_text());base=root/'bin'/a.cohort/'lookup';assert sha(base)==prior['binary_sha256'][a.cohort]
meta={'started':time.time(),'cohort':a.cohort,'seed':a.seed,'baseline_sha256':sha(base),'variants':{},'source_freeze':'ee8e7f70152404649ac947157fd662d11b4a00d5'}
for v in a.variants:
 src='variants/'+a.phase+'/'+v+'/zset_btree.c';binary='bin/'+a.phase+'-'+v;(root/'bin').mkdir(exist_ok=True)
 cmd=['cc']+(['-flto=auto'] if a.cohort=='gcc15-lto' else [])+['-std=c11','-O3','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-I'+exp+'/current/src','-I'+exp+'/current/compat','-I'+exp+'/current/vendor',exp+'/lookup.c',src,exp+'/current/compat/standalone.c',exp+'/current/vendor/siphash.c','-lm','-o',binary]
 if a.cohort=='gcc15-lto':cmd=['docker','run','--rm','--cpuset-cpus','0-3','--network','none','-v',str(root)+':/work','-w','/work',prior['gcc15_image']]+cmd
 else:cmd=['taskset','-c','0']+cmd
 run(cmd,'build-'+v);run(['objdump','-d',str(root/binary)],'assembly-'+v);run(['size',str(root/binary)],'size-'+v)
 meta['variants'][v]={'source_sha256':sha(root/src),'binary_sha256':sha(root/binary)}
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity-zero-work');assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
(out/'metadata.json').write_text(json.dumps(meta,indent=2))
cases={'hit':50000,'score':50000,'miss':100000,'long':20000,'external':20000,'update':20000}
for v in a.variants:
 binary=root/'bin'/(a.phase+'-'+v)
 for case,sweeps in cases.items():
  run(['taskset','-c','2',str(binary),'verify',case,a.seed,'1'],f'verify-{v}-{case}')
  for block in range(3):
   for slot,label in enumerate('ABBA'):
    target=base if label=='A' else binary
    q=run(['taskset','-c','2',str(target),'measure',case,a.seed,str(sweeps)],f'compare-{v}-{case}-{block}-{slot}')
    row=json.loads(q.stdout);row.update(cohort=a.cohort,variant=v,block=block,slot=slot,label=label,binary_sha256=sha(target))
    with (out/'comparison.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
    print('COMPARE',v,case,block,slot,flush=True)
(out/'COMPLETE.json').write_text(json.dumps({'timing_rows':72*len(a.variants),'finished':time.time()}));print('COMPLETE',flush=True)
