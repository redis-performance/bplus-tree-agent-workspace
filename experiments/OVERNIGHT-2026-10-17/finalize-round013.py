"""Curate completed round13 evidence; no measurements or source mutation."""
from pathlib import Path
import datetime,hashlib,json,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
rows=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 row=dict(name=name,command=cmd,started_utc=utc())
 out=P/('ROUND-013-final-'+name+'.stdout');err=P/('ROUND-013-final-'+name+'.stderr')
 with out.open('w') as so,err.open('w') as se:r=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120)
 row.update(returncode=r.returncode,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row)
 assert r.returncode==0
assert json.loads((P/'ROUND-013-VERIFY.json').read_text())['status']=='pass'
(P/'ROUND-013-FINAL-CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n')
files=[]
for name in ['DIAG-016','DIAG-017','DIAG-018','BOUNDARY-017','BOUNDARY-018']:files.extend(x for x in (P/name).rglob('*') if x.is_file())
files.extend(x for x in P.glob('ROUND-013-*') if x.is_file() and x.name not in ['ROUND-013-SHA256.json','ROUND-013-CURATION.json'])
files.extend([P/'ROUND-013.md',P/'verify-round013.py',Path(__file__).resolve()])
files.extend(R/n for n in ['README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','.workspace-memory/LIVE-STATUS.md','tests/index_storage_oracle.c','tests/leaf_id_registry_oracle.c'])
files=sorted(set(files));private=[]
for path in files:
 try:s=path.read_text()
 except UnicodeDecodeError:continue
 if '/Users/' in s or '/home/' in s:
  # This checker itself contains the patterns, not machine paths.
  if path!=Path(__file__).resolve():private.append(str(path.relative_to(R)))
assert not private,private
inventory={str(x.relative_to(R)):sha(x) for x in files}
(P/'ROUND-013-SHA256.json').write_text(json.dumps(inventory,indent=2)+'\n')
summary=dict(status='complete',curated_utc=utc(),files=len(files),bytes=sum(x.stat().st_size for x in files),private_path_audit='pass',source_adoption='NONE',existing_decisions={'EXP-004':'A/PARK','EXP-005':'PARK/NONE'},counts=dict(harnesses=6,baselines=12,diagnostics=26,boundary_suites=18,boundary_fault_types=36,populations=4,accepted=0,rejected=2,parked=2),measurements=864,warmups=4,serial_measurement_windows=868,validation_windows=52,intervals_checked=52,backend='unknown',model='unknown',token_cost='unknown; supervisor records usage separately',source_provenance='base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus uncommitted isolated snapshots',final_round=False)
(P/'ROUND-013-CURATION.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
