from pathlib import Path
import json,shutil,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-006/base'
F=json.loads((P.parent/'PROFILE-002/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert hashlib.sha256(src.read_bytes()).hexdigest()==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
patch=[]
for file in ['bench/self_sampler.h','bench/microbench.c']:
 original=(B/file).read_text();s=original
 if file.endswith('.h'):
  changes=[('value >= 1 && value <= 999999','value <= 999999'),('static void sample_start(void) {','static void sample_start(void) {\n    if (!sample_usec) return;'),('static void sample_stop(const char *scope) {','static void sample_stop(void) {\n    if (!sample_usec) return;'),('    unsigned n = atomic_load_explicit(&sample_count, memory_order_relaxed);','}\nstatic void sample_dump(const char *scope) {\n    unsigned n = atomic_load_explicit(&sample_count, memory_order_relaxed);')]
 else:
  changes=[('sample_stop(cases[c]);','sample_stop();'),('        int64_t thread_elapsed =','        sample_dump(cases[c]);\n        int64_t thread_elapsed =')]
 for a,b in changes:assert s.count(a)==1,a;s=s.replace(a,b)
 (B/file).write_text(s);patch+=difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/'+file,tofile='b/'+file)
(P/'diagnostic.patch').write_text(''.join(patch))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),provenance='uncommitted diagnostic extension over PROFILE-002',parent_freeze_sha256=hashlib.sha256((P.parent/'PROFILE-002/freeze.json').read_bytes()).hexdigest(),files={str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
