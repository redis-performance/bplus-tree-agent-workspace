#!/usr/bin/env python3
"""Pinned Git-blob evidence inventory only. No build, worktree, network or workload."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,re
E=Path(__file__).resolve().parent;URL='https://github.com/redis-performance/bplus-tree-agent-workspace/blob/'
refs={'arm':'a9b2127ec505978c711f2f24650dde8eff7ee3f5','amd':'af2131b804b94acad96f6de47f7a243d4fca4ca8','intel':'a8d051d0bef1363f09ab2981f410e2d1ffbaf5b1'};CORRECTED='13e459ff8800be3f02b6b45c87dd7b0c39453fa9';commands=[];catalog=[];cache={}
sha=lambda b:hashlib.sha256(b).hexdigest()
def read(ref,path,host=None,copy=False):
 key=(ref,path)
 if key not in cache:
  cmd=['git','show',ref+':'+path];q=subprocess.run(cmd,capture_output=True,timeout=20);commands.append(dict(command=cmd,returncode=q.returncode,stdout_sha256=sha(q.stdout),stderr_sha256=sha(q.stderr),bound_seconds=20));assert q.returncode==0,(path,q.stderr.decode());cache[key]=q.stdout
 data=cache[key];row=dict(commit=ref,path=path,sha256=sha(data),bytes=len(data),url=URL+ref+'/'+path)
 if copy:
  target=E/'inputs'/host/path.split('/20261019T020000Z/',1)[-1];target.parent.mkdir(parents=True,exist_ok=True)
  # Preserve exact public Git blob only if it contains no private path/credential marker.
  patterns=[rb'/' + rb'Users/[^\s\"\']+',rb'/' + rb'(?:private/)?var/folders/[^\s\"\']+',rb'BEGIN '+rb'[A-Z ]*PRIVATE'+rb' KEY',rb'github_'+rb'pat_']
  if any(re.search(p,data) for p in patterns):row['copy']='OMITTED: original public blob URL/hash retained; path hygiene'
  else:target.write_bytes(data);row['local_copy']=str(target.relative_to(E));row['copy']='byte-identical'
 if not any(x['commit']==ref and x['path']==path for x in catalog):catalog.append(row)
 return data
files={
'arm':['STATUS.md','015-corrected-scan-aa/PLAN.md','015-corrected-scan-aa/RESULT.md','016-corrected-arm-proposals/provenance.json','017-corrected-neon/PLAN.md','017-corrected-neon/RESULT.md','017-corrected-neon/VALIDATION-RESULT.md','017-corrected-neon/CONFIRMATION-PLAN.md','017-corrected-neon/inputs-freeze.json','017-corrected-neon/comparison-freeze.json','017-corrected-neon/all_match_guard_oracle_v2.c','017-corrected-neon/run-screen.py','017-corrected-neon/validate.py','017-corrected-neon/variants/A/provenance.json','017-corrected-neon/variants/A/implementation.md','021-fold-predicate-review/COMMON-PACKET.md','022-baseline-mask-attribution/README.md'],
'amd':['STATUS.md','008-scan-tags/COMMON-PACKET.md','008-scan-tags/independent-selection.md','008-scan-tags/implementation-selection.md','008-scan-tags/GUARDS.md','008-scan-tags/mechanism/RESULT.md','017-corrected-scan/RESULT.md','017-corrected-scan/AA-PLAN.md','019-corrected-B-replication/PLAN.md','019-corrected-B-replication/RESULT.md','019-corrected-B-replication/VALIDATION.md','019-corrected-B-replication/expected.json','019-corrected-B-replication/validation/freeze.json','019-corrected-B-replication/candidate.patch','020-arm-corrected-implementation-C/implementation.json'],
'intel':['STATUS.md','015-arm-corrected-scan-review/implementation-B/manifest.json','017-corrected-scan-replication/PLAN.md','017-corrected-scan-replication/plan-freeze.json','017-corrected-scan-replication/candidate.patch']}
for host,paths in files.items():
 for p in paths:read(refs[host],f'experiments/NIGHT-EXPLORATION-001/runs/aws-{host}/20261019T020000Z/'+p,host,True)
 for v in 'ABC':
  family='017-corrected-neon' if host=='arm' else '008-scan-tags' if host=='amd' else None
  if family:read(refs[host],f'experiments/NIGHT-EXPLORATION-001/runs/aws-{host}/20261019T020000Z/{family}/variants/{v}/candidate.patch',host,True)
  if host=='amd':read(refs[host],f'experiments/NIGHT-EXPLORATION-001/runs/aws-{host}/20261019T020000Z/008-scan-tags/variants/{v}/implementation.md',host,True)
source_files=['src/zset_btree.c','src/zset_btree.h','compat/server.h','compat/standalone.c','bench/microbench.c','tests/upstream.c','tests/scan_interval_oracle.c','tests/wide_scan_oracle.c','tests/live_widen_scan_oracle.c','tests/resize_generation_oracle.c','vendor/redis/siphash.c']
identities={label:{p:sha(read(ref,p)) for p in source_files} for label,ref in {**refs,'corrected_campaign_base':CORRECTED}.items()}
current={p:sha(Path(p).read_bytes()) for p in source_files};assert current==identities['corrected_campaign_base']
# Reconstruct target bytes entirely in memory; never apply a patch to any checkout.
def apply(source,patch):
 src=source.decode().splitlines(True);lines=patch.decode().splitlines(True);out=[];cursor=0;i=0
 while i<len(lines):
  m=re.match(r'^@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@',lines[i])
  if not m:i+=1;continue
  pos=int(m[1])-1;assert pos>=cursor;out+=src[cursor:pos];i+=1
  while i<len(lines) and not lines[i].startswith('@@ '):
   x=lines[i]
   if x.startswith(('diff --git','--- a/','+++ b/')):break
   if x.startswith(' '):assert src[pos]==x[1:];out.append(src[pos]);pos+=1
   elif x.startswith('-'):assert src[pos]==x[1:];pos+=1
   elif x.startswith('+'):out.append(x[1:])
   elif x.startswith('\\'):pass
   else:break
   i+=1
  cursor=pos
 out+=src[cursor:];return ''.join(out).encode()
base=read(CORRECTED,'src/zset_btree.c');variants=[]
armfreeze=json.loads(read(refs['arm'],'experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/017-corrected-neon/inputs-freeze.json'))
for host,family,owners in [('arm','017-corrected-neon',{'A':'/root/aws_arm','B':'/root/aws_intel','C':'/root/aws_amd'}),('amd','008-scan-tags',{'A':'/root/aws_amd','B':'/root/aws_intel','C':'/root/aws_arm'})]:
 for v in 'ABC':
  path=f'experiments/NIGHT-EXPLORATION-001/runs/aws-{host}/20261019T020000Z/{family}/variants/{v}/candidate.patch';patch=read(refs[host],path);target=apply(base,patch);entry=dict(family='corrected-NEON' if host=='arm' else 'original-SSE2',variant=v,author=owners[v],authoring='Actual distinct native agent, independently authored according to sealed provenance; not sequential self-passes',exact_model='unknown',token_currency_cost='unknown',patch_sha256=sha(patch),target_c_sha256=sha(target),url=URL+refs[host]+'/'+path,changed_file='src/zset_btree.c only')
  if host=='arm':assert entry['patch_sha256']==armfreeze['variants'][v]['patch_sha256'] and entry['target_c_sha256']==armfreeze['variants'][v]['source_sha256'];entry.update(armfreeze['variants'][v])
  variants.append(entry)
B=next(x for x in variants if x['family']=='original-SSE2' and x['variant']=='B');assert B['patch_sha256']=='bd93f3922c72c4f1e8776a897e80321e3380345ee4dbd37d6d62e99683f4a644' and B['target_c_sha256']=='204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23'
for h,p in [('amd','019-corrected-B-replication'),('intel','017-corrected-scan-replication')]:assert sha(read(refs[h],f'experiments/NIGHT-EXPLORATION-001/runs/aws-{h}/20261019T020000Z/{p}/candidate.patch'))==B['patch_sha256']
report=dict(status='READ-ONLY EVIDENCE INVENTORY COMPLETE; no hypothesis/source selected',participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact model/token/currency cost unknown',pinned_commits=refs,corrected_source_commit=CORRECTED,identities=identities,current_M6_hashes=current,current_M6_matches_actual_corrected_campaign_base=True,branch_root_adapter_caveat='All three pinned branch roots still have legacy compat79b3/adf0. Actual corrected campaign snapshots use13e and freezes record468a/c923. Do not build branch-root adapter by mistake.',candidate_variants=variants,corrected_AMD_Intel_replicate_exact_original_SSE2_B=True,repository_url=URL.removesuffix('/blob/'),public_links_network_verified=False,source_adoption='NONE',local_build_test_profile_measurements=0,git_mutations_network_jobs_ssh=0,unknowns=['M6 qualification/noise and full validation runtime unmeasured','ARM-native NEON path activation and generated Apple Clang21 code not checked by this read-only inventory','No full guard/confirmation campaign runtime proven before07:15UTC','Remote results read from pinned published reports, not recomputed from every raw timing/profile row'])
(E/'INVENTORY.json').write_text(json.dumps(report,indent=2)+'\n');(E/'SOURCES.json').write_text(json.dumps(catalog,indent=2)+'\n');(E/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
print('COMPLETE',len(catalog),'pinned blobs',len(commands),'bounded git-show reads; candidates',[(x['family'],x['variant'],x['patch_sha256'],x['target_c_sha256']) for x in variants])
