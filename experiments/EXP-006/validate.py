from pathlib import Path
import ast,csv,datetime,hashlib,itertools,json,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];D=P/'validation';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
M=dict(status='running',freeze_sha256=sha(P/'freeze.json'),plan_sha256=sha(P/'PLAN.md'),runs=[],binaries={});scope={'mask':(1<<64)-1}
T=ast.parse((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-007/attempt-002/validate.py').read_text())
for name in ['draw','permutation']:
 f=next(n for n in T.body if isinstance(n,ast.FunctionDef) and n.name==name);exec(compile(ast.Module(body=[f],type_ignores=[]),'<fixture-model>','exec'),scope)
def save():(P/'validation.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B):
 assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,18,5,33,tzinfo=datetime.timezone.utc)
 out=D/(tag+'.stdout');err=D/(tag+'.stderr');r=dict(name=tag,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save()
 if rc!=0:M['status']='failed';save();raise SystemExit((tag,rc))
 return out.read_text()
for v in ['control','A','B','C']:
 B=S/v
 for n,h in F['files'][v].items():assert sha(B/n)==h
 (B/'build').mkdir()
 for kind in ['release','sanitize']:
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  prefix=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags];support=['compat/standalone.c','vendor/redis/siphash.c','-lm']
  for name,source,extra,included in [('upstream','tests/upstream.c',['-DREDIS_TEST'],False),('raw','tests/raw_guard_oracle.c',[],False),('tags','tests/tag_search_oracle.c',[],True),('batch','bench/batch_lookup.c',[],False)]:
   binary='build/'+kind+'-'+name;run(v+'-'+kind+'-'+name+'-build',prefix+extra+[source]+([] if included else ['src/zset_btree.c'])+support+['-o',binary],B);M['binaries'][v+'-'+kind+'-'+name]=sha(B/binary);save()
   if name!='batch':
    out=run(v+'-'+kind+'-'+name,[binary],B)
    if name=='tags':assert 'PASS tagchecks=1585152' in out
    elif name=='raw':assert 'PASS fixtures=4' in out
    else:assert '43 tests' in out or '43 passed' in out or '43 passed, 0 failed' in out
  cells=0
  for n,bytes_,batch,layout in itertools.product([17,257],[16,320],[1,3,16],['hit','miss','mixed']):
   ops=n+3;args=['build/'+kind+'-batch','--size',str(n),'--ops',str(ops),'--member-bytes',str(bytes_),'--batch-size',str(batch),'--layout',layout,'--seed','80603','--query-seed','80611','--warmup-passes','2'];out=run(f'{v}-{kind}-fixture{cells}',args,B);row=next(csv.DictReader(out.splitlines()));q,qfp=scope['permutation'](n,80611,0)
   hits=[i for i in range(ops) if layout=='hit' or (layout=='mixed' and i%2==0)]
   for k,x in dict(operations=ops,api_calls=(ops+batch-1)//batch,hits=len(hits),checksum=sum(q[i%n]+1 for i in hits),query_fingerprint=qfp).items():assert int(row[k])==x
   cells+=1
  assert cells==36;print(v,kind,'43tests/raw/tags/36fixtures PASS',flush=True)
 for n,h in F['files'][v].items():assert sha(B/n)==h
M['status']='complete';save()
