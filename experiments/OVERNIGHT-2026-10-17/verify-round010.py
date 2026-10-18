from pathlib import Path
import json,csv,hashlib,difflib,statistics as st,math
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';H=O/'HARNESS-005';E=R/'experiments/EXP-004/ordered-guards';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[];windows=[];other=[];intervals=0

def record(s):checks.append(s);print('PASS',s,flush=True)
def logs(directory,row,named=False):
 assert row['returncode']==0
 for k in ['stdout','stderr']:
  p=directory/(row['name']+'.'+k) if named else directory/row[k];assert sha(p)==row[k+'_sha256'],p
 if 'started_utc' in row:other.append((row['started_utc'],row['ended_utc'],str(directory.relative_to(R))))
old=json.loads((O/'ROUND-007-METHOD.json').read_text())
for n,h in old['root_files'].items():assert sha(R/n)==h
record('root source/header/referee preserved')
F=json.loads((H/'freeze.json').read_text());S=R/F['snapshot']
for n,h in F['files'].items():assert sha(S/n)==h
parent=json.loads((O/'HARNESS-004/freeze.json').read_text());before=(R/parent['snapshot']/'bench/iterator_modes.c').read_text();after=(S/'bench/iterator_modes.c').read_text();patch=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='a/bench/iterator_modes.c',tofile='b/bench/iterator_modes.c'));assert patch==(H/'harness.patch').read_text()
for k,h in json.loads((H/'binaries.json').read_text()).items():assert sha(S/f'build/{k}/iterator-modes')==h
V=json.loads((H/'validation.json').read_text());assert len(V)==2832
for row in V:
 if row['returncode']==2:
  assert any(row['name'].endswith('-'+n) for n in ['bad-order','bad-encoding','zero-size','zero-ops','huge-ops']);copy=dict(row,returncode=0);logs(H,copy)
 else:logs(H,row)
assert sum(r['returncode']==2 for r in V)==10
faults=json.loads((H/'faults-complete.json').read_text());assert len(faults)==3 and all(r['detected'] and r['returncode']==-6 for r in faults)
assert json.loads((H/'faults.json').read_text())[0]['detected']
record('HARNESS-005 snapshot/patch/binaries and2832validationcommands intact;three faults detected;first driver mismatch retained')
for name,num in [('COUNTERS-004',96),('COUNTERS-005',672)]:
 D=O/name;M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and M['coverage_hypothesis_supported'] and len(M['runs'])==num
 for n,h in M['sources'].items():assert sha(R/M['snapshot']/n)==h
 for row in M['builds']+M['runs']:logs(D,row,True)
 results=M['runs'];count=num//2
 for i in range(count):
  a=results[i]['result'];b=results[count+i]['result'];assert {k:v for k,v in a.items() if k!='owned'}=={k:v for k,v in b.items() if k!='owned'}
 for r in results:
  d=r['result'];assert sum(d['widths'])==sum(d['shifts'])==d['n']==d['elements']
  if name=='COUNTERS-005':assert d['leaves']==1 and d['reversed']==(0 if d['construction']=='ascending' else d['n'])
record('768structuralchildren andfourbuilds pass;cross-build structural equality,packed histograms andfullyreversedrecipe verified')
for r in json.loads((O/'COUNTERS-005/fault-audit.json').read_text()):
 assert r['detected'] and not r['child_repeated'];p=O/'COUNTERS-005'/f'fault-{r["name"]}.stderr';assert sha(p)==r['stderr_sha256'] and r['checked_assertion'] in p.read_text()
record('two compact-recipe faults detected;earlier exact-bit assertion audit requires no rerun')
F=json.loads((E/'freeze.json').read_text());S=R/F['snapshot_root'];prior=json.loads((E.parent/'freeze.json').read_text())
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 for n,h in F['files']['control'].items():
  if n!='src/zset_btree.c':assert files[n]==h
 if v!='control':assert files['src/zset_btree.c']==prior['files'][v]['src/zset_btree.c']
 for k,h in json.loads((E/v/'binaries.json').read_text()).items():assert sha(S/v/f'build/{k}/iterator-modes')==h
 if v!='control':
  V=json.loads((E/v/'validation.json').read_text());assert len(V)==398
  for row in V:logs(E/v,row)
assert json.loads((E/'control/binaries.json').read_text())==json.loads((H/'binaries.json').read_text())
record('retainedEXP-004sources exact;referees identical;1194candidate validationcommands pass;qualifiedcontrol byteidentical')

def readruns(D,n,warmcount):
 M=json.loads((D/'manifest.json').read_text());assert M['status']=='complete' and len(M['runs'])==n and len(M.get('warmup',[]))==warmcount;data=[]
 for kind in ['warmup','runs']:
  for r in M[kind]:
   assert r['returncode']==0
   for k in ['csv','stderr']:assert sha(D/r[k])==r[k+'_sha256']
   rr=list(csv.DictReader((D/r['csv']).open()));assert len(rr)==1;x=rr[0];assert x['checksum']==x['expected_checksum'];windows.append((r['started_utc'],r['ended_utc'],str(D.relative_to(R))))
   if kind=='runs':data.append((r,x))
 return M,data

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
AM,AR=readruns(O/'AA-010',384,1)
for r in json.loads((O/'AA-010/summary.json').read_text()):
 filt=dict(cell=r['cell'],seed=r['seed']);ci=recompute(AR,filt,'elapsed_ns',6);close(ci,[r['mean_pct'],r['ci95_low_pct'],r['ci95_high_pct']]);close(recompute(AR,filt,'thread_elapsed_ns',6),r['thread_interval']);assert r['qualified']==(r['invariants'] and ci[1]>=-1 and ci[2]<=1 and r['min_wall_ms']>=10)
for phase,warmup in [('screen',4),('confirm',0)]:
 M,rows=readruns(E/phase,432,warmup)
 for r in json.loads((E/phase/'summary.json').read_text()):
  filt={k:r[k] for k in ['variant','cell','seed']};ci=recompute(rows,filt,'elapsed_ns',3);close(ci,[r['mean_pct'],r['ci95_low_pct'],r['ci95_high_pct']]);close(recompute(rows,filt,'thread_elapsed_ns',3),r['intervals']['thread_elapsed_ns']);assert r['invariants'] and r['guard_pass']==(ci[2]<=1) and r['guard_fail']==(ci[1]>1)
 for r in json.loads((E/phase/'decisions.json').read_text()):assert r['status']=='PARK' and len(r['both_seed_passes'])==6 and not r['both_seed_failures']
assert intervals==176
record('1248measuredrows+fivewarmups verified;176wall/thread intervals recomputed;allnewfreshguards pass')
PM=json.loads((E/'profiles/manifest.json').read_text());assert PM['status']=='complete' and len(PM['runs'])==12 and len(PM['calibrations'])==2
for section in ['preparation','calibrations','runs']:
 for row in PM[section]:
  if section=='preparation':logs(R,row)
  else:
   for k in ['stdout','stderr']:assert sha(R/row[k])==row[k+'_sha256']
   windows.append((row['started_utc'],row['ended_utc'],'profiles'));rr=list(csv.reader((R/row['stderr']).open()));head=[r for r in rr if r[0]=='PROFILE'];pcs=[r for r in rr if r[0]=='PC'];assert len(head)==1 and int(head[0][3])==len(pcs) and head[0][4]=='0'
for row in json.loads((E/'profiles/summary.json').read_text()):assert row['controls'] and sum(row['counts'].values())==row['samples']
record('12profiles/twocalibrations pass conservation andsymbol controls;logs intact')
windows.sort();assert len(windows)==1267
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
for a,b,name in other:
 for c,d,kind in windows:assert b<=c or a>=d,(name,kind,a,b,c,d)
record('1267measurementwindows serial;alltimestamped builds/correctness/census children disjoint')
for D in [H,E,O/'COUNTERS-004',O/'COUNTERS-005',O/'AA-010']:
 for p in D.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:
   raw=p.read_bytes();assert (b'/' + b'Users/') not in raw and (b'/' + b'private/var/') not in raw,str(p.relative_to(R))
record('new public experiment evidence has no private machine-path prefixes')
(O/'ROUND-010-VERIFY.json').write_text(json.dumps(dict(status='pass',checks=checks,intervals_recomputed=intervals,windows=len(windows),timestamped_nonmeasurement_commands=len(other),first_window=windows[0],last_window=windows[-1],review='sequentialcoordinatoraudit;notindependentagent'),indent=2)+'\n')
