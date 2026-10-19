#!/usr/bin/env python3
"""Exact preregistered144-process discovery; no retries or repairs."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,time
p=Path(__file__).resolve().parent;out=p/'screen';out.mkdir();raw=out/'raw';raw.mkdir();freeze=json.loads((p/'comparison-freeze.json').read_text());schedule=json.loads((p/'screen-schedule.json').read_text());assert len(schedule)==144
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(p/'run-screen.py')==freeze['driver_sha256'];assert sha(p/'screen-schedule.json')==freeze['schedule_sha256']
def check():
 for variant,v in freeze['sources'].items():
  root=Path(v['root'])
  assert sha(root/v['timing_binary'])==v['binary_sha256'],variant
  for f,h in v['source_hashes'].items():assert sha(root/f)==h,(variant,f)
check();start=time.monotonic();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();m={'status':'running','started_utc':now(),'rows':[],'attempts':[]}
def save():(out/'result.json').write_text(json.dumps(m,indent=2)+'\n')
save()
try:
 for index,item in enumerate(schedule):
  remaining=300-(time.monotonic()-start);assert remaining>0
  variant=item['variant'] if item['side']=='candidate'else 'base';v=freeze['sources'][variant];binary=str(Path(v['root'])/v['timing_binary']);cmd=[binary,'--case','scan','--size',str(item['size']),'--ops','5000000','--member-bytes','16','--seed',str(item['seed'])];tag=f'screen-{index:03d}';attempt=dict(item,command=cmd,started_utc=now())
  try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(60,remaining))
  except subprocess.TimeoutExpired as e:
   decode=lambda v:v.decode(errors='replace')if isinstance(v,bytes)else v or ''
   (raw/(tag+'.stdout')).write_text(decode(e.stdout));(raw/(tag+'.stderr')).write_text(decode(e.stderr));attempt.update(finished_utc=now(),returncode=None,status='timeout');m['attempts'].append(attempt);save();raise
  (raw/(tag+'.stdout')).write_text(r.stdout);(raw/(tag+'.stderr')).write_text(r.stderr);attempt.update(finished_utc=now(),returncode=r.returncode,status='complete');m['attempts'].append(attempt);save();assert r.returncode==0,r.stderr
  rr=list(csv.DictReader(r.stdout.splitlines()));assert len(rr)==1;row=rr[0];assert row['cpu_start']==row['cpu_end']=='2';assert row['case']=='scan' and int(row['size'])==item['size'] and int(row['seed'])==item['seed'] and row['requested_ops']=='5000000' and row['member_bytes']=='16'
  m['rows'].append(dict(attempt,row=row));save()
 effects=[]
 for i in range(0,len(m['rows']),4):
  rr=m['rows'][i:i+4];assert len({tuple(x['row'][k]for k in ['checksum','operations','tree_bytes','traversals','warmup_passes','size','seed','member_bytes'])for x in rr})==1
  ns=[int(x['row']['elapsed_ns'])/int(x['row']['operations'])for x in rr];effect=100*((ns[1]+ns[2])/(ns[0]+ns[3])-1);minimum=min(int(x['row']['elapsed_ns'])for x in rr);effects.append(dict(variant=rr[0]['variant'],size=rr[0]['size'],seed=rr[0]['seed'],block=rr[0]['block'],effect_pct=effect,min_window_ns=minimum,primary_gate=effect<=-2 and minimum>=10000000))
 check();m.update(status='complete',effects=effects)
except BaseException as e:m.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:m.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
print('Complete144 serial rows; all6 bothsize gates:',{v:all(x['primary_gate']for x in effects if x['variant']==v)for v in ['A','B','C']})
