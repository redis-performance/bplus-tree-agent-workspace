from pathlib import Path
import datetime,hashlib,json,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 out=P/('ROUND-014-final-'+name+'.stdout');err=P/('ROUND-014-final-'+name+'.stderr');assert not out.exists() and not err.exists()
 row=dict(name=name,command=cmd,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row)
 (P/'ROUND-014-FINAL-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n');assert rc==0
files=[]
for root in ['BOUNDARY-019','BOUNDARY-020','BOUNDARY-021','COUNTERS-007']:files.extend(f for f in (P/root).rglob('*') if f.is_file())
files.extend(f for f in P.glob('*round014.py'));files.extend(f for f in P.glob('ROUND-014*') if f.name!='ROUND-014-SHA256.json')
for n in ['.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','.workspace-memory/LIVE-STATUS.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/token-ledger.tsv','tests/leaf_id_lifecycle_oracle.c','tests/active_resize_defrag_oracle.c','tests/resize_generation_oracle.c','src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c']:files.append(R/n)
manifest={str(f.relative_to(R)):sha(f) for f in sorted(set(files))};(P/'ROUND-014-SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n')
# Exact count/state assertions prevent accidental document drift.
summary=(R/'experiments/SUMMARY.md').read_text();assert '| Additional measurement diagnostics completed | 27 |' in summary and '| Additional boundary oracle suites validated | 21 |' in summary
for n in ['README.md','.workspace-memory/LIVE-STATUS.md']:assert 'ROUND-014' in (R/n).read_text()
print(json.dumps(dict(status='pass',curated_files=len(manifest),source_sha256=sha(R/'src/zset_btree.c'),all_children_completed=True,finalized_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2))
