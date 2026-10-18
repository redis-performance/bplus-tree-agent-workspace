# EXP-008 proposal B — keep scalar decoding for short ranges

Proposer: B (delegated proposal pass; model/backend and token cost unknown).
Status: proposal only; no code, build, or timing performed.

## Evidence and hypothesis

EXP-007's fresh confirmation shows bulk B is 33.14% faster at 96 scores of width 60,
but 20.79% slower for one width-60 score and 6.49% slower for seven width-63 scores.
Its generated dispatch is outside the score loop; B's noncrossing path omits the
ninth-byte scaffold and its aligned path omits bit-offset arithmetic. B is outlined
while the control and other variants inline. The short-range call/dispatch overhead is
a plausible explanation, not an isolated causal finding. The recorded profile locates
active decode/checksum code but has no comparable timed-only cycle shares.

**Hypothesis:** use the scalar control decoder for ranges of 16 scores or fewer and
the retained B specialized bulk decoder for ranges above 16. The bulk path should
recover the full-leaf gain while the scalar path avoids B's observed short-range losses.
The crossover at 16 is deliberately concrete and falsifiable; EXP-007 did not measure
that count, so this proposal makes no claim that 16 is already optimal.

## Candidate and benchmark plan

The candidate is a single count check at the helper boundary: `count <= 16` selects the
scalar control path; `count > 16` selects B's bulk path. Preserve B unchanged as an
artifact and compare both candidate paths with the same frozen control and B binaries.
Do not alter the public iterator or add per-leaf state. Run one helper call per measured
range, with the same outputs and checksum work on every path.

Primary cases: width 60, forward and reversed, with counts 32 and 96. The primary
statistic is the geometric mean of paired ns/score ratios over those four cells;
require at least 2% improvement over control. Counts 32 and 96 are both above the
proposed crossover and show whether a gain survives below full-leaf size.

Exercise counts **2, 4, 8, 16, 32, 96**. Guard widths are 8 and 64 (aligned paths),
57, 59, 60, 61, 62, and 63 (including widths whose reachable offsets can cross the
ninth byte). Run both orientations. Apply the default no-demonstrated-regression
threshold of 1% to each guard cell versus control, including short counts, and report
every cell separately. Verify exact score bits, count, checksum, and output order for
all paths. Report helper stack usage and tree-owned bytes; no tree-owned-memory increase
is allowed. Keep the common bulk output buffer and all measurement work identical.

Use the EXP-007 frozen control and B artifacts, compiler/flags, fixtures and machine.
Requalify A/A for this candidate schedule, then run serial same-session ABBA with at
least three blocks and retain raw rows and paired effects. A/A must resolve the 1%
guard and 2% primary thresholds; otherwise PARK. If a variant is selected, confirm it
with held-out seeds and a fresh run before advancing to iterator integration. Benchmark
and profile are separate gates: inspect the timed helper's generated code and compare
the dispatch/call overhead and hot instructions; a timing win without supporting
mechanism evidence remains PARKED. The exact frozen commits and run details belong in
the experiment README before any implementation or measurement.

## Risks and falsification

The branch may cost enough on short ranges to erase the scalar savings, while 16 may
be on the wrong side of the crossover. The out-of-line B helper may dominate at counts
near the threshold. Dispatch must not read beyond the leaf, mishandle a width/offset
that spans bytes, change signed-zero or finite-score bits, or reorder outputs. Stack
usage can differ even when tree-owned memory does not. Results are scoped to the tested
architecture and warm-cache helper; they do not establish iterator or whole-tree gains.

Reject this threshold hypothesis if the primary geometric-mean gain is below 2%, any
guard demonstrates more than 1% regression, correctness or sanitizer checks fail, or
the candidate's code profile does not support reduced short-range overhead and useful
bulk work. If the crossover falls at or below 8, above 32, or changes materially by
width/orientation, this fixed-threshold candidate is falsified; record the result and
design a separately preregistered follow-up rather than moving the threshold after
seeing these measurements.
