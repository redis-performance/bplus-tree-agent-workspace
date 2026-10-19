#!/usr/bin/env python3
"""Read-only raw audit, independent of capture.py/classifier imports."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import csv, hashlib, io, json, re, signal, struct, time
R=Path.cwd(); E=Path(__file__).resolve().parent; P=E.parent/'019-corrected-member-index-profile'
report={'participant':'/root/followup_proposal_a','backend':'Inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown','status':'RUNNING','bound_seconds':180,'binary_executions':0,'captures':0,'timing_fields_used':False}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def when(x):return datetime.fromisoformat(x)
def expire(*args):raise TimeoutError('180-second independent offline audit bound')
def main():
 start=time.monotonic();signal.signal(signal.SIGALRM,expire);signal.alarm(180)
 freezes={str(d.relative_to(R)):load(d/'freeze.json')['files_sha256'] for d in [P,E]}
 tracked={}
 for paths in freezes.values():tracked.update(paths)
 for p in P.rglob('*'):
  if p.is_file():tracked.setdefault(str(p.relative_to(R)),sha(p))
 for name in ['freeze.json','PLAN.json','summary.json','commands.jsonl','capture-status.json','EXCLUSIVE-RELEASE.json']:
  tracked[str((E/name).relative_to(R))]=sha(E/name)
 assert all(sha(p)==h for p,h in tracked.items())
 before={p:sha(p) for p in tracked}
 report['freeze_counts']={str(d.relative_to(R)):len(load(d/'freeze.json')['files_sha256']) for d in [P,E]}
 report['freeze_sha256']={str(d.relative_to(R)):sha(d/'freeze.json') for d in [P,E]}
 ack=load(E/'EXCLUSIVE-RELEASE.json');plan=load(E/'PLAN.json');state=load(E/'capture-status.json')
 assert ack['status']=='authorized' and ack['exclusive_runner'] and ack['all_other_work_idle']
 for field,name in [('freeze_sha256','freeze.json'),('driver_sha256','capture.py'),('plan_sha256','PLAN.json')]:assert ack[field]==sha(E/name)
 assert re.fullmatch('[0-9a-f]{40}',ack['published_commit'])
 assert {'/root','/root/followup_proposal_b'}<={x['reviewer'] for x in ack['reviews'] if x['status']=='PASS'}
 assert ack['only_unstarted_indices']==list(range(3,16)) and ack['prior_captures_reused_without_rerun']==3
 report['published_commit']=ack['published_commit']
 # Parse actual immutable Mach-O bytes, not the prepared classifier map.
 binary=R/plan['binary'];b=binary.read_bytes();assert struct.unpack_from('<I',b)[0]==0xfeedfacf
 count=struct.unpack_from('<I',b,16)[0];offset=32;sections=[];image=None
 for _ in range(count):
  cmd,size=struct.unpack_from('<II',b,offset)
  if cmd==0x19:
   name=b[offset+8:offset+24].split(b'\0')[0].decode();vm=struct.unpack_from('<Q',b,offset+24)[0]
   if name=='__TEXT':image=vm
   nsects=struct.unpack_from('<I',b,offset+64)[0]
   for j in range(nsects):
    q=offset+72+80*j;sec=b[q:q+16].split(b'\0')[0].decode();seg=b[q+16:q+32].split(b'\0')[0].decode();addr,extent=struct.unpack_from('<QQ',b,q+32)
    sections.append(dict(segment=seg,section=sec,address=addr,size=extent))
  offset+=size
 assert len(sections)==9 and sections==load(E/'sections.json')['sections']
 text=next(s for s in sections if s['section']=='__text');lo=text['address'];hi=lo+text['size']
 groups=defaultdict(list)
 for line in (P/'enabled-nm.txt').read_text().splitlines():
  match=re.fullmatch(r'([0-9a-fA-F]+)\s+([Tt])\s+(\S+)',line)
  if match:
   addr=int(match[1],16)
   if lo<=addr<hi:groups[addr].append(match[3])
 entries=sorted(groups)
 prepared=load(E/'codegen.json')['enabled_mapping']
 assert [(s['address'],s.get('aliases',[s['name']])) for s in prepared['symbols']]==[(a,groups[a]) for a in entries]
 assert prepared['sections']==sections and prepared['image_vmaddr']==image and prepared['binary_sha256']==sha(binary)
 report['mapping']=dict(binary_sha256=sha(binary),actual_macho_sections=9,text_relative_bounds=[lo-image,hi-image],stubs_relative_bounds=[[s['address']-image,s['address']+s['size']-image] for s in sections if s['section']=='__stubs'],text_symbol_groups=len(entries),coalesced_alias_groups=sum(len(v)>1 for v in groups.values()),method='Actual Mach-O load-command bytes plus retained nm T/t entries; no classifier import')
 def classify(line):
  fields=line.split(',');assert len(fields)==6 and fields[0]=='PC'
  _,module,pcstr,basestr,symbol,symstr=fields;pc,base,sym=[int(x,16) for x in [pcstr,basestr,symstr]]
  aliases=[symbol];section=None;relative=None;kind='external-symbol';limited=False;symbol_start=None
  if module==binary.name:
   module='profile-program';symbol='unknown-own-image';aliases=[];within=None;limited=True;kind='unmapped-own-image'
   if base and pc>=base:
    relative=pc-base;actual=image+relative
    hits=[s for s in sections if s['address']<=actual<s['address']+s['size']]
    if len(hits)==1:section=hits[0]['segment']+','+hits[0]['section']
    if lo<=actual<hi and actual%4==0:
     preceding=[address for address in entries if address<=actual]
     if preceding:
      address=max(preceding);aliases=groups[address];symbol=aliases[0] if len(aliases)==1 else 'ambiguous-coalesced-symbol';within=actual-address;symbol_start=address-image;kind='text-symbol';limited=len(aliases)>1
    elif len(hits)==1 and hits[0]['segment']=='__TEXT' and hits[0]['section']=='__stubs':
     kind='import-stub';symbol='import-stub-unknown-target';within=actual-hits[0]['address'];symbol_start=hits[0]['address']-image
  else:within=pc-sym if sym and pc>=sym else None
  clean=lambda x,fallback:x if re.fullmatch(r'[A-Za-z0-9_.$-]{1,160}',x) else fallback
  module=module if re.fullmatch(r'[A-Za-z0-9_.-]{1,160}',module) else 'other-module';symbol=clean(symbol,'unknown');aliases=[clean(x,'unknown') for x in aliases]
  return dict(module=module,symbol=symbol,offset_bytes=within,symbol_image_offset=symbol_start,symbol_aliases=aliases,symbol_ambiguous=len(aliases)>1,classification=kind,own_image_pc_offset=relative,section=section,mapping_limit=limited)
 oldrec=[json.loads(l) for l in (P/'commands.jsonl').read_text().splitlines()];newrec=[json.loads(l) for l in (E/'commands.jsonl').read_text().splitlines()]
 records=oldrec+newrec;summary=load(E/'summary.json');assert len(oldrec)==3 and len(newrec)==13 and len(summary)==16
 schedule=[dict(case=c,size=n,seed=s,original_index=i,origin_campaign='019' if i<3 else '020') for i,(c,n,s) in enumerate((c,n,s) for c in ['lookup-hit','lookup-miss','rank','scan'] for n in [100000,1000000] for s in [1,2])]
 assert plan['captures']==schedule[3:] and load(P/'PLAN.json')['captures']==[{k:v for k,v in row.items() if k not in ['original_index','origin_campaign']} for row in schedule]
 overall=Counter();coarse=Counter();rows=[];last=None;owned=defaultdict(set);rawidentities={};totalsamples=0
 for item,rec,out in zip(schedule,records,summary):
  i=item['original_index'];case=item['case'];n=item['size'];seed=item['seed'];name=f'{i:02d}-{case}-{n}-s{seed}'
  expected=[str(binary.relative_to(R)),'--case',case,'--size',str(n),'--ops','10000000','--member-bytes','16','--seed',str(seed),'--warmup-passes','3']
  assert rec['name']==name and rec['command']==expected and rec['environment_overrides']=={'PROFILE_USEC':'1000'}
  assert rec['returncode']==0 and not rec['timed_out'] and rec['child_reaped'] and rec['owned_group_empty'] and rec['release_safe']
  assert rec['timeout_seconds']==45 and 0<rec['wall_seconds']<45
  began,ended=when(rec['started_utc']),when(rec['finished_utc']);assert began<ended and (last is None or began>=last);last=ended
  if i>=3:assert began>=when(ack['released_utc'])
  streams={ch:R/v['path'] for ch,v in rec['raw'].items()};assert set(streams)=={'stdout','stderr'}
  for ch,path in streams.items():
   meta=rec['raw'][ch];assert sha(path)==meta['sha256'] and path.stat().st_size==meta['bytes'];rawidentities[str(path.relative_to(R))]=meta['sha256']
  csvrows=list(csv.DictReader(io.StringIO(streams['stdout'].read_text())));assert len(csvrows)==1 and None not in csvrows[0];r=csvrows[0]
  for k,v in dict(case=case,size=n,seed=seed,requested_ops=10000000,member_bytes=16,warmup_passes=3).items():assert r[k]==str(v)
  operations,checksum,tree,traversals=[int(r[k]) for k in ['operations','checksum','tree_bytes','traversals']];assert tree>0
  if case in ['lookup-hit','rank']:assert operations==10000000 and checksum==(n*(n-1)//2)*(10000000//n) and traversals==0
  elif case=='lookup-miss':assert operations==10000000 and checksum==0 and traversals==0
  else:
   assert traversals==10000000//n and operations>=10000000 and operations%traversals==0 and checksum%traversals==0
   assert operations//traversals>=n and checksum//traversals>=n*(n-1)//2
  owned[(n,seed)].add(tree)
  lines=streams['stderr'].read_text().splitlines();header=lines[0].split(',');assert header[:3]==['PROFILE',case,'1000'] and len(header)==5
  count,cap=map(int,header[3:]);assert cap==0 and count==len(lines)-1 and 10<=count<=65536
  bins=Counter(json.dumps(classify(line),sort_keys=True) for line in lines[1:]);reconstructed=[dict(json.loads(key),samples=value) for key,value in bins.items()]
  normalized=lambda xs:sorted(json.dumps(x,sort_keys=True) for x in xs)
  assert normalized(reconstructed)==normalized(out['pc_bins']) and sum(b['samples'] for b in reconstructed)==count
  for k,v in {**item,'operations':operations,'checksum':str(checksum),'tree_bytes':tree,'traversals':traversals,'sample_count':count,'requested_ops':10000000,'sampler_usec_requested':1000,'capped':False,'sufficient':True,'timing_fields_used':False,'mapping_limit':any(b['mapping_limit'] for b in reconstructed)}.items():assert out[k]==v
  classcounts=Counter();locations=Counter()
  for b in reconstructed:
   classcounts[b['classification']]+=b['samples'];locations[b['symbol']]+=b['samples']
   if b['module']=='profile-program' and b['classification']!='text-symbol':assert b['mapping_limit'] and not b['symbol_aliases'] and b['symbol'] in ['unknown-own-image','import-stub-unknown-target']
   if b['symbol_ambiguous']:assert b['mapping_limit'] and b['symbol']=='ambiguous-coalesced-symbol'
  overall.update(classcounts);coarse.update(locations);totalsamples+=count
  rows.append(dict(**item,operations=operations,checksum=str(checksum),tree_bytes=tree,traversals=traversals,duplicate_scan_entries_per_traversal=operations//traversals-n if traversals else None,samples=count,classifications=dict(classcounts),symbol_locations=dict(locations),started_utc=rec['started_utc'],finished_utc=rec['finished_utc']))
 assert all(len(values)==1 for values in owned.values())
 assert totalsamples==2469 and min(x['samples'] for x in rows)==19 and max(x['samples'] for x in rows)==429
 pause=(when(newrec[0]['started_utc'])-when(oldrec[-1]['finished_utc'])).total_seconds()
 assert when(state['repair_pause_start_utc'])==when(load(P/'capture-status.json')['finished_utc'])
 report['seriality']=dict(all_16_intervals_serial=True,all_16_children_reaped=True,all_16_owned_groups_empty=True,repair_pause_between_child_intervals_seconds=pause,declared_repair_pause_seconds=(when(state['repair_pause_end_utc'])-when(state['repair_pause_start_utc'])).total_seconds(),repair_pause_is_separate_phase=True,prior_phase_seconds=plan['prior_phase_seconds'],continuation_phase_seconds=state['phase_wall_seconds'],combined_phase_seconds=state['combined_actual_phase_seconds'],first_utc=records[0]['started_utc'],last_utc=records[-1]['finished_utc'])
 assert state['completed_new_captures']==13 and state['combined_captures']==16 and state['post_continuation_identities_verified']==86 and state['exclusive_runner_release_safe'] and state['all_sufficient']
 assert state['phase_wall_seconds']<480 and when(state['finished_utc'])<when(plan['absolute_stop_utc'])
 # Exit-zero evidence is interpreted together with these frozen internal assertions.
 source=(P/'microbench-profile.c').read_text()
 for fragment in ['serverAssert(id < check->n && score == (double)id);','serverAssert(len == sdslen(check->keys[id]) && !memcmp(key, check->keys[id], len));','serverAssert(check.seen[i]);','serverAssert(scanned.count == check.result.count * traversals);','expected = check.result.sum * traversals;','serverAssert(checksum == expected);']:
  assert fragment in source
 prep=load(P/'PREPARATION.json');report['assertion_build_flags']=prep['flags']
 assert 'NDEBUG' not in json.dumps(prep['flags'])
 report['oracle_limit']='No new correctness execution. Frozen internal scan assertions independently check exact member bytes, score, coverage, emitted duplicate counts and checksum after bracket; exit-zero captures pass them. Raw aggregate rows alone cannot reconstruct each duplicate member.'
 assert all(sha(p)==h for p,h in before.items()) and all(sha(p)==h for p,h in rawidentities.items())
 report.update(status='PASS',schedule_cells=16,prior_processes=3,new_processes=13,total_retained_pcs=totalsamples,sample_range=[min(x['samples'] for x in rows),max(x['samples'] for x in rows)],all_uncapped_and_sufficient=True,classifications=dict(overall),coarse_symbol_locations=dict(coarse),rows=rows,raw_sha256=rawidentities,snapshotted_input_count=len(before),snapshotted_input_sha256=before,all_snapshots_unchanged=True,raw_streams_verified=len(rawidentities),audit_wall_seconds=time.monotonic()-start,source_candidate='NONE')
 signal.alarm(0)
if __name__=='__main__':
 try:main()
 except BaseException as ex:report.update(status='FAIL',error_type=type(ex).__name__,error=str(ex));raise
 finally:
  report['script_sha256']=sha(__file__)
  (E/'INDEPENDENT-CAPTURE-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['status','schedule_cells','total_retained_pcs','sample_range','classifications','raw_streams_verified','snapshotted_input_count','seriality']}))
