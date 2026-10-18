from pathlib import Path
import json,csv,hashlib,statistics as st,math,datetime,difflib
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();read=lambda p:json.loads(p.read_text());count=0;windows=[]
method=read(P/'ROUND-007-METHOD.json')
for n,h in method['root_files'].items():assert sha(R/n)==h
for folder in [P/'HARNESS-004',R/'experiments/EXP-002/guard-extension',R/'experiments/EXP-003']:
 F=read(folder/'freeze.json')
 if 'snapshot' in F:
  for n,h in F['files'].items():assert sha(R/F['snapshot']/n)==h
  V=read(folder/'validation.json');assert len(V)==1286 and all(r['returncode']==0 for r in V)
  for r in V:
   for k in ['stdout','stderr']:assert sha(folder/r[k])==r[k+'_sha256']
 else:
  for v,files in F['files'].items():
   for n,h in files.items():assert sha(R/F['snapshot_root']/v/n)==h
   V=read(folder/v/'validation.json');assert all(r['returncode']==0 for r in V)
   for r in V:
    for k in ['stdout','stderr']:assert sha(folder/v/r[k])==r[k+'_sha256']
for folder,manifest,expected in [(P/'AA-006','manifest.json',336),(R/'experiments/EXP-002/guard-extension','manifest.json',504),(R/'experiments/EXP-002/guard-extension','confirmation.json',216),(R/'experiments/EXP-003','manifest.json',504),(R/'experiments/EXP-003','confirmation.json',216)]:
 M=read(folder/manifest);assert M['status']=='complete' and len(M['runs'])==expected
 plan='CONFIRMATION-PLAN.md' if manifest=='confirmation.json' else 'PLAN.md';assert sha(folder/plan)==M['plan_sha256']
 for run in M.get('warmup',[])+M['runs']:
  assert run['returncode']==0
  for k in ['csv','stderr']:assert sha(folder/run[k])==run[k+'_sha256']
  data=list(csv.DictReader((folder/run['csv']).open()));assert len(data)==1;r=data[0];assert r['checksum']==r['expected_checksum']
  a=datetime.datetime.fromisoformat(run['started_utc']);b=datetime.datetime.fromisoformat(run['ended_utc']);assert a<=b;windows.append((a,b));count+=1
 if manifest=='manifest.json' and folder.name=='AA-006':continue
 summary=read(folder/('confirmation-summary.json' if manifest=='confirmation.json' else 'summary.json'))
 for result in summary['results']:
  for cell in result['cells']:
   rows=cell['rows'];effects=[]
   for b in range(1,4):
    rr=[r for r in rows if r['block']==b];assert ''.join(r['label'] for r in rr)=='ABBA';vals={l:[int(r['elapsed_ns'])/int(r['operations']) for r in rr if r['label']==l] for l in 'AB'};effects.append(100*(st.mean(vals['B'])/st.mean(vals['A'])-1))
   mean=st.mean(effects);half=4.302652729911275*st.stdev(effects)/math.sqrt(3)
   assert abs(mean-cell['mean_pct'])<1e-10 and abs(mean-half-cell['low_pct'])<1e-10 and abs(mean+half-cell['high_pct'])<1e-10 and cell['controls']
for folder in [R/'experiments/EXP-002/guard-extension/profiles',R/'experiments/EXP-003/profiles']:
 M=read(folder/'manifest.json');assert M['status']=='complete';summary=read(folder/'summary.json');assert all(r['controls'] and sum(r['counts'].values())==r['samples'] for r in summary)
 for run in M['calibrations']+M['runs']:
  assert run['returncode']==0
  for k in ['stdout','stderr']:assert sha(R/run[k])==run[k+'_sha256']
  assert sha(R/run['binary'])==run['binary_sha256'];windows.append((datetime.datetime.fromisoformat(run['started_utc']),datetime.datetime.fromisoformat(run['ended_utc'])))
windows.sort();assert all(a[1]<=b[0] for a,b in zip(windows,windows[1:]))
B=P/'BOUNDARY-012';M=read(B/'manifest.json');assert M['status']=='pass' and len(M['runs'])==16
for r in M['runs']:
 assert r['returncode']==0
 for k in ['stdout','stderr']:assert sha(B/r[k])==r[k+'_sha256']
faults=read(B/'fault-review.json');assert len(faults['runs'])==2 and all(r['returncode']==-6 for r in faults['runs'])
for ex in ['EXP-002','EXP-003']:
 folder=R/'experiments'/ex;G=folder/'guard-extension' if ex=='EXP-002' else folder;assert read(G/'confirmation-summary.json')['decision']=='REJECT'
 F=read(folder/'freeze.json');base=(R/F['snapshot_root']/'control/src/zset_btree.c').read_text()
 for v in ['A','B','C']:
  src=(R/F['snapshot_root']/v/'src/zset_btree.c').read_text();patch=''.join(difflib.unified_diff(base.splitlines(True),src.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'));assert patch==(folder/'variants'/v/'candidate.patch').read_text()
newdirs=[P/'HARNESS-004',P/'AA-006',P/'BOUNDARY-012',R/'experiments/EXP-002/guard-extension',R/'experiments/EXP-003']
for folder in newdirs:
 for f in folder.rglob('*'):
  if f.is_file():assert b'/Users/' not in f.read_bytes() and b'/private/var/' not in f.read_bytes(),str(f)
print(json.dumps(dict(status='PASS',measured_rows=count-1,prospective_warmup=1,serial_timing_profile_windows=len(windows),source_baseline_preserved=True,decisions={'EXP-002':'REJECT/NONE','EXP-003':'REJECT/NONE'},review='sequential read-only audit,not independent confirmation'),indent=2))
