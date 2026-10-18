from pathlib import Path
import json,hashlib,subprocess,itertools,csv,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P/'freeze.json').read_text());S=R/F['snapshot_root'];D=P/'validation';D.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[];binaries={}
def run(name,cmd,B):
 with (D/(name+'.stdout')).open('w') as so,(D/(name+'.stderr')).open('w') as se:
  try:q=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120);rc=q.returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),returncode=rc,stdout_sha256=sha(D/(name+'.stdout')),stderr_sha256=sha(D/(name+'.stderr')));rows.append(row);(P/'validation.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name;return D/(name+'.stdout')
for v in ['control','A']:
 B=S/v;(B/'build').mkdir()
 for kind in ['release','sanitize']:
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer',*flags,'bench/iterator_modes.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}'];run(v+'-'+kind+'-build',cmd,B)
  for caller,mask,d,e,b in itertools.product(['dynamic','fixed'],[4,6,7],['forward','reverse'],['integer','fraction','wide','zero'],[16,320]):
   name=f'{v}-{kind}-{caller}-m{mask}-{d}-{e}-b{b}';out=run(name,[f'build/{kind}','--caller',caller,'--mask',str(mask),'--direction',d,'--encoding',e,'--member-bytes',str(b),'--size','129','--ops','1000','--seed','14107'],B);data=list(csv.DictReader(out.open()));assert len(data)==1;r=data[0];assert r['operations']=='1032' and r['traversals']=='8' and r['checksum']==r['expected_checksum']
  binaries[v+'-'+kind]=sha(B/f'build/{kind}');print(v,kind,'192 fixture cells PASS',flush=True)
for v,files in F['files'].items():
 for name,h in files.items():assert sha(S/v/name)==h
(P/'binaries.json').write_text(json.dumps(binaries,indent=2)+'\n')
