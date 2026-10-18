from pathlib import Path
import datetime,difflib,hashlib,json,shutil,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'freeze.json').read_text());S=R/'scratch/experiment006-tag-guard';S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();M=dict(status='running',plan_sha256=sha(P/'PLAN.md'),snapshots={},runs=[])
def save():(P/'manifest.json').write_text(json.dumps(M,indent=2)+'\n')
def run(tag,args,B):
 r=dict(name=tag,command=args,cwd=str(B.relative_to(R)),started_utc=utc());out=P/(tag+'.stdout');err=P/(tag+'.stderr')
 with out.open('w') as o,err.open('w') as e:
  try:rc=subprocess.run(args,cwd=B,stdout=o,stderr=e,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 r.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));M['runs'].append(r);save();return rc,out,err
for v in ['control','A','B','C','fault']:
 orig='C' if v=='fault' else v;B=S/v;B.mkdir()
 for n,h in F['files'][orig].items():
  src=R/F['snapshot_root']/orig/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 shutil.copy2(R/'tests/tag_guard_oracle.c',B/'tests/tag_guard_oracle.c')
 if v=='fault':
  p=B/'src/zset_btree.c';old=p.read_text();assert old.count('while (n >= 16)')==1;changed=old.replace('while (n >= 16)','while (n > 0)');p.write_text(changed);(P/'overread.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
 M['snapshots'][v]=dict(path=str(B.relative_to(R)),files={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()});(B/'build').mkdir();save()
 for kind in (['sanitize'] if v=='fault' else ['release','sanitize']):
  flags=['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'];binary='build/'+kind
  cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-DREDIS_DEBUG',*flags,'tests/tag_guard_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary]
  rc,_,_=run(v+'-'+kind+'-build',cmd,B);assert rc==0
  rc,out,err=run(v+'-'+kind,[binary],B)
  if v=='fault':assert isinstance(rc,int) and rc!=0 and ('AddressSanitizer' in err.read_text() or 'Assertion' in err.read_text());M['fault_detected']=True
  else:assert rc==0 and 'PASS guardchecks=198144' in out.read_text()
  print(v,kind,'DETECTED' if v=='fault' else 'PASS',flush=True)
for d in M['snapshots'].values():
 for n,h in d['files'].items():assert sha(R/d['path']/n)==h
M['status']='complete';save()
