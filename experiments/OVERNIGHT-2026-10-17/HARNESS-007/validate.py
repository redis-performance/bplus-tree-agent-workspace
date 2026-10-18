from pathlib import Path
import csv,datetime,difflib,hashlib,itertools,json,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-harness-007/base'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
assert not (P/'validation.json').exists();(P/'raw').mkdir();(B/'build/batch').mkdir(parents=True)
F=json.loads((P.parent/'HARNESS-003/freeze.json').read_text())
for n,h in F['files'].items():assert sha(B/n)==h
files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()}
freeze=dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),parent_freeze_sha256=sha(P.parent/'HARNESS-003/freeze.json'),provenance='uncommitted isolated additional batch referee; source and inherited referee unchanged',frozen_utc=utc(),files=files)
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
(P/'harness.patch').write_text(''.join(difflib.unified_diff([], (B/'bench/batch_lookup.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/bench/batch_lookup.c')))
M=dict(status='running',plan_sha256=sha(P/'PLAN.md'),freeze_sha256=sha(P/'freeze.json'),runs=[],binaries={});start=time.monotonic()
def save():(P/'validation.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,cmd,expected=0):
 row=dict(name=tag,command=cmd,cwd=str(B.relative_to(R)),started_utc=utc());out=P/'raw'/(tag+'.stdout');err=P/'raw'/(tag+'.stderr')
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(cmd,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(row);save()
 if rc!=expected:M['status']='failed';save();raise SystemExit((tag,rc))
 return out.read_text()
mask=(1<<64)-1
def draw(state):
 state=(state+0x9e3779b97f4a7c15)&mask;z=state;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask
 return state,(z^(z>>31))&mask
def permutation(n,seed,skip):
 a=list(range(n));state=seed
 for _ in range(skip):state,_=draw(state)
 for i in range(n,1,-1):state,v=draw(state);j=v%i;a[i-1],a[j]=a[j],a[i-1]
 fp=14695981039346656037
 for x in a:fp=((fp^x)*1099511628211)&mask
 return a,fp
for kind in ['release','sanitize']:
 flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
 binary='build/batch/'+kind;cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'bench/batch_lookup.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
 run(kind+'-build',cmd);M['binaries'][kind]=sha(B/binary);save();cells=0
 for n,bytes_,batch,layout,part in itertools.product([1,17,257],[8,16,319,320,4097],[1,2,3,7,15,16],['hit','miss','mixed'],[0,1]):
  assert time.monotonic()-start<900
  ops=1 if part==0 else n+3;tag=f'{kind}-{cells:04d}';args=[binary,'--size',str(n),'--ops',str(ops),'--member-bytes',str(bytes_),'--batch-size',str(batch),'--layout',layout,'--seed','80603','--query-seed','80611','--warmup-passes','2']
  rows=list(csv.DictReader(run(tag,args).splitlines()));assert len(rows)==1;v=rows[0]
  query,qfp=permutation(n,80611,0);order,cfp=permutation(n,80603,16)
  hits=[i for i in range(ops) if layout=='hit' or (layout=='mixed' and i%2==0)]
  expected=dict(size=n,requested_ops=ops,member_bytes=bytes_,seed=80603,query_seed=80611,batch_size=batch,operations=ops,api_calls=(ops+batch-1)//batch,hits=len(hits),checksum=sum(query[i%n]+1 for i in hits),warmup_passes=2,construction_fingerprint=cfp,query_fingerprint=qfp)
  for k,x in expected.items():assert int(v[k])==x,(tag,k,v[k],x)
  assert v['case']==layout and v['qos_effective']=='unknown' and int(v['tree_bytes'])>0
  elapsed=int(v['elapsed_ns']);assert elapsed>0 and abs(float(v['ns_per_op'])-elapsed/ops)<=.00051
  assert abs(float(v['ops_per_sec'])-ops*1e9/elapsed)<=.001
  cells+=1
 assert cells==540;M.setdefault('cells',{})[kind]=cells;save();print(kind,cells,'PASS',flush=True)
 for i,args in enumerate([['--batch-size','17'],['--batch-size','0'],['--member-bytes','7'],['--layout','bad'],['--size','-1'],['--ops'],['--unknown','1']]):run(kind+'-invalid-'+str(i),[binary,*args],2)
for n,h in files.items():assert sha(B/n)==h
M['status']='complete';M['ended_utc']=utc();save()
