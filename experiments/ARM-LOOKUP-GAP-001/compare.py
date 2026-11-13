#!/usr/bin/env python3
"""Run only on the reserved fleet host, inside its bounded owned service."""
import argparse,hashlib,json,os,pathlib,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--root',required=True);args=p.parse_args();root=pathlib.Path(args.root);os.chdir(root)
out=root/'comparison';out.mkdir();lease=json.loads((root/'reservation.json').read_text());assert lease['state']=='RESERVED' and lease['owner']=='bplus ARM-LOOKUP-GAP-001' and time.time()<lease['deadline']-900
assert subprocess.check_output(['systemctl','is-active','bplus-arm-lookup-gap-20261113-release.timer'],text=True).strip()=='active'
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
def run(cmd,stem,cwd=None):
 q=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=180);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'stem':stem,'argv':cmd,'returncode':q.returncode})+'\n')
 assert q.returncode==0,(stem,q.stderr[-1000:]);return q
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
manifest={}
for v in ['A','B','C']:
 vr=root/'variants'/v
 run(['sh','experiments/ARM-LOOKUP-GAP-001/build.sh','bin'],'build-'+v,cwd=vr)
 src=vr/'experiments/ARM-LOOKUP-GAP-001/current/src/zset_btree.c'
 assert sha(src)==json.loads((root/'candidate-manifest.json').read_text())[v]['source_sha256']
 manifest[v]={'binary_sha256':sha(vr/'bin/lookup'),'source_sha256':sha(src)}
 run(['objcopy','--dump-section','.text='+str(out/(v+'.text')),str(vr/'bin/lookup')],'text-'+v)
 manifest[v]['text_sha256']=sha(out/(v+'.text'))
 run(['objdump','-d','--disassemble=zbtScoreLeafFindMember.constprop.0',str(vr/'bin/lookup')],'assembly-'+v)
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity-zero-work')
manifest['baseline']={'binary_sha256':sha(root/'bin/A')}
assert manifest['baseline']['binary_sha256']=='d54311ffae324cf623a000f1c026f377c3657f5810c76cd1b2284645b9411431'
(out/'manifest.json').write_text(json.dumps(manifest,indent=2))
for v in ['A','B','C']:
 for case in ['hit','score','miss','long']:
  run(['taskset','-c','2',str(root/'variants'/v/'bin/lookup'),'verify',case,'17','1'],f'verify-{v}-{case}')
  for block in range(3):
   for slot,arm in enumerate('ABBA'):
    binary=root/'bin/A' if arm=='A' else root/'variants'/v/'bin/lookup'
    q=run(['taskset','-c','2',str(binary),'measure',case,'17','100000'],f'{v}-{case}-{block}-{slot}')
    row=json.loads(q.stdout);row.update(variant=v,block=block,slot=slot,arm=arm)
    with (out/'rows.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
    print(v,case,block,slot,flush=True)
(out/'COMPLETE.json').write_text(json.dumps({'rows':144,'finished':time.time()}));print('COMPLETE',flush=True)
