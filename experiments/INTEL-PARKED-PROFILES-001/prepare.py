"""Isolated profile-only drivers; frozen original files are never changed."""
import hashlib,json,shutil,subprocess
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parent.parent;O=R/'scratch/intel-parked-profiles-inputs'
OLD=R/'experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z'
O.mkdir(exist_ok=True)
for v,patch in [('base',None),('itA',OLD/'004-iterator/variants/A/candidate.patch'),('itB',OLD/'004-iterator/variants/B/candidate.patch'),('scanB',OLD/'017-corrected-scan-replication/candidate.patch')]:
 d=O/'variants'/v;d.mkdir(parents=True,exist_ok=True)
 for name in ['src','compat','vendor','tests']:
  shutil.copytree(R/name,d/name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
  for p in (d/name).rglob('*'):
   if p.is_file():assert p.read_bytes()==subprocess.check_output(['git','show','37efd287f:'+str(p.relative_to(d))],cwd=R)
 if patch:
  subprocess.run(['patch','-p1','--forward','-i',str(patch)],cwd=d,check=True,stdout=subprocess.PIPE)
  (H/(v+'.patch')).write_bytes(patch.read_bytes())
d=O/'driver';d.mkdir(exist_ok=True)
for n in ['iterator.c','microbench.c','cache-oracle.c','cache-oracle-additive.c']:shutil.copy2(OLD/'004-iterator'/n,d/n)
shutil.copy2(R/'experiments/INTEL-ITERATOR-TMA-001/ops.h',d/'ops.h')
for name,source in [('update',OLD/'003-update/update.c'),('scan',R/'bench/microbench.c'),('guard',OLD/'017-corrected-scan-replication/referee/scan-supplement.c')]:shutil.copy2(source,d/(name+'-original.c'))
shutil.copy2(OLD/'017-corrected-scan-replication/referee/census.h',d/'census.h')
for name in ['iterator','update','scan','guard']:
 s=(d/('iterator.c' if name=='iterator' else name+'-original.c')).read_text()
 # Common readiness hook is outside measured work and inactive in completed checks.
 if name=='iterator':
  s=s.replace('#include <math.h>','#include <math.h>\n#include "ops.h"').replace('ops=number(v);','ops=long_ops(v);')
  s=s.replace('    size_t traversals=1+(ops-1)/n,count=traversals*n,owned=zbtreeAllocSize(tree);','    serverAssert(ops <= SIZE_MAX - n);\n    size_t traversals=1+(ops-1)/n,count=traversals*n,owned=zbtreeAllocSize(tree);')
 elif name in ['update','scan']:
  s=s.replace('#include <errno.h>','#include <errno.h>\n#include "ops.h"\nextern void sample_begin(void);')
  assert s.count('ops = number(value);')==1;s=s.replace('ops = number(value);','ops = long_ops(value);')
  assert s.count('        uint64_t start = now_ns();')==1;s=s.replace('        uint64_t start = now_ns();','        sample_begin();\n        uint64_t start = now_ns();')
  s=s.replace('        if (c == 4 || c == 5) count = traversals * n;','        serverAssert(ops <= SIZE_MAX - n);\n        if (c == 4 || c == 5) count = traversals * n;')
 else:
  s=s.replace('#include <time.h>','#include <time.h>\nextern void sample_begin(void);')
  assert 'passes <= 10000000' in s;s=s.replace('passes <= 10000000','passes <= UINT64_C(100000000000)')
  s=s.replace('    start_cpu = sched_getcpu();','    sample_begin();\n    start_cpu = sched_getcpu();')
 (d/(name+'-profile.c')).write_text(s)
for n in ['ready.c','protocol.json','collect.py','work.py','run.sh']:
 if (H/n).exists():shutil.copy2(H/n,O/n)
shutil.copytree(R/'scratch/intel-iterator-tma-inputs/glue',O/'glue',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
shutil.copytree(R/'scratch/intel-iterator-tma-inputs/pmu',O/'pmu',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
manifest={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(O.rglob('*')) if p.is_file()}
(H/'input-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(O)
