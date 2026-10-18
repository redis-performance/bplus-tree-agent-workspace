from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-008/base'
F=json.loads((P.parent/'DIAG-007/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
changes=[('argc == 8','argc == 9'),('seed=1301','seed=1723'),('size_t warm=argnum(argv[7]);','size_t warm=argnum(argv[7]); int warmmiss=(int)argnum(argv[8])-1;\n    serverAssert(warmmiss==0 || warmmiss==1);'),('double score;serverAssert(zbtreeScore(tree,keys[query[i]],&score) && score==(double)query[i]);','double score=0;\n        int found=zbtreeScore(tree,keys[query[i]+(warmmiss?n:0)],&score);\n        serverAssert(warmmiss ? !found : (found && score==(double)query[i]));'),('warmup_elapsed_ns");','warmup_elapsed_ns,warmup_case");'),('PRIu64 "\\n",','PRIu64 ",%s\\n",'),('outer,outer-totalwall,warm,warm_ns);','outer,outer-totalwall,warm,warm_ns,warmmiss?"lookup-miss":"lookup-hit");')]
for a,b in changes:assert s.count(a)==1,a;s=s.replace(a,b)
(B/'bench/microbench.c').write_text(s)
(P/'diagnostic.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=sha(P.parent/'DIAG-007/freeze.json'),provenance='uncommitted DIAG-008 warmup intervention over DIAG-007/HARNESS-002; root untouched',files={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
