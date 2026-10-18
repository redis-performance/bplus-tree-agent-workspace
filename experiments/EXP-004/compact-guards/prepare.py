from pathlib import Path
import json,hashlib,shutil,datetime
P=Path(__file__).resolve().parent;R=P.parents[2];H=R/'experiments/OVERNIGHT-2026-10-17/HARNESS-006';F=json.loads((H/'freeze.json').read_text());G=json.loads((P.parent/'freeze.json').read_text());S=R/'scratch/exp-004-compact';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={}
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for name in ['packed_decode_oracle.c','zero_physical_oracle.c']:shutil.copy2(R/'tests'/name,B/'tests'/name)
 if v!='control':
  src=R/G['snapshot_root']/v/'src/zset_btree.c';assert sha(src)==G['files'][v]['src/zset_btree.c'];shutil.copy2(src,B/'src/zset_btree.c')
 files[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()}
 if v=='control':
  for kind,h in json.loads((H/'binaries.json').read_text()).items():
   src=R/F['snapshot']/f'build/{kind}/iterator-modes';assert sha(src)==h;dst=B/f'build/{kind}/iterator-modes';dst.parent.mkdir(parents=True);shutil.copy2(src,dst)
 (P/v).mkdir();(P/v/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),files=files[v]),indent=2)+'\n')
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),provenance='uncommitted exact retained EXP-004 variants over new HARNESS-006; control binary copied byte-identical',harness_freeze_sha256=sha(H/'freeze.json'),candidate_freeze_sha256=sha(P.parent/'freeze.json'),files=files),indent=2)+'\n')
(P/'control/binaries.json').write_text((H/'binaries.json').read_text())
