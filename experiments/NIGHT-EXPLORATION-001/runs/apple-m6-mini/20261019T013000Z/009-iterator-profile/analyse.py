#!/usr/bin/env python3
from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,re,csv
OUT=Path(__file__).resolve().parent;ROOT=Path.cwd();SCR=Path('scratch/m6-iterator-profile')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
summary=json.loads((OUT/'summary.json').read_text());freeze=json.loads((OUT/'freeze.json').read_text());origins=json.loads((OUT/'ORIGINS.json').read_text())
for f,h in freeze['files_sha256'].items():assert sha(f)==h,f
for f,h in origins['files_sha256'].items():assert sha(OUT/f)==h,f
assert summary['total_captures']==16 and len(summary['captures'])==16
lines=(OUT/'zbtreeIteratorNext.asm').read_text().splitlines();inst={};start=None
for line in lines:
 m=re.match(r'^([0-9a-f]{16})\s+(.*)',line)
 if m:
  address=int(m.group(1),16)
  if start is None:start=address
  inst[address-start]=m.group(2)
regions=[(0,28,'stack prologue/register saves',4021),(28,48,'iterator entry and nullable-member test',4021),(48,80,'packed member-offset-array base calculation',356),(80,108,'member physical-position orientation',369),(108,132,'member offset/record-header dependent reads',613),(132,320,'packed member decoding and assertion cold paths',586),(320,332,'member pointer/length output stores',4031),(332,348,'nullable score/encoding tests',4035),(348,380,'score physical position and word address',499),(380,384,'packed score-word load',504),(384,432,'packed score alignment/cross-word reconstruction',499),(432,468,'packed score mask and scale',499),(468,496,'score base and ordered-double reconstruction',499),(496,500,'score output store',4035),(500,592,'iterator advance/direction/leaf transition',4037),(592,620,'stack epilogue/register restores/return',4059)]
mapping={}
for offset,text in inst.items():
 matches=[r for r in regions if r[0]<=offset<r[1]];assert len(matches)==1
 r=matches[0];mapping[offset]=dict(offset_bytes=offset,linked_address=hex(start+offset),instruction=text,semantic_region=r[2],source='src/zset_btree.c',source_reference_line=r[3],source_attribution='manual inspection, not DWARF; optimized instruction location is not its isolated cost')
aggregates={};rows=[];captured_offsets=Counter()
for c in summary['captures']:
 raw=SCR/Path(c['raw']['stderr']['path']).name;assert sha(raw)==c['raw']['stderr']['sha256']
 pcs=[s.split(',') for s in raw.read_text().splitlines() if s.startswith('PC,')];assert len(pcs)==c['samples']
 assert sum(b['count'] for b in c['pc_bins'])==c['samples']
 counts=Counter()
 for b in c['pc_bins']:
  if b['symbol']=='zbtreeIteratorNext':
   assert b['offset_bytes'] in mapping
   counts[mapping[b['offset_bytes']]['semantic_region']]+=b['count'];captured_offsets[b['offset_bytes']]+=b['count']
  else:counts['outside iterator: '+b['symbol']]+=b['count']
 c['semantic_region_pcs']=dict(counts)
 key=str(c['size'])+'-'+c['contract'];agg=aggregates.setdefault(key,dict(size=c['size'],contract=c['contract'],seeds=[],samples=0,iterator_pcs=0,regions=Counter(),iterator_offsets=Counter()))
 agg['seeds'].append(c['seed']);agg['samples']+=c['samples'];agg['iterator_pcs']+=c['symbols'].get('zbtreeIteratorNext',0);agg['regions'].update(counts)
 for b in c['pc_bins']:
  if b['symbol']=='zbtreeIteratorNext':agg['iterator_offsets'][b['offset_bytes']]+=b['count']
 rows.append(dict(size=c['size'],contract=c['contract'],seed=c['seed'],samples=c['samples'],iterator_pcs=c['symbols'].get('zbtreeIteratorNext',0),sufficient=c['sufficient']))
for agg in aggregates.values():
 agg['regions']=dict(agg['regions']);agg['top_iterator_offsets']=[dict(count=n,**mapping[o]) for o,n in agg.pop('iterator_offsets').most_common(8)]
map_data=dict(binary_sha256=freeze['binaries_sha256']['iterator-profile'],symbol='zbtreeIteratorNext',linked_symbol_start=hex(start),instruction_count=len(inst),exact_instruction_map=list(mapping.values()),captured_iterator_offset_counts=dict(captured_offsets),manual_regions=regions,dwarf_line_attribution_available=False,counts_are_not_instruction_cost=True)
(OUT/'pc-map.json').write_text(json.dumps(map_data,indent=2)+'\n');(OUT/'region-summary.json').write_text(json.dumps(dict(captures=summary['captures'],same_contract_two_seed_aggregates=list(aggregates.values()),no_speed_interpretation=True),indent=2)+'\n')
with (OUT/'capture-summary.csv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
result=['# M6 baseline iterator profile — 16/16 captures sufficient','', 'No optimization is selected. These are standalone baseline PC observations, not a candidate comparison. The exact Intel iterator referee and microbench source were copied from `'+origins['intel_commit']+'`; original PLAN.md/MATCHED-PROFILE.md remain clearly Intel evidence. The new M6 schedule is LOCAL-PLAN.json. No Intel/M6 timings or samples are pooled.','', 'Baseline source/header match the frozen Intel source exactly (d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83). Neither target nor referee semantics changed. Only a new Apple profiler bridge implements the existing PROFILE_SAMPLE hooks using the unchanged 002 public self-process sampler.','', 'Four contracts pass native and ASan/UBSan at size 1000 / requested 2003 / seed 1 (8 runs; each rounds to 3000 items). Member bytes 16; full-output mask 7 consumes pointer/length/score, score-only mask 4 requests score only. Exact member bytes/order, finite-score bits, iterator-copy next state, nullable outputs, exhausted state, checksum/count and owned memory checks are retained.','', 'Exactly 16 serial release captures ran: 100K/1M × four contracts × seeds 1/2, 100 million items each, three actual-contract warmup traversals. All 16 capture counts meet the fixed 25-PC minimum (43–83); no capture was retried. Sampler requested 1000 us ITIMER_PROF; delivered counts do not establish timer precision, hardware events or unbiased time shares.','', '|Members|Contract|Seed 1 PCs|Seed 2 PCs|IteratorNext PCs / all scoped PCs (two seeds)|','|---|---|---:|---:|---:|']
for agg in aggregates.values():
 cs=[x for x in summary['captures'] if x['size']==agg['size'] and x['contract']==agg['contract']];result.append(f"|{agg['size']}|{agg['contract']}|{cs[0]['samples']}|{cs[1]['samples']}|{agg['iterator_pcs']} / {agg['samples']}|")
result+=['', 'Across all 16 captures, 1054 PCs were recorded: 1031 in zbtreeIteratorNext, 11 in the traversal consumer and 12 in __thread_selfusage. These totals describe this fixed matrix only. Per-capture bins and per-contract two-seed views are retained; unlike-contract populations must not be interpreted as one universal workload.','', 'The iterator body has 155 instruction lines. Its full-output path still computes the packed-offset-array base using count×score width, maps orientation, loads a 16-bit record offset and reads the packed-record prefix. Score-only calls bypass the member-offset/prefix path. The score decoder and iterator advance remain separate observed instruction regions. Exact instruction offsets and manual source-region classifications are in pc-map.json. Reverse names traversal direction; these profiles do not establish the physical reversed-leaf population.','', 'The entry saves six register pairs in a 96-byte frame (+0x0..+0x18); the epilogue restores them (+0x250..+0x268). These exact stack regions contain 151 and 152 PCs respectively across the fixed matrix, with no cycle-cost interpretation. The frozen compat/server.h declares standalone_panic without a non-returning contract, while compat/standalone.c unconditionally aborts. The iterator body calls only that panic on its cold paths. This is a possible baseline adapter/compiler-contract artifact contributing to frame generation; it is not a cache diagnosis. Root has independent review of this possibility pending. These profiles remain valid for the exact frozen baseline; no adapter/target/referee change, rebuild or recapture was made.', '', 'Selected per-contract instruction observations (two seeds combined, counts only):','']
for agg in aggregates.values():
 top=agg['top_iterator_offsets'][:3];desc='; '.join(f"+0x{x['offset_bytes']:x}: {x['count']} PCs, `{x['instruction']}`" for x in top);result.append(f"- {agg['size']} / {agg['contract']}: {desc}.")
result+=['', 'The M6 PCs are distributed among entry/frame, score-mask/output, member materialization and advance regions. The dominant Intel packed-prefix comparison observation should not be assigned to M6 from geometry or symbol overlap. Seeing the repeated offset-base arithmetic in M6 assembly establishes that the proposed Intel cache would change real work here; it does not show that this work dominates or that the exact patch will improve M6. A replication decision, three-implementation selection, correctness guards, qualification, serial comparison, fresh confirmation and review remain separate future steps.','', 'Sampling starts/ends at the original referee hooks. They bracket QoS/CPU/thread-clock observations surrounding the traversal as well as the traversal itself; fixture construction, full verification and warmup are excluded. The 12 thread-selfusage PCs make this boundary visible. Raw command UTC bounds cover the process, not individual PCs. No frequency/DVFS/core-residency/cache/branch/cycle or isolated instruction-cost inference is made. Emitted elapsed fields are unused.','', 'Existing 002 known-work controls were inspected and pinned without rerunning them. Freeze.json was written after correctness and before all captures; it pins exact sources, sampler/bridge, flags/compiler and binaries. Raw profiles remain ignored scratch with SHA256/command/time bounds in public per-capture JSON and commands.jsonl.','', 'Limitations and retained failures: initial new bridge compilation omitted string.h; fixed only that bridge, preserving its failed log and reusing successful native/sanitizer binaries. No capture had started. Post-link dsymutil exited 0 but warned compiler temporary objects were gone; no DWARF lines were recovered. Public warnings use generic temporary paths; raw warnings/hash remain scratch. Exact PC offsets map to release assembly, with manually inspected source references, not exact DWARF source attribution. No rebuild or recapture was made to repair symbolization.','', 'All experimental processes finished. Participant /root/followup_proposal_b, inherited Codex/GPT-6 family; exact serving model/token usage/cost unknown. No source optimization, Git write, shared-memory edit or new agent was performed.']
# Count from inspected instruction text, not a hardcoded estimate.
result=[s.replace('has 155 instruction lines','has '+str(len(inst))+' instruction lines') for s in result]
(OUT/'RESULTS.md').write_text('\n'.join(result)+'\n')
assert sum(x['samples'] for x in summary['captures'])==1054
print('Mapped',sum(captured_offsets.values()),'IteratorNext PCs to',len(captured_offsets),'exact instruction offsets;',len(inst),'instructions')
