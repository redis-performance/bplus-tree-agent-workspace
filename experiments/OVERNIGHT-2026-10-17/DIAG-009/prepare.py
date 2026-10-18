from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib,difflib
P=Path(__file__).resolve().parent;R=P.parents[2];B=R/'scratch/overnight-diag-009/base'
F=json.loads((P.parent/'DIAG-006/freeze.json').read_text());assert not B.exists();B.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h
 dst=B/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
original=(B/'bench/calibrate.c').read_text();s=(P/'calibrate.c').read_text();(B/'bench/calibrate.c').write_text(s)
(P/'diagnostic.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),s.splitlines(True),fromfile='a/bench/calibrate.c',tofile='b/bench/calibrate.c')))
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),frozen_utc=datetime.now(timezone.utc).isoformat(),parent_freeze_sha256=sha(P.parent/'DIAG-006/freeze.json'),provenance='uncommitted DIAG-009 calibrated helper consolidation over DIAG-006; original frozen snapshots untouched',files={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}),indent=2)+'\n')
