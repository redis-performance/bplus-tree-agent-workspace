#!/usr/bin/env python3
import argparse,collections,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);a=p.parse_args();r=a.results;mapping=json.loads((r/'code-mapping.json').read_text())['sampled_instruction_map'];groups={}
for n in [100000,1000000]:
 total=0;events=0;periods=collections.Counter();counts=collections.Counter();instructions=collections.defaultdict(collections.Counter);instcounts=collections.defaultdict(collections.Counter);reference_chains=collections.Counter();reference_chain_events=collections.Counter()
 for file in sorted(r.glob(f'update-n{n}-s*-samples.stdout')):
  for block in re.split(r'\n\s*\n',file.read_text().strip()):
   lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',line) for line in lines[1:]];frames=[f for f in frames if f];assert frames;top=frames[0][1];same=[f[2] for f in frames if f[1]==top];names={s.split('+')[0] for s in same};physical=next((s for s in reversed(same) if '(inlined)' not in s),same[-1]);symbol=physical.split('+')[0];category='other'
   if 'zbtIndexTableFindReference' in names:category='reference-search'
   elif symbol=='zbtIndexMove' and 'zbtIndexSetId' in names:category='set-id-in-move'
   elif symbol=='zbtIndexMove':category='move-other'
   elif 'zbtIndexSetId' in names:category='set-id-outside-move'
   if category=='reference-search':
    chain=tuple(f[2].split('+')[0] for f in frames if f[1]!=top and '(inlined)' not in f[2]);reference_chains[chain]+=period;reference_chain_events[chain]+=1
   total+=period;events+=1;periods[category]+=period;counts[category]+=1;instructions[category][physical]+=period;instcounts[category][physical]+=1
 cells={}
 for category in ['reference-search','set-id-in-move','move-other','set-id-outside-move','other']:
  top=[]
  for physical,value in instructions[category].most_common(8):
   entry=mapping.get(physical,{});top.append(dict(physical=physical,period=value,events=instcounts[category][physical],operation_period_pct=100*value/total,category_period_pct=100*value/periods[category],all_three_bytes_equal=entry.get('all_three_encoded_bytes_equal'),source_line=entry.get('source_lines',{}).get('profile'),assembly=entry.get('assembly',{}).get('profile')))
  cells[category]=dict(period=periods[category],events=counts[category],operation_period_pct=100*periods[category]/total,top_instructions=top)
 assert sum(v['period'] for v in cells.values())==total and sum(v['events'] for v in cells.values())==events;groups[str(n)]=dict(total_period=total,events=events,categories=cells,reference_callchains=[dict(chain=list(k),period=v,events=reference_chain_events[k],reference_period_pct=100*v/periods['reference-search'],operation_period_pct=100*v/total) for k,v in reference_chains.most_common()])
result=dict(status='partitioned',groups=groups,classification='disjoint top-IP inline/physical symbols; callers at other IPs excluded',source_selection='NONE',limits=['A store-successor branch sample does not establish branch cost or removable store latency','Reference-search category is total sampled code in that helper, not a measured redundant-work fraction','No saved bucket pointer stability or new proposal is established by this profile','Existing correctness invariants and resize/migration lifecycle remain mandatory']);a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({n:{k:dict(events=v['events'],pct=v['operation_period_pct']) for k,v in g['categories'].items() if k!='other'} for n,g in groups.items()},indent=2))
