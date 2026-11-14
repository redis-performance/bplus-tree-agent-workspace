#!/usr/bin/env python3
"""Fleet-only baseline qualification; independent owned bounded unit required."""
import argparse,os,pathlib,json,hashlib,subprocess,time,shutil
p=argparse.ArgumentParser();p.add_argument('--root',required=True);a=p.parse_args();root=pathlib.Path(a.root);os.chdir(root)
out=root/'native-requalification';out.mkdir();exp='experiments/ARM-LOOKUP-CONT-001'
lease=json.loads((root/'reservation.json').read_text());assert lease['owner']=='bplus ARM-LOOKUP-CONT-001' and lease['state']=='RESERVED' and time.time()<lease['deadline']-600
assert subprocess.check_output(['systemctl','is-active',root.name+'-release.timer'],text=True).strip()=='active'
def run(cmd,stem,check=True):
 q=subprocess.run(cmd,capture_output=True,text=True,timeout=240);(out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps({'argv':cmd,'stem':stem,'returncode':q.returncode})+'\n')
 if check:assert q.returncode==0,(stem,q.stderr[-1600:])
 return q
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
image=json.loads(run(['docker','image','inspect','gcc:15.2.0-bookworm'],'image').stdout)[0]
imageid=image['Id'];meta={'source_manifest':json.loads((root/exp/'unstable-manifest.json').read_text()),'gcc15_image':imageid,'gcc15_digests':image.get('RepoDigests',[]),'started':time.time(),'CPU':2,'siblings':pathlib.Path('/sys/devices/system/cpu/cpu2/topology/thread_siblings_list').read_text().strip(),'runtime_libc':subprocess.check_output(['ldd','--version'],text=True).splitlines()[0]}
prior=json.loads((root/'baseline/metadata.json').read_text())
assert all(sha(root/'bin'/c/'lookup')==h for c,h in prior['binary_sha256'].items())
# Retain image identity only; this requalification executes native only.
run(['cc','--version'],'native-version');run(['lscpu'],'CPU');run(['uname','-r'],'kernel')
run(['taskset','-c','2','python3','-c','import os;assert os.sched_getaffinity(0)=={2};print("CPU2")'],'affinity-zero-work')
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
meta['binary_sha256']={c:sha(root/'bin'/c/'lookup') for c in ['native','gcc15-lto']};(out/'metadata.json').write_text(json.dumps(meta,indent=2))
cases={'hit':50000,'score':50000,'miss':100000,'long':20000,'external':20000,'update':20000}
for cohort in ['native']:
 binary=str(root/'bin'/cohort/'lookup')
 for case,sweeps in cases.items():
  run(['taskset','-c','2',binary,'verify',case,'17','1'],f'verify-{cohort}-{case}')
  for block in range(3):
   for slot,label in enumerate('ABBA'):
    q=run(['taskset','-c','2',binary,'measure',case,'17',str(sweeps)],f'aa-{cohort}-{case}-{block}-{slot}')
    row=json.loads(q.stdout);row.update(cohort=cohort,block=block,slot=slot,label=label)
    with (out/'aa.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
    print('AA',cohort,case,block,slot,flush=True)
(out/'COMPLETE.json').write_text(json.dumps({'timing_rows':72,'finished':time.time()}));print('COMPLETE',flush=True)
