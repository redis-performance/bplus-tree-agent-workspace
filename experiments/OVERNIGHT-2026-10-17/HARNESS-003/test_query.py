"""Independent Python fixture oracle; never uses benchmark's expected checksum."""
import csv,io,subprocess,sys
from pathlib import Path
BIN=Path(sys.argv[1]).resolve(); MASK=(1<<64)-1

def draws(seed):
 while True:
  seed=(seed+0x9e3779b97f4a7c15)&MASK;z=seed
  z=((z^(z>>30))*0xbf58476d1ce4e5b9)&MASK;z=((z^(z>>27))*0x94d049bb133111eb)&MASK
  yield z^(z>>31)
def permutation(n,seed,skip=0):
 rng=draws(seed)
 for _ in range(skip):next(rng)
 a=list(range(n))
 for i in range(n,1,-1):
  j=next(rng)%i;a[i-1],a[j]=a[j],a[i-1]
 return a
def fp(a):
 h=14695981039346656037
 for x in a:h=((h^x)*1099511628211)&MASK
 return str(h)
def run(args):
 p=subprocess.run([str(BIN),*map(str,args)],capture_output=True,text=True,timeout=120)
 assert p.returncode==0,(args,p.stderr)
 return list(csv.DictReader(io.StringIO(p.stdout)))
cells=0
for n in [1,31,128,1000]:
 for size in [8,16,319,320,321]:
  for seed,qseed in [(1,2),(101,307)]:
   ops=2*n+1;construction=permutation(n,seed,16)
   common=['--size',n,'--ops',ops,'--member-bytes',size,'--seed',seed,'--query-seed',qseed]
   coupled=run(common);independent=run(common+['--query-order','independent'])
   for mode,rows in [('coupled',coupled),('independent',independent)]:
    q=construction if mode=='coupled' else permutation(n,qseed)
    assert len(rows)==8
    for r in rows:
     assert r['construction_order']=='shuffled' and r['construction_fingerprint']==fp(construction)
     assert r['query_order']==mode and r['query_seed']==str(qseed) and r['query_fingerprint']==fp(q)
     c=r['case'];count=int(r['operations']);checksum=int(r['checksum'])
     assert r['warmup_case']==('none' if c=='insert' else 'lookup-miss' if c=='lookup-miss' else 'lookup-hit')
     if c in ['lookup-hit','rank']:assert count==ops and checksum==sum(q)*(ops//n)+sum(q[:ops%n])
     if c in ['lookup-miss','insert']:assert checksum==0
     if c in ['update','delete']:assert checksum==count
     if c in ['insert','delete']:assert count==n
     if c=='iterate':assert count==3*n and checksum==3*n*(n-1)//2
     if c=='scan':assert count>=3*n # internal binary member/full-scan oracle also runs
    cells+=1
   for a,b in zip(coupled,independent):
    # Mutating update order may change final tree shape; do not assert equal memory there.
    if a['case']!='update':assert a['tree_bytes']==b['tree_bytes'],a['case']
   # Explicit coupled with different query seed preserves historical order.
   extra=run(common+['--query-order','coupled','--query-seed',999,'--case','lookup-hit'])[0]
   assert extra['query_fingerprint']==fp(construction)
# Independent query permutation stays fixed across construction seeds.
a=run(['--size',128,'--case','lookup-hit','--query-order','independent','--seed',1,'--ops',257])[0]
b=run(['--size',128,'--case','lookup-hit','--query-order','independent','--seed',99,'--ops',257])[0]
assert a['query_fingerprint']==b['query_fingerprint'] and a['construction_fingerprint']!=b['construction_fingerprint']
for args in [['--query-order','bad'],['--query-seed','0'],['--query-seed','-1'],['--query-seed','junk'],['--query-seed','100000001'],['--query-order']]:
 p=subprocess.run([str(BIN),*args],capture_output=True,timeout=120);assert p.returncode==2,args
print(f'PASS {cells} all-case fixture cells; independent PRNG/fingerprints, partial-pass checksums, query-seed independence, malformed inputs')
