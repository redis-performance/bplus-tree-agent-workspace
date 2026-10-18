from pathlib import Path
import json,csv,hashlib,statistics as st,math
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
J=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(p,h):assert sha(p)==h,p
old=J(P/'HARNESS-001/freeze.json')
for n,h in old['files'].items():
 if n.startswith(('src/','compat/','vendor/','bench/')):ck(R/n,h)
for d in ['DIAG-010','PROFILE-003']:
 f=J(P/d/'freeze.json')
 for n,h in f['files'].items():ck(R/f['snapshot']/n,h)
 for row in J(P/d/'validation.json'):
  assert row['returncode']==0
  for k in ['stdout','stderr']:ck((R if row[k].startswith('scratch/') else P/d)/row[k],row[k+'_sha256'])
for d in ['DIAG-010','AA-005','PROFILE-003']:
 m=J(P/d/'manifest.json');assert m['status']=='complete';ck(P/d/'PLAN.md',m['plan_sha256']);ck(P/d/'run.py',m['runner_sha256']);ck(R/m['binary'],m['binary_sha256'])
 assert len(m['runs'])==(12 if d=='PROFILE-003' else 96)
 for row in m.get('warmup',[])+m['runs']:
  assert row['returncode']==0
  for k in ['csv','stdout','stderr']:
   if k in row:ck((R if row[k].startswith('scratch/') else P/d)/row[k],row[k+'_sha256'])
 for a,b in zip(m['runs'],m['runs'][1:]):assert a['ended_utc']<=b['started_utc']
 if d!='PROFILE-003':
  for cell in m['cells']:
   for b in range(1,7):assert ''.join(x['label'] for x in m['runs'] if x['cell']==cell[0] and x['block']==b)=='ABBA'
assert sum(x['qualified'] for x in J(P/'AA-005/summary.json'))==2
assert not J(P/'DIAG-010/summary.json')['hypothesis_supported']
m=J(P/'BOUNDARY-011/manifest.json');assert m['status']=='pass'
for n,h in m['sources'].items():ck(R/m['snapshot']/n,h)
for row in m['runs']:
 assert row['returncode']==0
 for k in ['stdout','stderr']:ck(P/'BOUNDARY-011'/(row['name']+'.'+k),row[k+'_sha256'])
for row in J(P/'BOUNDARY-011/faults.json'):
 assert row['returncode']==(0 if row['step']=='build' else -6)
 for k in ['stdout','stderr']:ck(P/'BOUNDARY-011'/row[k],row[k+'_sha256'])
assert 'earlier owned-byte' in J(P/'BOUNDARY-011/fault-review.json')['driver_failure']
E=R/'experiments/EXP-002';f=J(E/'freeze.json')
for v,files in f['files'].items():
 for n,h in files.items():ck(R/f['snapshot_root']/v/n,h)
 for n,h in files.items():
  if n!='src/zset_btree.c':assert h==f['files']['control'][n]
V=J(E/'validation.json');assert len(V)==64
for row in V:
 assert row['returncode']==0
 for k in ['stdout','stderr']:ck(E/row[k],row[k+'_sha256'])
for fn,sn,expected,plan in [('manifest.json','summary.json',72,'PLAN.md'),('confirmation.json','confirmation-summary.json',24,'CONFIRMATION-PLAN.md')]:
 m=J(E/fn);s=J(E/sn);assert m['status']=='complete' and len(m['runs'])==expected;ck(E/plan,m['plan_sha256'])
 for v,b in m['binaries'].items():ck(R/b,m['binary_hashes'][v])
 for row in m['runs']:
  assert row['returncode']==0
  for k in ['csv','stderr']:ck(E/row[k],row[k+'_sha256'])
 for result in s['results']:
  for c in result['cells']:
   effects=[]
   for block in range(1,4):
    runs=[x for x in m['runs'] if x['variant']==result['variant'] and x['member_bytes']==c['member_bytes'] and x['block']==block];assert ''.join(x['label'] for x in runs)=='ABBA'
    vals={'A':[],'B':[]}
    for x in runs:
     row=next(csv.DictReader((E/x['csv']).open()));vals[x['label']].append(int(row['elapsed_ns'])/int(row['operations']))
    effects.append(100*(st.mean(vals['B'])/st.mean(vals['A'])-1))
   assert all(abs(a-b)<1e-9 for a,b in zip(effects,c['effects_pct']))
   half=4.302652729911275*st.stdev(effects)/math.sqrt(3);assert abs(st.mean(effects)+half-c['high_pct'])<1e-9
 assert s['screen_winner']=='C'
pm=J(E/'profile-results/manifest.json');ps=J(E/'profile-results/summary.json');assert pm['status']=='complete' and len(ps)==4
for row in pm['runs']:
 for k in ['stdout','stderr']:ck(R/row[k],row[k+'_sha256'])
for s in ps:assert sum(s['counts'].values())==s['samples'] and s['samples']>=30
print('PASS root/snapshot/referee identity, raw/source hashes, serial ABBA schedules, candidate effects/intervals, correctness/fault evidence, profile count conservation; sequential audit only')
