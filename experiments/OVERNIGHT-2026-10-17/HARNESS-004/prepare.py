from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];F=json.loads((P.parent/'HARNESS-003/freeze.json').read_text());S=R/'scratch/overnight-harness-004/base';assert not S.exists();S.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for name,h in F['files'].items():
 src=R/F['snapshot']/name;assert sha(src)==h;dst=S/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
shutil.copy2(P/'iterator_modes.c',S/'bench/iterator_modes.c')
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),provenance='Uncommitted separate iterator referee, baseline unchanged; protected git not retried',parent_freeze_sha256=sha(P.parent/'HARNESS-003/freeze.json'),files={str(p.relative_to(S)):sha(p) for p in S.rglob('*') if p.is_file()}),indent=2)+'\n')
