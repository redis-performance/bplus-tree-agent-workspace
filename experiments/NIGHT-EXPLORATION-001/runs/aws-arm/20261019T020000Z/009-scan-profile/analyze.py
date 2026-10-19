from pathlib import Path
import json,re,csv,collections,hashlib
p=Path(__file__).resolve().parent;d=p/'profiles';out=p/'analysis';out.mkdir(exist_ok=True)
# Exact half-open offsets relative to physical zbtIndexScanSlot, identified from
# original source-linked assembly, NOT generic parent/child percentages.
ranges={'all_match_including_local_pointer_setup':[(0x1bc,0x238),(0x294,0x540)],'forward_word_loop':[(0x3a0,0x440)],'reversed_folded_word_loop':[(0x2bc,0x34c)],'reversed_ordinary_word_loop':[(0x440,0x4bc)],'scalar_tails':[(0x1e4,0x238),(0x34c,0x3a0),(0x4bc,0x540)],'forward_word_mask_and_fold_select':[(0x3bc,0x3fc)],'forward_word_candidate_recheck':[(0x418,0x430)]}
rows=[];totals={}
for f in sorted(d.glob('*.samples')):
 n=int(re.search('-n(\\d+)-',f.name).group(1));t=totals.setdefault(n,{'events':0,'period':0,'same_ip':collections.Counter(),'same_ip_events':collections.Counter(),'regions_period':collections.Counter(),'regions_events':collections.Counter(),'offsets':collections.defaultdict(lambda:{'events':0,'period':0})});row={'file':f.name,'events':0,'period':0,'regions_events':collections.Counter(),'regions_period':collections.Counter()}
 for block in re.split(r'\n\s*\n',f.read_text().strip()):
  lines=block.splitlines();period=int(lines[0]);frames=[re.match(r'\s*([0-9a-f]+)\s+(.*)',x) for x in lines[1:]];frames=[x for x in frames if x];assert frames;top=frames[0].group(1);same=[x for x in frames if x.group(1)==top]
  t['events']+=1;t['period']+=period;row['events']+=1;row['period']+=period
  names={x.group(2).split('+')[0] for x in same}
  for name in names:t['same_ip'][name]+=period;t['same_ip_events'][name]+=1
  offsets=[int(m.group(1),16) for x in same if (m:=re.match(r'zbtIndexScanSlot\+0x([0-9a-f]+)',x.group(2)))];assert len(offsets)<=1
  if offsets:
   off=offsets[0];t['offsets'][hex(off)]['events']+=1;t['offsets'][hex(off)]['period']+=period
   for name,rs in ranges.items():
    if any(a<=off<b for a,b in rs):t['regions_period'][name]+=period;t['regions_events'][name]+=1;row['regions_period'][name]+=period;row['regions_events'][name]+=1
 rows.append(row)
for t in totals.values():
 t['region_period_pct']={k:100*v/t['period'] for k,v in t['regions_period'].items()};t['same_ip_period_pct']={k:100*v/t['period'] for k,v in t['same_ip'].most_common()}
controls=[]
for n in [100000,1000000]:
 for seed in [1,2,3]:
  case=f'scan-n{n}-s{seed}';r={x:list(csv.DictReader((d/f'{case}-{x}.csv').open())) for x in ['original','disabled','profile']};assert all(len(x)==1 for x in r.values());fields=['case','size','requested_ops','member_bytes','seed','operations','tree_bytes','checksum','traversals','warmup_passes']
  for x in ['disabled','profile']:
   for k in fields:assert r[x][0][k]==r['original'][0][k],(case,x,k)
  assert all(x[0]['cpu_start']=='2' and x[0]['cpu_end']=='2' for x in r.values());controls.append({'case':case,'fields_equal':fields,'metadata':{k:r['original'][0][k] for k in fields},'profile_elapsed_ns':int(r['profile'][0]['elapsed_ns'])})
assert '<not counted>,,cycles:u,0,' in (d/'disabled.stat').read_text()
(out/'profile-summary.json').write_text(json.dumps(totals,indent=2)+'\n');(out/'profile-rows.json').write_text(json.dumps(rows,indent=2)+'\n');(out/'controls.json').write_text(json.dumps({'disabled_control_zero_events':True,'cases':controls},indent=2)+'\n');(out/'ranges.json').write_text(json.dumps({'symbol':'zbtIndexScanSlot','diagnostic_symbol_start':'0x1038c','half_open_relative_ranges':{k:[[hex(a),hex(b)]for a,b in v]for k,v in ranges.items()},'limits':'Includes local pointer/loop setup; excludes earlier leaf-ID assertion, rehash checks, later decoding/hash/callback. Period weights and sample skid are approximate.'},indent=2)+'\n')
print(json.dumps({n:{'events':t['events'],'regions_pct':t['region_period_pct'],'region_events':t['regions_events']}for n,t in totals.items()},indent=2))
