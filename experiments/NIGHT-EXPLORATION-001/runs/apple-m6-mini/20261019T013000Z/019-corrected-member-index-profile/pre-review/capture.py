#!/usr/bin/env python3
"""Only root-authorized frozen software captures; no builds, retries or timing inference."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,hashlib,json,os,re,signal,subprocess,time,csv,io,bisect
R=Path.cwd();E=Path(__file__).resolve().parent;S=R/'scratch/m6-corrected-member-index-profile';PLAN=json.loads((E/'PLAN.json').read_text())
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
 return rec,paths

def derive(rec,paths,item,mapping):
 data=list(csv.DictReader(io.StringIO(paths['stdout'].read_text())));assert len(data)==1 and None not in data[0];r=data[0]
 case,n,seed=item['case'],item['size'],item['seed'];ops=10000000
 for key,value in dict(case=case,size=n,seed=seed,requested_ops=ops,member_bytes=16,warmup_passes=3).items():assert r[key]==str(value)
 operations,checksum=int(r['operations']),int(r['checksum']);owned=int(r['tree_bytes']);assert owned>0
 if case in ['lookup-hit','rank']:assert operations==ops and checksum==(n*(n-1)//2)*(ops//n) and int(r['traversals'])==0
 elif case=='lookup-miss':assert operations==ops and checksum==0 and int(r['traversals'])==0
 else:
  assert case=='scan' and int(r['traversals'])==ops//n and operations>=ops and operations%(ops//n)==0 and checksum%(ops//n)==0
  # Frozen benchmark's independent scan_verify checks exact bytes/scores and coverage;
  # duplicate emissions are legal and cannot be replaced by n-only expectations.
 lines=paths['stderr'].read_text().splitlines();headers=[x for x in lines if x.startswith('PROFILE,')];assert len(headers)==1
 h=headers[0].split(',');assert len(h)==5 and h[1]==case and h[2]=='1000';count=int(h[3]);cap=int(h[4]);pc=[x.split(',') for x in lines if x.startswith('PC,')]
 assert count==len(pc) and cap==0 and count<=65536 and len(lines)==len(pc)+1
 bins=Counter();addresses=[x['address'] for x in mapping['symbols']]
 for row in pc:
  assert len(row)==6;_,module,rawpc,rawbase,symbol,rawsym=row;pcval,base,sym=map(lambda x:int(x,16),[rawpc,rawbase,rawsym])
  if module==Path(PLAN['binary']).name:
   address=pcval-base+mapping['image_vmaddr'];assert mapping['text_start']<=address<mapping['text_end']
   i=bisect.bisect_right(addresses,address)-1;assert i>=0;entry=mapping['symbols'][i];offset=address-entry['address'];symbol=entry['name'];module='profile-program';image_offset=entry['address']-mapping['image_vmaddr']
  else:offset=pcval-sym if sym and pcval>=sym else None;image_offset=None
  module=module if re.fullmatch(r'[A-Za-z0-9_.-]{1,160}',module) else 'other-module'
  symbol=symbol if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',symbol) else 'unknown'
  bins[(module,symbol,offset,image_offset)]+=1
 return dict(**item,requested_ops=ops,operations=operations,checksum=str(checksum),tree_bytes=owned,traversals=int(r['traversals']),sample_count=count,capped=False,sufficient=count>=10,sampler_usec_requested=1000,timing_fields_used=False,pc_bins=[dict(module=k[0],symbol=k[1],offset_bytes=k[2],symbol_image_offset=k[3],samples=v) for k,v in sorted(bins.items(),key=lambda x:(x[0][0],x[0][1],-1 if x[0][2] is None else x[0][2]))])

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
 started=time.monotonic();deadline=min(cutoff,time.time()+600);rows=[];state=dict(status='RUNNING',started_utc=utc(),planned_captures=16,timing_fields_used=False,exclusive_runner_release_safe=True)
 save(E/'capture-status.json',state);mapping=json.loads((E/'codegen.json').read_text())['enabled_mapping']
 try:
  for i,item in enumerate(PLAN['captures']):
   remaining=min(deadline-time.time(),600-(time.monotonic()-started));assert remaining>10,'phase/UTC cutoff; no retry'
   name=f"{i:02d}-{item['case']}-{item['size']}-s{item['seed']}";cmd=[PLAN['binary'],'--case',item['case'],'--size',str(item['size']),'--ops','10000000','--member-bytes','16','--seed',str(item['seed']),'--warmup-passes','3']
   state['exclusive_runner_release_safe']=False;save(E/'capture-status.json',state)
   rec,paths=run(cmd,name,min(45,remaining-10),deadline);state['exclusive_runner_release_safe']=rec['release_safe'];assert rec['returncode']==0 and not rec['timed_out'] and rec['release_safe'],rec
   assert time.time()<deadline,'deadline reached after child cleanup'
   rows.append(derive(rec,paths,item,mapping));save(E/'summary.json',rows)
  state['status']='COMPLETE descriptive capture set; sufficient only if all16>=10PCs and uncapped'
 except BaseException as ex:state.update(status='INCOMPLETE; preserve all evidence, no retry',error_type=type(ex).__name__);raise
 finally:
  state.update(finished_utc=utc(),phase_wall_seconds=time.monotonic()-started,completed_captures=len(rows),all_sufficient=len(rows)==16 and all(x['sufficient'] for x in rows),source_candidate='NONE')
  save(E/'capture-status.json',state)
if __name__=='__main__':main()
