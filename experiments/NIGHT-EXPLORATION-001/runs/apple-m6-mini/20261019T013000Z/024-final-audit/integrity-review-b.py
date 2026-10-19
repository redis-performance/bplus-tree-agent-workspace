#!/usr/bin/env python3
"""Read-only integrity reconstruction; no imports of experimental drivers or children."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,signal
R=Path.cwd();B=R/'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z';E=B/'024-final-audit'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def rel(p):return str(Path(p).relative_to(R))
def main():
 failures=[];seals=[];union={};pin_count=0;patches={};checked={}
 names=['018-decoder-replications/ROOT-FREEZE.json','019-corrected-member-index-profile/freeze.json','020-member-index-profile-continuation/freeze.json','022-source-proposal-review/inputs-sha256.json','023-neon-replication/validation-freeze.json','023-neon-replication/freeze.json']
 for name in names:
  file=B/name;obj=load(file);table=obj['files_sha256'] if 'files_sha256' in obj else obj;bad=[]
  for path,want in table.items():
   p=R/path;actual=sha(p) if p.is_file() else None;checked[path]=actual
   if actual!=want:bad.append({'path':path,'expected':want,'actual':actual})
   if path in union and union[path]!=want:failures.append({'type':'conflicting overlapping pin','path':path})
   union[path]=want;pin_count+=1
   if path.endswith('.patch'):patches[path]=want
  seals.append({'path':rel(file),'sha256':sha(file),'schema':'files_sha256 object' if 'files_sha256' in obj else 'direct path-to-SHA256 object','entries':len(table),'mismatches':bad})
  failures.extend(bad)
 manifest=load(B/'023-neon-replication/source-manifest.json');baseline=manifest['variants']['base']['source_hashes'];root_files={};root_absent=[]
 for name,want in baseline.items():
  if name=='Makefile' or name.startswith(('src/','compat/','vendor/','bench/','tests/')):
   p=R/name
   if not p.is_file():root_absent.append(name);continue
   actual=sha(p);root_files[name]=actual
   if actual!=want:failures.append({'type':'root source/referee mismatch','path':name,'expected':want,'actual':actual})
 expected_root={'src/zset_btree.c':'d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2','src/zset_btree.h':'496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83','compat/server.h':'468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7','compat/standalone.c':'c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3'}
 for name,want in expected_root.items():
  if root_files.get(name)!=want:failures.append({'type':'corrected root identity missing/mismatch','path':name})
 # The V2 supplemental referee was copied to isolated worktrees, never installed at root.
 supplemental={}
 for v,e in manifest['variants'].items():
  p=R/e['worktree']/'tests/all_match_guard_oracle_v2.c';supplemental[v]={'path':rel(p),'sha256':sha(p)}
  if sha(p)!='b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded':failures.append({'type':'supplemental referee mismatch','variant':v})
 if root_absent!=['tests/all_match_guard_oracle_v2.c']:failures.append({'type':'unexpected root absent files','paths':root_absent})
 historical_patches={}
 for campaign in ['002-rank','003-update','004-lookup']:
  m=load(B/campaign/'implementation-manifest.json')
  for v in ['A','B','C']:
   path=B/campaign/'variants'/v/'candidate.patch';want=m['variants'][v]['patch_sha256'];actual=sha(path);historical_patches[rel(path)]={'expected':want,'actual':actual}
   if actual!=want:failures.append({'type':'historical losing patch changed','path':rel(path)})
 for name in ['005-decode/comparison-freeze.json','006-followup/freeze.json']:
  for path,want in load(B/name)['files'].items():
   if path.endswith('.patch'):
    actual=sha(R/path);historical_patches[path]={'expected':want,'actual':actual}
    if actual!=want:failures.append({'type':'historical losing patch changed','path':path})
 for v in ['A','B','C']:
  entry=load(B/'006-followup/variants'/v/'validation.json')
  want=entry['artifacts']['candidate.patch'] if v=='A' else entry['patch_sha256'] if v=='B' else entry['hashes']['candidate.patch']
  path=B/'006-followup/variants'/v/'candidate.patch';actual=sha(path);historical_patches[rel(path)]={'expected':want,'actual':actual}
  if actual!=want:failures.append({'type':'historical006 losing patch changed','path':rel(path)})
 journals=[];intervals=[];raw_count=0
 def examine(label,records,owner=False):
  nonlocal raw_count
  issues=[];last=None
  for i,r in enumerate(records):
   reaped=r.get('driver_reaped') if owner else r.get('child_reaped');empty=r.get('owned_group_empty');safe=r.get('exclusive_release_safe') if owner else r.get('release_safe')
   if not (reaped is True and empty is True and safe is True) or r.get('timed_out',False):issues.append({'index':i,'type':'cleanup/timeout issue'})
   negative=r.get('negative_control',False)
   if (negative and r.get('returncode')!=-signal.SIGABRT) or (not negative and r.get('returncode')!=0):issues.append({'index':i,'type':'unexpected returncode','returncode':r.get('returncode')})
   start=datetime.fromisoformat(r['started_utc']);end=datetime.fromisoformat(r['ended_utc'] if owner else r['finished_utc'])
   if end<start or (last is not None and start<last):issues.append({'index':i,'type':'invalid/overlapping intervals'})
   last=end;intervals.append((start,end,label,i))
   for channel,meta in r.get('logs' if owner else 'raw',{}).items():
    p=R/meta['path'];raw_count+=1
    if not p.is_file() or sha(p)!=meta['sha256'] or p.stat().st_size!=meta['bytes']:issues.append({'index':i,'type':'raw log missing/changed','channel':channel})
  journals.append({'label':label,'entries':len(records),'all_recorded_reaped_group_empty_safe':not issues,'issues':issues});failures.extend(issues)
 owners=[]
 for file in sorted((B/'018-decoder-replications').glob('*-owner.json')):
  item=load(file);owners.append(item)
 owners.sort(key=lambda x:x['started_utc']);examine('018 outer phase owners',owners,True)
 for name in ['019-corrected-member-index-profile/commands.jsonl','020-member-index-profile-continuation/commands.jsonl','023-neon-replication/aa/commands.jsonl']:
  file=B/name;records=[json.loads(x) for x in file.read_text().splitlines()];examine(name,records)
 val=load(B/'023-neon-replication/validation/result.json');examine('023 validation commands',val['commands'])
 intervals.sort();overlaps=[]
 for first,second in zip(intervals,intervals[1:]):
  if first[1]>second[0]:overlaps.append({'first':first[2],'first_index':first[3],'second':second[2],'second_index':second[3]})
 failures.extend(overlaps)
 phase_states={}
 for name in ['019-corrected-member-index-profile/capture-status.json','020-member-index-profile-continuation/capture-status.json','023-neon-replication/aa/status.json']:
  state=load(B/name);phase_states[name]={k:state[k] for k in ['status','exclusive_runner_release_safe','release_safe','completed_captures','completed_new_captures','combined_captures','completed_processes','qualified'] if k in state}
  if not state.get('exclusive_runner_release_safe',state.get('release_safe',False)):failures.append({'type':'phase release unsafe','path':name})
 # Inspect only the scoped public 023 and its own private timing directory for launch artifacts.
 campaign=B/'023-neon-replication';discovery_dirs=[p for p in [campaign/'discovery',R/'scratch/m6-neon-replication/timing/discovery'] if p.exists()];discovery_acks=[]
 for p in campaign.rglob('*.json'):
  o=load(p)
  if isinstance(o,dict) and o.get('phase')=='discovery' and o.get('status')=='authorized':discovery_acks.append(rel(p))
 private_ack_candidates=[]
 for p in (R/'scratch').iterdir():
  if not (p.is_file() and p.suffix=='.json' and 'neon' in p.name.lower() and any(x in p.name.lower() for x in ['ack','release'])):continue
  o=load(p)
  if isinstance(o,dict) and o.get('phase')=='discovery' and o.get('status')=='authorized':private_ack_candidates.append(rel(p))
 if discovery_dirs or discovery_acks or private_ack_candidates:failures.append({'type':'unexpected discovery artifact','dirs':[rel(p) for p in discovery_dirs],'public_acks':discovery_acks,'private_acks':private_ack_candidates})
 # Re-read every pinned file after audit, catching concurrent changes to the actual byte snapshots.
 changed=[]
 for path,want in union.items():
  p=R/path
  if not p.is_file() or sha(p)!=want:changed.append(path)
 if changed:failures.append({'type':'post-audit frozen identity changed','paths':changed})
 report={'status':'PASS' if not failures else 'FAIL','scope':'Source and retained-evidence integrity only; not candidate acceptance','participant':'/root/followup_proposal_b','backend':'Inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown','generated_utc':datetime.now(timezone.utc).isoformat(),'failures':failures,'sealed_tables':seals,'total_pin_entries_including_overlap':pin_count,'distinct_exact_relative_paths':len(union),'repeat_pin_entries':pin_count-len(union),'root_source_referee_files_verified':root_files,'root_intentionally_absent_supplemental':root_absent,'supplemental_referee_copies':supplemental,'root_corrected_source_identity_unchanged':all(root_files.get(p)==h for p,h in expected_root.items()),'retained_frozen_patch_files':patches,'retained_patch_file_count':len(patches),'additional_historical_pinned_patches':historical_patches,'additional_historical_patch_count':len(historical_patches),'journal_results':journals,'total_journal_entries':sum(x['entries'] for x in journals),'outer_owner_vs_direct_child_journal_scope':'018 records are outer owned driver/group phases;019/020/023 are direct child records. Their counts are not equivalent process denominators.','raw_log_streams_verified':raw_count,'all_examined_intervals_serial':not overlaps,'phase_states':phase_states,'discovery_launch_artifacts':{'public_directory_exists':(campaign/'discovery').exists(),'private_raw_directory_exists':(R/'scratch/m6-neon-replication/timing/discovery').exists(),'public_authorized_acks':discovery_acks,'scoped_private_authorized_acks':private_ack_candidates,'prepared_schedule_exists':(campaign/'discovery-schedule.json').is_file()},'post_audit_frozen_entries_match':not changed,'source_adoption':'NONE: root source bytes remain exact baseline; no source acceptance inferred','limitations':['Hashes establish current retained bytes match sealed expected snapshots and remained unchanged during this audit; they do not prove every historical filesystem operation or Git history. No Git commands were run.','Historical reap/group-empty records and raw outputs are checked; no live process sweep or independent replay of past kernel state occurred.','Discovery absence is scoped to023 and its owned timing/ACK locations, not a claim about unrelated private filesystem locations.','Counts of overlapping seals are pin entries, not unique files. Distinct paths may still refer to identical byte content.','018 original-adapter decoder evidence remains separate from corrected019/020/023; identity verification never transfers timing qualification.','The original 019 INCOMPLETE state is preserved;020 forms a separate continuation. No PARK/REJECT result is promoted to candidate acceptance.'],'script_sha256':sha(__file__)}
 (E/'INTEGRITY-REVIEW-B.json').write_text(json.dumps(report,indent=2)+'\n')
 md=f'''# Final source and evidence integrity review — {report['status']}\n\nRoot target C/H and corrected compatibility files retain their exact expected identities. Another 51 root Makefile, benchmark, test and vendor files match the corrected baseline snapshot (55 root files total). The supplemental V2 oracle is intentionally absent from root; all four isolated worktree copies retain its exact frozen hash.\n\nThe requested seal tables contain {', '.join(str(x['entries']) for x in seals)} entries respectively (018 ROOT,019,020,022,023 validation,023 timing). Every entry matches, before and after this audit. These are {pin_count} overlapping pins across {len(union)} distinct relative paths, not {pin_count} unique files. All {len(patches)} distinct pinned patch files remain byte-identical. An additional {len(historical_patches)} earlier losing patch paths match their 002–006 implementation manifests/freezes; these are separate from the six requested seal counts. Full source identities, table identities and patch hashes are in INTEGRITY-REVIEW-B.json.\n\nExamined {sum(x['entries'] for x in journals)} journal entries: {len(owners)} outer 018 owned phases, 3 original 019 captures, 13 continuation 020 captures, 141 validation commands and 48 final 023 A/A children. Every record reports reaped owned child/driver, empty group, safe release and no timeout. All examined intervals are serial and {raw_count} associated raw log streams retain expected hashes and byte counts. Negative validation SIGABRT statuses are expected fault detections. Outer-driver phase records are not an additional count of every canonical process.\n\nNo 023 discovery output directory, private discovery raw directory or authorized discovery ACK exists in the inspected owned locations. Its prepared schedule remains, without a launch. The final A/A status is complete but unqualified; root source remains baseline and no adoption is inferred. Historical 019 INCOMPLETE remains intact beside separate 020 continuation evidence.\n\nThis is a local read-only byte/metadata audit, not candidate acceptance or a fresh correctness/performance run. It imports no experimental driver and spawns no child. Historical process cleanup cannot be independently replayed from retained logs, and hashes do not prove all historical filesystem operations. Reproduce with `python3 <024>/integrity-review-b.py` from root. Participant /root/followup_proposal_b; exact serving model/token/currency costs unknown.\n'''
 (E/'INTEGRITY-REVIEW-B.md').write_text(md)
 print(json.dumps({'status':report['status'],'pin_entries':pin_count,'distinct_paths':len(union),'journals':report['total_journal_entries'],'patches':len(patches),'failures':failures}))
if __name__=='__main__':main()
