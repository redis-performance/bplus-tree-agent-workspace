from pathlib import Path
import subprocess,json,hashlib,datetime
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();rows=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 started=utc();q=subprocess.run(cmd,cwd=R,capture_output=True,timeout=120)
 out=O/f'ROUND-011-final-{name}.stdout';err=O/f'ROUND-011-final-{name}.stderr';out.write_bytes(q.stdout);err.write_bytes(q.stderr)
 rows.append(dict(name=name,command=cmd,started_utc=started,ended_utc=utc(),returncode=q.returncode,stdout_sha256=sha(out),stderr_sha256=sha(err)));assert q.returncode==0,name
(O/'ROUND-011-FINAL-CHECKS.json').write_text(json.dumps(rows,indent=2)+'\n')
paths=[]
for D in [O/'COUNTERS-006',O/'HARNESS-006',O/'AA-011',O/'DIAG-013',R/'experiments/EXP-004/compact-guards']:
 paths += [p for p in D.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
paths += [p for p in O.glob('ROUND-011*') if p.is_file() and p.suffix!='.json']
paths += [R/p for p in ['README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/NEXT-STEPS.md','.workspace-memory/MEMORY.md','.workspace-memory/LIVE-STATUS.md','.workspace-memory/handoff.md']]
violations=[]
for p in paths:
 raw=p.read_bytes()
 if b'/Users/' in raw or b'/private/var/' in raw:violations.append(str(p.relative_to(R)))
(O/'ROUND-011-CURATION.json').write_text(json.dumps(dict(status='pass' if not violations else 'fail',files_checked=len(paths),violations=violations,scope='private machine path prefixes; raw method/profile output kept ignored'),indent=2)+'\n');assert not violations
paths += [p for p in O.glob('ROUND-011*.json') if p.name!='ROUND-011-SHA256.json']
paths += [O/'verify-round011.py',Path(__file__),R/'experiments/token-ledger.tsv',R/'experiments/EXP-004/README.md',R/'experiments/EXP-004/implementation-selection.md']
(O/'ROUND-011-SHA256.json').write_text(json.dumps({str(p.relative_to(R)):sha(p) for p in sorted(set(paths))},indent=2)+'\n')
print('Final checks, curation and hashes PASS;files',len(set(paths)))
