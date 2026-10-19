#!/usr/bin/env python3
"""Frozen corrected-adapter exact B primary replication."""
import argparse,datetime,hashlib,json,pathlib,subprocess,time,csv
p=argparse.ArgumentParser();p.add_argument('--baseline',required=True,type=pathlib.Path);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/'primary';out.mkdir();expected=json.loads((here/'expected.json').read_text());binary=a.baseline/'build/adapter-requalification/btree-bench';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before={f:sha(a.baseline/f) for f in expected['source_hashes']};assert before==expected['source_hashes'];assert sha(binary)==expected['aa_binary_sha256'];freeze=json.loads((here/'validation/freeze.json').read_text());assert json.loads((here/'validation/result.json').read_text())['status']=='complete';candidate=here/'B/build/native/btree-bench';assert sha(candidate)==freeze['snapshots']['B']['binaries']['build/native/btree-bench'];candidate_before={f:sha(here/'B'/f) for f in freeze['snapshots']['B']['source_hashes']};assert candidate_before==freeze['snapshots']['B']['source_hashes'];records=[];now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();state={'status':'running','started_utc':now(),'source_hashes_before':before,'binary_sha256_before':sha(binary),'runs':records,'candidate_source_before':candidate_before,'candidate_binary_before':sha(candidate)}
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
save()
try:
 for block in range(6):
  seed=401+block%3
  for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
   for position,label in enumerate('ABBA'):
    left=300-(time.monotonic()-start);assert left>0,'fixed primary cap reached';name=f'b{block}-n{n}-p{position}-{label}';cmd=[str(binary if label=='A' else candidate),'--case','scan','--size',str(n),'--ops','5000000','--member-bytes','16','--seed',str(seed)];rec=dict(name=name,block=block,seed=seed,size=n,position=position,label=label,started_utc=now(),command=[('<corrected-baseline>/build/adapter-requalification/btree-bench' if label=='A' else '<isolated-B>/build/native/btree-bench'),*cmd[1:]]);records.append(rec);save()
    try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(left,30))
    except subprocess.TimeoutExpired as e:
     rec.update(finished_utc=now(),returncode=124)
     for suffix,value in [('csv',e.stdout),('stderr',e.stderr)]:
      value=value or '';value=value.decode(errors='replace') if isinstance(value,bytes) else value;(out/(name+'.'+suffix)).write_text(value)
     save();raise
    rec.update(finished_utc=now(),returncode=r.returncode);(out/(name+'.csv')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr);save();r.check_returncode();rr=list(csv.DictReader(r.stdout.splitlines()));assert len(rr)==1;rec['row']=rr[0];save()
 state.update(candidate_source_after={f:sha(here/'B'/f) for f in candidate_before},candidate_binary_after=sha(candidate));assert state['candidate_source_after']==candidate_before and state['candidate_binary_after']==state['candidate_binary_before'];state.update(status='complete',source_hashes_after={f:sha(a.baseline/f) for f in expected['source_hashes']},binary_sha256_after=sha(binary));assert state['source_hashes_after']==before and state['binary_sha256_after']==expected['aa_binary_sha256']
except BaseException as e:state.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
