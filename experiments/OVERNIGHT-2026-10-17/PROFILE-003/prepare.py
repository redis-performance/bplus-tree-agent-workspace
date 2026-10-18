from pathlib import Path
from datetime import datetime,timezone
import json,shutil,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-profile-003/base'
F=json.loads((P.parent/'HARNESS-003/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h;dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
for a,b in [('int main(int argc, char **argv) {','#include "self_sampler.h"\nint main(int argc, char **argv) {'),('    uint64_t rng = seed;','    sample_init();\n    uint64_t rng = seed;'),('        uint64_t start = now_ns();','        sample_start();\n        uint64_t start = now_ns();'),('        uint64_t elapsed = now_ns() - start;','        uint64_t elapsed = now_ns() - start;\n        sample_stop();'),('        int64_t thread_elapsed =','        sample_dump(cases[c]);\n        int64_t thread_elapsed =')]:
 assert s.count(a)==1;s=s.replace(a,b)
(B/'bench/microbench.c').write_text(s)
G=json.loads((P.parent/'DIAG-009/freeze.json').read_text())
for name in ['bench/self_sampler.h','bench/calibrate.c']:
 src=R/G['snapshot']/name;assert sha(src)==G['files'][name];shutil.copy2(src,B/name)
(P/'profile-harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=sha(P.parent/'HARNESS-003/freeze.json'),helper_freeze_sha256=sha(P.parent/'DIAG-009/freeze.json'),provenance='uncommitted traversal profile instrumentation over HARNESS-003, DIAG-009 helpers; root unchanged',files={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
