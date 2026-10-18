from pathlib import Path
import json,hashlib,subprocess,itertools,csv,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'attempt-002/freeze.json').read_text());S=R/F['snapshot_root'];D=P/'fixtures';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[]
assert json.loads((P/'codegen-audit.json').read_text())['pass_all']
def run(name,cmd,B):
 with (D/(name+'.stdout')).open('w') as so,(D/(name+'.stderr')).open('w') as se:
  try:rc=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 rows.append(dict(name=name,command=cmd,cwd=str(B.relative_to(R)),returncode=rc,stdout_sha256=sha(D/(name+'.stdout')),stderr_sha256=sha(D/(name+'.stderr'))));(P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name;return D/(name+'.stdout')
for pad in [0,16,32,48]:
 B=S/str(pad)
 for kind in ['release','sanitize']:
  for mask,d,e,b in itertools.product(range(8),['forward','reverse'],['integer','fraction','wide','zero'],[16,320]):
   name=f'{pad}-{kind}-m{mask}-{d}-{e}-b{b}';out=run(name,[f'build/{kind}','--mask',str(mask),'--direction',d,'--encoding',e,'--member-bytes',str(b),'--size','129','--ops','1000','--seed','19103'],B);data=list(csv.DictReader(out.open()));assert len(data)==1;r=data[0];assert r['operations']=='1032' and r['traversals']=='8' and r['checksum']==r['expected_checksum']
  assert sha(B/f'build/{kind}')==F['binaries'][f'{pad}-{kind}'];print(pad,kind,'128 fixtures pass',flush=True)
 run(f'{pad}-upstream',['build/upstream'],B)
 for name,h in F['files'][str(pad)].items():assert sha(B/name)==h
assert len(rows)==1028
