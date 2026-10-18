from pathlib import Path
import subprocess,json,hashlib,os,csv,collections
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-profile-003/base';S=B.parent
assert not (P/'validation.json').exists();records=[]
def run(name,cmd,env=None):
 out=S/(name+'.stdout');err=S/(name+'.stderr')
 with out.open('w') as so,err.open('w') as se:
  try:p=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120,env=env);code=p.returncode
  except subprocess.TimeoutExpired:code='timeout'
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),returncode=code,environment_overrides={'PROFILE_USEC':env['PROFILE_USEC']} if env else {},stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),stderr_sha256=hashlib.sha256(err.read_bytes()).hexdigest())
 records.append(row);(P/'validation.json').write_text(json.dumps(records,indent=2)+'\n');print(name,code,flush=True);assert code==0
 return out,err,row
for kind in ['release','sanitize']:
 flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-DREDIS_DEBUG','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
 (B/f'build/{kind}').mkdir(parents=True)
 cmd=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags]
 support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
 run(kind+'-build',cmd+['bench/microbench.c',*support,'-o',f'build/{kind}/btree-bench'])
 out,err,row=run(kind+'-smoke',[f'build/{kind}/btree-bench','--size','1000','--ops','2501','--query-order','independent','--member-bytes','320'])
 assert len(list(csv.DictReader(out.open())))==8
 if kind=='release':
  run('calibrate-build',cmd+['bench/calibrate.c',*support,'-o','build/release/calibrate'])
  run('calibrate-dsym',['dsymutil','build/release/calibrate'])
  run('bench-dsym',['dsymutil','build/release/btree-bench'])
# Calibration measurements begin only after builds/smoke checks are all done.
for interval in [1000,3001]:
 out,err,row=run(f'calibrate-{interval}',['build/release/calibrate','400000000'],env=dict(os.environ,PROFILE_USEC=str(interval)))
 lines=list(csv.reader(err.open()));headers=[x for x in lines if x[0]=='PROFILE'];pcs=[x for x in lines if x[0]=='PC']
 assert len(headers)==1 and int(headers[0][3])==len(pcs) and headers[0][4]=='0'
 bases={x[3] for x in pcs if x[1]=='calibrate'};assert len(bases)==1
 addresses=[x[2] for x in pcs if x[1]=='calibrate']
 sym,serr,srow=run(f'calibrate-{interval}-symbols',['atos','-o','build/release/calibrate','-l',next(iter(bases)),*addresses])
 symbols=sym.read_text().splitlines();assert len(symbols)==len(addresses)
 good=sum(x.startswith('known_arithmetic ') for x in symbols)
 row.update(samples=len(pcs),known_arithmetic=good,known_share=good/len(pcs),criterion_met=len(pcs)>=20 and good/len(pcs)>=.9)
 (P/'validation.json').write_text(json.dumps(records,indent=2)+'\n')
 assert row['criterion_met'];print('calibration',interval,len(pcs),good,'PASS',flush=True)
