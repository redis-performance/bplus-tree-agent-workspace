from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-harness-003/base'
F=json.loads((P.parent/'HARNESS-002/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/microbench.c').read_text();s=original
changes=[('            serverAssert(zbtreeScore(tree, keys[query[i]], &score) && score == (double)query[i]);','''            if (c == 2) serverAssert(!zbtreeScore(tree, keys[query[i] + n], &score));
            else serverAssert(zbtreeScore(tree, keys[query[i]], &score) && score == (double)query[i]);'''),('query_fingerprint");','query_fingerprint,warmup_case");'),('PRIu64 "\\n",','PRIu64 ",%s\\n",'),('construction_fingerprint, query_order, query_seed, query_fingerprint);','construction_fingerprint, query_order, query_seed, query_fingerprint,\n               c == 0 ? "none" : c == 2 ? "lookup-miss" : "lookup-hit");')]
for a,b in changes:assert s.count(a)==1,a;s=s.replace(a,b)
(B/'bench/microbench.c').write_text(s)
(P/'harness.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/microbench.c',tofile='b/bench/microbench.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=sha(P.parent/'HARNESS-002/freeze.json'),provenance='uncommitted isolated HARNESS-003 miss warmup over HARNESS-002; main untouched',files={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
