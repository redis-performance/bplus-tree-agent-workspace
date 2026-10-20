"""Reconstruct exact baseline/B and an additive long-window referee in scratch."""
import hashlib,json,shutil,subprocess,tarfile
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
OUT=ROOT/'scratch/intel-iterator-tma-inputs';OUT.mkdir(exist_ok=True)
OLD=ROOT/'experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator'
for v in ['base','B']:
 d=OUT/'variants'/v;d.mkdir(parents=True,exist_ok=True)
 for name in ['src','compat','vendor','tests']:
  shutil.copytree(ROOT/name,d/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
  for file in (d/name).rglob('*'):
   if file.is_file():
    rel=str(file.relative_to(d))
    frozen=subprocess.check_output(['git','show','c6112e052:'+rel],cwd=ROOT)
    assert frozen==file.read_bytes(),rel
 if v=='B':
  patch=OLD/'variants/B/candidate.patch'
  assert hashlib.sha256(patch.read_bytes()).hexdigest()=='8ec11ac9b68af3a4aa7d80b41545a3b6428915ad77722710cb4ac0ba69f7be2f'
  subprocess.run(['patch','-p1','--forward','-i',str(patch)],cwd=d,check=True,stdout=subprocess.PIPE)
d=OUT/'driver';d.mkdir(exist_ok=True)
for name in ['microbench.c','iterator.c','cache-oracle.c','cache-oracle-additive.c']:shutil.copy2(OLD/name,d/name)
s=(d/'iterator.c').read_text();assert s.count('ops=number(v);')==1
s=s.replace('#include <math.h>','#include <math.h>\n#include "ops.h"').replace('ops=number(v);','ops=long_ops(v);')
needle='    size_t traversals=1+(ops-1)/n,count=traversals*n,owned=zbtreeAllocSize(tree);'
assert s.count(needle)==1
s=s.replace(needle,'    serverAssert(ops <= SIZE_MAX - n); /* rounded visit count cannot overflow */\n'+needle)
(d/'iterator-long.c').write_text(s)
for name in ['ops.h','ready.c','protocol.json','campaign.py','run.sh','work.sh']:
 if (HERE/name).exists():shutil.copy2(HERE/name,OUT/name)
shutil.copy2(HERE/'ops.h',d/'ops.h')
manifest={str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.rglob('*')) if p.is_file()}
(HERE/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(OUT)
