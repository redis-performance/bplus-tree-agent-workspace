import csv,datetime,itertools,json,struct,subprocess
from pathlib import Path
P=Path(__file__).resolve().parent;rows=[]
for build,n,b,encoding,direction,mask in itertools.product(['release','sanitize'],[1,31,32,33,129],[16,320,321],['integer','fraction','wide','zero'],['forward','reverse'],range(8)):
 cmd=[str(P/'build'/build),'--size',str(n),'--ops',str(2*n+1),'--member-bytes',str(b),'--encoding',encoding,'--direction',direction,'--mask',str(mask),'--seed','7103']
 r=subprocess.run(cmd,capture_output=True,text=True,timeout=30);assert r.returncode==0,(cmd,r.stderr)
 v=list(csv.DictReader(r.stdout.splitlines()))[0];expected=0
 for i in range(n):
  score=i-n//2+.25 if encoding=='fraction' else 2**53+2*i if encoding=='wide' else (-0.0 if i==0 else float(i)) if encoding=='zero' else float(i-n//2)
  bits=struct.unpack('<Q',struct.pack('<d',score))[0]
  expected+=1+(i%256 if mask&1 else 0)+(b if mask&2 else 0)+(bits if mask&4 else 0)
 expected=(3*expected)&((1<<64)-1)
 assert int(v['checksum'])==expected and int(v['operations'])==3*n and int(v['cpu_start'])==int(v['cpu_end'])==2
 rows.append(dict(build=build,row=v))
(P/'validation.json').write_text(json.dumps(dict(status='pass',rows=rows,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n');print('PASS',len(rows),'semantic cells')
