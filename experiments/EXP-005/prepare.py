from pathlib import Path
import json,hashlib,shutil,difflib,datetime
P=Path(__file__).resolve().parent;R=P.parents[1];F=json.loads((R/'experiments/OVERNIGHT-2026-10-17/HARNESS-004/freeze.json').read_text());S=R/'scratch/exp-005';assert not S.exists();S.mkdir();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();original=(R/F['snapshot']/'src/zset_btree.c').read_text();start=original.index('static double zbtScoreLeafScore(');end=original.index('/* Return the raw hash byte',start);body=original[start:end];old='if (bits < 64)\n            delta &= (UINT64_C(1) << bits) - 1;';assert body.count(old)==1
variants={'A':'delta &= UINT64_MAX >> (64 - bits);','B':'delta &= ((UINT64_C(1) << (bits - 1)) * 2) - 1;','C':'delta &= UINT64_MAX >> ((-bits) & 63);'};allfiles={}
for v in ['control','A','B','C']:
 B=S/v;B.mkdir()
 for n,h in F['files'].items():
  src=R/F['snapshot']/n;assert sha(src)==h;dst=B/n;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 for name in ['iterator_mutation_oracle.c','packed_decode_oracle.c','zero_physical_oracle.c']:shutil.copy2(R/'tests'/name,B/'tests'/name)
 if v!='control':
  changed=original[:start]+body.replace(old,variants[v])+original[end:];(B/'src/zset_btree.c').write_text(changed);D=P/'variants'/v;D.mkdir();(D/'candidate.patch').write_text(''.join(difflib.unified_diff(original.splitlines(True),changed.splitlines(True),fromfile='a/src/zset_btree.c',tofile='b/src/zset_btree.c')));(D/'implementation.md').write_text(f'# Variant {v}\n\nSequential implementation pass,not independent agent;backend/model/cost unknown.\nPredicate: `{variants[v]}`. One condition only in zbtScoreLeafScore.\nProof assumes valid packed widths1..64 inside nonzero guard and shift0..7.\nConditional access unchanged; no shift64 when merge executes. Root preserved.\n')
 allfiles[v]={str(p.relative_to(B)):sha(p) for p in B.rglob('*') if p.is_file()};D=P/v;D.mkdir();(D/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot=str(B.relative_to(R)),files=allfiles[v]),indent=2)+'\n')
(P/'freeze.json').write_text(json.dumps(dict(base_commit=F['base_commit'],snapshot_root=str(S.relative_to(R)),frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),parent_freeze_sha256=sha(R/'experiments/OVERNIGHT-2026-10-17/HARNESS-004/freeze.json'),provenance='uncommitted isolated EXP-005 predicate variants over frozen HARNESS-004',files=allfiles),indent=2)+'\n')
