import pathlib,subprocess,shutil,json,hashlib,datetime
root=pathlib.Path.cwd();d=root/'scratch/amd-lowerbound-build';d.mkdir(exist_ok=False);records=[]
def run(cmd,name,cwd):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=120)
 (d/(name+'.stdout')).write_text(r.stdout);(d/(name+'.stderr')).write_text(r.stderr)
 records.append(dict(name=name,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(d/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
for v in ['base','A','B','C']:
 dest=d/v;dest.mkdir()
 for part in ['src','compat','vendor','bench','tests']:shutil.copytree(root/part,dest/part)
 shutil.copy(root/'Makefile',dest/'Makefile')
 if v!='base':run(['patch','-p1','-i',str(root/'scratch/amd-lowerbound-input/variants'/v/'candidate.patch')],v+'-patch',dest)
 shutil.copy(root/'scratch/amd-lowerbound-input/lowerbound-oracle.c',dest/'lowerbound-oracle.c')
 for mode in ['native','san']:
  flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3'] if mode=='native' else ['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  run(['make','CC=clang','BUILD=build/'+mode,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'],v+'-'+mode+'-build-test',dest)
  run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','lowerbound-oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode+'/lowerbound-oracle'],v+'-'+mode+'-oracle-build',dest)
  run(['build/'+mode+'/lowerbound-oracle','17'],v+'-'+mode+'-oracle',dest)
files=['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','compat/server.h','Makefile','tests/upstream.c','vendor/redis/siphash.c','vendor/redis/sds.h','vendor/redis/testhelp.h','build/native/btree-bench','build/native/btree-test','build/san/btree-test','lowerbound-oracle.c']
manifest={v:{f:hashlib.sha256((d/v/f).read_bytes()).hexdigest() for f in files} for v in ['base','A','B','C']}
for f in files:
 if f.startswith('build/') or f=='src/zset_btree.c':continue
 assert len({manifest[v][f] for v in manifest})==1,(f,'referee mismatch')
(d/'freeze.json').write_text(json.dumps(manifest,indent=2)+'\n')
