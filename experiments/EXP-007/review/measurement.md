# EXP-007 measurement review before timing

Reviewer `/root/proposal_c`, Codex collaboration agent; exact backend model and
token/currency cost unavailable. This is a separate static review of A, B, the
control and the shared referee, not an independently executed performance
experiment. I also implemented C; I am not an independent reviewer of C's own
design. No builds or timings were performed during this review. At review time,
the chair supplied the run plan by message; README/selection were not yet present.

Verdict: the shared materializing bulk referee is appropriate for a bounded
comparison of these private bulk helpers, conditional on identical compilation,
generated-code inspection, correctness checks and the declared serial run plan.
It cannot establish a scalar iterator improvement or inherit EXP-004 timing values.

## Matched work and observable results

Control and candidates all accept the same logical start/count and write the same
number of doubles to a disjoint buffer. `decoder_batch` allocates the same
96-element stack array for each helper invocation, passes it to the decoder, then
uses the same four checksum chains and tail loop. The intervening empty inline
assembly takes the array address and has a memory clobber. It makes the buffer
observable before checksum consumption; the compiler should not fuse decoding
straight into the checksum and erase materialization for one implementation.
The round-level memory barrier also prevents invariant decoding from being moved
out of repeated rounds. Both barriers are present in the frozen common kernel.

The source-level output and checksum work is identical. Its executed instruction
cost need not be identical: inlining, vectorization, spills and loop placement can
change as a consequence of the helper. Do not subtract control overhead or describe
the reported ns/decode as arithmetic-only decoder cost. It measures dispatch,
decoding, output materialization, checksum consumption and loop bookkeeping.
Compiler-generated faster stores/vectorization are legitimate bulk implementation
effects, but a gain should not automatically be attributed only to branch removal.

A uses one crossing dispatch, a zero-width fill and an explicitly cached mask and
metadata on the simple path. B adds byte-aligned specialization and manually caches
metadata for its crossing path as well. These are coherent implementation choices
within leaf-geometry specialization, but B changes more than the crossing predicate.
Generated assembly must identify which paths actually changed. Neither variant
mutates public iterator state or makes the helper part of the public tree API.

Inspect every binary's `decoder_batch` for actual packed input loads, output stores
before checksum loads, and classification placement relative to the position loop.
Record vectorization and code-size changes if present. Fewer static conditional
branches are not dynamic instruction or cycle evidence. An empty assembly barrier
is not a hardware cache flush, and no cold-cache claim follows from its presence.

## Fixture scope and correctness boundaries

Fixture packing is independent bit-at-a-time code, and expected IEEE bits are
computed independently of the production ordered-score conversion. Bulk validation
compares individual output bits against that oracle for start0, midpoint and end,
with zero, single and remaining-length ranges; canaries check all unused output.
The separate scalar validation does not substitute for those bulk checks.
Release and sanitizer runs must execute these checks before eligibility.

The synthetic leaves are valid decoder layouts, not necessarily sorted canonical
leaves built through the tree API. They exercise physical reversal; the helper
always traverses a logical forward range. Report the two orientation cells as
physical forward/reversed layouts, not two public iterator traversal directions.
Count1 deterministically uses delta0; it is mainly a dispatch/short-range control,
not diverse value-distribution coverage. Counts7 and96 provide additional deltas.
Bit-pattern correctness coverage across all widths and score shifts remains
necessary even where the timing matrix samples fewer widths.

Eight warmed leaves and a reusable stack output establish a hot bulk experiment.
Output buffer size and tree-owned allocation must match, but larger generated code
is not captured by the tree-owned-memory metric. This experiment cannot establish
large working-set, cold-cache, random lookup, scalar iterator, or actual big-endian
performance. The original EXP-004 mixed-output guard remains unresolved.

## Run and inference requirements

The supplied plan fixes six ABBA blocks, 129 in-process samples, primary width60
forward/count96, full-count widths0/8/31/57/58/59/60/61/62/63/64 in both physical
orientations, and count1/7 guards at widths8/60/63/64 forward. Preserve all rows and
the full fixed schedule. Same fixture hashes, compiler options, source baseline,
allocator, checksum and materialization kernel are required across binaries.
No concurrent builds, profiles or other experimental processes during timing.

The declared acceptance gate is at least2% primary improvement, no demonstrated
guard regression greater than1%, and same-cell A/A block effects all within ±1%.
Freeze the exact effect statistic and aggregation rule before running; minima and
medians must not become competing post-hoc choices. Inner samples are correlated
within a process; six blocks, not 129 samples per child, are the independent
comparison units to the extent scheduling permits. Display retained dispersion,
and do not reclassify failed A/A cells by dropping a noisy block.

A candidate with a strong primary signal but unresolved guards may be shortlisted
for fresh-seed confirmation while explicitly PARKED. That is investigation, not
acceptance. Freeze which fresh cases/seeds will confirm before reading discovery
results, use the same referee, and keep discovery and confirmation summaries
separate. A held-out run by the same chair on the same host is fresh confirmation;
it is not independently operated experiment replication. Three candidate selection
also makes apparent discovery winners optimistic, reinforcing this separation.

One documentation defect is visible: the referee's opening comment still says
"Only EXP-004's source patch differs." EXP-007 instead appends a private bulk helper.
Correct this before freezing the referee, or explicitly record it as a stale
comment; it must not be used as provenance. This is not a runtime defect.

No runtime result or acceptance judgment is asserted by this pre-timing review.
