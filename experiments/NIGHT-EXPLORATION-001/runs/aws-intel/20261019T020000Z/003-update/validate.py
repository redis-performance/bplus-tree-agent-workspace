import csv,datetime,hashlib,json,subprocess
from pathlib import Path
P=Path(__file__).resolve().parent
M={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':[]}
def perm(n,seed):
 a=list(range(n));mask=(1<<64)-1
 for i in range(n,1,-1):
  seed=(seed+0x9e3779b97f4a7c15)&mask;z=seed;z=((z^(z>>30))*0xbf58476d1ce4e5b9)&mask;z=((z^(z>>27))*0x94d049bb133111eb)&mask;z^=z>>31;j=z%i;a[i-1],a[j]=a[j],a[i-1]
 return a
for build in ['release','sanitize']:
 for n in [1,17,257]:
  for b in [8,16,319,320,321,1024]:
   for pattern in ['same','position','nearby','distant','original']:
    for ops in [n+3,3*n]:
     cmd=[str(P/'build'/build),'--size',str(n),'--ops',str(ops),'--member-bytes',str(b),'--seed','7','--query-seed','11','--query-order','independent','--case','update','--pattern',pattern]
     r=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
     assert r.returncode==0,(cmd,r.stdout,r.stderr)
     row=list(csv.DictReader(r.stdout.splitlines()))[0]
     expected=[i if pattern=='original' else 4*i+(i&1) for i in range(n)]
     query=perm(n,11)
     for i in range(ops):
      key=query[i%n];turn=i//n+1;base=key if pattern=='original' else 4*key+(key&1)
      if pattern=='position':expected[key]=base+(turn&1)
      elif pattern=='nearby':expected[key]=4*(key^1)+((key^1)&1) if (turn&1) and (key^1)<n else base
      elif pattern=='distant':expected[key]=base+(turn&1)*8*n
      elif pattern=='original':expected[key]=base+turn*n
     assert int(row['final_score_sum'])==sum(expected) and row['pattern']==pattern
     assert int(row['operations'])==ops and int(row['checksum'])==ops
     M['rows'].append(dict(build=build,row=row))
M.update(status='pass',finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),harness_sha256=hashlib.sha256((P/'update.c').read_bytes()).hexdigest())
(P/'validation.json').write_text(json.dumps(M,indent=2)+'\n');print('PASS',len(M['rows']),'cells')
