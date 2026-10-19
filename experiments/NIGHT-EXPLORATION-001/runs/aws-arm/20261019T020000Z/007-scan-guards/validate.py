#!/usr/bin/env python3
"""Baseline correctness/census only. Passes is ALWAYS zero; no timing windows."""
import argparse, subprocess, pathlib, json, hashlib, itertools, datetime, time
p=argparse.ArgumentParser();p.add_argument('--native',required=True,type=pathlib.Path);p.add_argument('--sanitize',required=True,type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);p.add_argument('--seeds',default='101');p.add_argument('--seconds',type=int,default=600);a=p.parse_args()
o=a.out.resolve();o.mkdir(parents=True,exist_ok=True);fixtures=o/'fixtures';fixtures.mkdir(exist_ok=True);deadline=time.monotonic()+a.seconds;rows=[];manifest=[]
def run(args,name,expect=0):
 if time.monotonic()>=deadline:raise RuntimeError('fixed validation budget expired')
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run([str(x) for x in args],capture_output=True,text=True,timeout=min(90,deadline-time.monotonic()));end=datetime.datetime.now(datetime.timezone.utc).isoformat()
 (o/(name+'.stdout')).write_text(r.stdout);(o/(name+'.stderr')).write_text(r.stderr)
 rows.append({'name':name,'argv':[str(x) for x in args],'start_utc':start,'end_utc':end,'returncode':r.returncode,'expected_returncode':expect});(o/'commands.json').write_text(json.dumps(rows,indent=2)+'\n')
 assert r.returncode==expect,(name,r.returncode,r.stderr)
 return [json.loads(x) for x in r.stdout.splitlines()]
for seed,n,width,dist in itertools.product(map(int,a.seeds.split(',')),[4096,100000],[16,321],[0,1,2]):
 name=f's{seed}-n{n}-b{width}-d{dist}';f=fixtures/(name+'.bin')
 gen=run([a.native/'scan-guard','generate',f,n,width,seed,dist,'v1'],name+'-generate')[0]
 manifest.append({'name':name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'generator':gen})
 for order in [0,1,2]:
  cell=f'{name}-o{order}'
  diagnostic=run([a.native/'scan-census','run',f,order,0,0],cell+'-census');c,r=diagnostic
  assert c['members']==n and sum(c['tag_histogram'])==n
  if order==1:assert c['reversed_leaves']>0 and c['reversed_members']>0,'missing natural reversal'
  if dist==1:assert c['tag_histogram'][17]==n
  if dist==2:assert c['tag_histogram'][0]>0 and c['tag_histogram'][1]>0 and sum(c['tag_histogram'][:2])==n
  for mode,binary in [('native',a.native/'scan-guard'),('sanitize',a.sanitize/'scan-guard')]:
   actual=run([binary,'run',f,order,0,0],cell+'-'+mode)[0]
   keys=['n','bytes','seed','distribution','order']
   if mode=='native':keys+=['callbacks_per_pass','checksum_per_pass','tree_bytes']
   for key in keys:assert actual[key]==r[key],(cell,mode,key,actual[key],r[key])
  with (o/'census.jsonl').open('a') as out:out.write(json.dumps({'cell':cell,'census':c,'run':r})+'\n')
 (o/'fixture-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
f=fixtures/'s101-n4096-b16-d0.bin'
if f.exists():
 for mode,binary in [('native',a.native/'scan-guard'),('sanitize',a.sanitize/'scan-guard')]:
  for fault in [1,2,3,4]:run([binary,'run',f,0,0,fault],f'fault-{mode}-{fault}',2)
(o/'RESULT.json').write_text(json.dumps({'status':'pass','commands':len(rows),'fixture_files':len(manifest),'cells':len(manifest)*3,'seeds':a.seeds,'candidate_timings':0,'baseline_timings':0},indent=2)+'\n')
