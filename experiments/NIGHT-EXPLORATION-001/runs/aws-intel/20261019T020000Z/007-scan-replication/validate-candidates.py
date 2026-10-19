from pathlib import Path
import subprocess,json,hashlib,datetime,io,tarfile
root=Path.cwd();p=Path(__file__).parent;records=[];freeze={};d=root/'scratch/intel-scan-replication'
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def run(cmd,name,cwd):
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=120)
 (p/(name+'.stdout')).write_text(r.stdout);(p/(name+'.stderr')).write_text(r.stderr)
 records.append(dict(name=name,command=cmd,cwd=str(cwd.relative_to(root)),started_utc=t,finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(p/'validation-processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']
assert sha(d/'base/build/btree-bench')=='b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2'
for v in ['base','A','B']:
 dest=d/v
 if v!='base':
  dest.mkdir(exist_ok=False)
  data=subprocess.check_output(['git','archive','8fab511e','src','compat','vendor/redis','tests','bench','Makefile']);tarfile.open(fileobj=io.BytesIO(data)).extractall(dest)
  run(['patch','-p1','-i',str((p/'variants'/v/'candidate.patch').resolve())],v+'-patch',dest)
  run(['make','CC=clang','BUILD=build','OPT=-O3','build/btree-bench'],v+'-timing-build',dest)
 (dest/'tests/all_match_guard_oracle_v2.c').write_bytes((p/'all_match_guard_oracle_v2.c').read_bytes())
 for mode in ['native','san']:
  f=flags+(['-O3'] if mode=='native' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'])
  run(['make','CC=clang','BUILD=build/'+mode,'CFLAGS='+' '.join(f),'LDFLAGS='+('' if mode=='native' else '-fsanitize=address,undefined'),'check'],v+'-'+mode+'-original-tests',dest)
  for portable in ([False] if v=='base' else [False,True]):
   macro=[] if not portable else ['-D'+{'A':'ZBT_FORCE_PORTABLE_TAG_MATCHES','B':'ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE'}[v]]
   tag=v+'-'+mode+('-portable' if portable else '')+'-v2';binary='build/'+mode+'/'+('portable-' if portable else '')+'oracle-v2'
   run(['clang',*f,*macro,'-Isrc','-Icompat','-Ivendor/redis','tests/all_match_guard_oracle_v2.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',binary],tag+'-build',dest)
   run([binary],tag,dest)
 freeze[v]={f:sha(dest/f) for f in ['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','vendor/redis/siphash.c','tests/upstream.c','Makefile','tests/all_match_guard_oracle_v2.c','build/btree-bench','build/native/btree-test','build/san/btree-test']}
for f in freeze['base']:
 if not f.startswith('build/') and f!='src/zset_btree.c':assert len({freeze[v][f] for v in freeze})==1
assert freeze['base']['build/btree-bench']=='b598d273956f17e79480f0343eaaed5f9bd96170dfa36058b3d679e5f1adbdc2'
(p/'candidate-freeze.json').write_text(json.dumps(freeze,indent=2)+'\n');print('PASS original native/san tests; V2 oracle native/san all sources; candidate portable native/san; unchanged baseline binary')
