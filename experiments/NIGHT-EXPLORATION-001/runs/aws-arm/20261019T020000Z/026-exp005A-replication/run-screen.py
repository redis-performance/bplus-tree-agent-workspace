#!/usr/bin/env python3
import argparse,pathlib,json,hashlib,subprocess,time,datetime,os,csv
p=argparse.ArgumentParser();p.add_argument('--checkout',required=True,type=pathlib.Path);a=p.parse_args();here=pathlib.Path(__file__).resolve().parent;out=here/'screen';assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,19,7,15,tzinfo=datetime.timezone.utc);out.mkdir();assert sorted(os.sched_getaffinity(0))==[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();start=time.monotonic();e=json.loads((here/'expected.json').read_text());freeze=json.loads((here/'execution-freeze.json').read_text());schedule=json.loads((here/'screen-schedule.json').read_text())
for n,h in freeze['files'].items():assert sha(here/n)==h
validation=json.loads((here/'validation/result.json').read_text());gate=json.loads((here/'codegen-gate.json').read_text());
for n in ['actual','control','A']:assert gate['assembly_sha256'][n]==sha(here/'validation'/(n+'-asm.stdout'))
assert validation['status']=='correctness_complete_static_gate_pending';assert gate['status']=='PASS';assert gate['execution_freeze_sha256']==sha(here/'execution-freeze.json') and gate['validation_result_sha256']==sha(here/'validation/result.json');assert gate['baseline_mask_instructions']==4 and gate['candidate_mask_instructions']<=3 and gate['added_conditional_branches']==0 and gate['ordinary_nonzero_path_instruction_delta']<=-1 and gate['shared_caller_review_pass'] is True
roots={'baseline':a.checkout/'scratch/adapter-worktree-13e459ff8','candidate':here/'A'};binaries={k:v/'build/adapter-requalification/btree-bench' for k,v in roots.items()};before={k:sha(v) for k,v in binaries.items()};assert before['baseline']==e['aa_binary_sha256'] and before['candidate']==validation['binary_sha256']['A'];assert gate['timing_binary_sha256']==before
sources={k:{n:sha(v/n) for n in e['source_hashes']} for k,v in roots.items()}
assert sources['baseline']==e['source_hashes'];expectedA=dict(e['source_hashes'],**{'src/zset_btree.c':e['candidate_source_sha256']});assert sources['candidate']==expectedA
state=dict(status='running',started_utc=now(),execution_freeze_sha256=sha(here/'execution-freeze.json'),codegen_gate_sha256=sha(here/'codegen-gate.json'),binary_before=before,sources_before=sources,runs=[])
def save():(out/'result.json').write_text(json.dumps(state,indent=2)+'\n')
save()
try:
 for row in schedule:
  left=300-(time.monotonic()-start);assert left>0,'fixed300s cap reached';name=f"b{row['block']}-n{row['size']}-p{row['position']}-{row['label']}";args=['--case','iterate','--size',str(row['size']),'--ops','50000000','--member-bytes','16','--seed',str(row['seed'])];rec=dict(row,name=name,command=['<'+row['binary']+'>/build/adapter-requalification/btree-bench',*args],started_utc=now());state['runs'].append(rec);save()
  try:r=subprocess.run([str(binaries[row['binary']]),*args],capture_output=True,text=True,timeout=min(30,left))
  except subprocess.TimeoutExpired as ex:
   rec.update(returncode=124,finished_utc=now())
   for suffix,val in [('csv',ex.stdout),('stderr',ex.stderr)]:(out/(name+'.'+suffix)).write_text((val.decode(errors='replace') if isinstance(val,bytes) else val) or '')
   save();raise
  rec.update(returncode=r.returncode,finished_utc=now());(out/(name+'.csv')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr);save();r.check_returncode();rows=list(csv.DictReader(r.stdout.splitlines()));assert len(rows)==1;z=rows[0];n=row['size']
  exact=dict(case='iterate',size=n,seed=row['seed'],requested_ops=50000000,member_bytes=16,operations=50000000,traversals=50000000//n,checksum=50000000*(n-1)//2,warmup_passes=1,cpu_start=2,cpu_end=2)
  assert all(z[k]==str(v) for k,v in exact.items());assert int(z['elapsed_ns'])>0;rec['row']=z;save()
  if row['position']:
   prior=state['runs'][-2]['row'];assert all(z[k]==prior[k] for k in ['operations','checksum','tree_bytes','traversals','warmup_passes'])
 state['binary_after']={k:sha(v) for k,v in binaries.items()};state['sources_after']={k:{n:sha(v/n) for n in e['source_hashes']} for k,v in roots.items()};assert before==state['binary_after'] and sources==state['sources_after'];state['status']='complete'
except BaseException as ex:state.update(status='failed',error=type(ex).__name__+': '+str(ex));raise
finally:state.update(finished_utc=now(),elapsed_seconds=time.monotonic()-start);save()
