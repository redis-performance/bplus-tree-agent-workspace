# Next steps after EXP-008 (Apple M1)

The broad scalar/bulk crossover failed its preregistered gates. The only new lead is
a count1-only scalar path: at width60 forward, A/B cutoff variants were faster at count1
but broad scalar paths regress at counts4–8. Treat this as an unconfirmed local M1
observation; the count16 A/A precision gate failed. Do not add a count1 branch to source
or alter EXP-008 cutoffs after the result.

1. Reproduce EXP-004, EXP-007 and EXP-008 on Apple M6 mini using the
   [host replication runbook](REPLICATE-LATEST.md). Store separate host fingerprints,
   profiles, raw matrices and audits. Compare each host independently; never pool timing
   rows or infer architecture-wide speedups from these two machines.
2. If the M6 matrices support the same count1 signal and qualify their A/A controls,
   create a separate experiment for scalar only at count1, with count2+ guards and a
   fresh confirmation rule frozen before timing. Use the rapid narrow loop first, then
   broaden only the preregistered guard matrix if it survives.
3. Keep the scalar iterator and production source unchanged until correctness, guards,
   profiling and adversarial review all pass. EXP-007's bulk helper remains a private
   benchmark artifact, not an iterator optimization.

EXP-008 ran all 160 cells in serial ABBA blocks, but process-launch overhead and short
batch durations leave many cells unqualified. For future focused work, increase timed
work per process while keeping a small number of fixed cells and full paired blocks;
retain per-process distributions and A/A controls. This improves iteration speed without
confusing inner samples with independent trials.

# Next steps after round 16

## Archived next step after EXP-007 (superseded by EXP-008)

The [bulk decoder experiment](EXP-007/RESULTS.md) found reproducible full-leaf gains,
but B's three short-range losses block all-range adoption. Test a new hybrid with
scalar decoding for short ranges and specialization for longer noncrossing ranges.
Preregister counts 2/4/8/16/32/96, aligned/crossing guards and held-out confirmation
before choosing a threshold. Preserve existing B and both frozen matrices. A/A
precision remains incomplete; no unchanged schedule retry or guard substitution.
Only a guard-passing bulk candidate should advance to explicit scalar iterator
integration. Current source NONE; optimization totals 0 accepted / 2 rejected /
4 parked. Overnight remains stopped. Historical queued work below is superseded.

Read [ROUND-016](OVERNIGHT-2026-10-17/ROUND-016.md) and shared memory. Main source stays
baseline. EXP-002/003 are rejected; EXP-004 remains A/PARK and EXP-005 PARK/NONE.
Four sequential populations, zero accepted or published optimizations. All 12 candidate
patches reconstruct their frozen sources exactly in the new retained-candidate audit.

1. Preregister [score moves during actual mixed-width migration](OVERNIGHT-2026-10-17/ROUND-016-NEXT-FIXTURE.md).
   Round 16 now covers a live cursor spanning natural widening, clone/relocation,
   external ownership, bulk renumbering and narrowing. Cross-table score movement during
   natural mixed-width migration is distinct. Use fresh public lookup positions, an
   independent score/member model, callback-time exact score bits and observed source/
   destination leaf ownership. Extra lookups themselves advance migration. The recipe
   is untested; choose seeds, counts, sources, builds, faults and budget before execution.
2. Performance comparisons need a separately qualified runner or a distinctly justified
   method. Do not repeat failed duration/warmup/QoS/caller/placement/bookkeeping/transport
   protocols unchanged. Matching endpoint CPU IDs cannot exclude within-window migration;
   effective QoS and frequency remain unknown. No timing ran in rounds 14–16.
3. New optimizations still require profiles, qualification and both population stages.
   Do not replace EXP-004's unresolved original guard with favorable extra subsets, or
   pool EXP-005 A/C observations. Independent confirmation/review and committed provenance
   remain required. Root source waits for separate morning review.

Round 16 completes 192 semantic source/build/seed/mode cells, including 64 fresh-seed
cells with debug-only assertions omitted. All oracle CHECK and unconditional serverAssert
checks remain. Six deliberate faults are detected, three new distinct types. Initial
compile, classifier and documentation-link failures remain with separate corrections.
Six whole-oracle branch captures establish reachability, not CPU-time cost. No production
bug or performance improvement is claimed.

Totals: 6 harnesses, 12 baselines, 29 diagnostics, 23 boundary suites / 48 distinct fault
types; 4 sequential populations; 0 accepted / 2 rejected / 2 parked. Exact backend/model/
cost unknown; reviewer startup failed. No protected git retries, publication, permission,
runtime or STOP edits. Final worker writes MORNING-REPORT.md before 2026-10-18 07:00 UTC
/ 08:00 Europe/Lisbon.

Round17 handoff: [smaller/all-miss batch promotion preparation](OVERNIGHT-2026-10-17/ROUND-017-NEXT-FIXTURE.md).
Current16-lane mixed batch transition is covered; other transition counts/layouts are
not established. SourceNONE; no unchanged failed timing retries or guard substitution.

## After round 18

EXP-006 C/PARK adds a possible inline-tag-search improvement, with unresolved long-key guard uncertainty and concerning single-lane regression. Follow [the next-fixture note](OVERNIGHT-2026-10-17/ROUND-018-NEXT-FIXTURE.md); preserve all raw blocks and main baseline. Original guard qualification, independent review and committed provenance are still required.


## Latest follow-up: repeat the four-size matrix on M6

The requested 100/1K/10K/100K × eight-operation baseline is complete on Apple M1.
Use [SIZE-MATRIX-001](SIZE-MATRIX-001/README.md) and [the rerun guide](REPLICATE-LATEST.md)
to collect M6 results separately. Compare matched sizes/operations and retain compiler
and host differences. Small insert/delete windows and iteration duration need better
batching before fine-grained optimization claims. No unchanged rerun is needed on M1.
