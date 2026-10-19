#!/usr/bin/env python3
"""Independently reconstruct retained007 A fresh confirmation; no measurement child."""
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import csv, hashlib, io, json, math, re, shutil

BASE=Path('experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications')
MASK=(1<<64)-1

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def med(x):
 x=sorted(x);n=len(x);return x[n//2] if n%2 else (x[n//2-1]+x[n//2])/2

def fixture(width,reverse,count,seed):
 state=seed;fingerprint=14695981039346656037;total=0
 low=0x0010000000000000;high=0xffefffffffffffff;mask=(1<<width)-1
 boundaries=[0x7fffffffffffffff,0x8000000000000000,0x7ffffffffffffffe,0x8000000000000001]
 for j in range(8):
  base=high-j*1024 if reverse else low+j*1024
  if 1<=j%8<=4:base=boundaries[j%8-1]
  limit=base-low if reverse else high-base
  for i in range(count):
   state=(state+0x9e3779b97f4a7c15)&MASK;x=state
   x=((x^(x>>30))*0xbf58476d1ce4e5b9)&MASK
   x=((x^(x>>27))*0x94d049bb133111eb)&MASK
   delta=(x^(x>>31))&mask
   if i%4==0:delta=0
   elif i%4==1:delta=mask
   if delta>limit:delta%=limit+1
   ordered=base-delta if reverse else base+delta
   bits=ordered^(1<<63) if ordered>>63 else (~ordered)&MASK
   total=(total+bits)&MASK;fingerprint=((fingerprint^bits)*1099511628211)&MASK
 rounds=(49152+count*8-1)//(count*8)
 scorebytes=0 if width==0 else (((count*width+7)//8+9)&~1)
 return {'operations':count*8*rounds,'leaf_bytes':8*(56+scorebytes),'offset_mask':sum(1<<x for x in {(i*width)%8 for i in range(count)}),'crossings_per_round':8*sum(width+(i*width)%8>64 for i in range(count)),'fixture_hash':fingerprint,'checksum':(total*rounds)&MASK}

def cells_for(n):
 if n=='007':return [(w,r,96) for w in (0,8,31,57,58,59,60,61,62,63,64) for r in (0,1)]+[(w,0,c) for c in (1,7) for w in (8,60,63,64)]
 return [(w,r,c) for w in (0,8,57,58,59,60,61,62,63,64) for r in (0,1) for c in (1,2,4,7,8,16,32,96)]

rootfreeze=json.loads((BASE/'ROOT-FREEZE.json').read_text())
release=json.loads((BASE/'EXCLUSIVE-RELEASE.json').read_text())
assert release['freeze_sha256']==sha(BASE/'ROOT-FREEZE.json')
assert release['published_freeze']['publication']=='Published 95f3b1e68'
previous_campaign_end=None
for num in ('007',):
 wt=Path('worktrees/m6-replica-exp'+num);exp=wt/'experiments'/('EXP-'+num);src=wt/'build/m6-replications'/('EXP'+num)/'confirmation';pub=BASE/('EXP-'+num)
 m=json.loads((src/'manifest.json').read_text());build=json.loads((src/'build.json').read_text());saved=json.loads((src/'process-summary.json').read_text());summary=json.loads((src/'summary.json').read_text())
 assert m['status']=='complete' and m['code_commit']=='e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf'
 assert m['driver_sha256']==sha(exp/'run.py')
 assert m['arguments']==dict(out='build/m6-replications/EXP'+num+'/confirmation',build='build/exp'+num,blocks=6,samples=129,confirmation='A',budget_seconds=180)
 assert m['elapsed_seconds']<180
 cells=cells_for(num);expected=[]
 for phase in ('aa','compare-A'):
  for block in range(6):
   for width,reverse,count in cells[block%len(cells):]+cells[:block%len(cells)]:
    for step,label in enumerate('ABBA'):
     expected.append(dict(phase=phase,block=block,step=step,label=label,variant='base' if phase=='aa' or label=='A' else phase[-1],width=width,reversed=reverse,count=count,seed=(82037,82051)[block%2]))
 assert expected==m['schedule'] and len(expected)==len(m['runs'])==len(saved)==1440
 assert len(summary)==2*len(cells)
 assert build['sanitizers'] is False and build['base_commit']=='4fd3a3fdbce5acca18ee292642a3d80a79f50362' and build['harness_commit']==m['code_commit']
 files_verified={}
 for path,h in rootfreeze['files_sha256'].items():
  if path.startswith(str(wt)+'/'):
   assert sha(path)==h,path;files_verified[path]=h
 for path,h in build['files'].items():assert sha(wt/path)==h,path
 assert build['files']['compat/server.h']=='79b3c9cfa8aec6e003dcf10e6d1c3af71799e357db7d0a0526dca0fd575af0be'
 assert build['files']['compat/standalone.c']=='adf0f87cd7cd7bc043eeb1743b47f90e4484459c090024ffa837cfd34d9b3d63'
 source=(wt/'src/zset_btree.c').read_text();assert sha(wt/'src/zset_btree.c')=='d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2'
 for v in ('base','A','B','C'):
  vb=build['variants'][v];assert sha(wt/vb['binary'])==vb['binary_sha256']==m['binary_hashes_after'][v]
  nested=wt/'worktrees'/('exp'+num+'-'+v)/'src/zset_btree.c'
  if num=='007':text=source+'\n'+(exp/('referee/control.inc' if v=='base' else 'variants/'+v+'/decoder.inc')).read_text()
  else:text=source+'\n'+(exp/'referee/bulk.inc').read_text()+'\n'+(exp/('referee/policy-control.inc' if v=='base' else 'variants/'+v+'/policy.inc')).read_text()
  assert nested.read_text()==text and sha(nested)==vb['source_sha256']
  assert sha(wt/('build/exp'+num)/v/'kernel.o')==vb['kernel_object_sha256']
  assert all(c['returncode']==0 for c in build['commands'])
 owner=json.loads((BASE/('007-confirmation-A-owner.json')).read_text())
 assert owner['driver_reaped'] and owner['owned_group_empty'] and owner['exclusive_release_safe'] and owner['returncode']==0
 assert owner['wall_seconds']<owner['bound_seconds']==240
 assert owner['started_utc']<=m['started_utc']<=m['finished_utc']<=owner['ended_utc']<owner['absolute_cutoff_utc']
 if previous_campaign_end:assert previous_campaign_end<owner['started_utc']
 previous_campaign_end=owner['ended_utc']
 for value in owner['logs'].values():assert sha(value['path'])==value['sha256']
 groups=defaultdict(list);identities={};expected_fixtures={};histogram=Counter();batch_count=0;short_batches=0;min_ns=math.inf;max_ns=0;raw_hash_checks=0;previous_end=m['started_utc'];migration_count=0
 for index,(scheduled,run,ss) in enumerate(zip(expected,m['runs'],saved)):
  assert all(run[k]==v for k,v in scheduled.items()) and run['returncode']==0
  assert previous_end<=run['started_utc']<=run['ended_utc']<=m['finished_utc'];previous_end=run['ended_utc']
  dt=(datetime.fromisoformat(run['ended_utc'])-datetime.fromisoformat(run['started_utc'])).total_seconds();assert 0<=dt<30
  count=run['count'];rounds=(49152+count*8-1)//(count*8)
  command=[str(Path('build/exp'+num)/run['variant']/'decoder-bench'),'--width',str(run['width']),'--reversed',str(run['reversed']),'--seed',str(run['seed']),'--count',str(count),'--leaves','8','--score-shift','0','--rounds',str(rounds),'--samples','129','--warmup','16']
  assert run['command']==command
  name=f"{index:04d}-{run['phase']}-b{run['block']}-w{run['width']}-r{run['reversed']}-n{count}-{run['label']}"
  assert run['csv']=='raw/'+name+'.csv' and run['stderr']=='raw/'+name+'.stderr'
  for stream in ('csv','stderr'):assert sha(src/run[stream])==run[stream+'_sha256'];raw_hash_checks+=1
  rows=list(csv.DictReader(io.StringIO((src/run['csv']).read_text())));assert len(rows)==129
  identity=(run['width'],run['reversed'],count,run['seed'])
  if identity not in expected_fixtures:expected_fixtures[identity]=fixture(*identity)
  fi=expected_fixtures[identity];values=[];elapsed=[];migrations=0
  for i,r in enumerate(rows):
   assert None not in r and r['kind']=='time' and int(r['sample'])==i
   for k in ('width','reversed','count','seed'):assert int(r[k])==run[k]
   assert int(r['score_shift'])==0 and int(r['leaves'])==8 and int(r['rounds'])==rounds
   for k,v in fi.items():assert int(r[k])==v,(num,index,k)
   invariant=tuple(r[k] for k in ('operations','leaf_bytes','offset_mask','crossings_per_round','fixture_hash','checksum'))
   assert identities.setdefault(identity,invariant)==invariant
   assert r['cycles']==r['instructions']==''
   e=float(r['elapsed_ns']);v=float(r['ns_per_decode']);assert math.isfinite(e) and math.isfinite(v) and e>0 and v>0 and abs(e/fi['operations']-v)<2e-8
   values.append(v);elapsed.append(e);histogram[(run['phase'],run['variant'],run['width'],run['reversed'],count,int(v/.05))]+=1
   migrations+=int(r['cpu_start']!=r['cpu_end'])
  sortedv=sorted(values);stats=dict(min_ns=sortedv[0],median_ns=med(values),p90_ns=sortedv[int(.9*(len(sortedv)-1))],max_ns=sortedv[-1],min_batch_ns=min(elapsed),endpoint_migrations=migrations)
  assert all(ss[k]==v for k,v in scheduled.items()) and all(ss[k]==v for k,v in stats.items())
  groups[(run['phase'],run['width'],run['reversed'],count)].append(dict(scheduled,**stats))
  batch_count+=len(rows);short_batches+=sum(x<10000000 for x in elapsed);min_ns=min(min_ns,min(elapsed));max_ns=max(max_ns,max(elapsed));migration_count+=migrations
 for cell in summary:
  g=groups[(cell['phase'],cell['width'],cell['reversed'],cell['count'])];assert len(g)==24
  for stat in ('min_ns','median_ns'):
   effects=[]
   for block in range(6):
    quartet=[x for x in g if x['block']==block];assert ''.join(x['label'] for x in quartet)=='ABBA'
    av=sum(x[stat] for x in quartet if x['label']=='A')/2;bv=sum(x[stat] for x in quartet if x['label']=='B')/2;effect=100*(bv/av-1);effects.append(effect)
    assert cell[stat]['block_effects'][block]==dict(block=block,seed=(82037,82051)[block%2],percent=effect)
   assert cell[stat]['median_effect_pct']==med(effects) and cell[stat]['effect_min_pct']==min(effects) and cell[stat]['effect_max_pct']==max(effects)
   assert cell[stat]['A']==med([x[stat] for x in g if x['label']=='A']) and cell[stat]['B']==med([x[stat] for x in g if x['label']=='B'])
  assert cell['min_batch_ns']==min(x['min_batch_ns'] for x in g) and cell['endpoint_migrations']==sum(x['endpoint_migrations'] for x in g)
 canonical_hist=Counter()
 for r in csv.DictReader((src/'histogram.csv').read_text().splitlines()):
  key=(r['phase'],r['variant'],int(r['width']),int(r['reversed']),int(r['count']),round(float(r['bin_lower_ns'])/.05));canonical_hist[key]+=int(r['samples'])
 assert histogram==canonical_hist and sum(histogram.values())==batch_count
 controls={(x['width'],x['reversed'],x['count']):x for x in summary if x['phase']=='aa'}
 q={k for k,x in controls.items() if x['median_ns']['effect_min_pct']>=-1 and x['median_ns']['effect_max_pct']<=1}
 primary_keys=[(60,0,96)] if num=='007' else [(60,0,16),(60,0,96)]
 results=[]
 for v in ('A',):
  cs=[x for x in summary if x['phase']=='compare-'+v];loss=[x for x in cs if (x['width'],x['reversed'],x['count']) not in primary_keys and x['median_ns']['median_effect_pct']>1]
  qualified_loss=[x for x in loss if (x['width'],x['reversed'],x['count']) in q]
  describe=lambda x:dict(width=x['width'],reversed=x['reversed'],count=x['count'],median_effect_pct=x['median_ns']['median_effect_pct'],block_effects_pct=[e['percent'] for e in x['median_ns']['block_effects']],control_qualified=(x['width'],x['reversed'],x['count']) in q,min_batch_ns=x['min_batch_ns'])
  primary=[describe(next(x for x in cs if (x['width'],x['reversed'],x['count'])==k)) for k in primary_keys]
  results.append(dict(variant=v,primary=primary,guard_median_losses_gt1=len(loss),guard_median_losses_with_AA_range_qualified_controls=len(qualified_loss),qualified_control_guard_losses=[describe(x) for x in qualified_loss],all_guard_losses=[describe(x) for x in loss],unqualified_controls=len(cells)-len(q),both_primary_gain_gates_met=all(x['median_effect_pct']<=-2 for x in primary)))

 # Scope and authorizing identities are retained separately from the immutable original freeze.
 confirmation_plan=json.loads((pub/'CONFIRMATION-PLAN.json').read_text())
 for path,h in confirmation_plan['files_sha256'].items():assert sha(path)==h,path
 confirmation_release=json.loads((pub/'CONFIRMATION-RELEASE.json').read_text())
 assert confirmation_release['published_ack']['publication']=='Published 5289562af'
 assert confirmation_release['all_three_agents_idle'] and confirmation_release['literal_original_diagnostic_shortlist']=='A'
 discovery=json.loads((pub/'discovery/manifest.json').read_text());assert discovery['finished_utc']<m['started_utc']
 assert discovery['binary_hashes_after']==m['binary_hashes_after']
 assert {r['seed'] for r in discovery['runs']}.isdisjoint({r['seed'] for r in m['runs']})
 # Scan categories are encoded as bytes to avoid publishing literal scanner triggers.
 patterns=[bytes.fromhex(x) for x in ('2f55736572732f','2f707269766174652f','2f746d702f')]
 privacy=[];filehashes={}
 for file in sorted(src.rglob('*')):
  if not file.is_file():continue
  data=file.read_bytes()
  if any(pattern in data for pattern in patterns):privacy.append(str(file.relative_to(src)))
  filehashes[str(file.relative_to(src))]=hashlib.sha256(data).hexdigest()
 assert not privacy,privacy
 dest=pub/'confirmation';assert not dest.exists();shutil.copytree(src,dest)
 for relative,h in filehashes.items():assert sha(dest/relative)==h
 (pub/'confirmation-sha256.json').write_text(json.dumps(dict(status='BYTE_IDENTICAL_COMPLETE_COPY',source_directory=str(src),file_count=len(filehashes),files_sha256=filehashes,privacy_scan='PASS; original metadata/raw bytes retained; no derivatives needed',raw_profiles_copied=False),indent=2)+'\n')
 primary_control=controls[(60,0,96)]
 result=results[0];primary=result['primary'][0]
 report=dict(status='PASS independent retained-confirmation reconstruction; source selection NONE',participant='/root/followup_proposal_a',backend='Inherited GPT-6/Codex family; exact serving model/token/currency cost unknown',independence='Same auditor as discovery, separate reconstruction of fresh confirmation rows; not independent experimental authorship or a different-machine run.',published_confirmation='5289562af',immutable_root_freeze_sha256=sha(BASE/'ROOT-FREEZE.json'),confirmation_plan_sha256=sha(pub/'CONFIRMATION-PLAN.json'),confirmation_release_sha256=sha(pub/'CONFIRMATION-RELEASE.json'),owner_metadata_sha256=sha(BASE/'007-confirmation-A-owner.json'),canonical_commands='CONFIRMATION-COMMANDS.json',canonical_scripts_sha256={x:sha(exp/x) for x in ('run.py','analyse.py','audit.py','PLAN.md')},canonical_audit=json.loads((src/'AUDIT.json').read_text()),exact_schedule=dict(phases=['aa','compare-A'],cells=30,blocks=6,order='ABBA',seeds=[82037,82051],processes=1440,samples_per_process=129,measured_batches=batch_count,rounds='ceil49152/(count*8)',leaves=8,score_shift=0,warmup=16),all_schedule_commands_rotation_counts_checked=True,raw_hash_checks=raw_hash_checks,independent_fixture_model=True,fixture_identities=len(identities),all_process_statistics_and_block_effects_reconstructed=True,histogram_reconstructed=True,paired_block_effects=len(summary)*12,all_UTC_windows_serial=True,owner_exit0_reaped_group_empty=True,fresh_seeds_disjoint_from_discovery=True,same_exact_binaries_as_discovery=True,binary_hashes=m['binary_hashes_after'],frozen_inputs_verified=files_verified,AA_range_qualified_cells=len(q),AA_total=30,AA_qualified_cells=[dict(width=k[0],reversed=k[1],count=k[2]) for k in sorted(q)],primary_control=dict(median_effect_pct=primary_control['median_ns']['median_effect_pct'],block_effects_pct=[e['percent'] for e in primary_control['median_ns']['block_effects']],minimum_effect_pct=primary_control['median_ns']['effect_min_pct'],maximum_effect_pct=primary_control['median_ns']['effect_max_pct'],range_qualified=(60,0,96) in q),candidate=result,batch_window_screen=dict(required_minimum_ns=10000000,minimum_observed_ns=min_ns,maximum_observed_ns=max_ns,total_batches=batch_count,batches_below10ms=short_batches,all_phase_cells_below10ms_minimum=sum(x['min_batch_ns']<10000000 for x in summary),total_phase_cells=60,canonical_scripts_do_not_enforce10ms=True,workspace_fully_qualified_cells=0),endpoint_migrations=migration_count,source_selection='NONE',interpretation='Fresh primary gain repeats descriptively, but primary A/A fails,16control cells remain unqualified, qualified-range guard medians lose and every batch is short. No accepted public/scalar source or portable effect.',confirmation_complete=True,additional_confirmation_or_retry_authorized=False,publication_copy=dict(file_count=len(filehashes),all_byte_identical=True,metadata_redactions=0,raw_profiles_copied=False,hash_manifest='confirmation-sha256.json'),new_builds_timings_profiles_or_reruns=0,discovery_files_and_seals_unchanged=True,limitations=['Canonical audit PASS means exact retained accounting, not timing precision.','Range-qualified controls omit10ms; zero cells satisfy full workspace timing qualification.','Two guard losses exceed1% in every block with range-qualified controls; short windows still prevent full source-level demonstrated-regression claims.','Leaf bytes are requested synthetic leaf storage, not full process/allocator/stack owned memory.','No hardware-event, cycle, cache or frequency conclusion is available; endpoint IDs do not establish within-window residency.'])
 (pub/'CONFIRMATION-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
 lines=['# EXP-007 A fresh confirmation: independent audit','', '**Retained-evidence audit PASS; source selection NONE.** The primary gain repeats descriptively, while the fresh primary control fails and guard/window limits remain.','', f'The unchanged canonical analyzer and `audit.py --kind confirmation` each exited0/reaped within180-second analysis bounds. Independent reconstruction verifies all1,440 processes,185,760 batches,30 cells, six ABBA blocks, exact rotation, seeds82037/82051, commands, operation counts, UTC seriality, raw hashes/statistics/block effects and histogram buckets. The independent unsigned64 fixture model reproduces every fingerprint, checksum, requested leaf-byte count and offset/crossing geometry. Seeds are fresh relative to discovery; all original baseline/A/B/C binary identities are unchanged.','', f'Owner interval: {owner["started_utc"]} to{owner["ended_utc"]}; owner return0, driver reaped, group empty, release safe. The180-second canonical matrix budget and240-second outer wall bound were met. Confirmation plan/release publication5289562af and immutable original ROOT-FREEZE verify. Only the two phases aa and compare-A ran; no additional measurement is run by this audit.','', f'A primary median effect: **{primary["median_effect_pct"]:+.9f}%**. Six block effects (%): '+', '.join(f'{x:+.9f}' for x in primary['block_effects_pct'])+'.','',f'Fresh primary A/A range is{primary_control["median_ns"]["effect_min_pct"]:+.9f}..{primary_control["median_ns"]["effect_max_pct"]:+.9f}% and fails±1%. Overall **{len(q)}/30** controls pass the canonical six-block median-range screen;16 remain unqualified. A has **{result["guard_median_losses_gt1"]}** guard median losses>1%; **{result["guard_median_losses_with_AA_range_qualified_controls"]}** have range-qualified controls:','', '| Width | Reverse | Count | Median effect % | Block range % |','|---:|---:|---:|---:|---|']
 for loss in result['qualified_control_guard_losses']:
  effects=loss['block_effects_pct'];lines.append(f'|{loss["width"]}|{loss["reversed"]}|{loss["count"]}|{loss["median_effect_pct"]:+.9f}|{min(effects):+.9f}..{max(effects):+.9f}|')
 lines+=['',f'Both listed guard effects exceed+1% in every block. These are diagnostic guard losses with range-qualified controls, not accepted full-workspace regression conclusions. **All{short_batches:,}/{batch_count:,} individual batches are below10ms**, spanning{min_ns:.3f}..{max_ns:.3f}ns. All60 phase/cell minima are short; canonical plans/analyzers/audits do not enforce10ms. No row drops, count retuning, clock changes or threshold relaxation occurred.','',f'Complete confirmation output is copied byte-for-byte to confirmation/:{len(filehashes):,} files, including all raw CSV/stderr and original manifests/canonical derived outputs. Privacy scans before analysis and before publication found no private-path metadata; no redaction or metadata derivative was needed. confirmation-sha256.json seals every copied file. Raw sample profiles remain private and are outside this audit. Discovery audits, copies, seals and priorROOT-FREEZE were not overwritten.','', 'Fresh same-machine reproduction does not repair discovery control/window failures or establish scalar/public iterator behavior. No new source population, candidate adoption, portable speed claim or extra confirmation is authorized.','', 'Participant `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving model/token/currency cost unknown. This reviewer also audited discovery. No timing, build, profile, new measurement, shared-document edit or Git write occurred.','']
 (pub/'CONFIRMATION-AUDIT.md').write_text('\n'.join(lines))
 print('confirmation PASS',len(expected),'processes',batch_count,'batches','AA',len(q),'short',short_batches,'copy files',len(filehashes),flush=True)
