from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;R=P.parents[2];M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete';summary={}
for name,d in M['cases'].items():
 report=json.loads((R/d['snapshot']/'export.json').read_text());functions=[f for data in report['data'] for f in data['functions']]
 selected=[]
 for label in d['counts']:
  f=next(f for f in functions if f['name']==label or f['name'].endswith(':'+label));rows=[]
  for b in f['branches']:
   path=Path(f['filenames'][b[6]]);lines=path.read_text().splitlines();rows.append(dict(line=b[0],column=b[1],file=str(path.relative_to(R)),true=b[4],false=b[5],source=lines[b[0]-1]))
  selected.append(dict(name=label,count=f['count'],branches=rows))
 (P/(name+'-mapped-counts.json')).write_text(json.dumps(selected,indent=2)+'\n')
 def branch(fn,line,col):
  fs=next(f for f in selected if f['name']==fn);return next(b for b in fs['branches'] if b['line']==line and b['column']==col)
 summary[name]=dict(member_cursor_repair=branch('zbtScoreRemoveLeaf',1114,9)['true'],reuse_after_free=branch('zbtScoreRegisterLeaf',803,39)['true'],deferred_free_list_allocations=branch('zbtScoreRegisterLeaf',803,39)['false'],freed_member_cursor=branch('zbtIndexRehashStep',203,34)['true'],member_cursor_fallback=branch('zbtIndexRehashStep',2121,13)['true'],retired_defrag_cursor=branch('zbtreeDefragStep',3143,13)['true'],defrag_tree_reset=branch('zbtreeDefragStep',3133,9)['true'])
 assert summary[name]['freed_member_cursor']==0
assert summary['lifecycle']['member_cursor_repair']==2 and summary['lifecycle']['reuse_after_free']==4 and summary['lifecycle']['deferred_free_list_allocations']==16
assert summary['relocation']['retired_defrag_cursor']==4 and summary['mutation']['retired_defrag_cursor']==256
(P/'summary.json').write_text(json.dumps(dict(status='pass',scope='whole-process execution counts, no timing',observations=summary),indent=2)+'\n')
print(json.dumps(summary,indent=2))
