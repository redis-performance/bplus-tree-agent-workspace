import json,pathlib,sys,statistics
p=pathlib.Path(sys.argv[1]);rows=[json.loads(x) for x in (p/'aa.jsonl').read_text().splitlines()];assert len(rows)==144
out={'rows':144,'cohorts':{},'blocks':[]}
for cohort in ['native','gcc15-lto']:
 cs={};ok=True
 for case in ['hit','score','miss','long','external','update']:
  rr=[r for r in rows if r['cohort']==cohort and r['case']==case];assert len(rr)==12
  effects=[];passes=[]
  for b in range(3):
   r=[x for x in rr if x['block']==b];assert len(r)==4 and [x['label'] for x in r]==list('ABBA');assert len({x['owned_bytes'] for x in r})==1 and len({x['hits'] for x in r})==1 and len({x['score_sum'] for x in r})==1
   a=statistics.mean(x['elapsed_ns'] for x in r if x['label']=='A');c=statistics.mean(x['elapsed_ns'] for x in r if x['label']=='B');d=(c/a-1)*100;passed=abs(d)<=1 and all(x['elapsed_ns']>=250000000 for x in r);effects.append(d);passes.append(passed);out['blocks'].append({'cohort':cohort,'case':case,'block':b,'delta_pct':d,'pass':passed,'min_window_ns':min(x['elapsed_ns'] for x in r)})
  cs[case]={'effects_pct':effects,'all_pass':all(passes),'median_ns_op':statistics.median(x['elapsed_ns']/x['ops'] for x in rr),'owned_bytes':rr[0]['owned_bytes']};ok &= all(passes)
 out['cohorts'][cohort]={'all_pass':ok,'cases':cs}
(p/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['cohorts'],indent=2))
