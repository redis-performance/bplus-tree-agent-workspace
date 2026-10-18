from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];H=R/'experiments/OVERNIGHT-2026-10-17/HARNESS-004';F=json.loads((H/'freeze.json').read_text());E=json.loads((P.parent/'freeze.json').read_text());S=R/'scratch/exp-002-guards';assert not S.exists();S.mkdir()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();out={}
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 src=R/E['snapshot_root']/v/'src/zset_btree.c';assert sha(src)==E['files'][v]['src/zset_btree.c'];shutil.copy2(src,B/'src/zset_btree.c')
 out[v]={str(f.relative_to(B)):sha(f) for f in B.rglob('*') if f.is_file()}
 D=P/v;D.mkdir();(D/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),files=out[v]),indent=2)+'\n')
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),parent_harness_sha256=sha(H/'freeze.json'),parent_variants_sha256=sha(P.parent/'freeze.json'),provenance='uncommitted exact retained A/B/C sources and separately frozen HARNESS-004 referee',files=out),indent=2)+'\n')
code=(H/'validate.py').read_text().replace('P=Path(__file__).resolve().parent;R=P.parents[2];','import sys\nP=Path(sys.argv[1]).resolve();R=Path.cwd();')
(P/'validate-one.py').write_text(code)
