from pathlib import Path
import json,hashlib,shutil,subprocess,datetime,re
P=Path(__file__).resolve().parent;R=P.parents[2];P=P/'attempt-002';P.mkdir();shutil.copy2(P.parent/'PLAN.md',P/'PLAN.md');S=R/'scratch/overnight-diag-012-attempt002';assert not S.exists();S.mkdir();D=P/'validation';D.mkdir();F=json.loads((P.parent.parent/'HARNESS-004/freeze.json').read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rows=[];files={};binaries={}
def run(name,cmd,B):
 with (D/(name+'.stdout')).open('w') as so,(D/(name+'.stderr')).open('w') as se:
  try:rc=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120).returncode
  except subprocess.TimeoutExpired:rc='timeout'
 row=dict(name=name,command=cmd,cwd=str(B.relative_to(R)),returncode=rc,stdout_sha256=sha(D/(name+'.stdout')),stderr_sha256=sha(D/(name+'.stderr')));rows.append(row);(P/'builds.json').write_text(json.dumps(rows,indent=2)+'\n');assert rc==0,name
for pad in [0,16,32,48]:
 B=S/str(pad);B.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 (B/'build').mkdir();files[str(pad)]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()}
 for kind in ['release','sanitize']:
  flags=['-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer']+(['-O3'] if kind=='release' else ['-O1','-fsanitize=address,undefined','-fno-sanitize-recover=all']);common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags]
  if pad==0:run(f'{kind}-emit',common+['-S','src/zset_btree.c','-o',f'build/{kind}-original.s'],B)
  original=(S/'0'/f'build/{kind}-original.s').read_text(encoding='latin1');a=original.index('\t.globl\t_zbtreeIteratorNext');b=original.index('\t.cfi_endproc',a)+len('\t.cfi_endproc');new=original[:a]+f'\t.space {pad}\n'+original[a:b]+f'\n\t.space {64-pad}\n'+original[b:];(B/f'build/{kind}-placed.s').write_text(new,encoding='latin1')
  run(f'{pad}-{kind}-build',common+['bench/iterator_modes.c',f'build/{kind}-placed.s','compat/standalone.c','vendor/redis/siphash.c','-lm','-o',f'build/{kind}'],B)
  binaries[f'{pad}-{kind}']=sha(B/f'build/{kind}')
  if kind=='release':
   run(f'{pad}-symbols',['nm','-n','build/release'],B)
   run(f'{pad}-assembly',['otool','-tvV','build/release'],B)
 # Original tests require REDIS_TEST code; separately emit with same placement intervention.
 flags=['-std=c11','-O3','-g','-fno-omit-frame-pointer','-DREDIS_TEST','-DREDIS_DEBUG'];common=['cc','-Isrc','-Icompat','-Ivendor/redis',*flags]
 if pad==0:run('upstream-emit',common+['-S','src/zset_btree.c','-o','build/upstream-original.s'],B)
 original=(S/'0'/'build/upstream-original.s').read_text(encoding='latin1');a=original.index('\t.globl\t_zbtreeIteratorNext');b=original.index('\t.cfi_endproc',a)+len('\t.cfi_endproc');(B/'build/upstream-placed.s').write_text(original[:a]+f'\t.space {pad}\n'+original[a:b]+f'\n\t.space {64-pad}\n'+original[b:],encoding='latin1')
 run(f'{pad}-upstream-build',common+['tests/upstream.c','build/upstream-placed.s','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/upstream'],B)
 print(pad,'built',flush=True)
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),plan_sha256=sha(P/'PLAN.md'),files=files,binaries=binaries,assembly={str(p.relative_to(S)):sha(p) for p in S.rglob('*.s')}),indent=2)+'\n')
