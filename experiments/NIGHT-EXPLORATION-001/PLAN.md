# Eight-hour exploration queue

Status: PLANNED. No candidates selected and no overnight measurements collected.
Starting evidence: [four-size Apple M1 baseline](../SIZE-MATRIX-001/apple-m1/SUMMARY.md).
Tree source baseline is the unchanged extraction recorded by source-manifest.json;
record the exact launch HEAD and all source/referee hashes on each host.

## Time budget (relative to launch)

| Elapsed | Work | Deliverable |
|---|---|---|
| 0:00–0:20 | Host/toolchain capture; native/sanitizer validation; five-size inventory | Host manifest and baseline table |
| 0:20–1:00 | Targeted duration calibration, A/A controls and rank profile | Frozen harness and diagnosis |
| 1:00–2:30 | RANK-001: rank accumulation | Population records, variants, result |
| 2:30–4:00 | UPDATE-001: distinguish update paths | Workload breakdown; conditional candidate |
| 4:00–5:30 | LOOKUP-001: single-query member search | Population records, variants, result |
| 5:30–6:30 | DECODE-001 only if earlier work is concluded | Single-score policy result or explicit skip |
| 6:30–7:15 | Fresh confirmation/review of the best eligible candidate | Confirmation and review |
| 7:15–8:00 | Audit, charts, report, commits and handoff | Readable morning report |

These are ceilings, not quotas. Finish/skip a target early and advance. Never extend
one target because its measured result is disappointing. Reserve the final 45 minutes;
do not begin a child that cannot finish plus cleanup before the current round ends.
A target may span rounds using its saved state. No more than one measurement-harness
revision and one distinct noise diagnostic per target; after that record the blocker.
Stop early when no useful bounded work remains. Do not fill the night with unrelated
correctness matrices, repeated failed schedules, or bookkeeping.

## Baseline: five sizes, all eight operations

Run once per host/session using a new output directory:

```sh
python3 scripts/run-size-matrix.py --out "$CAMPAIGN_DIR/baseline" --budget-seconds 600
python3 scripts/analyse-size-matrix.py "$CAMPAIGN_DIR/baseline"
```

16-byte members; seeds 1/2/3; six same-binary ABBA blocks; 120 serial processes,
960 rows, 40 cells. Native/sanitizer validation precedes timing. The 600-second cap
is for timing, not builds/validation. Record incomplete work honestly if it overruns
the preflight slot. A repeated inventory does not resolve the existing precision
failures; targeted calibration below is a separate, frozen measurement revision.

## RANK-001 — first priority

Question: does ancestor sibling-count accumulation account for rank's size growth?
The current implementation locates the member, then sums preceding child counts
while walking to the root. Existing score lookup also decodes a score, whereas rank
with a NULL score output does not: never subtract their times as a component estimate.

1. Profile public rank at 10K, 100K and 1M. Inspect the actual release assembly.
2. Add a private diagnostic that pre-resolves leaf/position outside timing and
   measures the existing rank accumulation with consumed results. Report separately
   from the public API; the diagnostic's cache behavior is not the API's behavior.
3. In a separate instrumentation pass count tree height, parents visited, and
   sibling counts summed. No instrumentation in reported timing binaries.
4. If profile/code evidence supports this cost, use both population steps to choose
   one hypothesis. Candidate families to evaluate include dependency reduction,
   portable unrolling, and node-summary changes. These are possibilities, not selected
   implementations. Check whether Clang already vectorizes before writing intrinsics.

Primary: public rank at 100K/16-byte members, successful queries. Required second
primary: 1M rank. Guards: rank at 100/1K/10K, reverse rank, absent members, optional
score output, equal-score ties and mixed finite-score layouts. Mutation/memory guards:
all standard insert/update/delete sizes; all-eight-operation matrix before adoption.
If a node summary is proposed, add split/merge/count-maintenance tests and measure
mutation costs. Prefer a layout-preserving change for the first bounded test.

Stop: if accumulation is not material in public rank, retain the diagnosis and move
on; do not optimize a disconnected synthetic kernel.

## UPDATE-001 — identify which update path is expensive

The existing update case adds N to every score. It exercises large moves and cannot
stand for ordinary small changes. An in-place fast path already exists in the source.

Create independent, explicitly named cases at all five sizes:
- Same value: no score change.
- Position preserving: alternate between two exactly representable scores strictly
  between neighbors; use score gaps so this does not drift or cross a neighbor.
- Nearby reorder: alternate adjacent ranks using deterministic, reversible values.
- Distant move: alternate between two distant rank regions; also retain the original
  monotonically increasing +N workload as its own case.

Use matched initial trees and independent query order. Record actual in-place versus
remove/reinsert counts in an untimed instrumentation pass. Verify exact score bits,
member order, signed zero, ties, index ownership, and stable membership after runs.

Default optimization primary if profiles justify one: position-preserving updates at
100K/16 bytes; second primary 1M. Guards: all update patterns/sizes, long members,
lookup/rank/iteration, and owned memory. If profiling instead supports distant moves,
freeze a separate proposal with that primary before constructing/timing candidates.
Do not relabel the fastest observed workload as the primary afterward.

Stop: a useful result can be just a validated update-path benchmark and profile if
no meaningful, bounded implementation opportunity remains in the time slot.

## LOOKUP-001 — single-query lookup, not batch-only gains

Profile hit and miss lookup at 10K/100K/1M with 16-byte members. Determine whether
leaf-tag search remains hot; record tag candidates and full member comparisons in
separate instrumentation. Construction order and query permutation must be independent.

Review EXP-006 first: its retained inline scanner helped a batched workload but
showed concerning single-query regressions. Reusing that patch unchanged is a control,
not a new hypothesis. Potential proposals must explain the single-query difference.
Do not change hashing or silently assume all member lengths are equal.

Primary: public successful single-query lookup at 100K/16; second primary 1M.
Guards: hit/miss/mixed at all five sizes; 8/16/319/320/321/1024-byte keys at 100K;
existing batch sizes 1 and 16 at 10K; collisions and bounded reads, first match,
resizing and ownership correctness. No architecture-specific path without scalar
fallback and corresponding boundary checks. First try a portable change if justified.

## DECODE-001 — optional, lower priority

Test scalar fallback only for count == 1, retaining frozen EXP-007 B bulk decoding
for every larger range. EXP-008 cutoffs 4/8/16 failed; do not repeat those policies.
This is private-helper work, not a public iterator improvement.

Primary width60/forward/count1; guards widths0/8/31/57–64, both orientations,
counts1/2/4/7/8/16/32/96, partial/empty ranges, exact finite values and signed zero.
Use identical output-array materialization and checksums. Count1 inputs can be
seed-invariant; fresh measurements must not be described as new input diversity.
Correctness and code-size/call-overhead evidence are required. A bulk-helper win
needs a separate public integration experiment before any whole-tree claim.

## Progress rule

Each round must leave one of: a validated harness, a profile that answers a question,
a complete candidate comparison, a documented rejection, or a concrete blocker.
Keep a short scoreboard with NOT STARTED / RUNNING / CONFIRM / REJECT / PARK / COMPLETE.
Explain changed direction in one sentence. Do not equate number of tests with progress.
