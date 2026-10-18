from pathlib import Path
import json
P=Path(__file__).resolve().parent;M=json.loads((P/'manifest.json').read_text());assert M['status']=='complete'
result={}
for name in ['external','narrow']:
 fs=json.loads((P/(name+'-counts.json')).read_text());counts={f['name']:f['count'] for f in fs};text=(P/(name+'-capture.stdout')).read_text();assert 'PASS seed=' in text
 if name=='external':
  f=next(f for f in fs if f['name']=='zbtDefragExternalMember');bs=[b for b in f['branches'] if b['file']=='src/zset_btree.c' and b['start_line']==3089 and b['start_column']==9];assert len(bs)==1;assert bs[0]['true']>0 and bs[0]['false']>0;assert counts['zbtDefragExternalMember']>0
  result[name]=dict(external_calls=counts['zbtDefragExternalMember'],accepted=bs[0]['true'],declined=bs[0]['false'])
 else:
  assert counts['zbtScoreRenumberLeaves']>0 and counts['zbtIndexRebuild']>0;assert 'NARROW seed=' in text
  result[name]=dict(renumber=counts['zbtScoreRenumberLeaves'],rebuild=counts['zbtIndexRebuild'])
 result[name]['pass_line']=next(s for s in text.splitlines() if s.startswith('PASS '))
(P/'summary.json').write_text(json.dumps(dict(status='pass',captures=2,observations=result),indent=2)+'\n');print('PASS two additive reachability captures')
