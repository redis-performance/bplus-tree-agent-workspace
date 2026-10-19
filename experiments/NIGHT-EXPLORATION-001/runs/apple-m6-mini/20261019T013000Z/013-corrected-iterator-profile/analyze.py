#!/usr/bin/env python3
"""Read retained 013 evidence; write only analytical artifacts. No child processes."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, hashlib, io, json, re

OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if (p/'AGENTS.md').exists())
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(name): return json.loads((OUT/name).read_text())
def save(name,obj): (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')

# Explicit manual classification, independent of the sampled counts. Inclusive byte offsets.
REGIONS=[
 ('entry_current_and_output_selection', [(0x000,0x010)],4024,'entry'),
 ('member_offset_table_base',[(0x014,0x030)],344,'member'),
 ('member_physical_position_and_record_address',[(0x034,0x058)],369,'member'),
 ('member_inline_prefix_and_length_decode',[(0x05c,0x070),(0x07c,0x08c)],589,'member'),
 ('empty_end_return',[(0x074,0x078)],4025,'end'),
 ('member_and_length_output',[(0x090,0x098)],4033,'output'),
 ('score_selection_width_and_orientation',[(0x09c,0x0bc)],4036,'score'),
 ('score_bit_position_word_load_and_extraction',[(0x0c0,0x0fc)],501,'score'),
 ('score_mask_and_shift',[(0x100,0x120)],509,'score'),
 ('score_base_and_ordered_to_double',[(0x124,0x13c)],513,'score'),
 ('score_output',[(0x140,0x140)],4036,'output'),
 ('iterator_direction_position_and_leaf_advance',[(0x144,0x188)],4038,'advance'),
 ('successful_return',[(0x18c,0x190)],4059,'return'),
 ('external_member_pointer_and_length',[(0x194,0x1a4)],573,'member'),
 ('cold_null_external_pointer_panic_frame_and_call',[(0x1a8,0x1c4)],599,'cold_panic'),
]
byoff={}
for name,ranges,line,coarse in REGIONS:
 for lo,hi in ranges:
  for offset in range(lo,hi+1,4):
   assert offset not in byoff
   byoff[offset]=(name,line,coarse)
asm=(OUT/'zbtreeIteratorNext.asm').read_text()
ins=[]
for line in asm.splitlines():
 m=re.match(r'^([0-9a-fA-F]{16})\s+(.+)$',line)
 if m: ins.append((int(m.group(1),16),m.group(2)))
assert len(ins)==114
start=ins[0][0]
assert [a-start for a,_ in ins]==list(range(0,456,4))==sorted(byoff)
# The only stack pointer/frame setup and call in this symbol are the cold panic block.
stack_offsets=[a-start for a,s in ins if re.search(r'\bsp\b',s) or s.startswith('mov\tx29, sp')]
call_offsets=[a-start for a,s in ins if s.startswith('bl\t')]
assert stack_offsets==[0x1a8,0x1ac] and call_offsets==[0x1c4]
summary=read('summary.json');status=read('capture-status.json');freeze=read('freeze.json');plan=read('PLAN.json')
planned=read('planned-commands.json')['commands']
commands=[json.loads(line) for line in (OUT/'commands.jsonl').read_text().splitlines()]
assert summary['status']==status['status']=='complete'
assert summary['captures']==status['captures'] and len(summary['captures'])==16
assert status['all_children_reaped'] and len(commands)==30
assert all(x['process_reaped'] and not x['timed_out'] and x['returncode']==0 for x in commands)
assert len(planned)==len(plan['captures'])==16
captures=summary['captures'];capture_commands=commands[-16:]
verified_files={};verified_binaries={}
for section,dest in [('files_sha256',verified_files),('binaries_sha256',verified_binaries)]:
 for path,h in freeze[section].items():
  assert sha(ROOT/path)==h,path
  dest[path]=h
for name in ('iterator.c','microbench.c','apple-sampler-bridge.c'):
 assert (OUT/name).read_bytes()==(OUT.parent/'009-iterator-profile'/name).read_bytes()
assert sha(OUT/'AUTHORIZATION.json')==summary['ack_sha256']
ack=read('AUTHORIZATION.json')
for k,name in [('driver_sha256','run.py'),('plan_sha256','PLAN.json'),('freeze_sha256','freeze.json')]:assert ack[k]==sha(OUT/name)
assert ack['exclusive_runner'] and ack['other_work_idle'] and ack['status']=='authorized'
raw_hashes={};public_hashes={};capture_rows=[];offset_total=Counter();symbol_total=Counter();region_total=Counter();broad_total=Counter()
previous_end=None
for i,(cell,c,job,record) in enumerate(zip(plan['captures'],captures,planned,capture_commands)):
 assert c['size']==cell['size'] and c['seed']==cell['seed'] and c['contract']==cell['contract']
 expected_name=f"n{c['size']}-{c['contract']}-s{c['seed']}"
 assert job['name']==record['name']==expected_name and job['command']==record['command']
 assert record['environment_override']==job['environment']=={'PROFILE_USEC':'1000'}
 assert record['timeout_seconds']<=job['child_seconds_max']==120
 assert c['raw']==record['logs'] and c==read('profiles/'+expected_name+'.json')
 assert c['started_utc']==record['started_utc'] and c['finished_utc']==record['finished_utc']
 if previous_end is not None: assert previous_end<=c['started_utc']
 previous_end=c['finished_utc']
 assert c['checksum']==c['expected_checksum'] and c['operations']==cell['requested_items']==100000000
 assert c['sufficient'] and c['samples']>=c['minimum_samples']==plan['minimum_pcs']==25
 assert c['requested_interval_us']==plan['requested_sample_interval_us']==1000
 for stream,log in record['logs'].items():
  assert sha(OUT/log['file'])==log['sha256']
  public_hashes[log['file']]=log['sha256']
  relative=log['original_raw'].removeprefix('ignored ')
  assert sha(ROOT/relative)==log['original_raw_sha256']
  raw_hashes[relative]=log['original_raw_sha256']
 err=(ROOT/record['logs']['stderr']['original_raw'].removeprefix('ignored ')).read_text()
 rawpcs=[line.split(',') for line in err.splitlines() if line.startswith('PC,')]
 headers=[line.split(',') for line in err.splitlines() if line.startswith('PROFILE,')]
 assert len(headers)==1 and headers[0][1:]==['iterator-existing-profile-hooks','1000',str(len(rawpcs)),'0']
 # Reconstruct from private raw rows, retain only symbol-relative bins in the public output.
 rbins=Counter();rsymbols=Counter()
 for pc in rawpcs:
  assert len(pc)==6
  _,module,address,base,symbol,symbol_start=pc
  address=int(address,16);symbol_start=int(symbol_start,16)
  off=address-symbol_start if symbol_start and address>=symbol_start else None
  rbins[(Path(module).name,symbol,off)]+=1;rsymbols[symbol]+=1
 expected_bins=Counter({(x['module'],x['symbol'],x['offset_bytes']):x['count'] for x in c['pc_bins']})
 assert rbins==expected_bins and rsymbols==Counter(c['symbols'])
 assert len(rawpcs)==sum(rbins.values())==sum(rsymbols.values())==c['samples']
 rawout=(ROOT/record['logs']['stdout']['original_raw'].removeprefix('ignored ')).read_text()
 output_rows=list(csv.DictReader(io.StringIO(rawout)))
 assert len(output_rows)==1
 r=output_rows[0]
 for key,value in [('size',c['size']),('seed',c['seed']),('operations',100000000),('requested_ops',100000000),('member_bytes',16),('warmup_passes',3),('mask',c['mask']),('tree_bytes',c['tree_bytes'])]:assert int(r[key])==value
 for key in ('checksum','expected_checksum','construction_fingerprint','encoding','direction'): assert r[key]==str(c[key])
 fine=Counter({name:0 for name,_,_,_ in REGIONS});broad=Counter({key:0 for key in ('entry','member','score','output','advance','return','end','cold_panic','other_symbol')})
 others=Counter()
 for (module,symbol,off),count in rbins.items():
  if symbol=='zbtreeIteratorNext':
   assert module=='iterator-profile' and off in byoff
   name,_,group=byoff[off];fine[name]+=count;broad[group]+=count;offset_total[off]+=count
  else: others[symbol]+=count;broad['other_symbol']+=count
 assert sum(fine.values())==c['symbols'].get('zbtreeIteratorNext',0)
 assert sum(broad.values())==c['samples']
 assert fine['cold_null_external_pointer_panic_frame_and_call']==0
 if c['mask']==4:
  assert broad['member']==0 and fine['member_and_length_output']==0
 row={k:c[k] for k in ('size','contract','seed','mask','direction','encoding','operations','samples','tree_bytes','construction_fingerprint')}
 row.update(iterator_samples=sum(fine.values()),other_symbols=dict(others),fine_regions=dict(fine),broad_regions=dict(broad))
 capture_rows.append(row);symbol_total.update(rsymbols);region_total.update(fine);broad_total.update(broad)
# Verify all 30 command records' retained public/private logs, not just the capture subset.
for record in commands:
 for stream,log in record['logs'].items():
  assert sha(OUT/log['file'])==log['sha256']
  relative=log['original_raw'].removeprefix('ignored ')
  assert sha(ROOT/relative)==log['original_raw_sha256']
  public_hashes[log['file']]=log['sha256'];raw_hashes[relative]=log['original_raw_sha256']
prior_map=json.loads((OUT.parent/'009-iterator-profile/pc-map.json').read_text())
assert prior_map['instruction_count']==155
map_entries=[]
for address,instruction in ins:
 off=address-start;name,line,group=byoff[off]
 map_entries.append(dict(offset_bytes=off,offset_hex=f'+0x{off:03x}',linked_address=f'0x{address:x}',instruction=instruction,semantic_region=name,broad_region=group,source='src/zset_btree.c',source_reference_line=line,source_attribution='Manual semantic reference, not DWARF; optimized instruction location is not isolated cost.',captured_pcs=offset_total[off]))
manual_regions=[dict(id=name,ranges=[dict(first_offset_bytes=lo,last_offset_bytes=hi) for lo,hi in ranges],source_reference_line=line,broad_region=group,instruction_count=sum((hi-lo)//4+1 for lo,hi in ranges)) for name,ranges,line,group in REGIONS]
save('pc-map.json',dict(binary_sha256=freeze['binaries_sha256']['scratch/m6-corrected-iterator-profile/iterator-profile'],assembly_sha256=sha(OUT/'zbtreeIteratorNext.asm'),source_sha256=plan['source_sha256'],symbol='zbtreeIteratorNext',linked_symbol_start=f'0x{start:x}',instruction_count=114,exact_instruction_map=map_entries,manual_regions=manual_regions,normal_path_stack_frame_instructions=0,cold_panic_stack_frame_bytes=16,stack_or_frame_setup_offsets=stack_offsets,call_offsets=call_offsets,dwarf_line_attribution_available=False,counts_are_not_instruction_cost=True))
metadata=dict(status='PASS descriptive baseline inventory',participant='/root/followup_proposal_a',backend='Inherited GPT-6/Codex family; exact serving identifier/token/currency cost unknown',frozen_source_sha256=plan['source_sha256'],freeze_sha256=sha(OUT/'freeze.json'),capture_summary_sha256=sha(OUT/'summary.json'),capture_count=16,minimum_required_pcs=25,observed_pcs_min=min(x['samples'] for x in captures),observed_pcs_max=max(x['samples'] for x in captures),sample_scope=plan['sampling_scope'],counts_not_costs=True,no_old_adapter_count_pooling=True,aggregate_note='Totals below are bookkeeping across this fixed matrix of different contracts; they are not workload shares or cross-adapter effects.')
save('region-summary.json',dict(**metadata,manual_regions=manual_regions,captures=capture_rows,bookkeeping_totals=dict(samples=sum(x['samples'] for x in captures),symbols=dict(symbol_total),fine_regions=dict(region_total),broad_regions=dict(broad_total))))
fields=['size','contract','seed','mask','direction','encoding','samples','iterator_samples']+[name for name,_,_,_ in REGIONS]+['other_traverse','other___thread_selfusage','other_unclassified']
with (OUT/'region-summary.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for row in capture_rows:
  d={k:row[k] for k in fields if k in row};d.update(row['fine_regions']);other=row['other_symbols']
  d.update(other_traverse=other.get('traverse',0),other___thread_selfusage=other.get('__thread_selfusage',0),other_unclassified=sum(v for k,v in other.items() if k not in ('traverse','__thread_selfusage')));w.writerow(d)
# Analysis audit is a retained-evidence check only. It launches no executable and reads no elapsed_ns fields.
save('ANALYSIS-AUDIT.json',dict(status='PASS',participant=metadata['participant'],backend=metadata['backend'],analysis_command='python3 '+str(OUT.relative_to(ROOT)/'analyze.py'),new_builds_captures_timings_or_tests=0,frozen_inputs_verified=len(verified_files),frozen_binaries_verified=len(verified_binaries),frozen_inputs_sha256=verified_files,binaries_sha256=verified_binaries,commands_verified=30,preparation_commands=14,capture_commands=16,all_commands_zero_exit_reaped_without_timeout=True,capture_commands_exact_plan_and_environment=True,capture_intervals_serial=True,capture_operations_and_checksums_match=True,capture_public_private_log_pairs_verified=32,all_public_private_log_pairs_verified=len(public_hashes),raw_pc_bins_reconstructed_and_equal=True,pc_bins_reconcile_all16=True,pc_map_instructions=114,all_iterator_offsets_aligned_mapped=True,cold_panic_pcs=0,score_only_member_decode_and_output_pcs=0,sampling_overflow_count=0,source_referee_009_bytecopies=True,ack_sha256=summary['ack_sha256'],exclusive_ack_verified=True,capture_phase_wall_seconds=status['wall_seconds'],wall_seconds_purpose='Process-budget bookkeeping only; frontend elapsed_ns/thread_elapsed_ns fields unused.',capture_completed_before_global_stop=status['finished_utc']<=plan['budgets']['absolute_capture_stop_utc'],raw_private_logs_sha256=raw_hashes,public_logs_sha256=public_hashes,no_optimization_selected=True))
print(json.dumps(dict(captures=16,samples=sum(x['samples'] for x in captures),symbols=dict(symbol_total),broad_totals=dict(broad_total),offsets=dict(sorted(offset_total.items())),rows=[dict(size=r['size'],contract=r['contract'],seed=r['seed'],samples=r['samples'],next=r['iterator_samples'],**r['broad_regions']) for r in capture_rows]),indent=2))

lines=['# Corrected-adapter iterator profile: descriptive baseline complete','',
'All 16 fixed captures meet the preregistered 25-PC minimum (35–75 PCs each). Source adoption remains **NONE**; no tree hypothesis is selected by this report. The corrected iterator has 114 static instructions and no normal-path stack frame. The remaining 16-byte frame belongs solely to the failing external-pointer assertion path; that cold region has zero captured PCs.','',
'The baseline target remains `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`, with the corrected `_Noreturn` standalone adapter and unchanged decoder, scanner, layout, hash, allocator and assertions. The exact preparation freeze is `f5981f8a001f33ebc1ce06a3394d797afe21bfcabb98fec48ad28ea4c0cf3313`; profile binary SHA-256 is `e8b58ec2a89742221c00772c42493db2269fbd263c692a8db1474adb61066624`. Flags and all input identities are in [freeze.json](freeze.json).','',
'The root authorized an exclusive runner against that exact freeze. Captures ran serially from 04:29:21.425709 to 04:29:29.623856 UTC; the driver records 8.198410291 seconds of phase wall time solely for budget accounting. All 30 preparation/capture child records show zero exit, no timeout and reaped processes. No new child was launched for this analysis. All frontend elapsed/thread-time fields remain unused.','',
'## Retained evidence and checks','',
'The fixed matrix is 100K/1M members × integer full forward, integer full reverse, integer score-only forward, fractional full forward × seeds 1/2. Each capture visits exactly 100,000,000 items, after three full warmup traversals, with 16-byte binary members and the fixed requested 1000 µs sampler interval. No capture was repeated or retuned. Integer scores are `i - n/2`; fractional scores add `0.25`. Random insertion permutations and hash seeds are fixed by the published seed and construction fingerprint.','',
'The retained capture outputs pass exact counts/checksums, tree length and owned-memory invariants, full member/order/score-bit verification, copied iterator next-state checks, nullable-output sentinels and repeated end checks from the unchanged frontend. Preparation retains eight bounded native/ASan/UBSan checks (four contracts each), plus explicitly reused original 43-test evidence under matching corrected-baseline identities; these tests were not rerun during analysis.','',
'Analysis independently reconstructed every public PC bin from the private raw PC rows, verified all 60 public/private command-log stream pairs, matched all 16 commands and environment overrides to the frozen plan, and rehashed all 18 frozen inputs and three binaries. Every iterator PC is aligned to one of the 114 mapped instructions; all symbol counts and per-capture totals reconcile. Historical known-work sampler controls remain historical reused controls, not fresh corrected-adapter calibrations. See [ANALYSIS-AUDIT.json](ANALYSIS-AUDIT.json), [capture-status.json](capture-status.json) and [validation.json](validation.json).','',
'## Observed regions','',
'The table preserves each size, contract and seed. Entries are sampled-PC counts, not executed-instruction counts, costs, unbiased time shares or percentages. Member includes offset-table base, physical mapping/record address and packed prefix decoding. Score includes optional-output selection, width/orientation, packed word/extraction, mask/shift and ordered-score reconstruction. Output includes member pointer, length and score stores; advance includes direction, position and leaf transitions. Entry and return remain separate. Empty/end-return and cold panic are zero in every row.','',
'| Members | Contract | Seed | All PCs | Iterator PCs | Entry | Member | Score | Output | Advance | Return | Other symbols |',
'|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for r in capture_rows:
 b=r['broad_regions']
 lines.append('| '+ ' | '.join(map(str,[r['size'],r['contract'],r['seed'],r['samples'],r['iterator_samples'],b['entry'],b['member'],b['score'],b['output'],b['advance'],b['return'],b['other_symbol']]))+' |')
lines += ['',
'The fixed matrix contains 937 PCs: 734 attributed to `zbtreeIteratorNext`, 190 to its `traverse` consumer, and 13 to `__thread_selfusage` inside the retained sampling boundary. This is bookkeeping over different contracts, not a representative workload distribution. The exact fine-region table and all 16 rows are in [region-summary.json](region-summary.json) and [region-summary.csv](region-summary.csv).','',
'Full-output captures have member-region observations in every size/seed pair; all four score-only captures have zero member-region and member-output PCs, consistent with the optional-output branch in the assembly. Score, output and advance regions are observed in every capture. External-record decode and the cold panic frame have zero sampled PCs in this 16-byte inline-member matrix. Zero PCs do not prove a path never executed.','',
'Within this fixed matrix, the largest single instruction bin is `+0x100: mov x13, #-0x1` (159 PCs), followed by `+0x140: str x10, [x4]` (107). Other observed points include `+0x05c` packed prefix load (56), `+0x0cc` packed score-word load (49), `+0x034` reversed-flag load for member addressing (43), and `+0x188` iterator-position store (31). These locations identify where the sampler interrupted execution. They do not measure the latency of those instructions, establish predecessor stalls, demonstrate cache misses, or justify replacing the mask or output stores.','',
'## Exact assembly mechanism','',
'[pc-map.json](pc-map.json) maps every instruction, not just sampled offsets, to explicit nonoverlapping manual regions and source reference lines. References describe source semantics after optimization; DWARF line attribution is unavailable. Static linked addresses in the assembly/map are not private runtime pointers; published sample bins use symbol-relative offsets only.','',
'Current member work retains score-stream-size arithmetic to find the offset array, optional physical reversal, a 16-bit record-offset load, packed-record prefix decoding, then requested pointer/length stores. Score work retains the original physical-position/bit-position calculation, packed-word load and possible ninth-byte merge, mask/shift, base/orientation reconstruction, ordered-to-double transform and requested score store. Forward/reverse position and leaf transitions remain explicit. These are actual assembly dependencies, but this profile does not establish their critical-path latency or a profitable replacement.','',
'The original-adapter [009 map](../009-iterator-profile/pc-map.json) has 155 instructions, including a 96-byte normal frame with six register-pair saves and matching restores. In the corrected 114-instruction binary, normal entry begins directly with the iterator leaf load and normal returns have no register restores. Only `+0x1a8`/`+0x1ac` create a 16-byte cold panic frame, ending in the sole call at `+0x1c4` to the truthful always-aborting panic handler. The tree source is unchanged. This is a descriptive assembly comparison across adapter identities; no old/new PC populations are pooled or subtracted, and no speed effect is inferred from the 155→114 instruction difference.','',
'## Limits and grounds for later review','',
'The 25-PC floor is a screening sufficiency rule, not a precision guarantee. Each capture has only 35–75 samples; two seeds cannot remove sampling aliasing, interrupt skid, or scheduling effects. The requested 1000 µs interval is not proof of actual cadence. The sampler uses nearest-symbol attribution with explicit offsets, not hardware event counters or source-line cost attribution. The retained boundary includes traversal consumer work and QoS/CPU/thread-clock observations, reflected by the non-iterator samples. No cycles, cache behavior, branch-miss rate, frequency, actual core residency or migration history is established.','',
'This profile covers masks 7 and 4, ordinary integer/fraction scores and 16-byte inline members at 100K/1M. It does not supply all-output-mask, long/external-member, zero/small-size, empty/seek, copied-direction-change/invalidation, physically reversed-leaf, wide finite-score/score-width, signed-zero or portability performance guards. Semantic checks outside the sampling boundary remain useful correctness evidence without adding sampled coverage of those paths.','',
'The corrected baseline now has a trustworthy location inventory for future review: score decode/output, member-address/prefix work and iterator advance are still visible, while the old normal-frame mechanism is absent. This evidence alone does not establish that any extra cached state, early decode, decoder change or other added work would improve public lookup or iteration. A later chair must identify one new causal hypothesis, account for maintenance/state costs, retain full semantic guards, and obtain qualified same-session comparisons, candidate profiling, independent confirmation and adversarial review. This report proposes no tree candidate.','',
'Analysis participant: `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving identifier, token usage and currency cost are unknown. The analyst also prepared this frontend/freeze and earlier 007 geometry census; this is not an independent audit of its own harness authorship. Root runner/review and an independent artifact review remain distinct roles. No source/adapter/referee changes, build, capture, timing, Git write or new agent occurred during analysis.','',
'Reproduce the retained-evidence analysis from the repository root with:','',
'```sh',
'python3 '+str(OUT.relative_to(ROOT)/'analyze.py'),
'```','',
'The script reads retained evidence and emits only the PC map, region tables, analysis audit and this report. Public artifact hashes are sealed separately in `artifacts-sha256.json`; private raw logs remain scratch-only with preserved hashes.','']
(OUT/'RESULTS.md').write_text('\n'.join(lines))
