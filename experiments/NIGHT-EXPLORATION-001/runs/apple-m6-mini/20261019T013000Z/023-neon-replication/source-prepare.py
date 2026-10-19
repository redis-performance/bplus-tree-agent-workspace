#!/usr/bin/env python3
"""Create explicit partial Git worktrees and immutable exact-source snapshots; no build/run."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,os
R=Path.cwd();E=Path(__file__).resolve().parent;BASE='13e459ff8800be3f02b6b45c87dd7b0c39453fa9';I=E.parent/'021-cross-host-scan-inventory/inputs/arm/017-corrected-neon';records=[]
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def command(args,input=None):
 p=subprocess.run(list(map(str,args)),input=input,capture_output=True,timeout=60)
 rec=dict(command=[str(x).replace(str(R),'<workspace>') for x in args],returncode=p.returncode,stdout=p.stdout.decode(errors='replace').replace(str(R),'<workspace>'),stderr=p.stderr.decode(errors='replace').replace(str(R),'<workspace>'),stdout_sha256=sha(p.stdout),stderr_sha256=sha(p.stderr),bound_seconds=60)
 records.append(rec);save(E/'source-commands.json',records);assert p.returncode==0,rec
 return p.stdout
assert not (E/'source-manifest.json').exists()
paths=['src','compat','vendor','bench','tests','Makefile','AGENTS.md','docs/POPULATION.md','.workspace-memory/MEMORY.md','.workspace-memory/LIVE-STATUS.md','.workspace-memory/handoff.md']
listing=command(['git','ls-tree','-r',BASE,'--']+paths).decode().splitlines();entries={}
for line in listing:
 meta,path=line.split('\t');mode,kind,obj=meta.split();assert kind=='blob' and mode in ['100644','100755'];entries[path]=(mode,command(['git','show',BASE+':'+path]))
assert all(p in entries for p in ['src/zset_btree.c','src/zset_btree.h','compat/server.h','compat/standalone.c','bench/microbench.c','tests/upstream.c','tests/scan_interval_oracle.c','tests/wide_scan_oracle.c','tests/live_widen_scan_oracle.c','tests/resize_generation_oracle.c'])
oracle=(I/'all_match_guard_oracle_v2.c').read_bytes();assert sha(oracle)=='b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded'
assert 'tests/all_match_guard_oracle_v2.c' not in entries
expected=json.loads((I/'inputs-freeze.json').read_text());owners={'base':'Unmodified baseline, no implementation author','A':'/root/aws_arm','B':'/root/aws_intel','C':'/root/aws_amd'};variants={}
for variant in ['base','A','B','C']:
 wt=R/'worktrees'/('m6-neon-'+variant);assert not wt.exists(),('no overwrite',variant)
 command(['git','worktree','add','--detach','--no-checkout',str(wt),BASE])
 # Materialize exact blobs without checkout/index staging. Deliberately not a full checkout.
 for path,(mode,data) in entries.items():
  target=wt/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);target.chmod(0o755 if mode=='100755' else 0o644)
 assert command(['git','-C',wt,'show','-s','--format=%H','HEAD']).decode().strip()==BASE
 patch=None;macro=None;revision=None
 if variant!='base':
  path=I/'variants'/variant/'candidate.patch';patch=sha(path.read_bytes());assert patch==expected['variants'][variant]['patch_sha256'];macro=expected['variants'][variant]['portable_macro'];revision=expected['variants'][variant]['revision']
  command(['git','-C',wt,'apply','--check',str(path.resolve())]);command(['git','-C',wt,'apply',str(path.resolve())])
 csha=sha((wt/'src/zset_btree.c').read_bytes());assert csha==(expected['source_sha256']['src/zset_btree.c'] if variant=='base' else expected['variants'][variant]['source_sha256'])
 for path,(mode,data) in entries.items():
  if path!='src/zset_btree.c':assert (wt/path).read_bytes()==data,(variant,path)
 (wt/'tests/all_match_guard_oracle_v2.c').write_bytes(oracle)
 hashes={p:sha((wt/p).read_bytes()) for p in entries};hashes['tests/all_match_guard_oracle_v2.c']=sha(oracle)
 variants[variant]=dict(worktree=str(wt.relative_to(R)),git_HEAD=BASE,partial_git_worktree=True,index_staging_performed=False,source_hashes=hashes,original_tracked_materialized_files=len(entries),referee_additions={'tests/all_match_guard_oracle_v2.c':sha(oracle)},patch_sha256=patch,target_c_sha256=csha,portable_macro=macro,original_author=owners[variant],original_revision=revision,exact_model_token_currency_cost='unknown',build_executed=False,native_executed=False)
manifest=dict(status='SOURCE PREPARATION READY; no build/native/timing execution',prepared_utc=datetime.now(timezone.utc).isoformat(),base_commit=BASE,source_commit=BASE,variants=variants,common_original_referee_hashes={p:sha(data) for p,(mode,data) in entries.items() if p!='src/zset_btree.c'},referee_addition_origin=dict(path='021-cross-host-scan-inventory/inputs/arm/017-corrected-neon/all_match_guard_oracle_v2.c',sha256=sha(oracle),source_evidence_commit='a9b2127ec505978c711f2f24650dde8eff7ee3f5'),plan_sha256=sha((E/'PLAN.json').read_bytes()),participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown',scope='Exact previously authored frozen family replication, not new implementations/population',compiler_options='023 PLAN unchanged; no ISA flags added',no_root_source_or_other_campaign_edits=True,partial_scope=paths)
save(E/'source-manifest.json',manifest)
print('READY four partial Git worktrees;',len(entries),'original materialized files each; exact patches and V2 addition verified')
