from pathlib import Path
import json,hashlib,subprocess,datetime
R=Path(__file__).resolve().parents[2];O=R/'experiments/OVERNIGHT-2026-10-17';E=R/'experiments/EXP-004/ordered-guards';B=O/'BOUNDARY-014/compact-extension';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();utc=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();checks=[]
for name,cmd in [('workspace',['python3','scripts/check-workspace.py','--pristine-source']),('diff',['git','diff','--check']),('compiler',['cc','--version']),('os',['sw_vers']),('arch',['uname','-m'])]:
 out=O/f'ROUND-010-{name}.stdout';err=O/f'ROUND-010-{name}.stderr';start=utc()
 with out.open('w') as so,err.open('w') as se:
  q=subprocess.run(cmd,cwd=R,stdout=so,stderr=se,timeout=120)
 row=dict(name=name,command=cmd,returncode=q.returncode,started_utc=start,ended_utc=utc(),stdout=str(out.relative_to(R)),stderr=str(err.relative_to(R)),stdout_sha256=sha(out),stderr_sha256=sha(err));checks.append(row);assert q.returncode==0,name
A=json.loads((O/'ROUND-010-VERIFY.json').read_text());C=json.loads((B/'audit.json').read_text());M=json.loads((B/'manifest.json').read_text());assert A['status']=='pass' and C['children_passed']==8 and C['no_reruns']
for r in M['runs']:
 assert r['returncode']==0 and r['started_utc']>=A['last_window'][1]
 for k in ['stdout','stderr']:assert sha(B/f'{r["name"]}.{k}')==r[k+'_sha256']
for f in json.loads((B/'faults.json').read_text()):
 for r in f['commands']:
  assert r['started_utc']>=A['last_window'][1]
  for k in ['stdout','stderr']:assert sha(B/r[k])==r[k+'_sha256']
for v,ss in M['snapshots'].items():
 for n,h in ss['files'].items():assert sha(R/ss['path']/n)==h
 for kind,h in C['binaries'][v].items():assert sha(R/ss['path']/f'build/{kind}')==h
final=dict(status='pass',completed_utc=utc(),commands=checks,prior_timing_audit_sha256=sha(O/'ROUND-010-VERIFY.json'),compact_audit_sha256=sha(B/'audit.json'),compact_semantics_pass=True,compact_cross_build_aggregate_prediction='unsupported;original failed assertion retained',compact_commands_follow_all_timings=True,root_source_unchanged=True,accepted_source='NONE',exp004='A/PARK',exp005='PARK/NONE',counts=dict(harnesses=5,baselines=11,diagnostics=19,boundary_suites=14,boundary_fault_types=28,populations=4,accepted=0,rejected=2,parked=2),backend='unknown',model='unknown',cost='unknown')
(O/'ROUND-010-FINAL-CHECKS.json').write_text(json.dumps(final,indent=2)+'\n')
dirs=[O/'HARNESS-005',O/'AA-010',O/'COUNTERS-004',O/'COUNTERS-005',B,E];files=[p for d in dirs for p in d.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
files += list(O.glob('ROUND-010*'))+[O/'verify-round010.py',Path(__file__),R/'README.md',R/'experiments/EXPERIMENTS.md',R/'experiments/SUMMARY.md',R/'experiments/NEXT-STEPS.md',R/'experiments/token-ledger.tsv',R/'experiments/EXP-004/implementation-selection.md']+list((R/'.workspace-memory').glob('*.md'))
files=sorted(set(p for p in files if p.is_file() and p.name not in ['ROUND-010-SHA256.json','ROUND-010-CURATION.json']))
bad=[]
for p in files:
 s=p.read_bytes()
 if (b'/' + b'Users/') in s or (b'/' + b'private/var/') in s:bad.append(str(p.relative_to(R)))
assert not bad,bad
(O/'ROUND-010-CURATION.json').write_text(json.dumps(dict(status='pass',files_scanned=len(files),private_path_matches=bad,raw_method_and_profile_artifacts='ignored scratch; public manifests/checksums only'),indent=2)+'\n')
files.append(O/'ROUND-010-CURATION.json')
(O/'ROUND-010-SHA256.json').write_text(json.dumps({str(p.relative_to(R)):sha(p) for p in files},indent=2)+'\n');print(json.dumps(dict(status='pass',curated_files=len(files),measurement_windows=A['windows'],intervals=A['intervals_recomputed'],compact_cross_build_prediction='unsupported',root_source='preserved')))
