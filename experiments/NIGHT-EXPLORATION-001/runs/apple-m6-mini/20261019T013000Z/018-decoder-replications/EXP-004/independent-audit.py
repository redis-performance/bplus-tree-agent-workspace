#!/usr/bin/env python3
"""Independent retained-row audit; no measurements or runner imports."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal
from collections import defaultdict,Counter
from datetime import datetime
import csv,json,hashlib,statistics,re,shutil
R=Path.cwd();W=R/'worktrees/m6-replica-exp004';D=W/'build/m6-replications/EXP004/discovery';E=R/'experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/018-decoder-replications/EXP-004'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
M=load(D/'manifest.json');B=load(D/'build.json');saved=load(D/'process-summary.json');summary=load(D/'summary.json')
assert M['status']=='complete' and M['code_commit']=='e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf'
assert M['arguments']==dict(out='build/m6-replications/EXP004/discovery',build='build/decoder',blocks=6,samples=129,rounds=64,budget_seconds=300)
assert sha(W/'scripts/run-decoder.py')==M['driver_sha256']
assert all(sha(W/k)==v for k,v in B['files'].items())
for v,x in B['variants'].items():
 assert sha(W/x['binary'])==x['binary_sha256']==M['binary_hashes_after'][v]
 assert sha(W/f'build/decoder/{v}/kernel.o')==x['kernel_object_sha256']
cells=[(w,r) for w in (0,8,31,57,59,60,61,62,63,64) for r in (0,1)];schedule=[]
for phase in ('aa','compare'):
 for block in range(6):
  for w,r in cells[block:]+cells[:block]:
   for step,label in enumerate('ABBA'):
    schedule.append(dict(phase=phase,block=block,step=step,label=label,variant='base' if phase=='aa' or label=='A' else 'A',width=w,reversed=r,seed=(81031,81041)[block%2]))
assert M['schedule']==schedule and len(M['runs'])==len(saved)==len(schedule)==960
U=(1<<64)-1;fixtures={}
def fixture(w,rev,seed):
 key=(w,rev,seed)
 if key in fixtures:return fixtures[key]
 total=0;finger=14695981039346656037;mask=(1<<w)-1
 for j in range(8):
  base=0xffefffffffffffff-j*1024 if rev else 0x0010000000000000+j*1024
  limit=base-0x0010000000000000 if rev else 0xffefffffffffffff-base
  for i in range(96):
   seed=(seed+0x9e3779b97f4a7c15)&U;x=seed;x=((x^(x>>30))*0xbf58476d1ce4e5b9)&U;x=((x^(x>>27))*0x94d049bb133111eb)&U;x^=x>>31
   delta=x&mask
   if i%4==0:delta=0
   elif i%4==1:delta=mask
   if delta>limit:delta%=limit+1
   ordered=base-delta if rev else base+delta;bits=ordered^(1<<63) if ordered>>63 else (~ordered)&U
   total=(total+bits)&U;finger=((finger^bits)*1099511628211)&U
 scorebytes=0 if w==0 else (((96*w+7)//8+9)&~1)
 out=dict(checksum=(total*64)&U,fixture_hash=finger,leaf_bytes=8*(56+scorebytes),operations=49152,offset_mask=sum(1<<x for x in {(i*w)%8 for i in range(96)}),crossings_per_round=8*sum(w+(i*w)%8>64 for i in range(96)))
 fixtures[key]=out;return out
stats=[];rowsn=0;shortrows=0;shortprocess=0;shortprocesssum=0;end=M['started_utc'];minps=None;maxps=0;hist=Counter();timer_total_ps=0
for idx,(run,plan,ss) in enumerate(zip(M['runs'],schedule,saved)):
 assert all(run[k]==v for k,v in plan.items())
 name=f"{idx:04d}-{plan['phase']}-b{plan['block']}-w{plan['width']}-r{plan['reversed']}-{plan['label']}"
 assert run['csv']==f'raw/{name}.csv' and run['stderr']==f'raw/{name}.stderr'
 cmd=[f"build/decoder/{plan['variant']}/decoder-bench",'--width',str(plan['width']),'--reversed',str(plan['reversed']),'--seed',str(plan['seed']),'--count','96','--leaves','8','--score-shift','0','--rounds','64','--samples','129','--warmup','16']
 assert run['command']==cmd and run['returncode']==0 and end<=run['started_utc']<=run['ended_utc']<=M['finished_utc'];end=run['ended_utc']
 assert (datetime.fromisoformat(run['ended_utc'])-datetime.fromisoformat(run['started_utc'])).total_seconds()<=30
 for k in ['csv','stderr']:assert sha(D/run[k])==run[k+'_sha256']
 rows=list(csv.DictReader((D/run['csv']).read_text().splitlines()));assert len(rows)==129
 expected=fixture(plan['width'],plan['reversed'],plan['seed']);ns=[];ps=[];units=[];migrations=0
 for i,row in enumerate(rows):
  assert None not in row and row['kind']=='time' and int(row['sample'])==i
  for k in ['width','reversed','seed']:assert int(row[k])==plan[k]
  for k,v in dict(count=96,leaves=8,score_shift=0,rounds=64,**expected).items():assert int(row[k])==v,(k,row[k],v)
  assert row['cycles']==row['instructions']==''
  p=int(Decimal(row['elapsed_ns'])*1000);value=float(row['ns_per_decode']);assert p>0 and value>0
  assert abs(float(Decimal(row['elapsed_ns'])/49152)-value)<2e-8
  ps.append(p);ns.append(value);units.append(int(Decimal(row['ns_per_decode'])*1000000000));migrations+=row['cpu_start']!=row['cpu_end'];shortrows+=p<10000000000
  hist[(plan['phase'],plan['variant'],plan['width'],plan['reversed'],int(value/.05))]+=1
 ordered=sorted(ns);pordered=sorted(ps)
 rec=dict(plan,min_ns=min(ns),median_ns=statistics.median(ns),p90_ns=ordered[int(.9*(len(ordered)-1))],max_ns=max(ns),min_batch_ns=float(Fraction(min(ps),1000)),endpoint_migrations=migrations)
 assert rec==ss
 rec.update(median_units=sorted(units)[64],median_ps=pordered[64],min_ps=min(ps),sum_ps=sum(ps));stats.append(rec);rowsn+=len(rows);shortprocess+=min(ps)<10000000000;shortprocesssum+=sum(ps)<10000000000;timer_total_ps+=sum(ps);minps=min(minps,min(ps)) if minps is not None else min(ps);maxps=max(maxps,max(ps))
groups=defaultdict(list)
for s in stats:groups[(s['phase'],s['width'],s['reversed'])].append(s)
effects={}
for cell,group in groups.items():
 assert len(group)==24;output=[]
 for block in range(6):
  pair=[r for r in group if r['block']==block];assert ''.join(r['label'] for r in pair)=='ABBA'
  a=sum(r['median_units'] for r in pair if r['label']=='A');b=sum(r['median_units'] for r in pair if r['label']=='B');output.append(Fraction(100*(b-a),a))
 effects[cell]=output
for s in summary:
 key=(s['phase'],s['width'],s['reversed']);group=groups[key]
 for name in ['min_ns','median_ns']:
  eff=[]
  for block in range(6):
   pair=[r for r in group if r['block']==block];a=statistics.mean(r[name] for r in pair if r['label']=='A');b=statistics.mean(r[name] for r in pair if r['label']=='B');eff.append(100*(b/a-1))
  assert eff==[x['percent'] for x in s[name]['block_effects']]
  assert statistics.median(eff)==s[name]['median_effect_pct'] and min(eff)==s[name]['effect_min_pct'] and max(eff)==s[name]['effect_max_pct']
  assert s[name]['A']==statistics.median(r[name] for r in group if r['label']=='A') and s[name]['B']==statistics.median(r[name] for r in group if r['label']=='B')
 assert s['min_batch_ns']==min(x['min_batch_ns'] for x in group) and s['endpoint_migrations']==sum(x['endpoint_migrations'] for x in group)
 assert max(abs(float(a)-b['percent']) for a,b in zip(effects[key],s['median_ns']['block_effects']))<1e-6
assert len(summary)==40
actualhist=Counter()
for x in csv.DictReader((D/'histogram.csv').read_text().splitlines()):actualhist[(x['phase'],x['variant'],int(x['width']),int(x['reversed']),round(float(x['bin_lower_ns'])/.05))]+=int(x['samples'])
assert hist==actualhist and sum(hist.values())==rowsn==123840
AA=[];comparison=[]
for w,r in cells:
 aa=effects[('aa',w,r)];comp=effects[('compare',w,r)];ok=all(abs(x)<=1 for x in aa);minimum=min(x['min_ps'] for x in groups[('aa',w,r)])
 AA.append(dict(width=w,reversed=r,block_effects_pct=[float(x) for x in aa],max_abs_pct=float(max(abs(x) for x in aa)),relative_qualified=ok,min_window_ns=minimum/1000,minimum10ms_qualified=minimum>=10000000000,joint_qualified=ok and minimum>=10000000000))
 comparison.append(dict(width=w,reversed=r,block_effects_pct=[float(x) for x in comp],median_pct=float(statistics.median(comp)),min_pct=float(min(comp)),max_pct=float(max(comp)),aa_relative_qualified=ok,all_windows10ms=False,interpretation='conditional focused diagnostic; no acceptance'))
owner=load(E.parent/'004-discovery-owner.json');assert owner['returncode']==0 and owner['driver_reaped'] and owner['owned_group_empty'] and owner['exclusive_release_safe'];assert owner['started_utc']<=M['started_utc']<M['finished_utc']<=owner['ended_utc']<'2026-10-19T07:15:00+00:00'
for x in owner['logs'].values():assert sha(R/x['path'])==x['sha256']
assert M['elapsed_seconds']<300 and owner['wall_seconds']<360
patterns=[rb'/' + rb'Users/[^\s\"\']+',rb'/(?:private/)?var/folders/[^\s\"\']+',rb'(?i)(?:BEGIN [A-Z ]*PRIVATE KEY|Authorization' + rb': Bearer|github' + rb'_pat_|ghp_[A-Za-z0-9]{20,})']
allfiles=sorted(x for x in D.rglob('*') if x.is_file());sourcehashes={}
for x in allfiles:
 data=x.read_bytes();assert not any(re.search(p,data) for p in patterns),str(x.relative_to(D));sourcehashes[str(x.relative_to(D))]=hashlib.sha256(data).hexdigest()
DEST=E/'discovery';assert not DEST.exists(),'no overwrite';shutil.copytree(D,DEST)
assert sourcehashes=={str(x.relative_to(DEST)):sha(x) for x in DEST.rglob('*') if x.is_file()}
(E/'DISCOVERY-SHA256.json').write_text(json.dumps(sourcehashes,indent=2)+'\n')
report=dict(status='PASS raw arithmetic/artifact audit; measurement precision unqualified',participant='/root/followup_proposal_c',backend='Inherited Codex/GPT-6 family; exact model/token/currency cost unknown',independence='Did not prepare EXP004; independently audited root-run discovery without importing runner/analyser calculations',schedule_processes=960,rows=rowsn,raw_hashes=1920,fixture_contracts_independently_reconstructed=len(fixtures),all_schedule_commands_seeds_rotation_ABBA_exact=True,serial_UTC=True,semantic_checksum_fingerprint_geometry_owned_bytes=True,source_files_and_native_binaries_match=True,canonical_summary_histogram_reconstructed=True,rational_effect_method='Per-process median of 129 printed ns_per_decode values represented as integer billionths of ns/decode; exact rational paired sums independently agree with canonical float effects within 1e-6 percentage points. Printed elapsed_ns separately validates elapsed/operations consistency and 10ms windows.',aa_relative_qualified=sum(x['relative_qualified'] for x in AA),aa_full_window_qualified=sum(x['joint_qualified'] for x in AA),aa_cells=AA,comparisons=comparison,windows=dict(min_ns=minps/1000,max_ns=maxps/1000,short_below10ms_rows=shortrows,processes_with_any_short_window=shortprocess,processes_sum_timed_below10ms=shortprocesssum,row_windows=rowsn,processes=960),operation_timer_sum_seconds=timer_total_ps/1e12,campaign_wall_seconds=M['elapsed_seconds'],owner_reaped_release_safe=True,owner_sha256=sha(E.parent/'004-discovery-owner.json'),copy=dict(files=len(allfiles),all_byte_identical=True,privacy_hits=0,hash_manifest_sha256=sha(E/'DISCOVERY-SHA256.json')),source_root_adapter='Legacy adapter identity; no corrected-adapter or M1 timing pooling',no_acceptance=True,no_measurement_build_profile_rerun=True,preparation_error='Initial functions.exec call to write this script had a JavaScript parenthesis SyntaxError; it executed no shell command and changed no files.')
(E/'INDEPENDENT-AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
lines=['# EXP-004 M6 independent audit','',f"PASS on evidence/arithmetic: 960 exact scheduled processes, 123840 rows, 1920 raw hashes and {len(fixtures)} independently reconstructed finite-score fixture/checksum contracts. All six ABBA blocks, seeds81031/81041, deterministic rotations and commands match. UTC intervals are serial; all return zero. Source/referee/binary identities and owner logs match; owner records driver reaping, empty owned group and safe release.",'',f"Relative A/A qualifies {report['aa_relative_qualified']}/20 cells under every-block ±1%. Adding minimum10ms individual windows leaves {report['aa_full_window_qualified']}/20 qualified. All {shortrows} timed rows are shorter than10ms; all960 processes contain a short row. Windows span {minps/1000:.3f}–{maxps/1000:.3f}ns. {shortprocesssum}/960 processes also sum to less than10ms of timed work; summing rows does not create longer original timer windows.",'','Effects below are descriptive candidate/control elapsed-time changes, negative lower. All remain conditional focused decoder observations. Exact rational arithmetic over printed ns/decode agrees with canonical summaries; elapsed/operations consistency is checked separately. No iterator guard is cleared or source accepted.','', '| Width | Reverse | Median effect % | Six-block range % | Relative A/A |','|---:|---:|---:|---:|---|']
for c in comparison:lines.append(f"| {c['width']} | {c['reversed']} | {c['median_pct']:+.6f} | {c['min_pct']:+.6f}..{c['max_pct']:+.6f} | {'PASS' if c['aa_relative_qualified'] else 'FAIL'} |")
lines+=['',f"All {len(allfiles)} completed discovery files were scanned before copying for private home/temp paths and credential markers; no hits. Every copied file, including raw rows, is byte-identical and pinned by DISCOVERY-SHA256.json. Canonical analysis ran once with a180-second bound; command/log hashes are retained. No matrix/build/profile reran. Timing sums are descriptive budget fields, not hardware cycles or cross-host evidence.",'','Participant /root/followup_proposal_c; inherited Codex/GPT-6 family; exact model/usage/cost unknown. I did not prepare EXP004. M6 rows remain separate from M1 and corrected-adapter results. One initial orchestration syntax error executed no shell command or edits; a subsequent audit-only assertion also failed because it compared differently rounded CSV fields; its original script hash/error are preserved privately. Exact arithmetic was corrected to use the canonical ns/decode field, without changing input data. No acceptance follows.']
(E/'INDEPENDENT-AUDIT.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(dict(relative_AA=report['aa_relative_qualified'],qualified=report['aa_full_window_qualified'],shortrows=shortrows,shortprocess=shortprocess,processsum_short=shortprocesssum,min_ns=minps/1000,max_ns=maxps/1000,files=len(allfiles),headline=[c for c in comparison if c['width']==60]),indent=2))
