from pathlib import Path
import shutil,json,hashlib,difflib,subprocess
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
B=ROOT/'scratch/overnight-diag-003/base'
F=json.loads((P.parent/'HARNESS-001/freeze.json').read_text())
assert not B.exists();B.mkdir(parents=True)
for name,digest in F['files'].items():
 src=ROOT/F['snapshot']/name
 assert hashlib.sha256(src.read_bytes()).hexdigest()==digest
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text()
prefix=original[:original.index('static size_t number')]
main=(P/'diagnostic-main.c').read_text()
new=prefix+main;(B/'bench/microbench.c').write_text(new)
(P/'diagnostic-harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),new.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
freeze={'base_commit':F['base_commit'],'snapshot':str(B.relative_to(ROOT)),'provenance':'uncommitted diagnostic harness over frozen HARNESS-001; root source/referee untouched','files':{str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in B.rglob('*') if f.is_file()}}
(P/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
