from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for tag,args in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 out=P/f'ROUND-019-seal-{tag}.stdout';err=P/f'ROUND-019-seal-{tag}.stderr';row=dict(command=args,started_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)))
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(args,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));rows.append(row);assert rc==0
assert 'Workspace links and pinned source/support hashes: PASS' in (P/'ROUND-019-seal-workspace.stdout').read_text()
# Only this round's public artifacts and shared ledgers are sealed here; old evidence
# is protected by the prior seal plus the round19 immutable-file audit.
files=set()
for folder in ['PROFILE-005','DIAG-019','BOUNDARY-026','COUNTERS-011']:files.update(p for p in (P/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
files.update(P.glob('ROUND-019*'));files.update(P.glob('*round019*.py'))
files.update(R/n for n in ['README.md','experiments/SUMMARY.md','experiments/EXPERIMENTS.md','.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','.workspace-memory/LIVE-STATUS.md','tests/heterogeneous_batch_oracle.c','src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c'])
files={p for p in files if p.is_file() and p.name not in ['ROUND-019-SHA256.json','ROUND-019-FINAL-CHECKS.json']}
hits=[]
for p in files:
 if p.parts[-2]=='src' or p.name in ['microbench.c','standalone.c','upstream.c']:continue
 try:text=p.read_text()
 except UnicodeDecodeError:continue
 for pattern in [r'/Users/[A-Za-z0-9_.-]+/',r'/private/var/(?:folders|tmp)/']:
  if re.search(pattern,text):hits.append(str(p.relative_to(R)))
assert not hits,hits
counts=dict(harnesses=7,baselines=13,diagnostics=34,boundary_suites=26,historical_fault_types=54,unclassified_lane_reuse_controls=2,populations=5,accepted=0,rejected=2,parked=3)
s=(R/'experiments/SUMMARY.md').read_text()
for fragment in ['| Harness revisions locally validated; commit review pending | 7 |','| Baseline explorations completed; suite qualification parked | 13 |','| Optimisations accepted / rejected / parked | 0 / 2 / 3 |','| Population rounds executed | 5 (sequential fallback) |','| Additional measurement diagnostics completed | 34 |','| Additional boundary oracle suites validated | 26 |']:assert fragment in s
j=dict(status='PASS',utc=utc(),runs=rows,counts=counts,private_path_scan_hits=hits,source_adoption='NONE',backend='unknown',model='unknown',token_cost='unknown',independent_reviewer='startup failed',final_round=False,experimental_children_finished='2026-10-18T05:50:14.413751+00:00')
(P/'ROUND-019-FINAL-CHECKS.json').write_text(json.dumps(j,indent=2)+'\n');files.add(P/'ROUND-019-FINAL-CHECKS.json');sealed={str(p.relative_to(R)):sha(p) for p in sorted(files)};(P/'ROUND-019-SHA256.json').write_text(json.dumps(sealed,indent=2)+'\n');print(json.dumps(dict(status='PASS',sealed_files=len(sealed),counts=counts),indent=2))
