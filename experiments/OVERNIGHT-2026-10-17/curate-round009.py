from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';roots=[R/'experiments/EXP-005',O/'BOUNDARY-014',O/'DIAG-012',O/'AA-009'];files=[]
for root in roots:files += [p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
files += list(O.glob('ROUND-009*'));files += [O/'verify-round009.py',Path(__file__).resolve(),R/'tests/zero_physical_oracle.c']
files += [R/n for n in ['README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv','.workspace-memory/MEMORY.md','.workspace-memory/LIVE-STATUS.md','.workspace-memory/handoff.md']]
files=[p for p in files if p.name not in ['ROUND-009-SHA256.json','ROUND-009-CURATION.json']]
for p in files:
 data=p.read_bytes();assert (b'/' + b'Users/') not in data and (b'/' + b'private/var/') not in data,str(p.relative_to(R))
result=dict(status='pass',files=len(set(files)),bytes=sum(p.stat().st_size for p in set(files)),recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),prior_self_match_retained=True)
(O/'ROUND-009-CURATION.json').write_text(json.dumps(result,indent=2)+'\n');files.append(O/'ROUND-009-CURATION.json')
manifest={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(files))};(O/'ROUND-009-SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(result))
