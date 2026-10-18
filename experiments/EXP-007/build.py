#!/usr/bin/env python3
"""Build isolated EXP-007 source worktrees with an identical bulk decoder referee."""
import argparse, difflib, hashlib, json, os, shlex, shutil, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EXP=ROOT/'experiments/EXP-007'
BASE='4fd3a3fdbce5acca18ee292642a3d80a79f50362'
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--sanitize',action='store_true')
p.add_argument('--variants',nargs='+',default=['base','A','B','C'],choices=['base','A','B','C'])
a=p.parse_args();os.chdir(ROOT)
out=Path('build/exp007-sanitize' if a.sanitize else 'build/exp007');out.mkdir(parents=True,exist_ok=True)
cc=shlex.split(os.environ.get('CC','cc'))
flags=['-std=c11','-O1' if a.sanitize else '-O3','-g','-Wall','-Wextra','-Werror','-fno-omit-frame-pointer','-fno-lto','-Isrc','-Icompat','-Ivendor/redis','-Ibench',f'-ffile-prefix-map={ROOT}=.']
if a.sanitize: flags+=['-fsanitize=address,undefined','-fno-sanitize-recover=all']
manifest=dict(base_commit=BASE,harness_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),sanitizers=a.sanitize,compiler=subprocess.check_output(cc+['--version'],text=True),flags=[s.replace(str(ROOT),'<workspace>') for s in flags],commands=[],variants={},files={})
def run(cmd):
    q=subprocess.run(cmd,capture_output=True,text=True)
    manifest['commands'].append(dict(command=[str(s).replace(str(ROOT),'<workspace>') for s in cmd],returncode=q.returncode,stdout=q.stdout.replace(str(ROOT),'<workspace>'),stderr=q.stderr.replace(str(ROOT),'<workspace>')))
    (out/'build.json').write_text(json.dumps(manifest,indent=2)+'\n')
    if q.returncode: raise RuntimeError(q.stderr)
source=subprocess.check_output(['git','show',BASE+':src/zset_btree.c'],text=True)
assert source==Path('src/zset_btree.c').read_text()
control=source+'\n'+(EXP/'referee/control.inc').read_text()
objects=[]
for name,path in [('driver','bench/decoder_bench.c'),('standalone','compat/standalone.c'),('siphash','vendor/redis/siphash.c')]:
    obj=out/(name+'.o');run(cc+flags+['-c',path,'-o',str(obj)]);objects.append(str(obj))
for v in a.variants:
    wt=Path('worktrees/exp007-'+v)
    if not wt.exists():
        run(['git','worktree','add','--detach','--no-checkout',str(wt),BASE])
        run(['git','-C',str(wt),'checkout',BASE,'--','src/zset_btree.c','src/zset_btree.h'])
    assert subprocess.check_output(['git','-C',str(wt),'rev-parse','HEAD'],text=True).strip()==BASE
    helper=EXP/('referee/control.inc' if v=='base' else 'variants/'+v+'/decoder.inc')
    text=source+'\n'+helper.read_text();target=wt/'src/zset_btree.c';target.write_text(text)
    dest=out/v;dest.mkdir(exist_ok=True)
    vf=flags+['-DDECODER_TREE_SOURCE="'+os.path.relpath(target,EXP/'referee')+'"']
    run(cc+vf+['-c','experiments/EXP-007/referee/kernel.c','-o',str(dest/'kernel.o')])
    run(cc+flags+objects+[str(dest/'kernel.o'),'-lm','-o',str(dest/'decoder-bench')])
    if not a.sanitize: run(cc+vf+['-S','experiments/EXP-007/referee/kernel.c','-o',str(dest/'kernel.s')])
    manifest['variants'][v]=dict(source_sha256=sha(target),helper_sha256=sha(helper),binary=str(dest/'decoder-bench'),binary_sha256=sha(dest/'decoder-bench'),kernel_object_sha256=sha(dest/'kernel.o'))
    if v!='base':
        (EXP/'variants'/v/'candidate.patch').write_text(''.join(difflib.unified_diff(control.splitlines(True),text.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')))
for name in ['bench/decoder_bench.c','bench/decoder_kernel.h','tests/test_decoder.py','experiments/EXP-007/referee/control.inc','experiments/EXP-007/referee/kernel.c','experiments/EXP-007/build.py','compat/server.h','compat/standalone.c','vendor/redis/siphash.c','src/zset_btree.c','src/zset_btree.h']:
    manifest['files'][name]=sha(name)
manifest['shared_objects']={name:sha(name) for name in objects}
(out/'build.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Built {a.variants}, sanitizers={a.sanitize}')
