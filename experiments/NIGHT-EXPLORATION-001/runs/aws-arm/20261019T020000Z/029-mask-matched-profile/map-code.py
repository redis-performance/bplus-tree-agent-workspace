#!/usr/bin/env python3
import argparse,collections,hashlib,json,pathlib,re
p=argparse.ArgumentParser();p.add_argument('results',type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);p.add_argument('--variant',required=True,choices=['control','A']);a=p.parse_args();r=a.results;prefix=a.variant+'-'

from arm_asm import parse
assemblies={name:parse(r/(prefix+name+'-full-asm.stdout')) for name in ['profile','original','timing']};groups={};samples={};rows={};hot=collections.Counter()
for file in sorted(r.glob(prefix+'iterate-*-samples.stdout')):
 case,n,seed=re.match(r'(iterate)-n(\d+)-s(\d+)',file.name[len(prefix):]).groups();key=case+'/'+n;g=groups.setdefault(key,dict(total_period=0,events=0,mapped_equal_period=0,mapped_equal_events=0,mapped_different_period=0,mapped_different_events=0,missing_period=0,missing_events=0,tree_equal_period=0,tree_equal_events=0,tree_different_period=0,tree_different_events=0,tree_missing_period=0,tree_missing_events=0));samples[key]=[]
 for block in re.split(r'\n\s*\n',file.read_text().strip()):
  lines=block.splitlines();period=int(lines[0].strip());frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',line) for line in lines[1:]];frames=[f for f in frames if f];assert frames;top=frames[0][1];same=[f[2] for f in frames if f[1]==top];physical=next((f for f in reversed(same) if '(inlined)' not in f),same[-1]);m=re.match(r'(.+?)\+0x([0-9a-f]+)$',physical);g['total_period']+=period;g['events']+=1;category='missing'
  if m:
   symbol,off=m[1],int(m[2],16);ins={name:data.get(symbol,{}).get('instructions',{}).get(off) for name,data in assemblies.items()}
   if all(ins.values()):
    equal=len({tuple(v['bytes']) for v in ins.values()})==1;category='mapped_equal' if equal else 'mapped_different';rk=symbol+'+'+hex(off);entry=rows.setdefault(rk,dict(symbol=symbol,relative_offset=hex(off),all_three_encoded_bytes_equal=equal,source_lines={k:v['source_line'] for k,v in ins.items()},addresses={k:hex(assemblies[k][symbol]['start']+off) for k in ins},bytes={k:' '.join(v['bytes']) for k,v in ins.items()},assembly={k:v['assembly'] for k,v in ins.items()},events=0,period=0));entry['events']+=1;entry['period']+=period
    if symbol.startswith('zbt'):
     g['tree_equal_period' if equal else 'tree_different_period']+=period;g['tree_equal_events' if equal else 'tree_different_events']+=1;hot[symbol]+=period
  if m and m[1].startswith('zbt') and category=='missing':g['tree_missing_period']+=period;g['tree_missing_events']+=1
  g[category+'_period']+=period;g[category+'_events']+=1
assert len(groups)==2 and set(groups)=={'iterate/100000','iterate/1000000'}
for name,data in assemblies.items():
 assert data.get('zbtreeIteratorNext',{}).get('instructions'),name
fullbody={}
for symbol in ['zbtreeIteratorNext']:
 offsets=set().union(*(set(data[symbol]['instructions']) for data in assemblies.values()));difference=[]
 for off in sorted(offsets):
  entries={name:data[symbol]['instructions'].get(off) for name,data in assemblies.items()}
  if any(x is None for x in entries.values()) or len({tuple(x['bytes']) for x in entries.values() if x})!=1:
   difference.append(dict(offset=hex(off),entries=entries))
 fullbody[symbol]=dict(offset_entries=len(offsets),different_entries=len(difference),differences=difference)
for g in groups.values():
 for k in ['mapped_equal','mapped_different','missing','tree_equal','tree_different']:g[k+'_period_pct']=100*g[k+'_period']/g['total_period']
result={'status':'mapped','variant':a.variant,'all_sampled_tree_bytes_match_actual':all(g['tree_equal_events']>0 and g['tree_different_events']==0 and g['tree_missing_events']==0 for g in groups.values()),'raw_assembly_sha256':{n:hashlib.sha256((r/(prefix+n+'-full-asm.stdout')).read_bytes()).hexdigest() for n in assemblies},'actual_timing_binary_sha256':json.loads((pathlib.Path(__file__).parent/'expected.json').read_text())['timing_binaries'][a.variant]['sha256'],'groups':groups,'hot_physical_tree_functions':hot.most_common(),'sampled_instruction_map':rows,'full_tree_body_comparison':fullbody,'limits':['Maps sampled physical instruction offsets, not full-callchain cost','Encoded differences include relocation and actual driver/body differences; none silently normalized','Unmapped/library/unknown samples remain in denominators','Same source function offset alone does not prove code equivalence; only exact-byte rows count as matched','Code equality does not establish equal runtime/cache layout or removable cycles']};a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'groups':groups,'hot':hot.most_common(12)},indent=2))
