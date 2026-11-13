#!/usr/bin/env python3
import json,pathlib,statistics,sys
p=pathlib.Path(sys.argv[1]);rs=[json.loads(x) for x in (p/'rows.jsonl').read_text().splitlines()];assert len(rs)==144
out={'rows':len(rs),'variants':{},'effects':[]}
for v in 'ABC':
 cells={}
 for case in ['hit','score','miss','long']:
  effects=[];checks=[]
  for b in range(3):
   block=[r for r in rs if r['variant']==v and r['case']==case and r['block']==b]
   assert len(block)==4 and [r['arm'] for r in block]==list('ABBA')
   assert len({r['hits'] for r in block})==1 and len({r['score_sum'] for r in block})==1 and len({r['owned_bytes'] for r in block})==1 and all(r['ops']==50000000 and r['elapsed_ns']>=250000000 for r in block)
   a=statistics.mean(r['elapsed_ns'] for r in block if r['arm']=='A');c=statistics.mean(r['elapsed_ns'] for r in block if r['arm']=='B')
   d=(c/a-1)*100;effects.append(d);out['effects'].append({'variant':v,'case':case,'block':b,'delta_pct':d})
  cells[case]={'effects_pct':effects,'median_pct':statistics.median(effects),'min_pct':min(effects),'max_pct':max(effects)}
 eligible=all(d<=-2 for d in cells['hit']['effects_pct']) and all(d<=1 for c in ['score','miss','long'] for d in cells[c]['effects_pct'])
 out['variants'][v]={'cases':cells,'eligible_for_confirmation':eligible}
(p/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['variants'],indent=2))
