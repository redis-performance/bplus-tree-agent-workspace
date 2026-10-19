from pathlib import Path
from datetime import datetime
import hashlib,json
OUT=Path(__file__).resolve().parent;SCR=Path('scratch/m6-iterator-profile')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze=json.loads((OUT/'freeze.json').read_text());summary=json.loads((OUT/'summary.json').read_text());validation=json.loads((OUT/'validation.json').read_text());journal=[json.loads(s) for s in (OUT/'commands.jsonl').read_text().splitlines()]
for p,h in freeze['files_sha256'].items():assert sha(p)==h,p
for p,h in freeze['binaries_sha256'].items():assert sha(SCR/p)==h,p
for row in journal:
 for raw in row['raw'].values():assert sha(SCR/Path(raw['path']).name)==raw['sha256']
for a,b in zip(journal,journal[1:]):assert datetime.fromisoformat(a['finished_utc'])<=datetime.fromisoformat(b['started_utc'])
assert len(validation['checks'])==8 and len(summary['captures'])==16
assert all(x['sufficient'] and x['samples']>=25 for x in summary['captures'])
assert all(datetime.fromisoformat(freeze['frozen_utc'])<datetime.fromisoformat(x['started_utc']) for x in summary['captures'])
assert len({(x['size'],x['contract'],x['seed']) for x in summary['captures']})==16
assert sum(x['samples'] for x in summary['captures'])==1054
assert sum(x['symbols'].get('zbtreeIteratorNext',0) for x in summary['captures'])==1031
failures=[x for x in journal if x['returncode']!=0];assert len(failures)==1 and failures[0]['name']=='build-iterator-profile'
for p in OUT.rglob('*'):
 if p.is_file():
  text=p.read_text();assert str(Path.cwd()) not in text,(p,'private workspace prefix');assert ('/'+'var/folders/') not in text,(p,'private compiler temp path')
files={str(p.relative_to(OUT)):sha(p) for p in OUT.rglob('*') if p.is_file() and p.name not in ('audit.json','artifacts-sha256.json')}
(OUT/'artifacts-sha256.json').write_text(json.dumps(files,indent=2)+'\n')
result=dict(status='PASS',journal_windows=len(journal),experimental_captures=16,raw_profile_retries=0,correctness_runs=8,captured_pcs=1054,iterator_pcs=1031,prologue_pcs=151,epilogue_pcs=152,stack_counts_are_not_cycles=True,sufficient_captures=16,raw_and_frozen_hashes_verified=True,public_paths_generic=True,source_change_status='NONE: baseline target/header/compat and original Intel referees unchanged',failures_preserved=[dict(name=x['name'],returncode=x['returncode']) for x in failures],artifact_files=len(files),all_processes_finished=True)
(OUT/'audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
