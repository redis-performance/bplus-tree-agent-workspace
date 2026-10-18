from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete' and len(M['captures'])==16;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
for c in M['captures']:
 assert sha(R/c['counts'])==c['counts_sha256'];f=json.loads((R/c['counts']).read_text());rows.append((c,{x['name']:x for x in f}))
def signature(f):return dict(count=f['count'],branches=[dict(source=b['source'],true=b['true'],false=b['false']) for b in f['branches']])
comparisons=[]
for seed in [83103,83111]:
 rs=[(c,f) for c,f in rows if c['seed']==seed];base=next(f for c,f in rs if c['variant']=='control-on' and c['batch']==1)
 for c,f in rs:
  equal={n:signature(f[n])==signature(base[n]) for n in ['zbtIndexFind','zbtScoreLeafFindMember','dictGenHashFunction','siphash']};comparisons.append(dict(seed=seed,variant=c['variant'],batch=c['batch'],counts_equal=equal,leaf_calls=f['zbtScoreLeafFindMember']['count'],index_calls=f['zbtIndexFind']['count'],api_calls=f['zbtreeScores']['count']))
 assert len({c['tree_bytes'] for c,f in rs})==1
for v in ['C-on','C-off']:
 for seed in [83103,83111]:
  fs=[f['zbtInlineTagSearch'] for c,f in rows if c['variant']==v and c['seed']==seed];assert len(fs)==2;comparisons.append(dict(seed=seed,variant=v,helper_batch_counts_equal=signature(fs[0])==signature(fs[1])))
all_equal=all(all(x.get('counts_equal',{}).values()) and x.get('helper_batch_counts_equal',True) for x in comparisons)
out=dict(status='complete',captures=16,scope_control=M['calibration']['counts'],all_compared_logical_counts_equal=all_equal,comparisons=comparisons,source_selection='NONE',scope='dynamic logical executions, not cycles or time shares')
(P/'summary.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
