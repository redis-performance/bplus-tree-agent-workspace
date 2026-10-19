import csv,json,hashlib,sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
P=Path(sys.argv[1]);O=Path(sys.argv[2]);R=P/'aa';J=lambda n:json.loads((P/n).read_text());sha=lambda b:hashlib.sha256(b).hexdigest()
pub=J('aa/PUBLICATION.json')
for n,v in pub.items():assert sha((R/n).read_bytes())==v['public_sha256'],n
result=J('aa/result.json');freeze=J('execution-freeze.json');profile=J('profile/complete.json');build=J('profile/build-freeze.json')
assert result['binary_sha256_before']==result['binary_sha256_after']==freeze['actual_timing_binary_sha256']
assert result['source_hashes_before']==result['source_hashes_after']==build['source_hashes']
for key,path in [('execution_freeze_sha256','execution-freeze.json'),('profile_audit_sha256','profile/audit.json'),('profile_mapping_sha256','profile/code-map.json')]:assert result[key]==sha((P/path).read_bytes())
assert datetime.fromisoformat(profile['finished_utc'])<datetime.fromisoformat(result['started_utc'])
expected=[]
for block in range(6):
 for n in ([100000,1000000] if block%2==0 else [1000000,100000]):
  for pos,label in enumerate('ABBA'):expected.append(dict(index=len(expected),block=block,size=n,seed=701+block%3,position=pos,label=label,case='iterate',requested_ops=50000000,member_bytes=16,binary='baseline'))
assert expected==J('aa-schedule.json');runs=result['runs'];assert len(runs)==len(expected)==48
last=datetime.fromisoformat(result['started_utc']);groups=defaultdict(list);memory=defaultdict(set)
for e,r in zip(expected,runs):
 for key in ['block','seed','size','position','label']:assert r[key]==e[key]
 name=f"b{e['block']}-n{e['size']}-p{e['position']}-{e['label']}";assert r['name']==name
 assert r['command']==['<corrected-baseline>/build/adapter-requalification/btree-bench','--case','iterate','--size',str(e['size']),'--ops','50000000','--member-bytes','16','--seed',str(e['seed'])]
 assert r['returncode']==0 and not (R/(name+'.stderr')).read_text().strip()
 start=datetime.fromisoformat(r['started_utc']);end=datetime.fromisoformat(r['finished_utc']);assert last<=start<=end;last=end
 rows=list(csv.DictReader((R/(name+'.csv')).read_text().strip().splitlines()));assert len(rows)==1 and rows[0]==r['row'];x=rows[0];n=e['size']
 contract=dict(case='iterate',size=n,seed=e['seed'],requested_ops=50000000,member_bytes=16,operations=50000000,traversals=50000000//n,warmup_passes=1,cpu_start=2,cpu_end=2,checksum=50000000*(n-1)//2)
 for k,v in contract.items():assert x[k]==str(v),(name,k)
 elapsed=int(x['elapsed_ns']);assert elapsed>0
 assert abs(float(x['ns_per_op'])-elapsed/50000000)<=.000501
 assert abs(float(x['ops_per_sec'])-50000000*1e9/elapsed)<=.000501
 memory[(n,e['seed'])].add(int(x['tree_bytes']));groups[(n,e['block'])].append(elapsed)
assert all(len(x)==1 for x in memory.values());assert (last-datetime.fromisoformat(result['started_utc'])).total_seconds()<300
effects=[];summary={}
for n in [100000,1000000]:
 for block in range(6):
  a,b,c,d=groups[(n,block)];pct=((b+c)/(a+d)-1)*100;minimum=min(a,b,c,d)
  effects.append(dict(size=n,block=block,seed=701+block%3,effect_pct=pct,min_window_ns=minimum,qualified=abs(pct)<=1 and minimum>=10000000))
 es=[e for e in effects if e['size']==n];summary[str(n)]=dict(qualified=all(x['qualified'] for x in es),max_abs_pct=max(abs(x['effect_pct']) for x in es),minimum_window_ns=min(x['min_window_ns'] for x in es))
published=J('aa/audit.json')
for actual,reported in zip(effects,published['effects']):
 assert actual.keys()==reported.keys()
 for k,v in actual.items():
  if k=='effect_pct':assert abs(v-reported[k])<1e-12,(actual,reported)
  else:assert v==reported[k],(actual,reported)
for n,actual in summary.items():
 for k,v in actual.items():
  if k=='max_abs_pct':assert abs(v-published['summary'][n][k])<1e-12
  else:assert v==published['summary'][n][k]
assert not published['both_sizes_qualified']
for n,h in published['raw_sha256'].items():assert pub[n]['raw_sha256']==h
out=dict(status='PASS',input_revision='6d19f4df4',reviewer='/root/aws_arm',public_hashes_verified=len(pub),processes=48,blocks=12,serial=True,cpu=2,exact_schedule=True,source_identity_manifests_match=True,live_binary_read=False,binary_sha256=result['binary_sha256_before'],source_commit=freeze['source_commit'],summary=summary,effects=effects,source_selection='NONE',candidate_measurements=0,limits=['Independent review of immutable public CSV and identity manifests; no live runner access.','Failed first100K block retained; no retry/exclusion/duration change.','Qualified1M is baseline timer qualification only, not an optimization gain.'])
O.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
