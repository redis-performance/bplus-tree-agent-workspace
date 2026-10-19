import csv,datetime,hashlib,json,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
M={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runs':[]}
def perm(n,seed,skip=0):
 mask=(1<<64)-1
 def draw():
  nonlocal seed
  seed=(seed+0x9e3779b97f4a7c15)&mask;z=seed;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask
  return z^(z>>31)
 for _ in range(skip):draw()
 a=list(range(n))
 for i in range(n,1,-1):
  j=draw()%i;a[i-1],a[j]=a[j],a[i-1]
 f=14695981039346656037
 for v in a:f=((f^v)*1099511628211)&mask
 return a,f
variant=sys.argv[1] if len(sys.argv)>1 else None
for build in ([variant,variant+'-sanitize'] if variant else ['base','sanitize']):
 for n in [1,17,257]:
  for size in [8,16,319,320,321,1024]:
   for case in ['lookup-hit','lookup-miss','rank','update']:
    ops=n+3;query,qfp=perm(n,11);_,cfp=perm(n,7,16)
    cmd=[str(P/'build'/build),'--size',str(n),'--member-bytes',str(size),'--ops',str(ops),'--seed','7','--query-seed','11','--query-order','independent','--case',case]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=30);assert r.returncode==0,(cmd,r.stderr)
    row=list(csv.DictReader(r.stdout.splitlines()))[0]
    expected=sum(query[i%n] for i in range(ops)) if case in ['lookup-hit','rank'] else 0 if case=='lookup-miss' else ops
    assert int(row['checksum'])==expected
    assert int(row['construction_fingerprint'])==cfp and int(row['query_fingerprint'])==qfp
    assert int(row['operations'])==ops and int(row['cpu_start'])==2 and int(row['cpu_end'])==2
    assert int(row['tree_bytes'])>0 and abs(float(row['ns_per_op'])-int(row['elapsed_ns'])/ops)<=.00051
    M['runs'].append(dict(build=build,row=row))
M.update(status='pass',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),harness_sha256=hashlib.sha256((P/'lookup.c').read_bytes()).hexdigest())
(P/(('validation-'+variant if variant else 'validation')+'.json')).write_text(json.dumps(M,indent=2)+'\n')
print('PASS',len(M['runs']),'native/sanitizer fixture cells')
