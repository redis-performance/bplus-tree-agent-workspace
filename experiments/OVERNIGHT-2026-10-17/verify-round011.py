from pathlib import Path
import json,csv,hashlib,difflib,statistics as st,math
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';H=O/'HARNESS-006';E=R/'experiments/EXP-004/compact-guards';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[];windows=[];other=[];intervals=0
def record(s):checks.append(s);print('PASS',s,flush=True)
def logs(D,r,named=False,expected=0):
 assert r['returncode']==expected,(r['name'],r['returncode'])
 for k in ['stdout','stderr']:
  p=D/(r['name']+'.'+k) if named else D/r[k];assert sha(p)==r[k+'_sha256'],p
 if 'started_utc' in r:other.append((r['started_utc'],r['ended_utc'],str(D.relative_to(R))))
for n,h in json.loads((O/'ROUND-007-METHOD.json').read_text())['root_files'].items():assert sha(R/n)==h
record('root source/header/referee unchanged')
F=json.loads((H/'freeze.json').read_text());S=R/F['snapshot']
for n,h in F['files'].items():assert sha(S/n)==h
parent=json.loads((O/'HARNESS-005/freeze.json').read_text());before=(R/parent['snapshot']/'bench/iterator_modes.c').read_text();after=(S/'bench/iterator_modes.c').read_text()
assert (H/'harness.patch').read_text()==''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/bench/iterator_modes.c',tofile='b/bench/iterator_modes.c'))
for k,h in json.loads((H/'binaries.json').read_text()).items():assert sha(S/f'build/{k}/iterator-modes')==h
V=json.loads((H/'validation.json').read_text());assert len(V)==5136
for r in V:
 invalid=any(r['name'].endswith('-'+n) for n in ['bad-order','bad-encoding','zero-size','zero-ops','huge-ops']);logs(H,r,expected=2 if invalid else 0)
assert sum(r['returncode']==2 for r in V)==10
faults=json.loads((H/'faults.json').read_text());assert len(faults)==3
for r in faults:
 assert r['detected'] and r['returncode']==-6 and 'bench/iterator_modes.c:' in r['stderr']
 assert sha(R/'scratch/overnight-harness-006/faults'/r['name'])==r['binary_sha256']
record('HARNESS-006 patch/snapshot/binaries;5136 expected validation outcomes;three sensitivity faults')
C=O/'COUNTERS-006';M=json.loads((C/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==48
for d in M['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
for r in M['runs']:logs(C,r,True)
assert json.loads((C/'summary.json').read_text())['status']=='supported'
T=json.loads((C/'trace/manifest.json').read_text());assert T['status']=='complete' and len(T['runs'])==12
for r in T['runs']:logs(C/'trace',r,True)
assert json.loads((C/'trace/audit.json').read_text())['status']=='supported'
N=json.loads((C/'fresh/manifest.json').read_text());assert N['status']=='complete' and len(N['runs'])==32
for d in N['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
for r in N['runs']:logs(C/'fresh',r,True)
assert json.loads((C/'fresh/summary.json').read_text())['status']=='pass'
for policy in ['exact','round16']:
 output=[(C/'fresh'/(r['name']+'.stdout')).read_bytes() for r in N['runs'] if r['stage']=='run' and r['policy']==policy]
 assert len(output)==8 and len(set(output))==1
 assert len(output[0].splitlines())==3961 and b'PASS checks=325860 exact=163246200 ' in output[0].splitlines()[-1]
record('allocator factorial12unit+12semantic;6trace;16fresh-source cells intact and predictions supported')
F=json.loads((E/'freeze.json').read_text());S=R/F['snapshot_root'];old=json.loads((E.parent/'freeze.json').read_text())
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 for n,h in F['files']['control'].items():
  if n!='src/zset_btree.c':assert files[n]==h
 if v!='control':
  assert files['src/zset_btree.c']==old['files'][v]['src/zset_btree.c']
  V=json.loads((E/v/'validation.json').read_text());assert len(V)==590
  for r in V:logs(E/v,r)
 for k,h in json.loads((E/v/'binaries.json').read_text()).items():assert sha(S/v/f'build/{k}/iterator-modes')==h
assert json.loads((E/'control/binaries.json').read_text())==json.loads((H/'binaries.json').read_text())
record('EXP-004 exact retained sources;identical referees;1770 candidate commands;byte-identical control')
def readruns(D,n,warm):
 M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==n and len(M['warmup'])==warm;rows=[]
 for kind in ['warmup','runs']:
  for r in M[kind]:
   assert r['returncode']==0
   for k in ['csv','stderr']:assert sha(D/r[k])==r[k+'_sha256']
   data=list(csv.DictReader((D/r['csv']).open()));assert len(data)==1;x=data[0];assert x['checksum']==x['expected_checksum']
   assert int(x['size'])==95 and int(x['traversals'])==(int(x['requested_ops'])+94)//95 and int(x['operations'])==95*int(x['traversals'])
   windows.append((r['started_utc'],r['ended_utc'],str(D.relative_to(R))))
   if kind=='runs':rows.append((r,x))
 return M,rows
def recompute(rows,match,metric,blocks):
 global intervals
 subset=[(m,r) for m,r in rows if all(m[k]==v for k,v in match.items())];assert len(subset)==blocks*4
 assert all(len({r[k] for _,r in subset})==1 for k in ['checksum','operations','tree_bytes','construction_fingerprint'])
 effects=[]
 for b in range(1,blocks+1):
  rr=[(m,r) for m,r in subset if m['block']==b];assert ''.join(m['label'] for m,r in rr)=='ABBA'
  ab={l:[int(r[metric])/int(r['operations']) for m,r in rr if m['label']==l] for l in 'AB'};assert all(len(v)==2 for v in ab.values());effects.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
 mean=st.mean(effects);half={3:4.302652729696142,6:2.5705818366147395}[blocks]*st.stdev(effects)/math.sqrt(blocks);intervals+=1;return [mean,mean-half,mean+half]
def close(a,b):assert all(abs(x-y)<1e-10 for x,y in zip(a,b)),(a,b)
_,rows=readruns(O/'AA-011',384,1)
for r in json.loads((O/'AA-011/summary-corrected.json').read_text()):
 filt=dict(cell=r['cell'],seed=r['seed']);ci=recompute(rows,filt,'elapsed_ns',6);close(ci,[r['mean_pct'],r['ci95_low_pct'],r['ci95_high_pct']]);close(recompute(rows,filt,'thread_elapsed_ns',6),r['thread_interval']);assert r['invariants'] and r['qualified']==(ci[1]>=-1 and ci[2]<=1 and r['min_wall_ms']>=10)
assert len(json.loads((O/'AA-011/eligible-corrected.json').read_text()))==1
for phase,warm in [('screen',4),('confirm',0)]:
 _,rows=readruns(E/phase,72,warm)
 for r in json.loads((E/phase/'summary.json').read_text()):
  filt={k:r[k] for k in ['variant','cell','seed']};ci=recompute(rows,filt,'elapsed_ns',3);close(ci,[r['mean_pct'],r['ci95_low_pct'],r['ci95_high_pct']]);close(recompute(rows,filt,'thread_elapsed_ns',3),r['intervals']['thread_elapsed_ns']);assert r['invariants'] and r['guard_pass']==(ci[2]<=1) and r['guard_fail']==(ci[1]>1)
decisions=json.loads((E/'confirm/decisions.json').read_text());assert all(r['status']=='PARK' and not r['both_seed_failures'] for r in decisions)
assert [len(r['both_seed_passes']) for r in decisions]==[1,1,0]
_,rows=readruns(O/'DIAG-013',192,1);D=json.loads((O/'DIAG-013/summary.json').read_text());assert D['status']=='unsupported'
for r in D['results']:
 filt={k:r[k] for k in ['cell','seed','policy']}
 for metric in ['elapsed_ns','thread_elapsed_ns']:close(recompute(rows,filt,metric,6),r['intervals'][metric])
assert intervals==72
record('720measuredrows+6warmups;72wall/thread intervals independently recomputed from raw;analysis erratum retained')
for D,n in [(H/'profiles',6),(E/'profiles',12),(E/'profiles-exact',8)]:
 M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==n and len(M['calibrations'])==2
 for r in M.get('preparation',[]):logs(R,r)
 for r in M['calibrations']+M['runs']:
  assert r['returncode']==0
  for k in ['stdout','stderr']:assert sha(R/r[k])==r[k+'_sha256']
  windows.append((r['started_utc'],r['ended_utc'],str(D.relative_to(R))))
  raw=list(csv.reader((R/r['stderr']).open()));heads=[r for r in raw if r[0]=='PROFILE'];pcs=[r for r in raw if r[0]=='PC'];assert len(heads)==1 and int(heads[0][3])==len(pcs) and heads[0][4]=='0'
 for r in json.loads((D/'summary.json').read_text()):assert r['controls'] and sum(r['counts'].values())==r['samples']
record('26profiles and6calibrations conserve samples;symbol/control checks pass;no frequency inference')
windows.sort();assert len(windows)==758
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
for a,b,name in other:
 for c,d,kind in windows:assert b<=c or a>=d,(name,kind,a,b,c,d)
record('758serial measurement/profile windows;all timestamped build/test commands disjoint')
for D in [H,E,C,O/'AA-011',O/'DIAG-013']:
 for p in D.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   raw=p.read_bytes();assert b'/Users/' not in raw and b'/private/var/' not in raw,str(p.relative_to(R))
record('public evidence free of private machine-path prefixes')
(O/'ROUND-011-VERIFY.json').write_text(json.dumps(dict(status='pass',checks=checks,intervals_recomputed=intervals,windows=len(windows),timestamped_nonmeasurement_commands=len(other),first_window=windows[0],last_window=windows[-1],review='sequential coordinator audit;not independent agent'),indent=2)+'\n')
