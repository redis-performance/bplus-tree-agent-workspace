from pathlib import Path
import json,hashlib,shutil,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-profile-002/base'
F=json.loads((P.parent/'HARNESS-002/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
for a,b in [('int main(int argc, char **argv) {','#include "self_sampler.h"\nint main(int argc, char **argv) {'),('    uint64_t rng = seed;','    sample_init();\n    uint64_t rng = seed;'),('        uint64_t start = now_ns();','        sample_start();\n        uint64_t start = now_ns();'),('        uint64_t elapsed = now_ns() - start;','        uint64_t elapsed = now_ns() - start;\n        sample_stop(cases[c]);')]:
 assert s.count(a)==1;s=s.replace(a,b)
(B/'bench/microbench.c').write_text(s)
for name in ['self_sampler.h','calibrate.c']:shutil.copy2(P/name,B/'bench'/name)
(P/'profile-harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
f=dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),parent_freeze_sha256=hashlib.sha256((P.parent/'HARNESS-002/freeze.json').read_bytes()).hexdigest(),provenance='uncommitted diagnostic snapshot over HARNESS-002; root intact',files={str(x.relative_to(B)):hashlib.sha256(x.read_bytes()).hexdigest() for x in B.rglob('*') if x.is_file()})
(P/'freeze.json').write_text(json.dumps(f,indent=2)+'\n')
