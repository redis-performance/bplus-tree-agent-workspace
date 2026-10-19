from pathlib import Path
import json,datetime,hashlib,itertools
p=Path(__file__).parent;records=json.loads((p/'validation-processes.json').read_text());cells=json.loads((p/'validation-cells.json').read_text());last=None;faults=0
assert len(records)==673
for x in records:
 assert x['returncode']==x['expected_returncode'];a=datetime.datetime.fromisoformat(x['started_utc']);b=datetime.datetime.fromisoformat(x['finished_utc']);assert a<=b
 if last:assert last<=a
 last=b
 if x['expected_returncode']==2:assert 'scan-guard:' in (p/'validation'/(x['tag']+'.stderr')).read_text();faults+=1
assert faults==16
for v in ['base','B']:
 assert len(cells[v])==108
 for mode in ['native','san']:assert '43 passed' in (p/'validation'/f'{v}-{mode}-original-tests.stdout').read_text() and '0 failed, 43 total' in (p/'validation'/f'{v}-{mode}-original-tests.stdout').read_text()
 for tag,cell in cells[v].items():
  c,r=[json.loads(x) for x in (p/'validation'/f'{v}-{tag}-census.stdout').read_text().splitlines()];assert c==cell['census'];assert c['members']==r['n'] and sum(c['tag_histogram'])==r['n']
  for mode in ['native','san']:
   x=json.loads((p/'validation'/f'{v}-{tag}-{mode}.stdout').read_text());assert x==cell['models'][mode] and x['validation']=='pass' and x['passes']==x['elapsed_ns']==0
   for key in ['n','bytes','seed','distribution','order']:assert x[key]==r[key]
   if mode=='native':assert all(x[k]==r[k] for k in ['callbacks_per_pass','checksum_per_pass','tree_bytes'])
  if r['order']==1:assert c['reversed_members']==64 and c['reversed_leaves']>0
  if r['distribution']==1:assert c['tag_histogram'][17]==r['n']
  if r['distribution']==2:assert c['tag_histogram'][0]>0 and c['tag_histogram'][1]>0 and sum(c['tag_histogram'][:2])==r['n']
assert cells['base']==cells['B'];fixtures=json.loads((p/'fixture-manifest.json').read_text());assert len(fixtures)==36
for f in fixtures:assert hashlib.sha256((p/'fixtures'/(f['name']+'.bin')).read_bytes()).hexdigest()==f['sha256']
post=json.loads((p/'post-validation-hashes.json').read_text());assert post['status']=='pass' and post['observed']==json.loads((p/'build-freeze.json').read_text())
result=dict(status='pass',commands=673,serial=True,native_sanitizer_models=432,census_cells=216,source_mode_original_tests=4,tests_each=43,repeated_fault_controls=16,fixture_files=36,post_hashes=24,cross_source_models_and_census_equal=True,cross_allocator_byte_equality=False,timing_windows=0);(p/'validation-audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
