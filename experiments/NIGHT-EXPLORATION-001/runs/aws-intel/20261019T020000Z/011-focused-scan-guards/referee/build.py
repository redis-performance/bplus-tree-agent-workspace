#!/usr/bin/env python3
"""Build isolated original-tree and never-timed diagnostic binaries. No LTO.
Use the SAME relative --out location within each isolated source snapshot.
"""
import argparse, pathlib, subprocess, json, hashlib, shutil, os
p=argparse.ArgumentParser();p.add_argument('--source',required=True,type=pathlib.Path);p.add_argument('--out',required=True,type=pathlib.Path);p.add_argument('--cc',default='clang');p.add_argument('--sanitize',action='store_true');a=p.parse_args()
here=pathlib.Path(__file__).resolve().parent;s=a.source.resolve();o=a.out.resolve();o.mkdir(parents=True,exist_ok=True);inputs=o/'inputs';inputs.mkdir(exist_ok=True)
for name in ['scan-guard.c','tree-census.c']:shutil.copyfile(here/name,inputs/name)
rel=lambda x:os.path.relpath(x,s)
flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all'] if a.sanitize else ['-O3'])
inc=['-Isrc','-Icompat','-Ivendor/redis'];commands=[]
for name,driver,tree,extra in [('scan-guard',rel(inputs/'scan-guard.c'),'src/zset_btree.c',[]),('scan-census',rel(inputs/'scan-guard.c'),rel(inputs/'tree-census.c'),['-DSCAN_CENSUS']),('upstream-test','tests/upstream.c','src/zset_btree.c',['-DREDIS_TEST','-DREDIS_DEBUG'])]:
 cmd=[a.cc,*inc,*flags,*extra,driver,tree,'compat/standalone.c','vendor/redis/siphash.c','-lm','-o',rel(o/name)]
 subprocess.run(cmd,cwd=s,check=True);commands.append(cmd)
files=[here/'scan-guard.c',here/'tree-census.c',here/'build.py',s/'src/zset_btree.c',s/'src/zset_btree.h',s/'compat/standalone.c',s/'vendor/redis/siphash.c',o/'scan-guard',o/'scan-census',o/'upstream-test']
(o/'build-manifest.json').write_text(json.dumps({'compiler':subprocess.check_output([a.cc,'--version'],text=True),'flags':flags,'commands':commands,'sha256':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in files}},indent=2)+'\n')
