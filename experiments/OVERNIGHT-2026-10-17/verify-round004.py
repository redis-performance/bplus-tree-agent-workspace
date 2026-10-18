"""Read-only sequential audit, separate from run/analysis code; no timing work."""
from pathlib import Path
import csv,json,hashlib,math,statistics
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def data(path):return json.loads(path.read_text())
def checksum(path,want):assert sha(path)==want,path
old=data(P/'HARNESS-001/freeze.json')
for name,h in old['files'].items():
 if name.startswith(('src/','compat/','vendor/','bench/')):checksum(R/name,h)
for folder in ['HARNESS-002','PROFILE-002','DIAG-006']:
 f=data(P/folder/'freeze.json');B=R/f['snapshot']
 for name,h in f['files'].items():checksum(B/name,h)
 for name in ['src/zset_btree.c','src/zset_btree.h']:assert f['files'][name]==old['files'][name]
for name,h in data(P/'HARNESS-002/validation-freeze.json')['files'].items():checksum(R/name,h)
for folder in ['HARNESS-002','DIAG-006']:
 for row in data(P/folder/'validation.json'):
  assert row['returncode']==0
  for field in ['stdout','stderr']:checksum(P/folder/row[field],row[field+'_sha256'])
for row in data(P/'PROFILE-002/validation.json'):
 assert row['returncode']==0
 for field in ['stdout','stderr']:checksum(R/row[field],row[field+'_sha256'])
 if row['name'] in ['calibrate-1000','calibrate-3001']:
  assert row['criterion_met'] and row['samples']>=20 and row['known_arithmetic']/row['samples']>=.9
for folder in ['BOUNDARY-007','BOUNDARY-008']:
 m=data(P/folder/'manifest.json');B=R/m['snapshot'];assert m['status']=='pass'
 for name,h in m['sources'].items():checksum(B/name,h)
 for row in m['runs']:
  assert row['returncode']==0
  for field in ['stdout','stderr']:checksum(P/folder/(row['name']+'.'+field),row[field+'_sha256'])
  if row['name'].endswith('-run'):assert 'PASS cases=' in (P/folder/(row['name']+'.stdout')).read_text()
 for row in data(P/folder/'faults.json'):
  assert (row['returncode']==0) == (row['step']=='build')
  for field in ['stdout','stderr']:checksum(P/folder/row[field],row[field+'_sha256'])
  checksum(R/row['cwd']/'src/zset_btree.c',row['source_sha256'])
  if row['step']=='run':assert 'line=' in (P/folder/row['stderr']).read_text()
print('PASS root/snapshot/validation/boundary/fault hashes')

def interval(effects):
 avg=sum(effects)/len(effects)
 sd=(sum((x-avg)**2 for x in effects)/(len(effects)-1))**.5
 half=2.5705818366147395*sd/math.sqrt(6)
 return avg,avg-half,avg+half
# Verify fixed A/A schedule and recompute intervals directly from raw integer wall clocks.
m=data(P/'AA-003/manifest.json');assert m['status']=='complete' and len(m['runs'])==96 and len(m['warmup'])==1
checksum(P/'AA-003/PLAN.md',m['plan_sha256']);checksum(P/'AA-003/run.py',m['runner_sha256']);checksum(R/m['binary'],m['binary_sha256']);assert m['binary_sha256']==m['binary_sha256_after']
schedule=[];cells=m['cells']
for b in range(1,7):
 offset=(b-1)%4
 for cell in cells[offset:]+cells[:offset]:
  for step,label in enumerate('ABBA',1):schedule.append((b,cell[0],step,label))
assert [(r['block'],r['cell'],r['step'],r['label']) for r in m['runs']]==schedule
for r in m['warmup']+m['runs']:
 assert r['returncode']==0
 for field in ['csv','stderr']:checksum(P/'AA-003'/r[field],r[field+'_sha256'])
for summary in data(P/'AA-003/summary.json'):
 rr=[]
 for run in m['runs']:
  if run['cell']!=summary['cell']:continue
  rows=list(csv.DictReader((P/'AA-003'/run['csv']).open()));assert len(rows)==1;r=rows[0]
  assert r['seed']=='503' and r['query_seed']=='701' and r['query_order']=='independent'
  n=int(r['size']);ops=int(r['operations']);expected=ops*(n-1)//2 if r['case']=='lookup-hit' else 0
  assert int(r['checksum'])==expected
  rr.append((run,r))
 effects=[]
 for b in range(1,7):
  aa=[int(r['elapsed_ns'])/int(r['operations']) for run,r in rr if run['block']==b and run['label']=='A']
  bb=[int(r['elapsed_ns'])/int(r['operations']) for run,r in rr if run['block']==b and run['label']=='B']
  assert len(aa)==len(bb)==2;effects.append(100*(sum(bb)/sum(aa)-1))
 avg,lo,hi=interval(effects)
 for a,b in [(avg,summary['aa_mean_pct']),(lo,summary['ci95_low_pct']),(hi,summary['ci95_high_pct'])]:assert abs(a-b)<1e-9
 stable=all(len({r[k] for _,r in rr})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint','query_fingerprint'])
 good=stable and len(rr)==24 and min(int(r['elapsed_ns']) for _,r in rr)>=10000000 and lo>=-1 and hi<=1
 assert good==summary['qualified'] and not good
print('PASS AA-003 complete schedule/all raw rows/recomputed PARK')
# Verify capture rows, sample counts and symbolication coverage.
m=data(P/'PROFILE-002/manifest.json');assert m['status']=='complete' and len(m['runs'])==12
checksum(P/'PROFILE-002/PLAN.md',m['plan_sha256']);checksum(R/m['binary'],m['binary_sha256'])
want=[(seed,interval,case,size,ops) for seed in [503,809] for interval in [1000,3001] for case,size,ops in [('lookup-hit',16,50000000),('lookup-hit',320,10000000),('rank',16,10000000)]]
assert [(r['seed'],r['interval_usec'],r['case'],r['member_bytes'],r['operations']) for r in m['runs']]==want
summaries={r['name']:r for r in data(P/'PROFILE-002/summary.json')}
for run in m['runs']:
 assert run['returncode']==0
 for f in ['stdout','stderr']:checksum(R/run[f],run[f+'_sha256'])
 rows=list(csv.reader((R/run['stderr']).open()));h=[r for r in rows if r[0]=='PROFILE'];pcs=[r for r in rows if r[0]=='PC'];s=summaries[run['name']]
 assert len(h)==1 and h[0][4]=='0' and int(h[0][3])==len(pcs)==s['samples']>=100
 assert sum(s['counts'].values())==sum(s['locations'].values())==len(pcs) and s['unknown']==0
for cmd in data(P/'PROFILE-002/symbolication.json'):
 assert cmd['returncode']==0
 for f in ['stdout','stderr']:checksum(R/cmd[f],cmd[f+'_sha256'])
print('PASS PROFILE-002 fixed captures, sample/symbol conservation')
# Diagnostic effects from fixed ABBA off/on raw values.
m=data(P/'DIAG-006/manifest.json');assert m['status']=='complete' and len(m['runs'])==48
checksum(P/'DIAG-006/PLAN.md',m['plan_sha256']);checksum(R/m['binary'],m['binary_sha256'])
want=[(b,size,slot,label) for b in range(1,7) for size in ([16,320] if b%2 else [320,16]) for slot,label in enumerate('ABBA')]
assert [(r['block'],r['member_bytes'],r['slot'],r['label']) for r in m['runs']]==want
for s in data(P/'DIAG-006/summary.json'):
 rr=[]
 for run in m['runs']:
  if run['member_bytes']!=s['member_bytes']:continue
  assert run['returncode']==0;checksum(P/'DIAG-006'/run['csv'],run['csv_sha256']);checksum(R/run['stderr'],run['stderr_sha256'])
  row=next(csv.DictReader((P/'DIAG-006'/run['csv']).open()));profile=list(csv.reader((R/run['stderr']).open()));head=[r for r in profile if r[0]=='PROFILE'];pc=[r for r in profile if r[0]=='PC']
  assert len(head)==1 and head[0][4]=='0' and int(head[0][3])==len(pc)
  assert len(pc)==0 if run['label']=='A' else len(pc)>=50
  assert int(row['checksum'])==int(row['operations'])*99999//2
  rr.append((run,row))
 effects=[]
 for b in range(1,7):
  a=[int(row['elapsed_ns']) for run,row in rr if run['block']==b and run['label']=='A'];bb=[int(row['elapsed_ns']) for run,row in rr if run['block']==b and run['label']=='B'];effects.append(100*(sum(bb)/sum(a)-1))
 avg,lo,hi=interval(effects)
 for x,y in [(avg,s['mean_pct']),(lo,s['ci95_low_pct']),(hi,s['ci95_high_pct'])]:assert abs(x-y)<1e-9
 assert s['criterion_met']==(lo>=-5 and hi<=5 and s['invariants'] and s['min_wall_ns']>=100000000)
print('PASS DIAG-006 fixed schedule/all rows/recomputed bounded-perturbation result')
print('PASS round004 read-only sequential audit; not independent performance confirmation')
