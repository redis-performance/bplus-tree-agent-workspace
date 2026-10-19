#!/usr/bin/env python3
"""Fixed fresh corrected-adapter controls; no candidate executable is used."""
import argparse,datetime,hashlib,json,pathlib,subprocess,time,csv,os
p=argparse.ArgumentParser();p.add_argument('--baseline',required=True,type=pathlib.Path);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/'aa';out.mkdir();assert sorted(os.sched_getaffinity(0))==[2]
execution=json.loads((here/'execution-freeze.json').read_text())
for name,h in execution['files'].items():assert hashlib.sha256((here/name).read_bytes()).hexdigest()==h,name
assert json.loads((here/'profile/audit.json').read_text())['status']=='pass'
assert json.loads((here/'profile/code-map.json').read_text())['status']=='mapped'
expected=json.loads((here/'expected.json').read_text());binary=a.baseline/'build/adapter-requalification/btree-bench';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before={f:sha(a.baseline/f) for f in expected['source_hashes']};assert before==expected['source_hashes'];assert sha(binary)==expected['aa_binary_sha256'];records=[];now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();state={'status':'running','started_utc':now(),'source_hashes_before':before,'binary_sha256_before':sha(binary),'runs':records,'execution_freeze_sha256':sha(here/'execution-freeze.json'),'profile_audit_sha256':sha(here/'profile/audit.json'),'profile_mapping_sha256':sha(here/'profile/code-map.json')}
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
save()
try:
 for block in range(6):
  seed=701+block%3
  for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
   for position,label in enumerate('ABBA'):
    left=300-(time.monotonic()-start);assert left>0,'fixed AA cap reached';name=f'b{block}-n{n}-p{position}-{label}';cmd=[str(binary),'--case','iterate','--size',str(n),'--ops','50000000','--member-bytes','16','--seed',str(seed)];rec=dict(name=name,block=block,seed=seed,size=n,position=position,label=label,started_utc=now(),command=['<corrected-baseline>/build/adapter-requalification/btree-bench',*cmd[1:]]);records.append(rec);save()
    try:r=subprocess.run(cmd,capture_output=True,text=True,timeout=min(left,30))
    except subprocess.TimeoutExpired as e:
     rec.update(finished_utc=now(),returncode=124)
     for suffix,value in [('csv',e.stdout),('stderr',e.stderr)]:
      value=value or '';value=value.decode(errors='replace') if isinstance(value,bytes) else value;(out/(name+'.'+suffix)).write_text(value)
     save();raise
    rec.update(finished_utc=now(),returncode=r.returncode);(out/(name+'.csv')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr);save();r.check_returncode();rr=list(csv.DictReader(r.stdout.splitlines()));assert len(rr)==1;rec['row']=rr[0];save()
    z=rr[0];assert z['case']=='iterate' and z['cpu_start']==z['cpu_end']=='2'
    assert [int(z[k]) for k in ['size','requested_ops','member_bytes','seed','operations','traversals','warmup_passes']]==[n,50000000,16,seed,50000000,50000000//n,1]
    assert int(z['checksum'])==(n*(n-1)//2)*(50000000//n)
    if position:
     for k in ['operations','checksum','tree_bytes','traversals','warmup_passes']:assert z[k]==records[-2]['row'][k],k
 state.update(status='complete',source_hashes_after={f:sha(a.baseline/f) for f in expected['source_hashes']},binary_sha256_after=sha(binary));assert state['source_hashes_after']==before and state['binary_sha256_after']==expected['aa_binary_sha256']
except BaseException as e:state.update(status='failed',error=type(e).__name__+': '+str(e));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
