from pathlib import Path
import shutil,json,hashlib,difflib,subprocess
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-counters-002/base'
F=json.loads((P.parent/'DIAG-005/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();new=original
for old,replacement in [('#include <errno.h>','#include <errno.h>\n#include <profile/instr_prof_interface.h>'),('        uint64_t start = now_ns();','        __llvm_profile_reset_counters();\n        uint64_t start = now_ns();'),('        if (c == 5) {\n            /* Cursor scans','        serverAssert(__llvm_profile_dump() == 0);\n        if (c == 5) {\n            /* Cursor scans')]:
 assert new.count(old)==1;new=new.replace(old,replacement)
(B/'bench/microbench.c').write_text(new)
(P/'instrument.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),new.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
freeze={'base_commit':F['base_commit'],'snapshot':str(B.relative_to(R)),'provenance':'uncommitted source-count diagnostic over DIAG-005; tree source unchanged','files':{str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()}}
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n');(B/'build').mkdir()
cmd=['cc','-Isrc','-Icompat','-Ivendor/redis','-std=c11','-g','-Wall','-Wextra','-fno-omit-frame-pointer','-O3','-fprofile-instr-generate','-fcoverage-mapping','bench/microbench.c','src/zset_btree.c','compat/standalone.c','vendor/redis/siphash.c','-lm','-o','build/btree-bench']
with (P/'build.stdout').open('w') as so,(P/'build.stderr').open('w') as se:p=subprocess.run(cmd,cwd=B,stdout=so,stderr=se,timeout=120)
(P/'build.json').write_text(json.dumps({'command':cmd,'cwd':str(B.relative_to(R)),'returncode':p.returncode},indent=2)+'\n');assert p.returncode==0
