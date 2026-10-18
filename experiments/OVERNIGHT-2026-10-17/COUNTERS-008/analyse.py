from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete';observed={}
for name in ['singleton','batch','scan']:
 path=P/(name+'-counts.json');assert hashlib.sha256(path.read_bytes()).hexdigest()==M['cases'][name]['counts_sha256']
 fs={f['name']:f for f in json.loads(path.read_text())}
 def branch(fn,line,col):
  bs=[b for b in fs[fn]['branches'] if b['start_line']==line and b['start_column']==col and b['file']=='src/zset_btree.c'];assert len(bs)==1;return bs[0]['true']
 observed[name]=dict(natural_wrap=branch('zbtIndexStartResize',2075,9),active_batch_flush=branch('zbtreeAppendBatchFlush',3426,9),active_scan=branch('zbtreeScan',4335,9),displaced_slot=branch('zbtIndexScanSlot',4170,9),multiple_leaf_tags=branch('zbtIndexScanSlot',4207,13),probe_reach_rejection=branch('zbtIndexScanSlot',4212,30),scanned_slot_calls=fs['zbtIndexScanSlot']['count'])
assert observed['singleton']['natural_wrap']==2 and observed['batch']['natural_wrap']==4
assert observed['singleton']['active_batch_flush']==2 and observed['batch']['active_batch_flush']==6
assert observed['scan']['active_scan']==256 and all(observed['scan'][k]>0 for k in ['displaced_slot','multiple_leaf_tags','probe_reach_rejection'])
(P/'summary.json').write_text(json.dumps(dict(status='pass',scope='whole-oracle execution counts, not CPU time',observations=observed),indent=2)+'\n');print(json.dumps(observed,indent=2))
