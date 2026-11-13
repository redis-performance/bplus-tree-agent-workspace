import json,pathlib,sys,statistics
p=pathlib.Path(sys.argv[1]);rows=[json.loads(x) for x in (p/'comparison.jsonl').read_text().splitlines()];meta=json.loads((p/'metadata.json').read_text());out={'rows':len(rows),'variants':{},'blocks':[]}
assert len(rows)==72*len(meta['variants'])
for v,vm in meta['variants'].items():
 cases={};eligible=True
 for case in ['hit','score','miss','long','external','update']:
  rr=[r for r in rows if r['variant']==v and r['case']==case];assert len(rr)==12
  ds=[];ms=[];windows=[]
  for b in range(3):
   r=[x for x in rr if x['block']==b];assert len(r)==4 and [x['label'] for x in r]==list('ABBA') and [x['slot'] for x in r]==list(range(4))
   assert len({x['hits'] for x in r})==1 and len({x['score_sum'] for x in r})==1 and len({x['ops'] for x in r})==1
   assert all(x['binary_sha256']==(meta['baseline_sha256'] if x['label']=='A' else vm['binary_sha256']) for x in r)
   aa=[x for x in r if x['label']=='A'];bb=[x for x in r if x['label']=='B'];d=(statistics.mean(x['elapsed_ns'] for x in bb)/statistics.mean(x['elapsed_ns'] for x in aa)-1)*100
   m=(statistics.mean(x['owned_bytes'] for x in bb)/statistics.mean(x['owned_bytes'] for x in aa)-1)*100;w=min(x['elapsed_ns'] for x in r);ds.append(d);ms.append(m);windows.append(w)
   ok=d<=(-2 if case=='hit' else 1) and m<=1 and w>=250000000;eligible &= ok
   out['blocks'].append({'variant':v,'case':case,'block':b,'delta_pct':d,'memory_delta_pct':m,'min_window_ns':w,'pass':ok})
  cases[case]={'delta_pct':ds,'median_delta_pct':statistics.median(ds),'memory_delta_pct':ms,'min_window_ns':min(windows)}
 out['variants'][v]={'eligible':eligible,'cases':cases}
(p/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['variants'],indent=2))
