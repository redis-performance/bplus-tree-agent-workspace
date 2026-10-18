from pathlib import Path
import subprocess,json,hashlib,time,csv,itertools,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot'];D=P/'validation';D.mkdir();rows=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(name,cmd,expect=0):
 out=D/(name+'.stdout');err=D/(name+'.stderr');start=time.monotonic();started=utc()
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=S,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row=dict(name=name,command=cmd,returncode=rc,started_utc=started,ended_utc=utc(),seconds=time.monotonic()-start,stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row)
 (P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==expect,name
 return out
old=[(n,b,e,d,m,'shuffled',31001) for n,b,e,d,m in itertools.product([1,31,32,33,129],[16,320],['integer','fraction','wide','zero'],['forward','reverse'],range(8))]
new=[(n,b,e,d,m,c,31013) for n,b,e,c,d,m in itertools.product([1,32,97,513],[16,320],['integer','alternating-zero'],['shuffled','ascending','descending'],['forward','reverse'],range(8))]
assert len(old)==640 and len(new)==768
old+=new
new=[(n,b,e,d,m,c,41011) for n,b,e,c,d,m in itertools.product([1,31,32,95],[16,320],['integer','wide','alternating-zero'],['trimmed','trimmed-clone','trimmed-cycle'],['forward','reverse'],range(8))]
assert len(old)==1408 and len(new)==1152
for kind in ['release','sanitize']:
 (S/f'build/{kind}').mkdir(parents=True)
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
 run(kind+'-build',common+['bench/iterator_modes.c',*support,'-o',f'build/{kind}/iterator-modes'])
 run(kind+'-upstream-build',common+['-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c',*support,'-o',f'build/{kind}/upstream'])
 run(kind+'-upstream',[f'build/{kind}/upstream'])
 for i,(n,b,e,d,m,c,seed) in enumerate(old+new):
  name=f'{kind}-{i:04d}'
  out=run(name,[f'build/{kind}/iterator-modes','--size',str(n),'--ops',str(n*2+1),'--member-bytes',str(b),'--encoding',e,'--construction',c,'--direction',d,'--mask',str(m),'--seed',str(seed)])
  data=list(csv.DictReader(out.open()));assert len(data)==1;r=data[0]
  assert int(r['operations'])==3*n and r['traversals']=='3' and r['checksum']==r['expected_checksum'] and r['construction']==c
  if i%256==0:print(kind,i,'PASS',flush=True)
 for name,args in [('bad-order',['--construction','invalid']),('bad-encoding',['--encoding','invalid']),('zero-size',['--size','0']),('zero-ops',['--ops','0']),('huge-ops',['--ops','100000001'])]:run(kind+'-'+name,[f'build/{kind}/iterator-modes',*args],2)
 print(kind,len(old)+len(new),'fixture cells plus original tests PASS',flush=True)
for name,h in F['files'].items():assert sha(S/name)==h
(P/'binaries.json').write_text(json.dumps({k:sha(S/f'build/{k}/iterator-modes') for k in ['release','sanitize']},indent=2)+'\n')
