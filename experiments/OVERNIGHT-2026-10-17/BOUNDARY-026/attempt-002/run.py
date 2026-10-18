from pathlib import Path
import datetime,difflib,hashlib,json,os,re,shutil,subprocess,sys
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'scratch/overnight-boundary-026-attempt2';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();phase=sys.argv[1];F6=json.loads((R/'experiments/EXP-006/freeze.json').read_text());variants=['control','A','B','C'];D=P/phase;D.mkdir();M=dict(status='running',phase=phase,runs=[],binaries={},results=[])
def save():(D/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B,expect=True):
 assert datetime.datetime.now(datetime.timezone.utc)<datetime.datetime(2026,10,18,6,2,tzinfo=datetime.timezone.utc)
 out=D/(tag+'.stdout');err=D/(tag+'.stderr');r=dict(name=tag,command=args,cwd=str(B.relative_to(R)),started_utc=utc())
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save()
 if expect and rc!=0:M['status']='failed';save();raise SystemExit((tag,rc))
 return out.read_text(),err.read_text(),r
if phase=='discovery':
 S.mkdir();files={}
 for v in variants:
  B=S/v;B.mkdir()
  for n,h in F6['files'][v].items():
   src=R/F6['snapshot_root']/v/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
  shutil.copy2(R/'tests/heterogeneous_batch_oracle.c',B/'tests/heterogeneous_batch_oracle.c');files[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};(B/'build').mkdir()
 (P/'oracle.patch').write_text(''.join(difflib.unified_diff([], (R/'tests/heterogeneous_batch_oracle.c').read_text().splitlines(True),fromfile='/dev/null',tofile='b/tests/heterogeneous_batch_oracle.c')))
 (P/'freeze.json').write_text(json.dumps(dict(base_commit=F6['base_commit'],snapshot=str(S.relative_to(R)),files=files,plan_sha256=sha(P/'PLAN.md'),runner_sha256=sha(Path(__file__)),oracle_sha256=sha(R/'tests/heterogeneous_batch_oracle.c'),frozen_utc=utc(),provenance='uncommitted additive test; production baseline preserved'),indent=2)+'\n')
F=json.loads((P/'freeze.json').read_text());assert sha(P/'PLAN.md')==F['plan_sha256'];assert sha(Path(__file__))==F['runner_sha256'];save()
flags=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer'];support=['src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm'];oracle='tests/heterogeneous_batch_oracle.c'
if phase in ['discovery','confirm']:
 seeds=[82603,82611] if phase=='discovery' else [82703,82711];outputs={}
 for v in variants:
  B=S/v
  for n,h in F['files'][v].items():assert sha(B/n)==h
  for build in ['release','sanitize']:
   opts=['-O3'] if build=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];binary='build/'+phase+'-'+build;debug=['-DREDIS_DEBUG'] if phase=='discovery' else []
   run(v+'-'+build+'-build',flags+debug+opts+[oracle,*support,'-o',binary],B);M['binaries'][v+'-'+build]=sha(B/binary);save()
   for seed in seeds:
    out,err,row=run(f'{v}-{build}-{seed}',[binary,str(seed)],B);last=out.strip().splitlines()[-1];assert last.startswith('PASS ');nums=dict(re.findall(r'(\w+)=([0-9a-f]+)',last));assert int(nums['keys'])==1345 and int(nums['models'])==6 and int(nums['batches'])==342975
    key=(build,seed)
    if v=='control':outputs[key]=out
    else:assert out==outputs[key],(v,build,seed,'full model/memory output mismatch')
    M['results'].append(dict(variant=v,build=build,seed=seed,debug=phase=='discovery',counts=nums));save();print(phase,v,build,seed,last,flush=True)
  for n,h in F['files'][v].items():assert sha(B/n)==h
elif phase=='faults':
 for name in ['lane-zero-hash','lane-zero-length']:
  B=S/name;shutil.copytree(S/'C',B,ignore=shutil.ignore_patterns('build'));(B/'build').mkdir();p=B/'src/zset_btree.c';old=p.read_text();a=old.index('unsigned int zbtreeScores(');b=old.index('\n/* Lookup used by ZADD.',a);body=old[a:b]
  if name=='lane-zero-hash':body=body.replace('zbtIndexFind(zs, hashes[i],','zbtIndexFind(zs, hashes[0],')
  else:body=body.replace('sdslen(members[i]), &scores[i]','sdslen(members[0]), &scores[i]')
  s=old[:a]+body+old[b:];assert s!=old;p.write_text(s);(D/(name+'.patch')).write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
  run(name+'-build',flags+['-DREDIS_DEBUG','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all',oracle,*support,'-o','build/fault'],B)
  out,err,row=run(name+'-run',['build/fault','82603'],B,expect=False);detected=isinstance(row['returncode'],int) and row['returncode']!=0 and ('found==expected' in err or 'AddressSanitizer' in err or 'runtime error:' in err)
  M['results'].append(dict(fault=name,detected=detected,returncode=row['returncode'],source_sha256=sha(p),patch_sha256=sha(D/(name+'.patch'))));save();print(name,'detected',detected,flush=True)
else:raise SystemExit('discovery|confirm|faults')
M['status']='complete';save()
