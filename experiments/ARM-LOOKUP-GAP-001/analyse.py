#!/usr/bin/env python3
import json,pathlib,statistics,sys
p=pathlib.Path(sys.argv[1]);rows=[json.loads(l) for l in (p/'aa.jsonl').read_text().splitlines()];assert len(rows)==48
out={'rows':48,'blocks':[],'cases':{},'all_qualified':True}
for case in ['hit','score','miss','long']:
 cr=[r for r in rows if r['case']==case];assert len(cr)==12
 blocks=[]
 for block in range(3):
  rs=[r for r in cr if r['block']==block];assert len(rs)==4 and [r['label'] for r in rs]==list('ABBA')
  assert len({r['owned_bytes'] for r in rs})==1 and len({r['hits'] for r in rs})==1 and len({r['score_sum'] for r in rs})==1 and all(r['ops']==50000000 for r in rs)
  a=statistics.mean(r['elapsed_ns'] for r in rs if r['label']=='A');b=statistics.mean(r['elapsed_ns'] for r in rs if r['label']=='B');delta=(b/a-1)*100
  ok=abs(delta)<=1 and all(r['elapsed_ns']>=250000000 for r in rs)
  x={'case':case,'block':block,'delta_pct':delta,'qualified':ok,'min_window_ns':min(r['elapsed_ns'] for r in rs)};blocks.append(x);out['blocks'].append(x)
 out['cases'][case]={'qualified_blocks':sum(b['qualified'] for b in blocks),'total_blocks':3,'median_ns_per_lookup':statistics.median(r['elapsed_ns']/r['ops'] for r in cr),'range_ns_per_lookup':[min(r['elapsed_ns']/r['ops'] for r in cr),max(r['elapsed_ns']/r['ops'] for r in cr)],'owned_bytes':cr[0]['owned_bytes']}
 out['all_qualified'] &= all(b['qualified'] for b in blocks)
(p/'aa-analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
