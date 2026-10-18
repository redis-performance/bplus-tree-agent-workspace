from pathlib import Path
import datetime,hashlib,json,re,subprocess
P=Path(__file__).resolve().parent;R=P.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[]
for tag,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check']),('compiler',['cc','--version']),('arch',['uname','-m']),('os',['sw_vers']),('commit',['git','rev-parse','HEAD'])]:
 out=P/('ROUND-020-final-'+tag+'.stdout');err=P/('ROUND-020-final-'+tag+'.stderr');row=dict(name=tag,command=cmd,started_utc=utc())
 with out.open('w') as o,err.open('w') as e:rc=subprocess.run(cmd,cwd=R,stdout=o,stderr=e,timeout=120).returncode
 row.update(returncode=rc,ended_utc=utc(),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert rc==0,tag
assert (P/'ROUND-020-final-commit.stdout').read_text().strip()=='a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c'
roots=[R/'experiments/EXP-006'/x for x in ['cross-boundary-round020','scalar-fallback-round020','dense-promotion-round020','generation-wrap-round020']]
files=[p for base in roots for p in base.rglob('*') if p.is_file()]
files += [p for p in P.glob('ROUND-020*') if p.is_file() and p.name not in ['ROUND-020-SHA256.json','ROUND-020-FINAL-CHECKS.json']]
files += [P/'verify-round020.py',P/'audit-round020-static-leaf.py',Path(__file__).resolve()]
files.append(P/'MORNING-DRAFT-ROUND020.md')
files += [R/n for n in ['README.md','experiments/EXPERIMENTS.md','experiments/SUMMARY.md','.workspace-memory/MEMORY.md','.workspace-memory/LIVE-STATUS.md','.workspace-memory/handoff.md','src/zset_btree.c','src/zset_btree.h','bench/microbench.c','compat/standalone.c','tests/upstream.c']]
files=sorted(set(files));private=[];trailing=[]
for p in files:
 t=p.read_text()
 if str(R) in t or re.search(r'/Users/[A-Za-z0-9_.-]+/',t):private.append(str(p.relative_to(R)))
 if p.suffix in ['.md','.py','.c']:
  for i,line in enumerate(t.splitlines(),1):
   if line.rstrip()!=line:trailing.append((str(p.relative_to(R)),i))
assert not private,private
assert not trailing,trailing
m=json.loads((P/'ROUND-020-VERIFY.json').read_text());assert m['status']=='PASS'
method=json.loads((P/'ROUND-020-METHOD.json').read_text());assert sha(R/method['raw'])==method['sha256']
for n in ['cross-boundary-round020','scalar-fallback-round020','dense-promotion-round020','generation-wrap-round020']:
 x=json.loads((R/'experiments/EXP-006'/n/'manifest.json').read_text());assert x['status']=='complete' and 'active_command' not in x
final=dict(status='PASS',utc=utc(),checks=checks,public_files_scanned=len(files),private_paths=[],trailing_whitespace=[],experiments_complete=True,experimental_children_ended_utc=m['ended_utc'],source_adoption='NONE',counts=dict(harnesses=7,baselines=13,diagnostics=34,named_boundary_suites=26,sequential_populations=5,accepted=0,rejected=2,parked=3),backend='unknown',model='unknown',token_cost='unknown; supervisor records CLI usage separately')
(P/'ROUND-020-FINAL-CHECKS.json').write_text(json.dumps(final,indent=2)+'\n');files.append(P/'ROUND-020-FINAL-CHECKS.json')
(P/'ROUND-020-SHA256.json').write_text(json.dumps({str(p.relative_to(R)):sha(p) for p in sorted(files)},indent=2)+'\n')
print(json.dumps(dict(status='PASS',sealed_files=len(files),experimental_children_ended_utc=m['ended_utc'],utc=final['utc'])))
