# Fourth population — repeated leaf rejection, diagnostic first

**Recommendation: NONE for implementation now.** A distinct source-supported
opportunity is to avoid searching a leaf again after the same table lookup has
already searched that leaf and rejected the member. However, the saved evidence
contains no count of those repeated searches, especially in the primary hit
fixture. Adding remembered state to every candidate could cost more than it saves.
The required next step is a separately authorized, fleet-only diagnostic of leaf
search multiplicity, not a candidate or a retry of an earlier failed mechanism.

This proposal was written independently without reading any other fourth-population
draft, including `lookup-state.md`. The public role is tags-path proposer; the
participant implemented earlier candidates, including H3-B, H5-B, H6-B, H7-B and
H8-B. That overlap supplies context, not independent acceptance credit. Detailed
backend provenance remains private; exact token/cost accounting is unknown.
No source change, build, workload, timing, profiling or fleet action occurred.

## Frozen evidence and exclusions

Rehashed original `current/src/zset_btree.c`:
`16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, extraction
`e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, pinned upstream
`ee8e7f70152404649ac947157fd662d11b4a00d5`. All prospective work starts there.
H7 exact candidate masks and H8 range-first record classification are already
assigned and explicitly excluded. This proposal changes neither mechanism.

The [original native profile](../native-profile/report.stdout) puts41.38% of
whole-process user-cycle sample period in the leaf helper and21.77% in raw lookup;
named `memcmp` accounts for2.82%. These locate a substantial search path, but
provide no repeated-leaf frequency or marginal cost. A sample in the leaf helper
cannot distinguish its first invocation from an avoidable repeat. No symbol
percentage is treated as a speedup budget or pipeline category.

The rejection packet materially limits the proposal:

* [H1](../reviews/H1-FINAL.md) rejects helper-boundary variants. Selective inlining
  wins hits but loses score/miss/update, and raw frames grow to272 bytes. Additional
  per-lookup cache state must therefore pass an exact frame/spill screen; no leaf
  inlining is part of this idea.
* [H3](../reviews/H3-FINAL.md) rejects short equality variants because target or
  Intel long/external guards fail. Keep the original byte equality and external
  fallback; no specialized short comparator.
* [H4](../reviews/H4-FINAL.md) rejects query-filter changes, including B's repeated
  Intel miss regression. The home filter, its formula and placement stay unchanged.
* [H5](../reviews/H5-FINAL.md) closes NONE: B does not specialize its stable kernel,
  C misses native primary, A misses LTO primary. No resize-dispatch outlining or
  stable-state assumption is introduced here.
* [H6](../reviews/H6-FINAL.md) rejects all descriptor-length variants on primary;
  A/B also have failed guards. No descriptor hints, tag-width change, metadata
  cache or record-layout change is proposed.
* [H2 final](../reviews/H2-FINAL.md) is **PARK, source NONE** after ARM seed43 miss
  A/A fails at−3.601147%; no ARM43 comparison ran. Its matched profiles remain
  supporting evidence about address arithmetic only. No H2 patch, control,
  acceptance status or profile gain is borrowed.

This is also distinct from replacing the leaf `memchr` scanner, changing the
successful physical/logical mapping, or revisiting an unused-position shortcut.

## Concrete source opportunity and semantic proof

`zbtIndexTableInsertRaw` inserts one `(folded tag, leaf ID)` entry per member.
Several members may occupy one score leaf, and several entries can therefore
refer to that leaf. The unchanged `zbtIndexTableFind` enumerates matching bucket
slots, rejects false approximate tag bits, skips tombstones, validates the leaf ID
and migration ownership, then calls `zbtScoreLeafFindMember` for each candidate.
It remembers no previous failed leaf search. A collision-heavy probe run can thus
invoke the same full leaf search more than once for one query.

The leaf helper searches all matching tags through its whole eligible leaf,
checks full hashes for external records, and compares exact length/bytes. A zero
return proves absence from that leaf for that query, including every same-tag
candidate inside it. It leaves score/position outputs untouched on failure.
During one table-finder invocation, those helper calls and their score reads do
not mutate records, move leaves, advance rehash or change the query. Under the
same single-operation mutation assumptions as the current implementation,
searching that same validated leaf again cannot change a failure into a hit.

The safe cache event would be **a completed failed leaf search**, not merely an
encountered ID, rejected raw tag, tombstone, invalid/free reference or migration
mismatch. Successful searches return immediately and cannot be cached. Before
skipping a repeat, preserve original tag, bounds/free-ID and migration checks;
otherwise an optimization could suppress required assertions or conflate an
ineligible reference with a fully examined leaf. Reset remembered state on every
finder invocation. Do not carry it across destination/current-table calls, rehash
steps, API calls, mutations or queries. Insertion-hint/tombstone enumeration still
runs in the original order after candidates are exhausted.

There is no persistent metadata or ownership invariant, and no permission to
collapse index entries: deleting apparently duplicate references would break
member counts, repair and migration. This is elimination of repeated *search*,
not index deduplication.

## Three contingent implementation shapes

These are implementation options for the same unselected mechanism, not new
independent population members. Do not implement any until the diagnostic closes
the missing opportunity evidence and the chair selects this hypothesis.

| Option | State and skip test | Benefit envelope and cost |
|---|---|---|
| T1, smallest scope | Remember the last validated leaf whose full search failed; compare after normal validation and update only on another completed failure. | Removes consecutive repeated failed-leaf searches, including across adjacent buckets. One pointer/ID and one comparison can tax the first useful candidate; likely best maintainability if data supports it. |
| T2 | Two-entry local cache of validated failed leaf identities, replaced deterministically on a new failure. | Also removes short alternating repeats. Extra comparisons/live registers may erase any saving or grow raw frames. No array indexed by fixture rank and no persistent cache. |
| T3 | Within each bucket, retain a bitmask of candidate slots whose full leaf searches failed; inspect IDs of those marked slots to detect a repeat before another leaf call. | Limits remembered state to one bucket and uses existing packed IDs, but adds ID loads/scans and needs width-correct decoding. It may be plainly inferior; do not prefer it merely because it avoids a pointer spill. |

No option changes tag math, memchr/memcmp, decoder, reference repair, probing,
hash seed/function, allocator or outputs. T2/T3 are not fallbacks to rescue T1
through post-result stacking. Each would start from the same original source.

## Required diagnostic before nomination

The source proves possibility, not frequency. The original primary often may
succeed in its first eligible leaf; such a query has no failed search to reuse.
This proposal predicts **no saving at all on those paths**, while an implementation
may still add work. That is the leading reason for NONE now.
Even when a hit visits several index entries, the first eligible occurrence of
its actual leaf finds the member and returns. Any reusable failures on that hit
must belong to other leaves encountered earlier; repeated references to the
successful leaf itself cannot supply the proposed saving.

If separately authorized, preregister a bounded diagnostic executable on the
benchmark fleet after live reservation and isolation checks. Do not run it on the
controller. Instrument an isolated copy of the unchanged baseline finder solely
to count work; do not modify the frozen timing referee or label instrumented
elapsed time as baseline/candidate acceptance evidence. Pin source, instrumentation
patch, ELF, compiler, exact fixture/counts, seed and command before running.
Record complete totals per case/query class, including zero-opportunity cells:

1. Bucket visits, approximate-mask candidates, true stored-tag candidates,
   tombstones, invalid/free references and migration-owner rejections.
2. Completed leaf searches, successful versus failed searches, distinct validated
   failed-leaf identities, and repeats of an already failed leaf within the same
   finder call. Separate immediately repeated, alternating and different-bucket
   repeats, matching the three prospective caches' exact coverage.
3. Hits ending on the first eligible leaf versus after failures, and the number
   of eliminated calls each cache shape could cover. Keep hits, scored hits,
   negative queries, long inline, external, updates and resizing separate.
4. For repeated calls, leaf entry count, number of candidate tags and decoded
   records/bytes examined. These are opportunity counts, **not** equivalent cycles
   and not a claim of a particular fraction of elapsed time.

Use the original six cases at their frozen seed17 inputs; held-out seeds29/43
must not be searched to select a favorable seed. Separately preregister same-tag
collision/displaced/tombstone and active/final-resize inputs with fixed construction
rules. Those adversarial cases establish correctness/performance exposure, but a
win confined to them cannot satisfy the unchanged ordinary primary. Do not
reorder members or manufacture duplicates to make the primary diagnostic favorable.

Stop at NONE if primary eligible repeats are absent, if repeat coverage is only in
guards, or if the evidence gives no credible route to the2% ordinary-primary gate
after unavoidable new comparisons/live state. A nonzero count alone is not
sufficient. Counts cannot establish marginal scan-cycle cost: any further matched
profile or candidate timing needs its own reviewed, qualified fleet protocol.
No diagnostic has been implemented or executed by this proposer.

## Conditional correctness, static and performance gates

If selected later, retain57 native+57 sanitizer tests,36 fixture cells and135k
supplied output/external checks. Add deterministic fixtures where two matching
index entries identify the same leaf after a full miss; alternating leaf IDs;
repeats across wrap/displacement; tombstones and stale/free IDs during rehash;
new/old ownership and final resize completion; narrow/wide IDs; raw/prehashed and
all optional outputs; insertion-hint equality; full-hash collisions with distinct
binary members; empty/short/long/external and externally represented short records.
A missed query must leave all original outputs unchanged. Pair tests with the
unchanged referee and verify entry counts, reference repair, split/merge, score
moves, duplication and defragmentation. A cache must never outlive a lookup.

Exact ARM native and target LTO assembly must retain the original helper, loops,
filter and validations; the repeat path must bypass an entire leaf call without
new decode work. Reject if frame growth/spills or duplicated hot-path state make
net benefit implausible. Inspect first-candidate-hit and no-candidate-miss paths,
not only the repeated collision path. The state/control overhead must be listed
explicitly; smaller source is not a cost proof.

Acceptance remains independently qualified same-session A/A, at least three ABBA
blocks, every row≥250ms, primary improvement≥2% in every block, all guard and
owned-memory changes≤1%, separate native/LTO and Intel portability cohorts, and
no pooling/unchanged retries. Original six cases, iterator/rank/churn guards and
separately frozen collision/displaced/active-resize guards remain required before
adoption. Exact bytes should be unchanged because there is no allocation/layout
change; stack/text growth are separate. Fresh seeds, matched profiles and final
independent review follow only discovery success. H2's PARK gives no waiver.

## Consultation and TMA

Fresh own enabled-tool discovery matched no callable cpu-perf/library-status tool.
Therefore no own `library_status`, `ask` or source retrieval is claimed. Prior
controller consultations recorded in the selection/review packet are shared
context only, with3/287 sources and158 passages and no supporting retrieved passage
for this new mechanism. The earlier mask/classifier consultation does not consult
or validate repeated-leaf caching. A fresh question should present the exact
multiplicity counters, cache miss/hit paths and prior frame/guard failures before
choosing any implementation. No speculative external source citation substitutes
for that missing diagnostic.

Qualified ARM baseline Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring
and their children remain unavailable; there is no new candidate or pipeline
measurement. Intel/H2 supporting categories cannot establish an ARM cause or
acceptance. Final proposal disposition remains **NONE pending opportunity evidence**.
