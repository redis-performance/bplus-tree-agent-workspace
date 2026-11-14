# Slot-zero positive-hint shadow census: design only

The source audit supports preparing this diagnostic. No candidate implementation
is selected. This directory currently contains a design and pinned inputs only;
there is no generated diagnostic, compilation, execution, counter result or speed
claim. The original source, lookup harness, prior census and all variants remain
unchanged. [The chair decision](../FIFTH-DECISION.md) admits preparation only.

The question is whether the exact seeding policy in [proposal C](../proposals-fifth/C.md)
provides useful positive physical-position hints in the original primary fixture,
and how often a folded 56-bit home filter would admit an additional lookup. A
zero useful primary count closes this lead as NONE. A positive count establishes
exposure only; it does not admit a candidate or predict a 2% gain.

## Frozen work and observation boundary

Pin upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, source SHA256
`16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, and original
lookup SHA256 `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`.
`DESIGN-INPUTS.json` pins the decision, selected policy and reusable census inputs.
Generated changes will be a separate instrumented copy and patch in this directory.
The source generator must fail closed on unexpected source text or hash.

Preserve the exact original seed 17, 500 members, six cases (hit, score, miss,
long, external, update), construction/reservation order, independent query/storage
buffers, query order and 1000-sweep warmup. Count one sweep for reads and two for
update, restoring integer scores. No additional seeds, collision fixtures, forced
resizes, searches to create hints, or altered insertion order are admitted.

Maintain shadow lifetime and hint state from the first allocation through setup
and warmup. Only counting state is reset after warmup. Resetting hints there would
silently change the policy and is prohibited. Enable counting immediately before
the fixed counted loop; disable it immediately afterward, then capture owned bytes
and resize state before validation or printing. Capture later validation memory
separately. The source and target trees have independent shadow allocations.

Required exact models are 500 read operations (500 hits except miss=0), score sum
125250 only for score, and 1000 update pairs/1000 hits/zero score sum. Before and
immediate-after owned bytes must both equal hit/score/miss=14272, long=146656,
external=217600, update=14432. These independent original-baseline endpoints are
pinned by the prior census's memory provenance, not learned from this diagnostic.
Exact final iteration, bytes/order, successful scores, negative output sentinels,
and final integer update scores retain the prior census's checks.

## Exact hint policy

The shadow represents one high-byte hint per bucket, for index slot zero only.
Zero means disabled; 1–96 represents physical position 0–95. Reserved codes are
unavailable, never positions. No ID bit is borrowed: original narrow and wide IDs,
including legal narrow IDs above 32767 and all tombstones, remain untouched.

Only `zbtIndexCopyLeaf` and `zbtIndexRebuild` may seed. Each already iterates a
known logical position; bracket its existing raw insertion with a diagnostic
seeding context containing that leaf, `zbtScoreLeafPhysicalPos(leaf,i)` and hash.
The original raw insertion runs once, unmodified in its placement decision.
After its existing ID write, a diagnostic hook seeds only if its chosen index
slot is zero. All other raw insertion sites have no seeding context. Context
must be cleared immediately after the call and absent at public query entry.

Every `zbtIndexSetId` write to slot zero first invalidates its prior shadow hint,
even if the new ID equals the old ID. This includes ordinary insertion, deletion,
reference repair and moves. Nonzero index slots do not invalidate it. A known
CopyLeaf/Rebuild position may then replace the invalidated hint. No read refreshes
a hint. Leaf shifts, reverse order, compaction, replacement, split/merge or same-ID
reuse can stale a surviving hint; they do not trigger eager maintenance.

Retain exact seed identity (full hash, length and member bytes) in diagnostic
storage solely to distinguish staleness from mismatch against a different query.
The physical position comes from the existing loop; no new lookup chooses it.
The six fixtures bound member bytes at 384. A longer seed asserts, rather than
truncating identity or extending the fixture. The seed snapshot must not retain
leaf/external pointers that can become dangling.

## Allocation identity and lifecycle audit

Key shadow tables by bucket allocation identity, not `zbtIndexTable *`: descriptors
are copied to locals and promoted during resize. Use a monotonically increasing
generation with an integer address key captured while the allocation is live.
Released address reuse creates a fresh generation with zero hints. Keep all state
in fixed diagnostic arrays, outside tree ownership and allocator accounting.

| Original operation | Required shadow transition |
|---|---|
| Successful `zbtIndexTableAlloc` | Register a fresh zeroed generation after allocation succeeds; allocation failure registers nothing. |
| `zbtIndexTableRelease` | Retire the live generation before its original free; assert matching size/width. An empty descriptor has no live allocation. |
| Rehash descriptor promotion | Preserve the receiving allocation's identity and hints; retire only the subsequently released old allocation. |
| `zbtIndexDupTable` byte copy | Register a separate generation and copy hints and exact seed snapshots, including already stale hints; never re-seed from current leaves. |
| `zbtreeDefragStart` bucket relocation | Rebind the same generation to the returned live address, preserving all hints. Capture old address as an integer before the original relocation can free it. NULL/no-move retains the key. |
| Header/rehash descriptor relocation | No shadow identity change, because bucket identity is the key. |
| Rebuild and final free | Follow normal allocation/release hooks; no hidden reset or dangling generation. |

The source audit found all production ID array writes in `zbtIndexSetId`; table
allocation, explicit duplication memcpy, release and defrag are separate sites
and each needs an explicit hook. Do not infer duplication from matching addresses
or lazily initialize shadow state when a lookup first sees a table. Registry
lookup failure, duplicate live identity, size/width mismatch, capacity exhaustion
or unmatched release must abort the diagnostic.

Initial fixed bounds are 16 simultaneously live tables, 1024 buckets per table,
384 bytes per seeded member, 4096 counted table calls and 1000 queries. Preserve
at most 4096 lifecycle events per process and 65536 counted eligible leaf events;
assert before every append. Each table slot can be reused only after retirement,
with its next generation. Exceeding a bound is a diagnostic failure requiring a
separate reviewed revision; never silently truncate or expand after observing counts.
Setup/warmup lifecycle totals and the counted-phase totals are reported separately.

## Observing hints without changing lookup behavior

Retain the original approximate-tag check, actual index-tag check, tombstone,
ID-range, free-leaf, leaf-ID and migration checks in their original order. Only
the resulting eligible original leaf call can inspect a shadow hint. Nonzero
index slots are counted as ineligible; eligible slot-zero calls partition into:

1. Disabled/unavailable hint.
2. Position outside the current leaf count.
3. Current physical raw leaf tag differs from `hash >> 24`.
4. Raw tag agrees but the complete current-record predicate fails.
5. Complete predicate succeeds.

Decode only a bounded current physical position through the current offset array;
never use an old record offset. The diagnostic predicate reproduces the original
external-hash rejection before pointer validation, packed decoding, exact length
and `memcmp` equality. Compute prospective logical position and score into private
locals only. Always execute the full original `zbtScoreLeafFindMember` exactly once
with its original arguments and outputs. A hinted success must agree with the
original successful result and every requested output, including score object
bytes. A failed hint does not require the original scan to fail.

Staleness is a separate classification, not a replacement for that partition.
Out-of-range hints are stale. For a position still in range, compare its current
member identity against the exact seed snapshot (external hash before pointer
access); a changed identity is stale even if its current member matches this
query. An unchanged seeded member can fail the query predicate without being
stale. Report stale/unchanged subsets for each applicable terminal classification.
These extra diagnostic reads are not claimed to be candidate work or free work.

Count original leaf results independently. A useful primary exposure requires a
slot-zero hinted success on an actual original successful leaf call. Record unique
query IDs as well as event totals; do not count one query multiple times. The
original full scan may succeed after an unavailable or failed hint, which remains
a normal fallback observation. No original leaf scan, tag candidate or probe is
skipped. No observed identity establishes absence.

## Folded-filter observation

Define `fold(x) = (x & ((1ULL << 56) - 1)) | (x >> 56)`. Derive the shadow filter
from the original current home word at each original filter evaluation, and fold
the original query mask the same way. Because fold commutes with OR, this is
equivalent to recording every original mask in a 56-bit filter, while leaving
every original filter write and branch untouched. Shadow hint bytes never enter
the calculation. Assert that an original positive is also a folded positive.

Record original positive, original negative/folded negative, and original
negative/folded positive counts separately. Observe `zbtIndexHomeMayContain` and
the direct `zbtIndexScanSlot` filter consumer with separate categories; the fixed
six cases need not exercise scan, and zero scan observations is a coverage gap.
Observe only evaluations the original control flow reaches. Do not follow the
folded-positive branch when the original rejects, or simulate extra bucket visits.
Therefore these counts quantify additional filter positives, not additional
leaf work or the complete counterfactual candidate path.

## Evidence, checker and review gates

The future generated harness will emit ordered per-query and per-table records,
ordered eligible-leaf classifications, phase-separated lifecycle totals/events,
table generation/width/bucket count, seeded/invalidated hint totals, filter totals,
exact operation/checksum results, immediate memory and resize endpoints. It must
emit no addresses or elapsed/cycle fields. Raw event fields permit the checker to
rederive aggregate classifications and unique successful query exposure; they do
not substitute for the original C assertions about current bytes and outputs.

Reuse the hardened prior census's model/memory and aggregate invariants in a
separate checker. Add negative synthetic cases for every impossible partition,
success without original success, useful count exceeding unique successful queries,
stale/unchanged overlap, filter false negatives, nonzero-slot hint success, invalid
hint code/position, missing generation, release/reuse/duplication mistakes and
seed creation outside the two admitted sites. Include positive abstract lifecycle
traces for promotion, copied stale hints and released-address reuse. Exhaustive
Python integer checks cover all byte tags, folded membership under OR, and hint
replacement independence. These are synthetic/static tests, not C executions.

Keep the prior clock-denial design: no clock reader in the harness; all 13 denied
clock/syscall wrapper symbols retained under native and LTO linking; verify the
saved ELF symbols/undefined references and explicit static link probe. Compile and
inspect only locally. Do not execute the diagnostic, correctness harness, clock
probe, pilot, profile or counter workload locally. Preserve all failed preparation
attempts and revision freezes. Generated patches must be reconstructible and
unmodified source regions byte-identical to the original.

After independent source/parser review, separately build native and target on the
owned Intel fleet under controller authorization, with live reservation, isolation
and exact source/compiler/ELF checks. Review exact emitted code before any six-case
execution. This design authorizes neither stage. ARM is released; no reacquisition
or ARM result is assumed. Each later case is one fresh process, fixed inputs, no
timing, no retries or expanded seeding after seeing coverage. No performance
population, qualification or accepted source is created by this diagnostic.

## Limits and provenance

The sparse seeding policy can provide no usable hints; that is a valid negative
result, not justification for searching to create more. The fixed six warm states
do not cover large IDs, all mutation histories, active resize, duplication, defrag,
binary members or scan unless those original cases naturally reach them. Lifecycle
hooks and synthetic state tests are necessary preparation, not runtime coverage
of those paths. Candidate correctness would require a separately admitted matrix.
Neither useful hints nor additional filter positives can be multiplied by hotspot
samples, instruction estimates or pipeline shares to predict elapsed gain.

Public role: diagnostic preparation author. Own tool discovery found no callable
cpu-perf or library_status endpoint; exposed topdown tools were not invoked. The
controller's fresh actual fifth consultation challenged this exact 56-bit mechanism:
revision `deb5a0bac467`, 3/287 sources, 158 passages, no supporting passage. This is
shared consultation, not an independent call or literature proof by this author.
Backend provenance remains private and exact costs are unknown.

| TMA share of total pipeline slots | Baseline for this diagnostic | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No TMA roots or children were collected. There is no candidate and no diagnostic
execution; historical samples do not fill these missing measurements.
