#!/usr/bin/env python3
"""Fresh-seed qualification followed by comparison of immutable selected ELFs."""
import argparse,hashlib,json,os,pathlib,shutil,statistics,subprocess,time
p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--phase',required=True);p.add_argument('--cohort',required=True);p.add_argument('--seed',type=int,choices=[29,43],required=True);p.add_argument('--scale',type=int,choices=[1,5],required=True);p.add_argument('--variant',required=True);p.add_argument('--binary',required=True);p.add_argument('--binary-sha256',required=True);p.add_argument('--source-sha256',required=True);a=p.parse_args()
root=pathlib.Path(a.root);out=root/a.phase;out.mkdir();os.chdir(root)
sha=lambda p:hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
lease=json.loads((root/'reservation.json').read_text());assert lease['owner']=='bplus ARM-LOOKUP-CONT-001' and lease['state']=='RESERVED' and time.time()<lease['deadline']-1800
assert subprocess.run(['systemctl','is-active','--quiet',root.name+'-release.timer']).returncode==0 and os.sched_getaffinity(0)=={0}
assert not subprocess.check_output(['docker','ps','-q'],text=True).strip()
prior=json.loads((root/'baseline/metadata.json').read_text());base=root/'bin'/a.cohort/'lookup';candidate=root/a.binary
assert sha(base)==prior['binary_sha256'][a.cohort] and sha(candidate)==a.binary_sha256
link=root/'bin'/(a.phase+'-'+a.variant);assert not link.exists();os.link(candidate,link)
cases={k:v*a.scale for k,v in {'hit':50000,'score':50000,'miss':100000,'long':20000,'external':20000,'update':20000}.items()}
meta=dict(scale=a.scale,started=time.time(),cohort=a.cohort,seed=str(a.seed),baseline_sha256=sha(base),variants={a.variant:dict(source_sha256=a.source_sha256,binary_sha256=sha(candidate))},candidate_origin=a.binary,source_freeze='ee8e7f70152404649ac947157fd662d11b4a00d5',confirmation=True,sweeps=cases)
(out/'metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
def run(cmd,stem):
 d=json.loads((root/'reservation.json').read_text());assert d['state']=='RESERVED' and time.time()<d['deadline']-300
 start=time.time();q=subprocess.run(cmd,capture_output=True,text=True,timeout=240)
 (out/(stem+'.stdout')).write_text(q.stdout);(out/(stem+'.stderr')).write_text(q.stderr)
 with (out/'commands.jsonl').open('a') as f:f.write(json.dumps(dict(argv=cmd,stem=stem,returncode=q.returncode,started=start,finished=time.time()))+'\n')
 assert q.returncode==0,(stem,q.stderr[-1000:]);return q.stdout
blocks=[]
for case,sweeps in cases.items():
 for name,binary in [('base',base),('candidate',candidate)]:run(['taskset','-c','2',str(binary),'verify',case,str(a.seed),'1'],'verify-'+name+'-'+case)
 for block in range(3):
  rr=[]
  for slot,label in enumerate('ABBA'):
   row=json.loads(run(['taskset','-c','2',str(base),'measure',case,str(a.seed),str(sweeps)],f'aa-{case}-{block}-{slot}'))
   row.update(cohort=a.cohort,block=block,slot=slot,label=label,binary_sha256=sha(base));rr.append(row)
   with (out/'aa.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
   print('AA',case,block,slot,flush=True)
  for k in ['hits','score_sum','ops','owned_bytes']:assert len({r[k] for r in rr})==1
  delta=(statistics.mean(r['elapsed_ns'] for r in rr if r['label']=='B')/statistics.mean(r['elapsed_ns'] for r in rr if r['label']=='A')-1)*100
  blocks.append(dict(case=case,block=block,delta_pct=delta,min_window_ns=min(r['elapsed_ns'] for r in rr),passed=abs(delta)<=1 and min(r['elapsed_ns'] for r in rr)>=250000000))
qualified=all(b['passed'] for b in blocks);(out/'qualification.json').write_text(json.dumps({'pass':qualified,'blocks':blocks,'rows':72},indent=2)+'\n')
if not qualified:print('PARK qualification',flush=True);raise SystemExit(0)
subprocess.run(['python3',str(root/'experiments/ARM-LOOKUP-CONT-001/fleet_compare.py'),'--root',str(root),'--phase',a.phase,'--cohort',a.cohort,'--seed',str(a.seed),'--scale',str(a.scale),'--variants',a.variant,'--measure-only'],check=True)
