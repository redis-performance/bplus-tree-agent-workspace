from pathlib import Path
import subprocess,json,hashlib,time,csv,itertools
import sys
P=Path(sys.argv[1]).resolve();R=Path.cwd();F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot'];D=P/'validation';D.mkdir();rows=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run(name,cmd):
 out=D/(name+'.stdout');err=D/(name+'.stderr');start=time.monotonic()
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=S,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row=dict(name=name,command=cmd,returncode=rc,seconds=time.monotonic()-start,stdout=str(out.relative_to(P)),stderr=str(err.relative_to(P)),stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row)
 (P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name
 return out
for kind in ['release','sanitize']:
 (S/f'build/{kind}').mkdir(parents=True)
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
 run(kind+'-build',common+['bench/iterator_modes.c',*support,'-o',f'build/{kind}/iterator-modes'])
 run(kind+'-upstream-build',common+['-DREDIS_TEST','-DREDIS_DEBUG','tests/upstream.c',*support,'-o',f'build/{kind}/upstream'])
 run(kind+'-upstream',[f'build/{kind}/upstream'])
 for n,b,e,d,m in itertools.product([129],[16,320],['integer','fraction','wide','zero'],['forward','reverse'],range(8)):
  name=f'{kind}-n{n}-b{b}-{e}-{d}-m{m}'
  out=run(name,[f'build/{kind}/iterator-modes','--size',str(n),'--ops',str(n*2+1),'--member-bytes',str(b),'--encoding',e,'--direction',d,'--mask',str(m),'--seed','7103'])
  data=list(csv.DictReader(out.open()));assert len(data)==1
  row=data[0];assert int(row['operations'])==3*n and row['traversals']=='3' and row['checksum']==row['expected_checksum']
 run(kind+'-mutation-build',common+['-DREDIS_DEBUG','tests/iterator_mutation_oracle.c',*support,'-o',f'build/{kind}/mutation'])
 run(kind+'-mutation',[f'build/{kind}/mutation'])
 run(kind+'-packed-build',common+['-DREDIS_DEBUG','tests/packed_decode_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}/packed'])
 run(kind+'-packed',[f'build/{kind}/packed'])
 run(kind+'-zero-build',common+['-DREDIS_DEBUG','tests/zero_physical_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}/zero'])
 run(kind+'-zero',[f'build/{kind}/zero'])
 print(kind,'128 fixture cells plus original,mutation,packed tests PASS',flush=True)
for name,h in F['files'].items():assert sha(S/name)==h
(P/'binaries.json').write_text(json.dumps({k:sha(S/f'build/{k}/iterator-modes') for k in ['release','sanitize']},indent=2)+'\n')
