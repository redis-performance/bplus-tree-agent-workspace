"""Read-only coordinator audit; no measured children or independent confirmation."""
from pathlib import Path
import csv,json,hashlib,statistics,math
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name in ['HARNESS-001','DIAG-003','DIAG-004','DIAG-005','COUNTERS-002']:
 f=json.loads((P/name/'freeze.json').read_text());B=R/f['snapshot']
 for path,h in f['files'].items():assert sha(B/path)==h,(name,path)
 if name=='HARNESS-001':
  for path,h in f['files'].items():assert sha(R/path)==h,('root referee changed',path)
 print(name,'snapshot integrity PASS')
for name,expected_processes,expected_rows in [('DIAG-003',6,24),('DIAG-004',48,48),('DIAG-005',48,48)]:
 d=P/name;m=json.loads((d/'manifest.json').read_text());summary=json.loads((d/'summary.json').read_text())
 assert m['status']=='complete' and len(m['runs'])==expected_processes
 assert sha(d/'PLAN.md')==m['plan_sha256'] and sha(d/'run.py')==m['runner_sha256']
 assert sha(R/m['binary'])==m['binary_sha256']==m['binary_sha256_after']
 rows=[];last_end=None
 for run in m['runs']:
  assert run['returncode']==0 and run['elapsed_seconds']<=120
  if last_end:assert last_end<=run['started_utc']
  last_end=run['ended_utc']
  for out in ['csv','stderr']:assert sha(d/run[out])==run[out+'_sha256']
  data=list(csv.DictReader((d/run['csv']).open()));assert len(data)==(4 if name=='DIAG-003' else 1)
  for row in data:
   n=int(row['size']);ops=int(row['operations']);assert n==100000 and ops%n==0
   assert int(row['checksum'])==n*(n-1)//2*(ops//n)
   assert int(row['elapsed_ns'])>=10000000
   rows.append((run,row,int(row['elapsed_ns'])/ops))
 assert len(rows)==expected_rows
 ratios=[]
 for b in range(1,7):
  block=[x for x in rows if x[0]['block']==b]
  if name=='DIAG-003':
   assert ''.join(x[1]['arm'] for x in block)==('RIIR' if b%2 else 'IRRI')
   values={a:[x[2] for x in block if x[1]['arm']==a] for a in 'RI'}
   ratio=(sum(values['R'])/2)/(sum(values['I'])/2)
  elif name=='DIAG-004':
   for size in [16,320]:
    group=[x for x in block if int(x[1]['member_bytes'])==size]
    assert ''.join(x[0]['arm'] for x in group)==('ABBA' if b%2 else 'BAAB')
   values={a:[x[2] for x in block if x[0]['arm']==a and int(x[1]['member_bytes'])==16] for a in 'AB'}
   ratio=(sum(values['A'])/2)/(sum(values['B'])/2)
  else:
   first=['AS','BS','BI','AI'] if b%2 else ['AI','BI','BS','AS']
   assert [x[0]['cell'] for x in block]==first+list(reversed(first))
   values={c:sum(x[2] for x in block if x[0]['cell']==c)/2 for c in first}
   ratio=(values['AS']/values['BS'])/(values['AI']/values['BI'])
  ratios.append(ratio)
 median=statistics.median(ratios)
 field={'DIAG-003':'median_ratio_R_I','DIAG-004':'primary_median_ratio_A_B','DIAG-005':'median_interaction'}[name]
 assert math.isclose(median,summary[field],abs_tol=1e-12)
 criterion=(median>=1.10 and sum(r>1 for r in ratios)>=5) if name=='DIAG-005' else (median<=(.98 if name=='DIAG-003' else .95) and sum(r<1 for r in ratios)>=5)
 assert criterion==summary['criterion_met']
 for row in json.loads((d/'validation.json').read_text()):assert row['returncode']==0
 print(name,'raw hashes/counts/checksums, fixed schedule, independently recomputed criterion PASS')
for name in ['BOUNDARY-005','BOUNDARY-006']:
 d=P/name;versions=[d,d/'attempt2',d/'attempt3'] if name=='BOUNDARY-005' else [d]
 for v in versions:
  m=json.loads((v/'manifest.json').read_text());B=R/m['snapshot']
  for path,h in m['sources'].items():assert sha(B/path)==h
  expected_failure=name=='BOUNDARY-005' and v!=d/'attempt3'
  for run in m['runs']:
   assert run['returncode']==(-6 if expected_failure and run['name']=='release-run' else 0)
   for out in ['stdout','stderr']:assert sha(v/(run['name']+'.'+out))==run[out+'_sha256']
   if 'binary_sha256' in run:assert sha(B/run['command'][0])==run['binary_sha256']
 latest=versions[-1];m=json.loads((latest/'manifest.json').read_text());assert m['status']=='pass'
 oracle='index_probe_oracle.c' if name=='BOUNDARY-005' else 'bulk_delete_oracle.c'
 assert sha(R/'tests'/oracle)==m['sources']['tests/'+oracle]
 for mutant in json.loads((d/'mutations/manifest.json').read_text()):
  assert mutant['runs'][0]['returncode']==0 and mutant['runs'][1]['returncode']==-6
  B=R/mutant['snapshot'];assert sha(B/'fault-test')==mutant['binary_sha256']
  assert sha(B/'src/zset_btree.c')==mutant['source_sha256']
  assert sha(d/'mutations'/(mutant['name']+'.patch'))==mutant['patch_sha256']
  for run in mutant['runs']:
   for out in ['stdout','stderr']:assert sha(d/'mutations'/(mutant['name']+'-'+run['step']+'.'+out))==run[out+'_sha256']
 print(name,'all retained attempts, final tests and fault controls PASS')
d=P/'COUNTERS-002';m=json.loads((d/'manifest.json').read_text());assert m['status']=='complete'
assert sha(d/'PLAN.md')==m['plan_sha256'] and m['binary_sha256']==m['binary_sha256_after']
for run in m['runs']:
 assert run['returncode']==0 and all(run['assertions'].values())
 for filename,h in run['outputs'].items():assert sha(d/run['cell']/filename)==h
 raw=R/run['raw'];assert sha(raw)==run['raw_sha256']
 assert sha(raw.with_suffix('.profdata'))==run['data_sha256'] and sha(raw.with_suffix('.json'))==run['export_sha256']
for a in 'AB':
 s=json.loads((d/(a+'S')/'tree-counts.json').read_text());i=json.loads((d/(a+'I')/'tree-counts.json').read_text());assert s==i
print('COUNTERS-002 raw captures, all tree region/branch/function comparisons PASS')
print('PASS: read-only sequential coordinator audit, not independent performance confirmation')
