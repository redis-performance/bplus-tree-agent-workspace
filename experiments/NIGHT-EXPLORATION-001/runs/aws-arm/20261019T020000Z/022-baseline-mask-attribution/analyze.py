#!/usr/bin/env python3
"""Read-only exclusive baseline attribution from already audited019 samples."""
from pathlib import Path
import collections,hashlib,json,re
p=Path(__file__).resolve().parent;c=p.parent;d=c/'019-neon-matched-profile';seal=json.loads((d/'evidence-sha256.json').read_text());sample=d/'analysis/sample-classifications.json';assert hashlib.sha256(sample.read_bytes()).hexdigest()==seal['analysis/sample-classifications.json'];samples=json.loads(sample.read_text());asm=c/'017-corrected-neon/validation/base-native-codegen.stdout';text=asm.read_text();ins={int(a,16):(op,t)for a,op,t in re.findall(r'^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)$',text,re.M)}
R=lambda a,b:set(range(a,b,4))
groups={
 'query_pattern_setup':R(0x104dc,0x104e4),
 'word_mask_construction':R(0x10520,0x10528)|R(0x1052c,0x10544)|{0x105f8,0x105fc,0x10600}|R(0x10608,0x1062c)|R(0x10698,0x106a0)|R(0x106a4,0x106b4),
 'word_load_and_address':{0x1051c,0x10528,0x105f4,0x10604,0x10694,0x106a0},
 'candidate_position_extract':R(0x10558,0x10564)|{0x10640,0x10648,0x1064c}|R(0x106c8,0x106d4),
 'candidate_byte_recheck':R(0x10564,0x10570)|{0x10644}|R(0x10650,0x10668)|R(0x106d4,0x106e0),
 'candidate_position_output':R(0x10570,0x10580)|R(0x10668,0x10674)|R(0x106e0,0x106f0),
 'candidate_mask_iteration_control':R(0x10544,0x10558)|{0x10580}|R(0x1062c,0x10640)|{0x10674}|R(0x106b4,0x106c8)|{0x106f0},
 'word_loop_control':R(0x10510,0x1051c)|R(0x105e8,0x105f4)|R(0x10688,0x10694),
 'scalar_tail_and_tail_setup':R(0x10438,0x104a0)|R(0x10584,0x105d8)|R(0x106f4,0x10778),
 'remaining_helper_pointer_dispatch_setup':R(0x103f8,0x10438)|R(0x104e4,0x10510)|R(0x105d8,0x105e8)|R(0x10678,0x10688)}
all_ips=R(0x103f8,0x104a0)|R(0x104dc,0x10778);assigned={}
for name,ips in groups.items():
 for ip in ips:assert ip in ins and ip not in assigned;(assigned.__setitem__(ip,name))
assert set(assigned)==all_ips and len(all_ips)==209
mapping={name:[dict(address=hex(ip),symbol_offset=hex(ip-0x10298),opcode=ins[ip][0],instruction=ins[ip][1])for ip in sorted(ips)]for name,ips in groups.items()}
rows=[];details=[]
for n in [100000,1000000]:
 for seed in [1,2,3]:
  name=f'base-n{n}-s{seed}';ss=[s for s in samples if s['capture']==name and s['scope']=='timed'];row=dict(size=n,seed=seed,timed_events=len(ss),timed_period=sum(s['period']for s in ss),groups={k:dict(events=0,period=0)for k in list(groups)+['slot_outside_helper','outside_slot']});counts=collections.Counter();events=collections.Counter()
  for s in ss:
   ip=0x10298+s['slot_offset']if s['slot_offset']is not None else None;group=assigned.get(ip,'slot_outside_helper'if ip is not None else 'outside_slot');row['groups'][group]['events']+=1;row['groups'][group]['period']+=s['period']
   if ip in assigned:counts[ip]+=s['period'];events[ip]+=1
  assert sum(x['events']for x in row['groups'].values())==row['timed_events'];assert sum(x['period']for x in row['groups'].values())==row['timed_period'];rows.append(row)
  details.append(dict(size=n,seed=seed,ips=[dict(address=hex(ip),group=assigned[ip],events=events[ip],period=v,instruction=ins[ip][1])for ip,v in counts.most_common()]))
summary=[]
for n in [100000,1000000]:
 rr=[r for r in rows if r['size']==n];total=sum(r['timed_period']for r in rr);summary.append(dict(size=n,timed_events=sum(r['timed_events']for r in rr),timed_period=total,groups={k:dict(events=sum(r['groups'][k]['events']for r in rr),period=sum(r['groups'][k]['period']for r in rr),timed_period_pct=100*sum(r['groups'][k]['period']for r in rr)/total)for k in rr[0]['groups']}))
for name,data in [('exclusive-map',mapping),('per-capture',rows),('sampled-ips',details),('summary',summary)]: (p/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
(p/'inputs.json').write_text(json.dumps(dict(profile_commit='cb708e4ec',sample_classifications_sha256=hashlib.sha256(sample.read_bytes()).hexdigest(),baseline_asm_sha256=hashlib.sha256(asm.read_bytes()).hexdigest(),baseline_binary='869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055',symbol_start='0x10298',helper_total_instructions=209,groups_exclusive=True,no_new_measurement=True),indent=2)+'\n')
print(json.dumps({r['size']:{k:round(v['timed_period_pct'],4)for k,v in r['groups'].items()}for r in summary},indent=2))
# Transparent nested diagnostic: optional folded-zero construction/selection in the
# forward word loop. This subset is NOT additive to word_mask_construction above.
subset=[]
fold_addresses=[0x105fc,0x10610,0x10618,0x10620,0x10624,0x10628]
for n in [100000,1000000]:
 ss=[s for s in samples if s['capture'].startswith(f'base-n{n}-')and s['scope']=='timed'];matched=[s for s in ss if s['slot_offset']is not None and s['slot_offset']+0x10298 in fold_addresses];period=sum(s['period']for s in matched);subset.append(dict(size=n,forward_fold_specific_addresses=[hex(x)for x in fold_addresses],events=len(matched),period=period,timed_period_pct=100*period/sum(s['period']for s in ss),scope='Subset of word_mask_construction, not additive to that group; excludes word load, ordinary mask arithmetic, common constants and byte recheck.'))
(p/'forward-fold-subset.json').write_text(json.dumps(subset,indent=2)+'\n')
