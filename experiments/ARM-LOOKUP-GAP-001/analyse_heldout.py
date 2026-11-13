#!/usr/bin/env python3
import pathlib,json,statistics,sys
p=pathlib.Path(sys.argv[1]);rows=[json.loads(x) for x in (p/'rows.jsonl').read_text().splitlines()];assert len(rows)==96
stage=rows[0]['stage'];assert stage in ['controls','confirm'];out={'stage':stage,'rows':96,'blocks':[],'all_pass':True}
for seed in [29,43]:
 for case in ['hit','score','miss','long']:
  for block in range(3):
   r=[x for x in rows if x['seed']==seed and x['case']==case and x['block']==block];assert len(r)==4 and [x['arm'] for x in r]==list('ABBA')
   assert len({x['hits'] for x in r})==len({x['score_sum'] for x in r})==len({x['owned_bytes'] for x in r})==1
   assert all(x['ops']==50000000 and x['elapsed_ns']>=250000000 for x in r)
   a=statistics.mean(x['elapsed_ns'] for x in r if x['arm']=='A');b=statistics.mean(x['elapsed_ns'] for x in r if x['arm']=='B');d=(b/a-1)*100
   good=abs(d)<=1 if stage=='controls' else d<=(-2 if case=='hit' else 1)
   out['blocks'].append({'seed':seed,'case':case,'block':block,'delta_pct':d,'pass':good});out['all_pass'] &= good
(p/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
