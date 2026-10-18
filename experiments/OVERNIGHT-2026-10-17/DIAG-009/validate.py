from pathlib import Path
import subprocess,json,hashlib,os,csv
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-009/base';S=B.parent
assert not (P/'validation.json').exists();records=[]
def run(name,cmd,mode=None):
 out=S/(name+'.stdout');err=S/(name+'.stderr')
 with out.open('w') as so,err.open('w') as se:
  try:p=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120,env=dict(os.environ,PROFILE_USEC=mode) if mode is not None else None);code=p.returncode
  except subprocess.TimeoutExpired:code='timeout'
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),returncode=code,profile_usec=mode,stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),stderr_sha256=hashlib.sha256(err.read_bytes()).hexdigest())
 records.append(row);(P/'validation.json').write_text(json.dumps(records,indent=2)+'\n');assert code==0,row
 return out,err
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 (B/f'build/{kind}').mkdir(parents=True)
 binary=f'build/{kind}/calibrate';cmd=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags,'bench/calibrate.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
 run(kind+'-build',cmd)
 for mode in ['0','1000']:
  out,err=run(kind+'-smoke-'+mode,[binary,'10000'],mode)
  row=next(csv.DictReader(out.open()));assert row['checksum']=='80000' and row['requested_usec']==mode
  if mode=='0':assert row['samples']=='0'
 print(kind,'PASS',flush=True)
run('dsym',['dsymutil','build/release/calibrate'])
out,err=run('atomic-imports',['nm','-u','build/release/calibrate']);assert 'atomic' not in out.read_text()
run('uuid',['xcrun','dwarfdump','--uuid','build/release/calibrate','build/release/calibrate.dSYM'])
