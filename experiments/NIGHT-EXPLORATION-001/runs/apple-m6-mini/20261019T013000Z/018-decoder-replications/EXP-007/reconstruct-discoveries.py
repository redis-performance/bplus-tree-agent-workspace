#!/usr/bin/env python3
"""Independently reconstruct retained 007/008 discoveries; no measurement child."""
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
for num in ('007','008'):
 wt=Path('worktrees/m6-replica-exp'+num);exp=wt/'experiments'/('EXP-'+num);src=wt/'build/m6-replications'/('EXP'+num)/'discovery';pub=BASE/('EXP-'+num)
 m=json.loads((src/'manifest.json').read_text());build=json.loads((src/'build.json').read_text());saved=json.loads((src/'process-summary.json').read_text());summary=json.loads((src/'summary.json').read_text())
 assert m['status']=='complete' and m['code_commit']=='e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf'
 assert m['driver_sha256']==sha(exp/'run.py')
 assert m['arguments']==dict(out='build/m6-replications/EXP'+num+'/discovery',build='build/exp'+num,blocks=6,samples=129,confirmation=None,budget_seconds=300)
 assert m['elapsed_seconds']<300
 cells=cells_for(num);expected=[]
 for phase in ('aa','compare-A','compare-B','compare-C'):
  for block in range(6):
   for width,reverse,count in cells[block%len(cells):]+cells[:block%len(cells)]:
    for step,label in enumerate('ABBA'):
     expected.append(dict(phase=phase,block=block,step=step,label=label,variant='base' if phase=='aa' or label=='A' else phase[-1],width=width,reversed=reverse,count=count,seed=(81031,81041)[block%2]))
 assert expected==m['schedule'] and len(expected)==len(m['runs'])==len(saved)==(2880 if num=='007' else 15360)
 assert len(summary)==4*len(cells)
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
 owner=json.loads((BASE/(num+'-discovery-owner.json')).read_text())
 assert owner['driver_reaped'] and owner['owned_group_empty'] and owner['exclusive_release_safe'] and owner['returncode']==0
 assert owner['wall_seconds']<owner['bound_seconds']==360
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
    assert cell[stat]['block_effects'][block]==dict(block=block,seed=(81031,81041)[block%2],percent=effect)
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
 for v in ('A','B','C'):
  cs=[x for x in summary if x['phase']=='compare-'+v];loss=[x for x in cs if (x['width'],x['reversed'],x['count']) not in primary_keys and x['median_ns']['median_effect_pct']>1]
  qualified_loss=[x for x in loss if (x['width'],x['reversed'],x['count']) in q]
  describe=lambda x:dict(width=x['width'],reversed=x['reversed'],count=x['count'],median_effect_pct=x['median_ns']['median_effect_pct'],block_effects_pct=[e['percent'] for e in x['median_ns']['block_effects']],control_qualified=(x['width'],x['reversed'],x['count']) in q,min_batch_ns=x['min_batch_ns'])
  primary=[describe(next(x for x in cs if (x['width'],x['reversed'],x['count'])==k)) for k in primary_keys]
  results.append(dict(variant=v,primary=primary,guard_median_losses_gt1=len(loss),guard_median_losses_with_AA_range_qualified_controls=len(qualified_loss),qualified_control_guard_losses=[describe(x) for x in qualified_loss],all_guard_losses=[describe(x) for x in loss],unqualified_controls=len(cells)-len(q),both_primary_gain_gates_met=all(x['median_effect_pct']<=-2 for x in primary)))
 if num=='007':
  shortlist=sorted([r for r in results if r['both_primary_gain_gates_met']],key=lambda x:(x['guard_median_losses_gt1'],x['primary'][0]['median_effect_pct']))[0]['variant']
  assert shortlist=='A'
  eligibility={'canonical_diagnostic_shortlist':shortlist,'literal_original_PLAN_confirmation_trigger':True,'confirmation_executed_by_auditor':False,'source_acceptance_eligible':False,'reason':'A is the diagnostic shortlist; primary A/A fails, guard losses/unqualified cells remain and short batches cannot qualify workspace timing. Literal original PLAN still requests one fixed fresh diagnostic confirmation when a shortlist exists. Root owns any later authorization.'}
 else:
  assert not any(x['both_primary_gain_gates_met'] for x in results)
  eligibility={'canonical_eligible_variant':'NONE','literal_original_PLAN_confirmation_trigger':False,'confirmation_executed_by_auditor':False,'source_acceptance_eligible':False,'reason':'All three fail count16 primary>=2% gain; A/A/guard losses and all-cell short-window gaps also remain. Count96 gains alone cannot substitute.'}
 # Inspect every source output before publication; original metadata and raw bytes are retained.
 privacy=[];filehashes={}
 for file in sorted(src.rglob('*')):
  if not file.is_file():continue
  data=file.read_bytes()
  if re.search(rb'/' + rb'Users/|/' + rb'private/|/' + rb'tmp/|-----BEGIN [^-]*PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{20,}',data):privacy.append(str(file.relative_to(src)))
  filehashes[str(file.relative_to(src))]=hashlib.sha256(data).hexdigest()
 assert not privacy,privacy
 dest=pub/'discovery';assert not dest.exists();shutil.copytree(src,dest)
 for relative,h in filehashes.items():assert sha(dest/relative)==h
 output_manifest=dict(status='BYTE_IDENTICAL_COMPLETE_COPY',source_directory=str(src),file_count=len(filehashes),files_sha256=filehashes,privacy_scan='PASS; no metadata derivatives/redaction needed',raw_profiles_copied=False)
 (pub/'discovery-sha256.json').write_text(json.dumps(output_manifest,indent=2)+'\n')
 report=dict(status='PASS independent reconstruction; performance eligibility remains separately limited',participant='/root/followup_proposal_a',backend='Inherited GPT-6/Codex family; exact serving model/token/currency cost unknown',independence='Reviewer did not prepare these007/008 implementations/builds. Same-machine retained-evidence reconstruction, not new experimental confirmation.',published_freeze='95f3b1e68',root_freeze_sha256=sha(BASE/'ROOT-FREEZE.json'),corrected018_plan_sha256=sha(BASE/'PLAN.json'),canonical_source_hashes={n:sha(exp/n) for n in ('PLAN.md','run.py','analyse.py','audit.py','build.py')},canonical_audit=json.loads((src/'AUDIT.json').read_text()),canonical_commands='INDEPENDENT-COMMANDS.json',schedule_reconstructed_from_canonical_source=True,cells=len(cells),schedule_processes=len(expected),measured_batches=batch_count,paired_block_effects=len(summary)*12,fixture_identities=len(identities),independent_splitmix_geometry_checksum_model=True,raw_hash_checks=raw_hash_checks,histogram_reconstructed=True,process_statistics_reconstructed=True,all_UTC_windows_serial=True,campaigns007_then008_serial=True,owner_reaped_group_empty_evidence=True,owner_metadata_sha256=sha(BASE/(num+'-discovery-owner.json')),manifest_sha256=sha(src/'manifest.json'),build_manifest_sha256=sha(src/'build.json'),binary_hashes_after=m['binary_hashes_after'],root_frozen_inputs_verified=files_verified,AA_median_block_range_qualified=len(q),AA_total=len(cells),AA_qualified_cells=[dict(width=k[0],reversed=k[1],count=k[2]) for k in sorted(q)],batch_window_screen=dict(required_minimum_ns=10000000,minimum_observed_ns=min_ns,maximum_observed_ns=max_ns,total_batches=batch_count,batches_below10ms=short_batches,AA_cells_with_minimum_ge10ms=sum(x['min_batch_ns']>=10000000 for x in controls.values()),all_phase_cells_below10ms_minimum=sum(x['min_batch_ns']<10000000 for x in summary),total_phase_cells=len(summary),canonical_plan_analyzer_audit_does_not_enforce10ms=True,range_qualification_is_not_full_workspace_timing_qualification=True),endpoint_migrations=migration_count,results=results,eligibility=eligibility,publication_copy=dict(file_count=len(filehashes),all_byte_identical=True,private_paths_or_credentials_detected=False,metadata_redactions=0,sha_manifest='discovery-sha256.json'),retained_review_read_failure='An exploratory read expected an EXP008 freeze.json that canonical EXP008 does not provide; FileNotFoundError only. No analysis, measurement or source failure; no rerun.',new_timings_builds_profiles_or_confirmation=0,limitations=['Canonical range qualification omits the workspace10ms batch minimum; every cell minimum is short. No hidden correction or threshold/count retuning applied.','Canonical selection-input calls all >1% median cells guards, including primaries; independent guard counts explicitly exclude the declared primary cells.','M6 only; no M1 pooling or historical time subtraction. Legacy adapter remains distinct from current corrected baseline.','Endpoint CPU IDs do not prove complete residency/frequency; no hardware events, cycles or instruction costs are inferred.','Leaf_bytes are requested synthetic leaf storage, not full allocator/process/stack ownership measurements.','Independent reconstruction is not independent experimental confirmation; profiles stay private and no fresh confirmation was run.'])
 (pub/'INDEPENDENT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
 md=[f'# EXP-{num} M6 discovery: independent audit','', '**Retained-evidence audit PASS. No source acceptance.** '+eligibility['reason'],'',f'The unchanged canonical analyzer and `audit.py --kind discovery` both exited0 within their300-second analysis bounds. This independent reconstruction confirms {len(expected):,} processes, {batch_count:,} batches, {len(cells)} cells, all four phases, six alternating-seed ABBA blocks, exact rotation/commands and serial UTC windows. All raw hashes and min/median/p90/max statistics, block effects and histogram buckets agree. A separate Python unsigned64 SplitMix/finite-score model reproduces every fixture fingerprint, checksum, requested leaf byte count and offset/crossing geometry.','',f'Current018 PLAN correctly declares2,880 EXP007 discovery/1,440 conditional confirmation and15,360 EXP008 discovery. Published freeze95f3b1e68, exact source/referee/helper/binaries and intentional legacy adapter verify. The stale earlier preparation count is not the published plan. Both campaign owner records show exit0, driver reaped, group empty and release safe; no probe is repeated by the auditor.','',f'A/A block-range qualification is **{len(q)}/{len(cells)}**. This is the canonical six-median-effects-within±1% screen, not full timing qualification. All{len(summary)} phase/cell minima are below10ms; {short_batches:,}/{batch_count:,} individual batches are below10ms, spanning{min_ns:.3f}..{max_ns:.3f}ns overall. The canonical scripts do not reject short batches. Their PASS is raw-accounting integrity and must not be promoted to workspace precision. No batch count, clock, gate or row was changed.','', '| Variant | Primary median effects % | Guard median losses >1% | Losses with range-qualified A/A |','|---|---|---:|---:|']
 for r in results:md.append('| '+r['variant']+' | '+', '.join(f"count{x['count']}: {x['median_effect_pct']:+.6f}" for x in r['primary'])+f" | {r['guard_median_losses_gt1']} | {r['guard_median_losses_with_AA_range_qualified_controls']} |")
 md+=['','Guard counts exclude the declared primaries; canonical selection-input includes primary regressions in its broader diagnostic list. All individual losses, primary block effects and qualified-control cell identities are retained in INDEPENDENT-AUDIT.json. These are median diagnostic losses with range-qualified controls, not confidence intervals or accepted full-workspace guards.','']
 if num=='007':
  ar=results[0];md+=['A primary six block effects (%): '+', '.join(f'{x:+.9f}' for x in ar['primary'][0]['block_effects_pct'])+'.','', 'A has one >1% guard median loss with a range-qualified control: width62, reverse, count96, +1.179487%. B has four; C has two. The primary control itself fails, and16/30 control cells are unqualified. Under the unchanged diagnostic shortlist rule A is provisionally selected and the literal PLAN requests one fixed fresh diagnostic confirmation; this audit does not execute or authorize it. The failed/short controls and guard losses preclude acceptance.','']
 else:md+=['Count16 primary control passes its±1% block-range screen, but A offers only−0.042088%, B regresses+5.728661%, and C+71.145130%. None reaches the required2% gain. Count96 control fails, so A/B count96 gains cannot rescue selection. Exact canonical outcome isNONE/no confirmation.','']
 md+=[f'Complete new discovery output is copied byte-for-byte to discovery/:{len(filehashes):,} files, including every raw CSV/stderr, original manifest/build metadata and canonical derived summaries. Source output was scanned before canonical analysis and again before copying; no private prefixes/credentials were detected, so no metadata redaction/derivative was needed. discovery-sha256.json seals the copy. Raw sample profiles are not copied.','', 'One exploratory read expected a nonexistent EXP008 freeze.json and failed read-only; canonical EXP008 supplies build/file identities rather than that file. It caused no experiment or canonical-analysis retry.','', 'Participant `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving model/token/currency cost unknown. I did not prepare007/008. No new build, timing, profile, rerun, confirmation, shared README/memory/Git write or source edit occurred. Same-host reconstruction is distinct from independent experimental confirmation.','']
 (pub/'INDEPENDENT-AUDIT.md').write_text('\n'.join(md))
 print(num,'PASS',len(expected),'processes',batch_count,'batches','copy files',len(filehashes),'AA',len(q),'short',short_batches,flush=True)
