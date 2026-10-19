#!/usr/bin/env python3
"""Offline independent raw audit. Never imports the timing driver or runs native code."""
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from fractions import Fraction
import argparse,csv,hashlib,io,json,math,re,signal,time
R=Path.cwd();E=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def dt(s):return datetime.fromisoformat(s)
def expire(*args):raise TimeoutError('180-second offline audit bound')
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=['aa','discovery'],required=True);ap.add_argument('--ack',required=True);args=ap.parse_args()
 signal.signal(signal.SIGALRM,expire);signal.alarm(180);started=time.monotonic()
 phase=args.phase;out=E/phase;raw=R/'scratch/m6-neon-replication/timing'/phase
 report=dict(status='RUNNING',phase=phase,participant='/root/followup_proposal_a',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown',native_executions=0,audit_bound_seconds=180)
 target=out/'independent-audit.json';assert not target.exists(),'preserve prior audit; no overwrite'
 try:
  freeze=load(E/'freeze.json');ack=load(Path(args.ack));plan=load(E/'PLAN.json');manifest=load(E/'source-manifest.json')
  pins=freeze['files_sha256'];assert all(not Path(p).is_absolute() and '..' not in Path(p).parts for p in pins)
  before={p:sha(R/p) for p in pins};assert before==pins
  assert ack['status']=='authorized' and ack['phase']==phase and ack['validation_status']=='PASS' and ack['exclusive_runner'] is True and ack['all_other_work_idle'] is True
  for key,name in [('freeze_sha256','freeze.json'),('driver_sha256','timing.py'),('plan_sha256','PLAN.json'),('schedule_sha256',phase+'-schedule.json')]:assert ack[key]==sha(E/name)
  assert re.fullmatch(r'[0-9a-f]{40}',ack['published_commit'])
  reviewers={x['reviewer'] for x in ack['reviews'] if x['status']=='PASS'};assert '/root' in reviewers and bool(reviewers-{'/root','/root/followup_proposal_b'})
  assert load(E/'validation/result.json')['status']=='PASS'
  validation=load(E/'validation/binary-freeze.json')['snapshots']
  binary={v:str(Path(entry['worktree'])/'build/native/btree-bench') for v,entry in manifest['variants'].items()};assert set(binary)=={'base','A','B','C'}
  for v,entry in manifest['variants'].items():
   assert all(sha(R/entry['worktree']/p)==h for p,h in entry['source_hashes'].items())
   assert binary[v] in pins and sha(R/binary[v])==validation[v]['timing_binary_sha256']
   assert all(sha(R/entry['worktree']/p)==h for p,h in validation[v]['binaries'].items())
  # Construct without loading any schedule/derived output until expected order exists.
  schedule=[]
  for block in range(6):
   sources=['base'] if phase=='aa' else [ ['A','B','C'][(block+j)%3] for j in range(3)]
   for variant in sources:
    for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
     for position,side in enumerate(('A','B','B','A')):
      schedule.append(dict(index=len(schedule),block=block,variant=variant,size=n,seed=(401,402,403)[block%3],position=position,side=side,binary='base' if phase=='aa' or side=='A' else variant,case='scan',requested_ops=5000000,member_bytes=16,warmup_passes=1))
  assert len(schedule)==(48 if phase=='aa' else 144) and schedule==load(E/(phase+'-schedule.json'))
  records=[json.loads(line) for line in (out/'commands.jsonl').read_text().splitlines()];state=load(out/'status.json');published=load(out/'summary.json')
  report.update(expected_processes=len(schedule),actual_journaled_processes=len(records),published_commit=ack['published_commit'],input_freeze_sha256=sha(E/'freeze.json'),input_pin_count=len(pins))
  assert len(records)<=len(schedule)
  expected_environment=dict(PATH='/usr/bin:/bin:/usr/sbin:/sbin',LC_ALL='C',LANG='C',TZ='UTC')
  columns='case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns'.split(',')
  fingerprint_keys=['case','size','seed','requested_ops','member_bytes','warmup_passes','operations','checksum','tree_bytes','traversals']
  rows=[];raw_hashes={};previous=None;errors=[];identities={};all_reaped=True
  for i,rec in enumerate(records):
   item=schedule[i];assert rec['name']==f'{i:03d}'
   cmd=[binary[item['binary']],'--case','scan','--size',str(item['size']),'--ops','5000000','--member-bytes','16','--seed',str(item['seed']),'--warmup-passes','1']
   assert rec['command']==cmd and rec['environment']==expected_environment
   begin,end=dt(rec['started_utc']),dt(rec['finished_utc']);assert begin<end and (previous is None or begin>=previous);previous=end
   assert dt(state['started_utc'])<=begin and end<=dt(state['finished_utc']) and end<dt(plan['experimental_cutoff_utc']) and end<dt(ack['absolute_stop_utc'])
   assert 0<rec['timeout_seconds']<=60 and rec['wall_seconds']<=rec['timeout_seconds']+10
   all_reaped=all_reaped and rec.get('child_reaped',False) and rec.get('owned_group_empty',False) and rec.get('release_safe',False)
   assert set(rec['raw'])=={'stdout','stderr'}
   paths={ch:R/info['path'] for ch,info in rec['raw'].items()}
   for ch,path in paths.items():
    info=rec['raw'][ch];assert path==raw/(f'{i:03d}.'+ch) and path.stat().st_size==info['bytes'] and sha(path)==info['sha256'];raw_hashes[str(path.relative_to(R))]=info['sha256']
   if rec.get('returncode')!=0 or rec['timed_out'] or not rec['release_safe']:
    errors.append(dict(index=i,kind='child failure',returncode=rec.get('returncode'),timed_out=rec['timed_out']));continue
   assert paths['stderr'].stat().st_size==0
   reader=csv.DictReader(io.StringIO(paths['stdout'].read_text()));data=list(reader);assert reader.fieldnames==columns and len(data)==1 and None not in data[0];r=data[0]
   for k,v in dict(case='scan',size=item['size'],seed=item['seed'],requested_ops=5000000,member_bytes=16,warmup_passes=1).items():assert r[k]==str(v)
   for key,value in r.items():
    assert re.fullmatch(r'[A-Za-z0-9_-]{1,80}' if key in ['case','qos_reported_start','qos_reported_end','qos_effective'] else r'-?[0-9]+(?:\.[0-9]+)?',value)
   elapsed,ops,owned,checksum,traversals=[int(r[k]) for k in ['elapsed_ns','operations','tree_bytes','checksum','traversals']];n=item['size'];trav=(5000000+n-1)//n
   assert elapsed>0 and owned>0 and traversals==trav and ops>=trav*n and ops%trav==0 and checksum>=trav*n*(n-1)//2 and checksum%trav==0
   assert abs(Decimal(r['ns_per_op'])-Decimal(elapsed)/ops)<=Decimal('.000501') and abs(Decimal(r['ops_per_sec'])-Decimal(ops)*1000000000/elapsed)<=Decimal('.000501')
   assert all(math.isfinite(float(r[k])) for k in ['ns_per_op','ops_per_sec'])
   fingerprint={k:r[k] for k in fingerprint_keys};key=(n,item['seed'])
   assert key not in identities or identities[key]==fingerprint;identities[key]=fingerprint
   row=dict(**item,csv=r,elapsed_ns=elapsed,operations=ops,tree_bytes=owned,checksum=str(checksum),ns_per_op_exact=elapsed/ops,window_qualified=elapsed>=10000000,fingerprint=fingerprint)
   rows.append(row)
  assert {str(x.relative_to(R)) for x in raw.iterdir() if x.is_file()}==set(raw_hashes),'unaccounted raw output; preserve and investigate'
  report.update(all_raw_streams_retained=True,raw_sha256=raw_hashes,all_journaled_children_reaped_and_groups_empty=all_reaped,process_errors=errors)
  assert not errors and all_reaped and len(rows)==len(schedule) and len(records)==len(schedule),'incomplete phase; all raw identities retained in report'
  blocks=[]
  for i in range(0,len(rows),4):
   q=rows[i:i+4];assert [r['side'] for r in q]==['A','B','B','A'] and [r['position'] for r in q]==[0,1,2,3]
   assert all(r['fingerprint']==q[0]['fingerprint'] for r in q)
   left=q[0]['elapsed_ns']+q[3]['elapsed_ns'];middle=q[1]['elapsed_ns']+q[2]['elapsed_ns'];windows=all(r['elapsed_ns']>=10000000 for r in q)
   effect=Fraction((middle-left)*100,left)
   blocks.append(dict(block=q[0]['block'],size=q[0]['size'],seed=q[0]['seed'],variant=q[0]['variant'],effect_percent=float(effect),all_windows_qualified=windows,baseline_elapsed_sum=left,candidate_elapsed_sum=middle,aa_qualified=windows and abs(middle-left)*100<=left,primary_speed_gate=windows and middle*100<=left*98))
  assert rows==published['rows'] and len(blocks)==len(published['blocks'])
  for actual,derived in zip(blocks,published['blocks']):
   assert set(actual)==set(derived)
   for k,v in actual.items():assert abs(v-derived[k])<1e-12 if k=='effect_percent' else v==derived[k]
  assert state['status']=='COMPLETE' and state['completed_processes']==len(rows) and state['journaled_process_attempts']==len(records) and state['release_safe'] and state['freeze_sha256']==sha(E/'freeze.json') and state['post_identities_verified']==len(pins)
  assert state['phase_wall_seconds']<300 and (dt(state['finished_utc'])-dt(state['started_utc'])).total_seconds()<300
  qualification=all(b['aa_qualified'] for b in blocks) if phase=='aa' else False
  survivors=[] if phase=='aa' else [v for v in ['B','C','A'] if len([b for b in blocks if b['variant']==v])==12 and all(b['primary_speed_gate'] for b in blocks if b['variant']==v)]
  if phase=='aa':assert state['qualified'] is qualification
  else:
   assert state['primary_survivors']==survivors and state['selected_for_further_gates']==(survivors[0] if survivors else 'NONE')
   assert ack['aa_status_sha256']==sha(E/'aa/status.json') and ack['aa_summary_sha256']==sha(E/'aa/summary.json')
   prior=load(E/'aa/independent-audit.json');assert prior['status']=='PASS' and prior['all_aa_blocks_qualified'] is True
   assert all(prior['fixture_fingerprints'][f'{n}:{s}']==fp for (n,s),fp in identities.items())
  assert {p:sha(R/p) for p in pins}==before and all(sha(R/p)==h for p,h in raw_hashes.items())
  report.update(status='PASS',complete_raw_reconstruction=True,processes=len(records),raw_rows=len(rows),blocks=blocks,all_aa_blocks_qualified=qualification,failed_aa_blocks=[b for b in blocks if not b['aa_qualified']],short_window_rows=[r['index'] for r in rows if not r['window_qualified']],primary_survivors=survivors,fixture_fingerprints={f'{n}:{s}':fp for (n,s),fp in identities.items()},all_input_pins_unchanged=True,all_raw_hashes_unchanged=True,phase_wall_seconds=state['phase_wall_seconds'],source_adoption='NONE',limitations='Recorded UTC/process cleanup and exact raw integer gates only. Native macOS unpinned; CPU endpoint metadata cannot prove core residency/frequency or explain variance. Passing raw audit does not imply timing qualification or acceptance.')
 except BaseException as ex:
  report.update(status='FAIL_OR_INCOMPLETE',error_type=type(ex).__name__,error=str(ex).replace(str(R),'<workspace>'));raise
 finally:
  signal.alarm(0);report.update(audit_wall_seconds=time.monotonic()-started,script_sha256=sha(__file__))
  target.write_text(json.dumps(report,indent=2)+'\n')
  (out/'independent-audit-seal.json').write_text(json.dumps({'report_sha256':sha(target),'script_sha256':sha(__file__),'phase':phase,'status':report['status'],'native_executions':0},indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['status','phase','raw_rows','all_aa_blocks_qualified','short_window_rows','primary_survivors']}))
if __name__=='__main__':main()
