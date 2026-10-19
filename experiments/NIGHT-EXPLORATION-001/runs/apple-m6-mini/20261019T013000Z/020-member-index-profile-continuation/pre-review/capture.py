#!/usr/bin/env python3
"""Only root-authorized frozen software captures; no builds, retries or timing inference."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,hashlib,json,os,re,signal,subprocess,time,csv,io,bisect
R=Path.cwd();E=Path(__file__).resolve().parent;S=R/'scratch/m6-corrected-member-index-profile-continuation';PLAN=json.loads((E/'PLAN.json').read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def utc():return datetime.now(timezone.utc).isoformat()
def alive(group):
 try:os.killpg(group,0);return True
 except ProcessLookupError:return False
def cancelled(signum,frame):raise KeyboardInterrupt('capture owner cancelled')
def run(cmd,name,seconds,absolute_deadline):
 raw=S/'capture-logs';raw.mkdir(exist_ok=True);paths={x:raw/(name+'.'+x) for x in ['stdout','stderr']}
 assert not any(p.exists() for p in paths.values()),'no overwrite/retry'
 rec=dict(name=name,command=cmd,environment_overrides={'PROFILE_USEC':'1000'},started_utc=utc(),timeout_seconds=seconds,timed_out=False)
 child=None;t=time.monotonic()
 try:
  with paths['stdout'].open('xb') as out,paths['stderr'].open('xb') as err:
   child=subprocess.Popen(cmd,stdout=out,stderr=err,env=dict(os.environ,PROFILE_USEC='1000'),start_new_session=True)
   while child.poll() is None:
    if time.monotonic()-t>=seconds or time.time()>=absolute_deadline-10:rec['timed_out']=True;break
    time.sleep(.05)
 except BaseException as ex:rec['exception_type']=type(ex).__name__;raise
 finally:
  previous_mask=signal.pthread_sigmask(signal.SIG_BLOCK,{signal.SIGALRM})
  try:
   if child is not None:
    if alive(child.pid):
     try:os.killpg(child.pid,signal.SIGKILL);rec['owned_group_killed']=True
     except ProcessLookupError:rec['owned_group_exited_before_kill']=True
    try:child.wait(timeout=5);rec['child_reaped']=True
    except subprocess.TimeoutExpired:rec['child_reaped']=False
    until=time.monotonic()+3
    while alive(child.pid) and time.monotonic()<until:time.sleep(.05)
    rec['owned_group_empty']=not alive(child.pid);rec['returncode']=child.returncode
   rec.update(finished_utc=utc(),wall_seconds=time.monotonic()-t,raw={})
   for ch,p in paths.items():
    if p.exists():rec['raw'][ch]=dict(path=str(p.relative_to(R)),sha256=sha(p),bytes=p.stat().st_size)
   rec['release_safe']=bool(rec.get('child_reaped') and rec.get('owned_group_empty'))
   with (E/'commands.jsonl').open('a') as f:f.write(json.dumps(rec)+'\n')
  finally:
   signal.pthread_sigmask(signal.SIG_SETMASK,previous_mask)
 return rec,paths

def classify_pc(row,mapping):
 assert len(row)==6
 _,module,rawpc,rawbase,symbol,rawsym=row;pcval,base,sym=map(lambda x:int(x,16),[rawpc,rawbase,rawsym])
 aliases=(symbol,);section=None;image_pc=None;classification='external-symbol';limit=False
 if module==Path(PLAN['binary']).name:
  module='profile-program';aliases=();offset=None;image_start=None;symbol='unknown-own-image';classification='unmapped-own-image';limit=True
  if base and pcval>=base:
   image_pc=pcval-base;address=image_pc+mapping['image_vmaddr']
   matches=[s for s in mapping['sections'] if s['address']<=address<s['address']+s['size']]
   section=matches[0]['segment']+','+matches[0]['section'] if len(matches)==1 else None
   if mapping['text_start']<=address<mapping['text_end'] and address%4==0:
    addresses=[x['address'] for x in mapping['symbols']];i=bisect.bisect_right(addresses,address)-1
    if i>=0:
     entry=mapping['symbols'][i];offset=address-entry['address'];aliases=tuple(entry.get('aliases',[entry['name']]));symbol=entry['name'] if len(aliases)==1 else 'ambiguous-coalesced-symbol';image_start=entry['address']-mapping['image_vmaddr'];classification='text-symbol';limit=len(aliases)>1
   elif len(matches)==1 and matches[0]['segment']=='__TEXT' and matches[0]['section']=='__stubs':
    stub=matches[0];classification='import-stub';symbol='import-stub-unknown-target';offset=address-stub['address'];image_start=stub['address']-mapping['image_vmaddr'];limit=True
 else:offset=pcval-sym if sym and pcval>=sym else None;image_start=None
 module=module if re.fullmatch(r'[A-Za-z0-9_.-]{1,160}',module) else 'other-module'
 symbol=symbol if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',symbol) else 'unknown'
 aliases=tuple(x if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',x) else 'unknown' for x in aliases)
 return (module,symbol,offset,image_start,aliases,classification,image_pc,section,limit)

def derive(rec,paths,item,mapping):
 data=list(csv.DictReader(io.StringIO(paths['stdout'].read_text())));assert len(data)==1 and None not in data[0];r=data[0]
 case,n,seed=item['case'],item['size'],item['seed'];ops=10000000
 for key,value in dict(case=case,size=n,seed=seed,requested_ops=ops,member_bytes=16,warmup_passes=3).items():assert r[key]==str(value)
 operations,checksum=int(r['operations']),int(r['checksum']);owned=int(r['tree_bytes']);assert owned>0
 if case in ['lookup-hit','rank']:assert operations==ops and checksum==(n*(n-1)//2)*(ops//n) and int(r['traversals'])==0
 elif case=='lookup-miss':assert operations==ops and checksum==0 and int(r['traversals'])==0
 else:
  assert case=='scan' and int(r['traversals'])==ops//n and operations>=ops and operations%(ops//n)==0 and checksum%(ops//n)==0
 lines=paths['stderr'].read_text().splitlines();headers=[x for x in lines if x.startswith('PROFILE,')];assert len(headers)==1
 h=headers[0].split(',');assert len(h)==5 and h[1]==case and h[2]=='1000';count=int(h[3]);cap=int(h[4]);pc=[x.split(',') for x in lines if x.startswith('PC,')]
 assert count==len(pc) and cap==0 and count<=65536 and len(lines)==len(pc)+1
 bins=Counter(classify_pc(row,mapping) for row in pc)
 output=[dict(module=k[0],symbol=k[1],offset_bytes=k[2],symbol_image_offset=k[3],symbol_aliases=list(k[4]),symbol_ambiguous=len(k[4])>1,classification=k[5],own_image_pc_offset=k[6],section=k[7],mapping_limit=k[8],samples=v) for k,v in sorted(bins.items(),key=lambda x:repr(x[0]))]
 assert sum(x['samples'] for x in output)==count
 return dict(**item,requested_ops=ops,operations=operations,checksum=str(checksum),tree_bytes=owned,traversals=int(r['traversals']),sample_count=count,capped=False,sufficient=count>=10,sampler_usec_requested=1000,timing_fields_used=False,mapping_limit=any(x['mapping_limit'] for x in output),pc_bins=output)


def main():
 p=argparse.ArgumentParser();p.add_argument('--ack',required=True);a=p.parse_args();ack=json.loads(Path(a.ack).read_text());freeze=json.loads((E/'freeze.json').read_text())
 assert ack['status']=='authorized' and ack['exclusive_runner'] is True and ack['all_other_work_idle'] is True
 for field,file in [('freeze_sha256','freeze.json'),('driver_sha256','capture.py'),('plan_sha256','PLAN.json')]:assert ack[field]==sha(E/file)
 assert re.fullmatch('[0-9a-f]{40}',ack['published_commit'])
 assert any(x['reviewer']=='/root' and x['status']=='PASS' for x in ack['reviews'])
 assert any(x['reviewer'] not in ['/root','/root/followup_proposal_c'] and x['status']=='PASS' for x in ack['reviews'])
 for path,digest in freeze['files_sha256'].items():assert sha(path)==digest
 assert not any((E/x).exists() for x in ['commands.jsonl','capture-status.json','summary.json']),'no retry/overwrite'
 assert not (S/'capture-logs').exists(),'no private overwrite'
 cutoff=min(datetime.fromisoformat(PLAN['absolute_stop_utc']).timestamp(),datetime.fromisoformat(ack['absolute_stop_utc']).timestamp());assert time.time()+20<cutoff
 for sig in [signal.SIGTERM,signal.SIGHUP]:signal.signal(sig,cancelled)
 started=time.monotonic();deadline=min(cutoff,time.time()+480);rows=json.loads((E/'offline-summary.json').read_text());assert len(rows)==3;state=dict(status='RUNNING',started_utc=utc(),planned_captures=13,combined_planned_captures=16,prior_retained_captures=3,original019status='INCOMPLETE',repair_pause_start_utc=PLAN['prior_finished_utc'],repair_pause_end_utc=utc(),timing_fields_used=False,exclusive_runner_release_safe=True)
 save(E/'capture-status.json',state);mapping=json.loads((E/'codegen.json').read_text())['enabled_mapping']
 def phase_expired(signum,frame):raise TimeoutError('parent phase deadline reached')
 signal.signal(signal.SIGALRM,phase_expired)
 signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.time()-10))
 try:
  for item in PLAN['captures']:
   i=item['original_index']
   remaining=min(deadline-time.time(),480-(time.monotonic()-started));assert remaining>10,'phase/UTC cutoff; no retry'
   name=f"{i:02d}-{item['case']}-{item['size']}-s{item['seed']}";cmd=[PLAN['binary'],'--case',item['case'],'--size',str(item['size']),'--ops','10000000','--member-bytes','16','--seed',str(item['seed']),'--warmup-passes','3']
   state['exclusive_runner_release_safe']=False;save(E/'capture-status.json',state)
   rec,paths=run(cmd,name,min(45,remaining-10),deadline);state['exclusive_runner_release_safe']=rec['release_safe'];assert rec['returncode']==0 and not rec['timed_out'] and rec['release_safe'],rec
   assert time.time()<deadline,'deadline reached after child cleanup'
   derived=derive(rec,paths,item,mapping)
   assert time.time()<deadline and time.monotonic()-started<480,'deadline reached during derivation'
   rows.append(derived);save(E/'summary.json',rows)
   assert time.time()<deadline and time.monotonic()-started<480,'deadline reached during serialization'
  state['status']='COMPLETE020 continuation; combined16 descriptive rows,019 remains INCOMPLETE'
 except BaseException as ex:state.update(status='INCOMPLETE; preserve all evidence, no retry',error_type=type(ex).__name__);raise
 finally:
  signal.setitimer(signal.ITIMER_REAL,0)
  state.update(finished_utc=utc(),phase_wall_seconds=time.monotonic()-started,completed_new_captures=len(rows)-3,combined_captures=len(rows),combined_actual_phase_seconds=PLAN['prior_phase_seconds']+time.monotonic()-started,all_sufficient=len(rows)==16 and all(x['sufficient'] for x in rows),source_candidate='NONE')
  save(E/'capture-status.json',state)
if __name__=='__main__':main()
