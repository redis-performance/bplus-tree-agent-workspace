from pathlib import Path
import json,re
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
# Fixed source/column mappings preregistered before captures.
map=[('narrow_wide_read','zbtIndexGetId',1775,9),('resize_finish','zbtIndexRehashStep',2123,13),('active_scan','zbtreeScan',4335,9),('active_clone','zbtreeDup',2901,9),('active_defrag_start','zbtreeDefragStart',3027,9),('declined_plain','zbtDefragPlainAllocation',3004,9),('declined_node','zbtDefragScoreNode',3052,9),('leaf_move','zbtDefragScoreNode',3061,9)]
result={}
for name in M['cases']:
 fs=json.loads((P/(name+'-counts.json')).read_text());vals={}
 for label,fn,line,col in map:
  f=next(x for x in fs if x['name']==fn);bs=[b for b in f['branches'] if b['start_line']==line and b['start_column']==col and b['file']=='src/zset_btree.c'];assert len(bs)==1,(name,label,bs)
  vals[label]=dict(true=bs[0]['true'],false=bs[0]['false'])
 assert vals['narrow_wide_read']['true']>0 and vals['narrow_wide_read']['false']>0
 assert vals['active_scan']['true']>0 and vals['resize_finish']['true']>0
 if name=='mode0':assert vals['active_clone']['true']>0
 if name in ['mode1','mode2']:assert vals['active_defrag_start']['true']>0 and vals['leaf_move']['true']>0
 if name=='mode2':assert vals['declined_plain']['true']>0 and vals['declined_node']['true']>0
 output=(P/(name+'-capture.stdout')).read_text();line=next(s for s in output.splitlines() if s.startswith('PASS '));fields=dict(re.findall(r'(\w+)=([^ ]+)',line));assert int(fields['active'])>0
 vals['pass_line']=line;result[name]=vals
(P/'summary.json').write_text(json.dumps(dict(status='pass',captures=4,scope='whole-oracle execution counts, not timed-loop hotness',observations=result),indent=2)+'\n');print('PASS four fixed reachability captures')
