import pathlib,subprocess,shutil,json,hashlib,datetime
root=pathlib.Path.cwd();d=root/'scratch/amd-scan-build';d.mkdir(exist_ok=False);records=[]
def run(cmd,name,cwd):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,timeout=300)
 except subprocess.TimeoutExpired as e:
  records.append(dict(name=name,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),timeout=True));(d/'processes.json').write_text(json.dumps(records,indent=2)+'\n');raise
 (d/(name+'.stdout')).write_text(r.stdout);(d/(name+'.stderr')).write_text(r.stderr)
 records.append(dict(name=name,command=cmd,start=start,end=datetime.datetime.now(datetime.timezone.utc).isoformat(),returncode=r.returncode));(d/'processes.json').write_text(json.dumps(records,indent=2)+'\n');r.check_returncode()
oracles={'all_match_guard_oracle':[[]],'scan_interval_oracle':[[]],'wide_scan_oracle':[['7'],['19']],'live_widen_scan_oracle':[['7'],['19']],'resize_generation_oracle':[[]]}
flags_native=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3']
for v in ['base','A','B','C']:
 dest=d/v;dest.mkdir()
 for part in ['src','compat','vendor','bench','tests']:shutil.copytree(root/part,dest/part)
 shutil.copy(root/'Makefile',dest/'Makefile')
 shutil.copy(root/'scratch/amd-scan-input/all_match_guard_oracle_v2.c',dest/'tests/all_match_guard_oracle.c')
 if v!='base':run(['patch','-p1','-i',str(root/'scratch/amd-scan-input/variants'/v/'candidate.patch')],v+'-patch',dest)
 for mode in ['native','san']:
  flags=flags_native if mode=='native' else ['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  run(['make','CC=clang','BUILD=build/'+mode,'CFLAGS='+' '.join(flags),'LDFLAGS='+('-fsanitize=address,undefined' if mode=='san' else ''),'all','check'],v+'-'+mode+'-build-test',dest)
  for oracle,seeds in oracles.items():
   run(['clang',*flags,'-Isrc','-Icompat','-Ivendor/redis','tests/'+oracle+'.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode+'/'+oracle],v+'-'+mode+'-'+oracle+'-build',dest)
   for seed in seeds:run(['build/'+mode+'/'+oracle,*seed],v+'-'+mode+'-'+oracle+('-'+seed[0] if seed else ''),dest)
 # Source-local fallback selectors only for bounded semantic checks, never timing.
 selector={"base":[],"A":["-DZBT_FORCE_PORTABLE_TAG_MATCHES"],"B":["-DZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE"],"C":["-DZBT_LEAF_TAG_MATCHES_SCALAR"]}[v]
 for mode in ['native','san']:
  flags=flags_native if mode=='native' else ['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']
  run(['clang',*flags,*selector,'-Isrc','-Icompat','-Ivendor/redis','tests/all_match_guard_oracle.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/'+mode+'/portable-oracle'],v+'-'+mode+'-portable-build',dest)
  run(['build/'+mode+'/portable-oracle'],v+'-'+mode+'-portable-oracle',dest)
files=['src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','compat/server.h','Makefile','tests/upstream.c','vendor/redis/siphash.c','vendor/redis/sds.h','vendor/redis/testhelp.h','build/native/btree-bench','build/native/btree-test','build/san/btree-test']+['tests/'+x+'.c' for x in oracles]
manifest={v:{f:hashlib.sha256((d/v/f).read_bytes()).hexdigest() for f in files} for v in ['base','A','B','C']}
for f in files:
 if f.startswith('build/') or f=='src/zset_btree.c':continue
 assert len({manifest[v][f] for v in manifest})==1,(f,'referee mismatch')
(d/'freeze.json').write_text(json.dumps(manifest,indent=2)+'\n')
