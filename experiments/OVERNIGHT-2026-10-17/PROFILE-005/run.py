from pathlib import Path
import collections,csv,datetime,difflib,hashlib,json,os,shutil,subprocess,time,sys
ROOT=Path(__file__).resolve().parent;R=ROOT.parents[2];variant=sys.argv[1];assert variant in ['control','C'];P=ROOT/variant;P.mkdir();S=R/('scratch/overnight-profile-005-'+variant);B=S/'base';B.mkdir(parents=True);D=S/'raw';D.mkdir()
H=ROOT.parent/'HARNESS-007/attempt-002';F=json.loads((H/'freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
for n,h in F['files'].items():
 src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
F6=json.loads((R/'experiments/EXP-006/freeze.json').read_text());src=R/F6['snapshot_root']/variant/'src/zset_btree.c';assert sha(src)==F6['files'][variant]['src/zset_btree.c'];shutil.copy2(src,B/'src/zset_btree.c')
for name in ['self_sampler.h','calibrate.c']:shutil.copy2(R/'scratch/overnight-diag-009/base/bench'/name,B/'bench'/name)
p=B/'bench/batch_lookup.c';old=p.read_text();s=old.replace('int main(int argc,char **argv){','#include "self_sampler.h"\nint main(int argc,char **argv){\n sample_init();')
s=s.replace('uint64_t start=now_ns();','sample_start();uint64_t start=now_ns();').replace('uint64_t elapsed=now_ns()-start;int64_t te=thread_ns();','uint64_t elapsed=now_ns()-start;sample_stop();int64_t te=thread_ns();').replace('serverAssert(r.checksum==expected','sample_dump(layout);\n serverAssert(r.checksum==expected');p.write_text(s)
(P/'profile.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='a/bench/batch_lookup.c',tofile='b/bench/batch_lookup.c')))
files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};(B/'build').mkdir()
M=dict(status='frozen',base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),files=files,plan_sha256=sha(ROOT/'PLAN.md'),frozen_utc=utc(),runs=[],captures=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,interval=None):
 assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,18,6,2,tzinfo=datetime.timezone.utc)
 out=D/(tag+'.stdout');err=D/(tag+'.stderr');r=dict(name=tag,command=args,cwd=str(B.relative_to(R)),started_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),interval=interval)
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,timeout=120,env=dict(os.environ,PROFILE_USEC=str(interval)) if interval else None).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save()
 if rc!=0:M['status']='failed';save();raise SystemExit((tag,rc))
 return out,err,r
def symbols(tag,err,binary):
 raw=list(csv.reader(err.open()));heads=[x for x in raw if x[0]=='PROFILE'];pcs=[x for x in raw if x[0]=='PC'];assert len(heads)==1 and int(heads[0][3])==len(pcs) and heads[0][4]=='0'
 local=[x for x in pcs if x[1]==binary];bases={x[3] for x in local};assert len(bases)==1
 addresses=sorted({x[2] for x in local});out,_,_=run(tag+'-symbols',['atos','-o','build/'+binary,'-l',next(iter(bases)),*addresses]);syms=out.read_text().splitlines();assert len(syms)==len(addresses);mapping=dict(zip(addresses,syms));counts=collections.Counter()
 for x in pcs:counts[mapping[x[2]].split(' (in ')[0] if x[1]==binary else x[4]]+=1
 unknown=sum(n for f,n in counts.items() if f=='unknown' or f.startswith('0x'))
 return dict(samples=len(pcs),unknown=unknown,counts=dict(counts.most_common()))
save();flags=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-O3','-Wall','-Wextra','-Werror','-DREDIS_DEBUG','-fno-omit-frame-pointer'];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm']
for name,source in [('batch-profile','batch_lookup.c'),('calibrate','calibrate.c')]:
 run(name+'-build',flags+['bench/'+source,*support,'-o','build/'+name]);run(name+'-dsym',['dsymutil','build/'+name]);M.setdefault('binaries',{})[name]=sha(B/'build'/name);save()
for interval in [1000,3001]:
 out,err,row=run('cal-'+str(interval),['build/calibrate','200000000'],interval);z=symbols('cal-'+str(interval),err,'calibrate');good=z['counts'].get('known_arithmetic',0);z['pass']=z['samples']>=20 and good/z['samples']>=.9 and z['unknown']==0;M.setdefault('calibrations',[]).append(z);save();assert z['pass'];print('calibration',interval,'PASS',flush=True)
start=time.monotonic()
for seed,qseed in [(81903,81919),(81911,81923)]:
 for interval in [1000,3001]:
  for layout,bytes_,ops in [('hit',16,50000000)]:
   assert time.monotonic()-start<240
   tag=f'{seed}-{interval}-{layout}{bytes_}';args=['build/batch-profile','--size','8192','--ops',str(ops),'--seed',str(seed),'--query-seed',str(qseed),'--layout',layout,'--member-bytes',str(bytes_),'--batch-size','1','--warmup-passes','3']
   out,err,row=run(tag,args,interval);v=next(csv.DictReader(out.open()));assert int(v['operations'])==ops;z=symbols(tag,err,'batch-profile');z.update(name=tag,layout=layout,member_bytes=bytes_,operations=ops,seed=seed,query_seed=qseed,interval_usec=interval,sufficient=z['samples']>=100 and z['unknown']==0);M['captures'].append(z);save();print(tag,z['samples'],z['sufficient'],flush=True)
for n,h in files.items():assert sha(B/n)==h
M['status']='complete';save();(P/'summary.json').write_text(json.dumps(dict(calibrations=M['calibrations'],captures=M['captures']),indent=2)+'\n')
