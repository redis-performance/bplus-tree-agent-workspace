from pathlib import Path
import json,csv,hashlib,difflib,statistics as st,math,datetime
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';E=R/'experiments/EXP-005';D=O/'DIAG-012';B=O/'BOUNDARY-014';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[];windows=[];intervals=0

def record(s):checks.append(s);print('PASS',s,flush=True)
def raw(directory,row,named=False):
 assert row['returncode']==0
 for k in ['stdout','stderr']:
  p=directory/(row['name']+'.'+k) if named else directory/row[k]
  assert sha(p)==row[k+'_sha256'],p
old=json.loads((O/'ROUND-007-METHOD.json').read_text())
for n,h in old['root_files'].items():assert sha(R/n)==h
record('root source/header/referee match preserved prior-round hashes')
BM=json.loads((B/'attempt-002/manifest.json').read_text());assert BM['status']=='pass' and len(BM['runs'])==16
for v,ss in BM['snapshots'].items():
 for n,h in ss['files'].items():assert sha(R/ss['path']/n)==h
for row in BM['runs']:raw(B/'attempt-002',row,True)
outputs=[(B/'attempt-002'/f'{v}-{k}-run.stdout').read_text() for v in ['control','A','B','C'] for k in ['release','sanitize']];assert len(set(outputs))==1 and 'exact=46005384' in outputs[0]
first=json.loads((B/'manifest.json').read_text());assert first['runs'][-1]['returncode']!=0 and 'zbtreeAllocSize(tree)==owned' in (B/'control-release-run.stderr').read_text()
for f in json.loads((B/'faults.json').read_text()):
 assert f['detected'] and f['commands'][0]['returncode']==0 and f['commands'][1]['returncode']!=0
 for stage,row in zip(['build','run'],f['commands']):
  for k in ['stdout','stderr']:assert sha(B/(f['name']+'-'+stage+'.'+k))==row[k+'_sha256']
record('eight boundary outputs identical;46,005,384exact results/build;first failure and two faults intact')
F=json.loads((E/'freeze.json').read_text());S=R/F['snapshot_root'];control=(S/'control/src/zset_btree.c').read_text();a=control.index('static double zbtScoreLeafScore(');b=control.index('/* Return the raw hash byte',a)
oldmask='if (bits < 64)\n            delta &= (UINT64_C(1) << bits) - 1;'
for v,expr in {'A':'delta &= UINT64_MAX >> (64 - bits);','B':'delta &= ((UINT64_C(1) << (bits - 1)) * 2) - 1;','C':'delta &= UINT64_MAX >> ((-bits) & 63);'}.items():
 actual=(S/v/'src/zset_btree.c').read_text();assert actual==control[:a]+control[a:b].replace(oldmask,expr)+control[b:]
 patch=''.join(difflib.unified_diff(control.splitlines(True),actual.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c'));assert patch==(E/'variants'/v/'candidate.patch').read_text()
 for n,h in F['files']['control'].items():
  if n!='src/zset_btree.c':assert F['files'][v][n]==h
for v,files in F['files'].items():
 for n,h in files.items():assert sha(S/v/n)==h
 V=json.loads((E/v/'validation.json').read_text());assert len(V)==274
 for row in V:raw(E/v,row)
record('mask patches exact;referee identical;1096validation commands and source hashes intact')
DF=json.loads((D/'attempt-002/freeze.json').read_text());DS=R/DF['snapshot_root']
for v,files in DF['files'].items():
 for n,h in files.items():assert sha(DS/v/n)==h
for n,h in DF['assembly'].items():assert sha(DS/n)==h
for row in json.loads((D/'attempt-002/builds.json').read_text()):raw(D/'attempt-002/validation',row,True)
DV=json.loads((D/'validation.json').read_text());assert len(DV)==1028
for row in DV:raw(D/'fixtures',row,True)
assert json.loads((D/'codegen-audit.json').read_text())['pass_all']
record('placement assembly/source hashes,1028validationruns and corrected complete code audit intact')

def read_runs(directory,filename,n,warmkey=None):
 M=json.loads((directory/filename).read_text());assert M['status']=='complete' and len(M['runs'])==n;data=[]
 for run in M['runs']+(M.get(warmkey,[]) if warmkey else []):
  assert run['returncode']==0
  for k in ['csv','stderr']:assert sha(directory/run[k])==run[k+'_sha256']
  rr=list(csv.DictReader((directory/run['csv']).open()));assert len(rr)==1;r=rr[0];assert r['checksum']==r['expected_checksum'];windows.append((run['started_utc'],run['ended_utc'],str(directory.relative_to(R))))
  if run in M['runs']:data.append((run,r))
 return M,data

def recompute(rows,filter,metric,blocks):
 global intervals
 values=[]
 subset=[(m,r) for m,r in rows if all(m.get(k)==v for k,v in filter.items())]
 assert len(subset)==blocks*4
 for block in range(1,blocks+1):
  rr=[(m,r) for m,r in subset if m['block']==block];assert ''.join(m['label'] for m,r in rr)=='ABBA'
  ab={l:[int(r[metric])/int(r['operations']) for m,r in rr if m['label']==l] for l in 'AB'};values.append(100*(st.mean(ab['B'])/st.mean(ab['A'])-1))
 mean=st.mean(values);half={3:4.302652729911275,6:2.5705818366147395}[blocks]*st.stdev(values)/math.sqrt(blocks);intervals+=1;return mean,mean-half,mean+half

def close(actual,expected):assert all(abs(a-b)<1e-9 for a,b in zip(actual,expected)),(actual,expected)
AM,AR=read_runs(O/'AA-009','manifest.json',72,'warmup');assert sha(R/AM['binary'])==AM['binary_sha256']
for c in json.loads((O/'AA-009/summary.json').read_text()):
 ci=recompute(AR,dict(cell=c['cell']),'elapsed_ns',6);close(ci,[c['mean_pct'],c['ci95_low_pct'],c['ci95_high_pct']]);assert c['qualified']==(c['invariants'] and ci[1]>=-1 and ci[2]<=1 and c['min_wall_ms']>=10)
DM,DR=read_runs(D,'manifest.json',480,'warmups')
for c in json.loads((D/'summary.json').read_text())['results']:
 for key,metric in [('wall','elapsed_ns'),('thread','thread_elapsed_ns')]:
  ci=recompute(DR,{k:c[k] for k in ['seed','target','mask']},metric,6);close(ci,[c[key][k] for k in ['mean','low','high']])
EM,ER=read_runs(E,'manifest.json',180)
for v in json.loads((E/'summary.json').read_text())['results']:
 for c in v['cells']:close(recompute(ER,dict(variant=v['variant'],cell=c['cell']),'elapsed_ns',3),[c['mean_pct'],c['low_pct'],c['high_pct']])
CM,CR=read_runs(E,'confirmation.json',216)
for v in json.loads((E/'confirmation-summary.json').read_text())['results']:
 for c in v['cells']:close(recompute(CR,dict(variant=v['variant'],cell=c['cell'],seed=c['seed']),'elapsed_ns',3),[c['mean_pct'],c['low_pct'],c['high_pct']])
assert intervals==76
record('all948timingrows+5warmups intact;76wall/thread intervals independently recomputed from raw')
PM=json.loads((E/'profiles/manifest.json').read_text());assert PM['status']=='complete' and len(PM['runs'])==12 and len(PM['calibrations'])==2
for section in ['preparation','calibrations','runs']:
 for row in PM[section]:
  raw(R,row)
  if section!='preparation':
   windows.append((row['started_utc'],row['ended_utc'],'profiles'));rr=list(csv.reader((R/row['stderr']).open()));head=[r for r in rr if r[0]=='PROFILE'];pcs=[r for r in rr if r[0]=='PC'];assert len(head)==1 and int(head[0][3])==len(pcs) and head[0][4]=='0'
for row in json.loads((E/'profiles/summary.json').read_text()):assert row['controls'] and sum(row['counts'].values())==row['samples']
record('12profiles/2calibrations pass conservation;all raw logs intact')
windows.sort();assert len(windows)==967
for a,b in zip(windows,windows[1:]):assert a[1]<=b[0],(a,b)
for row in PM['preparation']:
 for a,b,_ in windows:assert row['ended_utc']<=a or row['started_utc']>=b
record('all967measured/warmup/profile windows serial;profile builds do not overlap any')
for directory in [E,D,B,O/'AA-009']:
 for p in directory.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:assert (b'/' + b'Users/') not in p.read_bytes() and (b'/' + b'private/var/') not in p.read_bytes(),str(p.relative_to(R))
record('new public evidence contains no private machine path prefixes')
result=dict(status='pass',checks=checks,intervals_recomputed=intervals,windows=len(windows),first_window=windows[0],last_window=windows[-1],review='Sequential coordinator audit;not independent agent')
(O/'ROUND-009-VERIFY.json').write_text(json.dumps(result,indent=2)+'\n')
