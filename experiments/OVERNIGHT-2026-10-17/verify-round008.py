from pathlib import Path
import json,csv,hashlib,datetime,difflib,statistics as st,math
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';E=R/'experiments/EXP-004';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[];windows=[]
def record(s):checks.append(s);print('PASS',s)
old=json.loads((O/'ROUND-007-METHOD.json').read_text())
for n,h in old['root_files'].items():assert sha(R/n)==h
record('root source/header/referee match prior round hashes')
for D in [O/'COUNTERS-003',O/'BOUNDARY-013']:
 M=json.loads((D/'manifest.json').read_text());B=R/M['snapshot']
 for n,h in M['sources'].items():assert sha(B/n)==h
 for section in ['builds','runs']:
  for row in M.get(section,[]):
   assert row['returncode']==0
   for k in ['stdout','stderr']:assert sha(D/(row['name']+'.'+k))==row[k+'_sha256']
record('census/boundary source freezes and raw outputs intact')
for D in [E,O/'DIAG-011']:
 F=json.loads((D/'freeze.json').read_text());S=R/F['snapshot_root']
 for v,files in F['files'].items():
  for n,h in files.items():assert sha(S/v/n)==h
record('all candidate/diagnostic snapshot hashes intact')
F=json.loads((E/'freeze.json').read_text());control=(R/F['snapshot_root']/'control/src/zset_btree.c').read_text()
a=control.index('static double zbtScoreLeafScore(');b=control.index('/* Return the raw hash byte',a)
for v,condition in {'A':'if (bits + shift > 64)','B':'if (bits > 64 - shift)','C':'if (shift > 64 - bits)'}.items():
 actual=(R/F['snapshot_root']/v/'src/zset_btree.c').read_text();expected=control[:a]+control[a:b].replace('if (shift && bits > 64 - shift)',condition)+control[b:];assert actual==expected
 patch=''.join(difflib.unified_diff(control.splitlines(True),actual.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'));assert patch==(E/'variants'/v/'candidate.patch').read_text()
 for n,h in F['files']['control'].items():
  if n!='src/zset_btree.c':assert F['files'][v][n]==h
record('one-condition patches exact;all referee/support/test files identical')
for v in F['files']:
 V=json.loads((E/v/'validation.json').read_text());assert len(V)==270 and all(r['returncode']==0 for r in V)
 for r in V:
  for k in ['stdout','stderr']:assert sha(E/v/r[k])==r[k+'_sha256']
V=json.loads((O/'DIAG-011/validation.json').read_text());assert len(V)==388 and all(r['returncode']==0 for r in V)
for r in V:
 for k in ['stdout','stderr']:assert sha(O/'DIAG-011/validation'/(r['name']+'.'+k))==r[k+'_sha256']
record('1080 candidate validation commands and388 diagnostic commands intact')
for name in ['AA-007','AA-008']:
 D=O/name;M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete';assert sha(D/'PLAN.md')==M['plan_sha256'];assert sha(R/M['binary'])==M['binary_sha256']
 for run in M['warmup']+M['runs']:
  assert run['returncode']==0
  for k in ['csv','stderr']:assert sha(D/run[k])==run[k+'_sha256']
  windows.append((run['started_utc'],run['ended_utc'],name))
 for c in json.loads((D/'summary.json').read_text()):
  vals=c['effects_pct'];mean=st.mean(vals);half=2.5705818366147395*st.stdev(vals)/math.sqrt(6);assert abs(c['mean_pct']-mean)<1e-10 and abs(c['ci95_low_pct']-(mean-half))<1e-10
  assert c['qualified']==(c['invariants'] and mean-half>=-1 and mean+half<=1 and c['min_wall_ms']>=10)
record('A/A gates independently recomputed;raw binaries/hash checks pass')
for D,file,n in [(E,'manifest.json',504),(E,'confirmation.json',216),(O/'DIAG-011','manifest.json',144)]:
 M=json.loads((D/file).read_text());assert M['status']=='complete' and len(M['runs'])==n
 for run in M['runs']:
  assert run['returncode']==0
  for k in ['csv','stderr']:assert sha(D/run[k])==run[k+'_sha256']
  row=next(csv.DictReader((D/run['csv']).open()));assert row['checksum']==row['expected_checksum'];windows.append((run['started_utc'],run['ended_utc'],str(D.relative_to(R))))
record('864 source-comparison/caller rows intact;checksums pass')
for D,expected in [(E/'profiles',12),(O/'DIAG-011/profiles',8)]:
 M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==expected and len(M['calibrations'])==2
 for row in M['preparation']+M['calibrations']+M['runs']:
  assert row['returncode']==0
  for k in ['stdout','stderr']:assert sha(R/row[k])==row[k+'_sha256']
 for row in M['calibrations']+M['runs']:
  windows.append((row['started_utc'],row['ended_utc'],str(D.relative_to(R))));raw=list(csv.reader((R/row['stderr']).open()));heads=[r for r in raw if r[0]=='PROFILE'];pcs=[r for r in raw if r[0]=='PC'];assert len(heads)==1 and int(heads[0][3])==len(pcs) and heads[0][4]=='0'
 for row in json.loads((D/'summary.json').read_text()):assert row['controls'] and sum(row['counts'].values())==row['samples']
record('20profiles/4calibrations count conservation and raw integrity pass')
windows.sort();assert len(windows)==1226
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
record('all1226 measured/warmup/profile/calibration windows serial')
for row in json.loads((O/'BOUNDARY-013/faults.json').read_text()):
 assert row['detected'];assert row['commands'][0]['returncode']==0 and row['commands'][1]['returncode']!=0
assert not (E/'long-guard/manifest.json').exists()
record('twofaults detected;unqualified long-guard comparison correctly skipped')
for D in [E,O/'COUNTERS-003',O/'BOUNDARY-013',O/'AA-007',O/'AA-008',O/'DIAG-011']:
 for p in D.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   assert b'/Users/' not in p.read_bytes() and b'/private/var/' not in p.read_bytes(),str(p.relative_to(R))
record('new public experiment artifacts contain no private machine prefixes')
out=dict(status='pass',checks=checks,windows=len(windows),first_window=windows[0],last_window=windows[-1],review='sequential coordinator audit,not independent agent');(O/'ROUND-008-VERIFY.json').write_text(json.dumps(out,indent=2)+'\n')
