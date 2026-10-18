"""Separate sequential read-only evidence audit; not independent confirmation."""
from pathlib import Path
import csv,json,hashlib,math,statistics as st
R=Path(__file__).resolve().parents[2];P=Path(__file__).resolve().parent
J=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def ck(p,h):assert sha(p)==h,p
def eq(x,y):assert abs(x-y)<1e-9,(x,y)
old=J(P/'HARNESS-001/freeze.json')
for name,h in old['files'].items():
 if name.startswith(('src/','compat/','vendor/','bench/')):ck(R/name,h)
for folder in ['DIAG-007','DIAG-008','DIAG-009','HARNESS-003']:
 f=J(P/folder/'freeze.json');B=R/f['snapshot']
 for name,h in f['files'].items():ck(B/name,h)
 for name in ['src/zset_btree.c','src/zset_btree.h']:assert f['files'][name]==old['files'][name]
 for row in J(P/folder/'validation.json'):
  assert row['returncode']==0
  for key in ['stdout','stderr']:
   path=R/row[key] if row[key].startswith('scratch/') else P/folder/row[key]
   ck(path,row[key+'_sha256'])
print('PASS frozen root/snapshots/validation hashes')
for folder,filename in [('BOUNDARY-009','manifest.json'),('BOUNDARY-010','manifest-final.json')]:
 m=J(P/folder/filename);assert m['status']=='pass';B=R/m['snapshot']
 for name,h in m['sources'].items():ck(B/name,h)
 for row in m['runs']:
  assert row['returncode']==0
  for key in ['stdout','stderr']:ck(P/folder/(row['name']+'.'+key),row[key+'_sha256'])
  if 'binary_sha256' in row:ck(B/('build/'+('sanitize' if 'sanitize' in row['name'] else 'release')),row['binary_sha256'])
 for row in J(P/folder/'faults.json'):
  assert (row['returncode']==0)==(row['step']=='build')
  for key in ['stdout','stderr']:ck(P/folder/row[key],row[key+'_sha256'])
  ck(R/row['cwd']/'src/zset_btree.c',row['source_sha256'])
  if row['step']=='run':
   err=(P/folder/row['stderr']).read_text()
   if row['fault']=='read-past-end':assert row['returncode'] in [-10,-11]
   else:assert 'line=' in err
m=J(P/'BOUNDARY-010/manifest.json');assert len(m['runs'])==1 and m['runs'][0]['returncode']==1
for name,h in m['sources'].items():ck(R/m['snapshot']/name,h)
for field in ['stdout','stderr']:ck(P/'BOUNDARY-010'/('release-build.'+field),m['runs'][0][field+'_sha256'])
assert 'undeclared library function' in (P/'BOUNDARY-010/release-build.stderr').read_text()
print('PASS boundary suites/fault controls and retained first compile failure')

def manifest(folder,count):
 D=P/folder;m=J(D/'manifest.json');assert m['status']=='complete' and len(m['runs'])==count
 ck(D/'PLAN.md',m['plan_sha256']);ck(D/'run.py',m['runner_sha256']);ck(R/m['binary'],m['binary_sha256']);assert m['binary_sha256']==m['binary_sha256_after']
 rows=[]
 for run in m.get('warmup',[])+m['runs']:
  assert run['returncode']==0
  for k in ['csv','stdout','stderr']:
   if k in run:ck((R if run[k].startswith('scratch/') else D)/run[k],run[k+'_sha256'])
 for a,b in zip(m['runs'],m['runs'][1:]):assert a['ended_utc']<=b['started_utc']
 return m
# Independent PRNG/fingerprints for measured fixtures.
def perm(n,seed,skip):
 mask=(1<<64)-1
 def rnd():
  nonlocal seed
  seed=(seed+0x9e3779b97f4a7c15)&mask;z=seed
  z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask
  return z^(z>>31)
 for _ in range(skip):rnd()
 a=list(range(n))
 for i in range(n-1,0,-1):
  j=rnd()%(i+1);a[i],a[j]=a[j],a[i]
 h=14695981039346656037
 for v in a:h=((h^v)*1099511628211)&mask
 return str(h)
fps={seed:perm(100000,seed,skip) for seed,skip in [(1301,16),(1409,0),(1723,16),(1861,0),(2503,16),(2707,0)]}
# DIAG-007 all windows, fixed rotation and phase decision.
m=manifest('DIAG-007',24);D=P/'DIAG-007';s=J(D/'summary.json');cells=[(16,0),(16,1),(320,0),(320,1)]
want=[]
for b in range(1,7):
 o=(b-1)%4
 want += [(b,size,miss) for size,miss in cells[o:]+cells[:o]]
assert [(r['block'],r['member_bytes'],r['miss']) for r in m['runs']]==want
ratios={c:[] for c in cells};controls={c:True for c in cells};mem={c:set() for c in cells}
for run in m['runs']:
 rr=list(csv.DictReader((D/run['csv']).open()));assert len(rr)==16;key=run['member_bytes'],run['miss'];v=[]
 for i,r in enumerate(rr):
  assert int(r['window'])==i and r['windows']=='16' and r['operations']=='500000'
  assert r['construction_fingerprint']==fps[1301] and r['query_fingerprint']==fps[1409]
  assert int(r['checksum'])==int(r['expected'])==(0 if key[1] else 24999750000)
  assert r['warmup_passes']=='10';v.append(int(r['elapsed_ns']));mem[key].add(r['tree_bytes'])
 gap=int(rr[0]['gap_ns']);outer=int(rr[0]['outer_elapsed_ns']);assert outer==sum(v)+gap and gap>=0
 controls[key] &= min(v)>=10000000 and gap/outer<=.01
 ratios[key].append(sum(v[:4])/sum(v[-4:]))
passcells=0
for cell in s['cells']:
 key=cell['member_bytes'],int(cell['case']=='lookup-miss');r=ratios[key];assert len(mem[key])==1
 for a,b in zip(r,cell['ratios']):eq(a,b)
 passed=controls[key] and st.median(r)>=1.03 and sum(x>1 for x in r)>=5
 assert passed==cell['phase_criterion_met'];passcells+=passed
assert s['hypothesis_supported']==(all(controls.values()) and passcells>=2)==False
print('PASS DIAG-007 fixed schedule, independent fingerprints,384 rows,recomputed unsupported')
# DIAG-008 fixed ABBA, warmup cases, phase intervention.
m=manifest('DIAG-008',48);D=P/'DIAG-008';s=J(D/'summary.json')
want=[(b,size,slot,label) for b in range(1,7) for size in ([16,320] if b%2 else [320,16]) for slot,label in enumerate('ABBA')]
assert [(r['block'],r['member_bytes'],r['slot'],r['label']) for r in m['runs']]==want
for cell in s['cells']:
 groups={};control=True;memory=set()
 for run in m['runs']:
  if run['member_bytes']!=cell['member_bytes']:continue
  rr=list(csv.DictReader((D/run['csv']).open()));assert len(rr)==16;v=[]
  for i,r in enumerate(rr):
   assert int(r['window'])==i and r['operations']=='500000' and r['checksum']==r['expected']=='0'
   assert r['construction_fingerprint']==fps[1723] and r['query_fingerprint']==fps[1861]
   assert r['warmup_case']==('lookup-hit' if run['label']=='A' else 'lookup-miss')
   v.append(int(r['elapsed_ns']));memory.add(r['tree_bytes'])
  gap=int(rr[0]['gap_ns']);outer=int(rr[0]['outer_elapsed_ns']);assert outer==sum(v)+gap and gap>=0
  control &= min(v)>=10000000 and gap/outer<=.01
  groups.setdefault((run['block'],run['label']),[]).append(sum(v[:4])/sum(v[-4:]))
 assert len(memory)==1;c=[];bs=[]
 for b in range(1,7):
  a=st.mean(groups[b,'A']);bb=st.mean(groups[b,'B']);c.append(a/bb);bs.append(bb)
  eq(a/bb,cell['blocks'][b-1]['contrast'])
 passed=control and st.median(c)>=1.02 and sum(v>1 for v in c)>=5 and .99<=st.median(bs)<=1.01
 assert passed==cell['criterion']
assert s['hypothesis_supported']==all(c['controls'] for c in s['cells']) and s['cells'][0]['criterion']
print('PASS DIAG-008 fixed schedule,768 rows,recomputed primary support')
# AA-004 exact unchanged precision rule.
m=manifest('AA-004',96);D=P/'AA-004';assert len(m['warmup'])==1
cells=m['cells'];want=[]
for b in range(1,7):
 o=(b-1)%4
 for c in cells[o:]+cells[:o]:want += [(b,c[0],slot,label) for slot,label in enumerate('ABBA',1)]
assert [(r['block'],r['cell'],r['step'],r['label']) for r in m['runs']]==want
for cell in J(D/'summary.json'):
 effects=[];rr=[]
 for run in m['runs']:
  if run['cell']!=cell['cell']:continue
  r=next(csv.DictReader((D/run['csv']).open()));n=int(r['size']);ops=int(r['operations']);assert n==100000
  assert r['construction_fingerprint']==fps[2503] and r['query_fingerprint']==fps[2707]
  assert int(r['checksum'])==(ops*99999//2 if r['case']=='lookup-hit' else 0)
  assert r['warmup_case']==r['case'];rr.append((run,r))
 for b in range(1,7):
  a=[int(r['elapsed_ns']) for run,r in rr if run['block']==b and run['label']=='A'];bb=[int(r['elapsed_ns']) for run,r in rr if run['block']==b and run['label']=='B'];assert len(a)==len(bb)==2;effects.append(100*(sum(bb)/sum(a)-1))
 avg=sum(effects)/6;sd=(sum((x-avg)**2 for x in effects)/5)**.5;half=2.5705818366147395*sd/math.sqrt(6);lo=avg-half;hi=avg+half
 for a,b in [(avg,cell['aa_mean_pct']),(lo,cell['ci95_low_pct']),(hi,cell['ci95_high_pct'])]:eq(a,b)
 stable=all(len({r[k] for _,r in rr})==1 for k in ['operations','checksum','tree_bytes'])
 good=stable and min(int(r['elapsed_ns']) for _,r in rr)>=10000000 and lo>=-1 and hi<=1
 assert good==cell['qualified']==False
print('PASS AA-00496 rows/all intervals/recomputed PARK')
# DIAG-009 every sample resolved; rate decisions computed from original counters.
m=manifest('DIAG-009',18);D=P/'DIAG-009';s=J(D/'summary.json');want=[];modes=[1000,3001,17011]
for b in range(1,7):
 o=(b-1)%3;want += [(b,q) for q in modes[o:]+modes[:o]]
assert [(r['block'],r['profile_usec']) for r in m['runs']]==want
sym={r['name']:r for r in J(D/'symbolication.json')};rates={};valid=True
for run,summary in zip(m['runs'],s['results']):
 raw=list(csv.reader((R/run['stderr']).open()));head=[r for r in raw if r[0]=='PROFILE'];pc=[r for r in raw if r[0]=='PC']
 assert len(head)==1 and head[0][4]=='0' and int(head[0][3])==len(pc)
 row=next(csv.DictReader((R/run['stdout']).open()));assert row['checksum']=='3200000000' and int(row['samples'])==len(pc)
 cmd=sym[run['name']];assert cmd['returncode']==0
 for field in ['stdout','stderr']:ck(R/cmd[field],cmd[field+'_sha256'])
 addresses=sorted({r[2] for r in pc if r[1]=='calibrate'});symbols=(R/cmd['stdout']).read_text().splitlines();assert len(addresses)==len(symbols)
 mapping=dict(zip(addresses,symbols));known=sum(r[1]=='calibrate' and mapping[r[2]].startswith('known_arithmetic ') for r in pc)
 valid &= len(pc)>=20 and known/len(pc)>=.9
 assert known==summary['known'];rate=len(pc)*1e9/int(row['thread_ns']);eq(rate,summary['rate_per_thread_second']);rates[run['block'],run['profile_usec']]=rate
ra=[];rb=[]
for b in range(1,7):ra.append(rates[b,1000]/rates[b,3001]);rb.append(rates[b,17011]/rates[b,1000])
good=valid and .9<=st.median(ra)<=1.1 and sum(.9<=v<=1.1 for v in ra)>=5 and st.median(rb)<.75 and sum(v<.75 for v in rb)>=5
assert s['all_controls']==valid and s['hypothesis_supported']==good==False
print('PASS DIAG-009 fixed18 captures/sample conservation/recomputed unsupported')
print('PASS round005 read-only sequential audit; source NONE, qualification PARK')
