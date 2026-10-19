#!/usr/bin/env python3
"""Independent offline EXP009 reconstruction; no driver/mapper import or subprocess."""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime
from fractions import Fraction
import array,csv,hashlib,io,json,math,re,signal,struct,sys,time
E=Path(__file__).resolve().parent.parent;R=E.parent.parent;O=E/'review';MASK=(1<<64)-1
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def utc(x):return datetime.fromisoformat(x)
def alarm(*args):raise TimeoutError('180-second pure offline audit cap')
def main():
 signal.signal(signal.SIGALRM,alarm);signal.alarm(180);start=time.monotonic()
 report=dict(status='RUNNING',participant='/root/followup_proposal_a',backend='Inherited Codex/GPT-6 family; exact model/token/currency costs unknown',author_disclosure='Authored profile mapper and earlier static review; independent reconstruction here imports neither mapper nor B driver. No independent timing confirmation claimed.',native_executions=0)
 try:
  inputs=load(E/'input-manifest-v2.json');timing=load(E/'timing-manifest.json');build=load(E/'bench-results/build/build-manifest.json');plan=load(E/'PLAN.json')
  assert len(inputs['files_sha256'])==69 and len(timing['files_sha256'])==297 and len(build['files_sha256'])==241
  pins={**inputs['files_sha256'],**build['files_sha256'],**timing['files_sha256']};before={p:sha(R/p) for p in pins};assert before==pins
  assert all(timing['files_sha256'].get(p)==h for p,h in build['files_sha256'].items())
  report['manifests']={p:dict(entries=len(load(E/p)['files_sha256']),sha256=sha(E/p)) for p in ['input-manifest-v2.json','timing-manifest.json']}
  phases={'build':E/'bench-results/build','profile':E/'profile-results/run','calibrate':E/'bench-results/calibrate','aa':E/'bench-results/aa'};counts={'build':63,'profile':8,'calibrate':6,'aa':48};states={};journals={};rawhash={};allrecords=[]
  for phase,folder in phases.items():
   state=load(folder/'status.json');records=[json.loads(x) for x in (folder/'commands.jsonl').read_text().splitlines()];assert len(records)==counts[phase]==state['journaled_attempts']
   assert state['status']=='COMPLETE' and state['release_safe'] and state['source_adoption']=='NONE' and state['phase_wall_seconds']<state['wall_limit_seconds']
   manifest=E/'input-manifest-v2.json' if phase=='build' else E/'timing-manifest.json' if phase=='aa' else E/'bench-results/build/build-manifest.json'
   assert state['manifest_sha256']==sha(manifest) and state['post_frozen_entries_verified']==len(load(manifest)['files_sha256'])
   for p,h in state['prerequisite_final_status_sha256'].items():assert sha(R/p)==h
   for rec in records:
    assert rec['cwd']=='.' and rec['child_reaped'] and rec['owned_group_empty'] and rec['release_safe'] and not rec['timed_out']
    assert rec['returncode']==(2 if '-invalid-' in rec['name'] else 0)
    assert 0<rec['timeout_seconds']<=120 and rec['wall_seconds']<=rec['timeout_seconds']+10
    assert utc(state['started_utc'])<=utc(rec['started_utc'])<utc(rec['finished_utc'])<=utc(state['finished_utc'])<utc(plan['overall_stop_utc'])
    env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LANG':'C','LC_ALL':'C','TZ':'UTC'}
    if phase=='profile' and not rec['name'].endswith('-offline-map'):env['PROFILE_USEC']='1000'
    assert rec['environment']==env
    for stream,meta in rec['raw'].items():
     path=R/meta['path'];assert sha(path)==meta['sha256'] and path.stat().st_size==meta['bytes'];rawhash[meta['path']]=meta['sha256']
    allrecords.append(rec)
   states[phase]=state;journals[phase]=records
  serial=sorted(allrecords,key=lambda x:utc(x['started_utc']));assert all(utc(a['finished_utc'])<=utc(b['started_utc']) for a,b in zip(serial,serial[1:]));assert len(serial)==125 and len(rawhash)==250
  report['phase_journals']={k:dict(commands=len(v),wall_seconds=states[k]['phase_wall_seconds'],release_safe=True) for k,v in journals.items()}
  report['all_125_recorded_intervals_serial_and_reaped']=True;report['raw_streams_verified']=250
  models={}
  def permutation(n,seed):
   if (n,seed) not in models:
    sequence=list(range(n));state=seed^0xd02703a89f4c51e7
    for upper in range(n,1,-1):
     state=(state+0x9e3779b97f4a7c15)&MASK;z=state;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK;z^=z>>31
     j=z%upper;sequence[upper-1],sequence[j]=sequence[j],sequence[upper-1]
    packed=array.array('Q',sequence)
    if sys.byteorder!='little':packed.byteswap()
    models[n,seed]=(sequence,hashlib.sha256(packed.tobytes()).hexdigest())
   return models[n,seed]
  def checksum(case,n,ops,seed):
   sequence,digest=permutation(n,seed);whole,tail=divmod(ops,n)
   if case=='lookup-hit':value=whole*n*(n-1)//2+sum(sequence[:tail])
   elif case=='lookup-miss':value=0
   else:value=whole*sum(x+1 for i,x in enumerate(sequence) if i%2==0)+sum(sequence[i]+1 for i in range(0,tail,2))
   return value&MASK,digest
  fields='case,size,requested_ops,member_bytes,seed,operations,elapsed_ns,ns_per_op,ops_per_sec,tree_bytes,checksum,thread_elapsed_ns,cpu_start,cpu_end,qos_reported_start,qos_reported_end,qos_relpri_start,qos_relpri_end,qos_effective,traversals,warmup_passes,warmup_elapsed_ns'.split(',')
  fingerprint=['case','size','requested_ops','member_bytes','seed','operations','warmup_passes','traversals','checksum','tree_bytes']
  def parse(rec,n,ops,seed,case='lookup-hit',member=16,profile=False):
   paths={k:R/v['path'] for k,v in rec['raw'].items()}
   if not profile:assert paths['stderr'].stat().st_size==0
   reader=csv.DictReader(io.StringIO(paths['stdout'].read_text()));data=list(reader);assert reader.fieldnames==fields and len(data)==1 and None not in data[0];r=data[0]
   for k,v in dict(case=case,size=n,requested_ops=ops,member_bytes=member,seed=seed,operations=ops,warmup_passes=1,traversals=0).items():assert r[k]==str(v)
   expected,digest=checksum(case,n,ops,seed);assert int(r['checksum'])==expected and int(r['tree_bytes'])>0 and int(r['elapsed_ns'])>0
   for k,v in r.items():
    if k in ['case','qos_reported_start','qos_reported_end','qos_effective']:assert re.fullmatch(r'[A-Za-z0-9_-]{1,80}',v)
    elif k in ['ns_per_op','ops_per_sec']:assert re.fullmatch(r'(0|[1-9][0-9]*)\.[0-9]{3}',v) and math.isfinite(float(v))
    else:assert re.fullmatch(r'-?(0|[1-9][0-9]*)',v) and v!='-0'
   elapsed=int(r['elapsed_ns']);assert abs(float(r['ns_per_op'])-elapsed/ops)<=.0006 and abs(float(r['ops_per_sec'])-ops*1e9/elapsed)<=.0006
   assert int(r['warmup_elapsed_ns'])>=0 and int(r['thread_elapsed_ns'])>=-1 and min(int(r['cpu_start']),int(r['cpu_end']))>=-1
   return dict(csv=r,elapsed_ns=elapsed,operations=ops,checksum=str(expected),tree_bytes=int(r['tree_bytes']),query_order_sha256_le_u64=digest,fingerprint={k:r[k] for k in fingerprint},output_mode='score nonNULL / public zbtreeScore')
  # Read original native/san outputs without executing them.
  smokes=0;original=oracles=invalid=0
  for rec in journals['build']:
   out=(R/rec['raw']['stdout']['path']).read_text()
   if rec['name'] in ['native-original43','san-original43']:assert re.search('43 passed',out) and '0 failed, 43 total' in out;original+=1
   if rec['name'] in ['native-physical-oracle','san-physical-oracle']:assert 'PASS cells=4160 exact-score/position/output checks=515840' in out;oracles+=1
   match=re.fullmatch(r'(native|san)-(lookup-(?:hit|miss|mixed))-m(\d+)',rec['name'])
   if match:
    parsed=parse(rec,1000,2003,1,match[2],int(match[3]));assert parsed==load(phases['build']/(rec['name']+'.json'));smokes+=1
   invalid+='-invalid-' in rec['name']
  assert (original,oracles,smokes,invalid)==(2,2,36,8)
  report['baseline_validation']=dict(original43_invocations=2,physical_oracle_invocations=2,cells_per_oracle=4160,checks_per_oracle=515840,semantic_smokes=36,invalid_cli_checks=8)
  calibration=load(phases['calibrate']/'counts.json');assert calibration['build_manifest_sha256']==sha(E/'bench-results/build/build-manifest.json');calrows=[];fixed={}
  for i,rec in enumerate(journals['calibrate']):
   n=[100000,1000000][i//3];rep=i%3;assert rec['name']==f'n{n}-rep{rep}';assert rec['command']==[build['binaries']['native'],'--case','lookup-hit','--size',str(n),'--ops','200000','--seed','1','--member-bytes','16','--warmup-passes','1']
   parsed=parse(rec,n,200000,1);calrows.append(parsed);assert parsed==calibration['observations'][i]
  for n in [100000,1000000]:
   fastest=min(r['elapsed_ns'] for r in calrows if int(r['csv']['size'])==n);desired=(600000000*200000+fastest-1)//fastest;ops=min(100000000,desired);cfg=calibration['fixed'][str(n)]
   assert (cfg['operations'],cfg['uncapped_operations'],cfg['capped'],cfg['fastest_elapsed_ns_at_200000'])==(ops,desired,desired>100000000,fastest);fixed[n]=ops
  report['calibration_fixed_operations']=fixed
  # Independent raw PC reconstruction from Mach-O bytes and retained nm; no mapper import.
  def pcmap(binary,nm):
   blob=(R/binary).read_bytes();assert struct.unpack_from('<I',blob)[0]==0xfeedfacf;offset=32;sections=[];image=None
   for _ in range(struct.unpack_from('<I',blob,16)[0]):
    cmd,size=struct.unpack_from('<II',blob,offset)
    if cmd==0x19:
     seg=blob[offset+8:offset+24].split(b'\0')[0].decode()
     if seg=='__TEXT':image=struct.unpack_from('<Q',blob,offset+24)[0]
     for j in range(struct.unpack_from('<I',blob,offset+64)[0]):
      q=offset+72+80*j;sec=blob[q:q+16].split(b'\0')[0].decode();sg=blob[q+16:q+32].split(b'\0')[0].decode();address,extent=struct.unpack_from('<QQ',blob,q+32);sections.append((sg,sec,address,extent))
    offset+=size
   text=next(x for x in sections if x[:2]==('__TEXT','__text'));symbols=defaultdict(list)
   for line in (R/nm).read_text().splitlines():
    m=re.fullmatch(r'([0-9a-fA-F]+)\s+[Tt]\s+(\S+)',line.strip())
    if m and text[2]<=int(m[1],16)<text[2]+text[3]:symbols[int(m[1],16)].append(m[2])
   return image,sections,text,symbols
  def classify(line,binary,mapping):
   x=line.split(',');assert len(x)==6 and x[0]=='PC';_,module,pc,base,label,sym=x;pc,base,sym=[int(z,16) for z in [pc,base,sym]];image,sections,text,symbols=mapping
   own=module==Path(binary).name;r=dict(module='profile-program' if own else module,symbol=label,symbol_aliases=[],symbol_ambiguous=False,symbol_offset_bytes=None,own_image_pc_offset=None,symbol_image_offset=None,section=None,mapping_limit=True,classification='external-unknown')
   if not own:
    if label!='unknown' and sym and pc>=sym:r.update(symbol_aliases=[label],symbol_offset_bytes=pc-sym,classification='external-dladdr-label',mapping_limit=False)
    return r
   r.update(symbol='unknown-own-image',classification='unmapped-own-image')
   if not base or pc<base:return r
   relative=pc-base;address=image+relative;r['own_image_pc_offset']=relative;hits=[s for s in sections if s[2]<=address<s[2]+s[3]]
   if len(hits)==1:r['section']=hits[0][0]+','+hits[0][1]
   if text[2]<=address<text[2]+text[3] and address%4==0:
    earlier=[a for a in symbols if a<=address]
    if earlier:
     a=max(earlier);aliases=symbols[a];r.update(symbol=aliases[0] if len(aliases)==1 else 'ambiguous-coalesced-symbol',symbol_aliases=aliases,symbol_ambiguous=len(aliases)>1,symbol_offset_bytes=address-a,symbol_image_offset=a-image,classification='text-symbol',mapping_limit=len(aliases)>1)
   elif len(hits)==1 and hits[0][:2]==('__TEXT','__stubs'):r.update(symbol='import-stub-unknown-target',classification='import-stub',symbol_offset_bytes=address-hits[0][2],symbol_image_offset=hits[0][2]-image)
   return r
  profiles=load(phases['profile']/'summary.json');assert len(profiles)==4;profile_rows=[]
  nativeprofile=[r for r in journals['profile'] if not r['name'].endswith('-offline-map')];assert [r['name'] for r in nativeprofile]==['sampler-0','sampler-1','hit-n100000','hit-n1000000']
  multiplier,increment=1,0;a,c,n=1664525,1013904223,200000000
  while n:
   if n&1:multiplier,increment=(a*multiplier)&MASK,(a*increment+c)&MASK
   a,c=(a*a)&MASK,(a*c+c)&MASK;n>>=1
  known=(multiplier+increment)&MASK;assert known==1128443088728658433
  for i,rec in enumerate(nativeprofile):
   control=i<2;mode='sampler' if control else 'profile';binary=build['binaries'][mode];mapping=pcmap(binary,build['metadata'][mode]['nm']);mapped=load(R/profiles[i]['map_path']);assert sha(R/profiles[i]['map_path'])==profiles[i]['map_sha256']
   lines=(R/rec['raw']['stderr']['path']).read_text().splitlines();header=lines[0].split(',');expected_scope='sampler_probe' if control else 'lookup-hit';assert header[:3]==['PROFILE',expected_scope,'1000'] and header[4]=='0';count=int(header[3]);assert count==len(lines)-1 and 25<=count<=65536
   derived=[dict(ordinal=j,**classify(line,binary,mapping)) for j,line in enumerate(lines[1:])];assert derived==mapped['observations'];bins=Counter(json.dumps({k:v for k,v in x.items() if k!='ordinal'},sort_keys=True) for x in derived)
   assert bins==Counter({json.dumps({k:v for k,v in x.items() if k!='samples'},sort_keys=True):x['samples'] for x in mapped['pc_bins']}) and sum(bins.values())==count
   assert mapped['sample_count']==profiles[i]['sample_count']==count and mapped['status']=='PASS' and mapped['timing_fields_used'] is False and mapped['all_observations_conserved']
   if control:
    assert rec['command']==[binary] and (R/rec['raw']['stdout']['path']).read_text()==f'result,{known}\n'
    assembly=(R/build['metadata'][mode]['assembly']).read_text();body=assembly.split('_sampler_probe:\n',1)[1].split('_main:',1)[0];addresses=[int(m[1],16) for line in body.splitlines() if (m:=re.match(r'^\s*([0-9a-fA-F]{16})\s+',line))];assert addresses and addresses==list(range(addresses[0],addresses[-1]+4,4));lo=addresses[0]-mapping[0];hi=addresses[-1]+4-mapping[0]
    assert mapping[3][addresses[0]]==['_sampler_probe'] and all(x['module']=='profile-program' and x['own_image_pc_offset'] is not None and lo<=x['own_image_pc_offset']<hi and x['own_image_pc_offset']%4==0 for x in derived)
   else:
    size=[100000,1000000][i-2];assert rec['command']==[binary,'--case','lookup-hit','--size',str(size),'--ops','10000000','--seed','1','--member-bytes','16','--warmup-passes','1'];assert parse(rec,size,10000000,1,profile=True)==profiles[i]['csv']
   profile_rows.append(dict(name=rec['name'],observations=count,classifications=dict(Counter(x['classification'] for x in derived)),all_probe_extent=control))
  assert [x['observations'] for x in profile_rows]==[81,67,83,283];report['profiles']=profile_rows
  # Reconstruct new AA schedule and every statistic from native raw rows.
  schedule=[]
  for block,seed in enumerate([1,2,3,1,2,3]):
   for size in ([100000,1000000] if block%2==0 else [1000000,100000]):
    for position,side in enumerate('ABBA'):schedule.append(dict(index=len(schedule),block=block,seed=seed,size=size,case='lookup-hit',member_bytes=16,warmup_passes=1,position=position,side=side,operations=fixed[size]))
  assert schedule==load(phases['calibrate']/'aa-schedule.json') and len(schedule)==48
  rows=[];blocks=[];public=load(phases['aa']/'summary.json');fixture={}
  for item,rec in zip(schedule,journals['aa']):
   n,ops,seed=item['size'],item['operations'],item['seed'];assert rec['name']==f"{item['index']:03d}" and rec['command']==[build['binaries']['native'],'--case','lookup-hit','--size',str(n),'--ops',str(ops),'--seed',str(seed),'--member-bytes','16','--warmup-passes','1']
   row=parse(rec,n,ops,seed);row.update(item);rows.append(row)
   key=(n,seed);assert key not in fixture or fixture[key]==row['fingerprint'];fixture[key]=row['fingerprint']
  assert rows==public['rows']
  for i in range(0,48,4):
   q=rows[i:i+4];assert all(x['fingerprint']==q[0]['fingerprint'] for x in q);a=q[0]['elapsed_ns']+q[3]['elapsed_ns'];b=q[1]['elapsed_ns']+q[2]['elapsed_ns'];minimum=min(x['elapsed_ns'] for x in q)
   value=dict(block=q[0]['block'],size=q[0]['size'],seed=q[0]['seed'],baseline_elapsed_sum=a,paired_elapsed_sum=b,effect_percent_display_only=float(Fraction(100*(b-a),a)),minimum_elapsed_ns=minimum,qualified=abs(b-a)*100<=a and minimum>=10000000)
   reported=public['blocks'][i//4];assert all(abs(value[k]-reported[k])<1e-12 if k=='effect_percent_display_only' else value[k]==reported[k] for k in value);blocks.append(value)
  assert states['aa']['qualified'] is False and sum(x['qualified'] for x in blocks if x['size']==100000)==6 and sum(x['qualified'] for x in blocks if x['size']==1000000)==3
  assert {p:sha(R/p) for p in pins}==before and all(sha(R/p)==h for p,h in rawhash.items())
  report.update(status='PASS',aa_processes=48,aa_blocks=blocks,aa_qualified=False,failed_aa_blocks=[x for x in blocks if not x['qualified']],aa_minimum_ns=min(r['elapsed_ns'] for r in rows),aa_maximum_ns=max(r['elapsed_ns'] for r in rows),all_input_and_raw_hashes_unchanged=True,raw_sha256=rawhash,fixture_fingerprints={f'{n}:{s}':v for (n,s),v in fixture.items()},decision='PARK; source NONE; no proposals or implementation population; historical counts unchanged',limitations='PC locations not cycles/costs. Native macOS unpinned; endpoint metadata not residency/frequency/causality. Baseline prerequisites only, no candidate timing, new source, fresh confirmation or acceptance.')
 except BaseException as ex:report.update(status='FAIL',error_type=type(ex).__name__,error=str(ex).replace(str(R),'<workspace>'));raise
 finally:
  signal.alarm(0);report.update(audit_wall_seconds=time.monotonic()-start,script_sha256=sha(__file__));(O/'FINAL-RAW-AUDIT-A.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['status','aa_qualified','failed_aa_blocks','profiles','phase_journals']}))
if __name__=='__main__':main()
