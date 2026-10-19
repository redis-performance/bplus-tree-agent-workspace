"""Synthetic parser/fixture tests only; no benchmark timings or runner work."""
import csv,io,json,copy
from native_common import HERE,CELLS,ORACLE,check_row,same_semantics
s=json.loads((HERE/'schedules.json').read_text());assert len(s['native-AA'])==len(s['native-comparison'])==144;tests=[]
def text(z):
 f=io.StringIO();w=csv.DictWriter(f,fieldnames=z);w.writeheader();w.writerow(z);return f.getvalue()
for contract in [s['native-AA'][0],s['native-AA'][8],s['native-AA'][16]]:
 c=CELLS[contract['cell']];n=c['size'];t=c['requested_ops']//n;ref=ORACLE[f'{n}/{contract["seed"]}'];checksum=(ref[c['frontend']+'_one_traversal_checksum']*t)&((1<<64)-1)
 row=dict(case='iterate' if c['frontend']=='primary' else 'iterator-modes',size=n,seed=contract['seed'],requested_ops=c['requested_ops'],member_bytes=16,operations=t*n,traversals=t,checksum=checksum,warmup_passes=c['warmup_passes'],cpu_start=2,cpu_end=2,elapsed_ns=20000000,thread_elapsed_ns=19000000,tree_bytes=123456,warmup_elapsed_ns=10000000)
 if c['frontend']=='h4':row.update(direction=c['direction'],mask=4,encoding='integer',expected_checksum=checksum,construction_fingerprint=ref['h4_construction_fingerprint'])
 check_row(text(row),contract);tests.append(contract['cell']+'-positive')
 for field in ['seed','checksum','operations','warmup_passes','cpu_end']:
  bad=dict(row);bad[field]=int(bad[field])+1
  try:check_row(text(bad),contract)
  except AssertionError:tests.append(contract['cell']+'-detect-'+field)
  else:raise AssertionError('fault escaped '+field)
 for field in ['direction','mask','encoding','construction_fingerprint']:
  if field not in row:continue
  bad=dict(row);bad[field]='incorrect'
  try:check_row(text(bad),contract)
  except AssertionError:tests.append(contract['cell']+'-detect-'+field)
  else:raise AssertionError('fault escaped '+field)
r=dict(scope='synthetic local parser checks, not measured rows',status='PASS',checks=len(tests),tests=tests);(HERE/'NATIVE-LOCAL-CHECKS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
