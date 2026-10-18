from pathlib import Path
import datetime,hashlib,json,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert json.loads((P/'ROUND-017-VERIFY.json').read_text())['status']=='pass'
assert json.loads((P/'ROUND-017-CANDIDATE-AUDIT.json').read_text())['candidate_patches_reconstructed']==12
checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check'])]:
 out=P/('ROUND-017-final-'+name+'.stdout');err=P/('ROUND-017-final-'+name+'.stderr');assert not out.exists();row=dict(name=name,command=cmd,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert rc==0
(P/'ROUND-017-FINAL-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
files=[]
for root in ['BOUNDARY-024','COUNTERS-010','ROUND-017-CONFIRMATION']:files.extend(p for p in (P/root).rglob('*') if p.is_file())
files.extend(p for p in P.glob('ROUND-017*') if p.is_file() and p.name!='ROUND-017-SHA256.json')
files.extend(p for p in P.glob('*round017*.py'))
for n in ['.workspace-memory/MEMORY.md','.workspace-memory/handoff.md','.workspace-memory/LIVE-STATUS.md','README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','experiments/NEXT-STEPS.md','experiments/token-ledger.tsv','tests/live_widen_score_oracle.c','tests/live_widen_external_score_oracle.c','tests/live_widen_finite_score_oracle.c','tests/live_widen_tie_neighbor_oracle.c','tests/live_widen_batch_score_oracle.c','src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c']:files.append(R/n)
for f in sorted(set(files)):
 text=f.read_text();assert ('/'+'Users/') not in text and ('/'+'private/var/') not in text,str(f)
manifest={str(f.relative_to(R)):sha(f) for f in sorted(set(files))};(P/'ROUND-017-SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n')
assert all(sha(R/n)==h for n,h in manifest.items())
s=(R/'experiments/SUMMARY.md').read_text();assert '| Additional measurement diagnostics completed | 30 |' in s and '| Additional boundary oracle suites validated | 24 |' in s
for n in ['README.md','.workspace-memory/LIVE-STATUS.md']:assert 'ROUND-017' in (R/n).read_text()
print(json.dumps(dict(status='pass',curated_files=len(manifest),source_sha256=sha(R/'src/zset_btree.c'),finalized_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2))
