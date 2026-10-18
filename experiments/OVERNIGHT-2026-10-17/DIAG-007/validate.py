from pathlib import Path
import subprocess,json,hashlib,csv,io
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-007/base'
assert not (P/'validation.json').exists();records=[];mask=(1<<64)-1
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def perm(n,seed,skip=0):
 def draw():
  nonlocal seed
  seed=(seed+0x9e3779b97f4a7c15)&mask;z=seed
  z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask
  return z^(z>>31)
 for _ in range(skip):draw()
 a=list(range(n))
 for i in range(n,1,-1):
  j=draw()%i;a[j],a[i-1]=a[i-1],a[j]
 return a
def fp(a):
 h=14695981039346656037
 for x in a:h=((h^x)*1099511628211)&mask
 return str(h)
def run(kind,name,cmd):
 row=dict(kind=kind,name=name,command=cmd,cwd=str(B.relative_to(R)))
 out=P/f'{kind}-{name}.stdout';err=P/f'{kind}-{name}.stderr'
 with out.open('w') as so,err.open('w') as se:
  try:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120);code=q.returncode
  except subprocess.TimeoutExpired:code='timeout'
 row.update(returncode=code,stdout=out.name,stderr=err.name,stdout_sha256=sha(out),stderr_sha256=sha(err))
 records.append(row);(P/'validation.json').write_text(json.dumps(records,indent=2)+'\n');assert code==0,row
 return out
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 (B/f'build/{kind}').mkdir(parents=True)
 binary=f'build/{kind}/btree-bench'
 run(kind,'build',['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary])
 for size in [16,320]:
  for miss in [0,1]:
   for qs in [1409,1423]:
    out=run(kind,f'{size}-{miss}-{qs}',[binary,'997','1999',str(size),'4',str(miss+1),str(qs),'2'])
    rows=list(csv.DictReader(out.open()));q=perm(997,qs);assert len(rows)==4
    for w,r in enumerate(rows):
     expected=0 if miss else sum(q[(w*1999+i)%997] for i in range(1999))
     assert r['window']==str(w) and r['windows']=='4' and r['operations']=='1999'
     assert int(r['checksum'])==int(r['expected'])==expected
     assert r['construction_fingerprint']==fp(perm(997,1301,16)) and r['query_fingerprint']==fp(q)
     assert int(r['elapsed_ns'])>0 and int(r['thread_elapsed_ns'])>0
     assert int(r['outer_elapsed_ns'])==sum(int(x['elapsed_ns']) for x in rows)+int(r['gap_ns'])
    assert len({r['tree_bytes'] for r in rows})==1
 print(kind,'PASS eight cells / 32 windows; independent partial-pass oracle',flush=True)
