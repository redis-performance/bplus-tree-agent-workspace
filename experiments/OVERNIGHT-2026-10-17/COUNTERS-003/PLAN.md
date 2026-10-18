# COUNTERS-003 — packed iterator fixture path census

Preregistered before new diagnostic output. No speed hypothesis or source candidate.
Use unchanged source from HARNESS-004, base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c
plus explicit uncommitted snapshot. Root source/referee remains unchanged. New diagnostic
includes the tree implementation solely to inspect private leaf layout; no changed tree
code, no instrumented timing comparisons. Original iterator oracle remains unchanged.

Hypothesis: in the existing shuffled integer fixtures, >=99% of elements in EACH of
100000-entry,16/320-byte,seed7103/11213 fixtures use nonzero score widths <=56 bits.
This is a path-coverage hypothesis, not a claim that specialization will improve time.
A future score-decoder hypothesis requires this plus time-profile/codegen evidence.
Reject this coverage hypothesis if any of those four cells fails; do not change threshold.

Fixed census: size4096, seeds7103/11213, encodings integer/fraction/wide/zero,
construction shuffled/ascending/descending, member lengths16/253/254/255/319/320:
144 fixtures; plus size100000, both seeds, all four encodings, shuffled, lengths16/320:
16 fixtures. All160 fixtures run release/debug and ASan/UBSan,serial,120s child limit.
Do not use census durations as performance data. No optional stopping/exclusions.

For every fixture: unchanged full byte/order/exact score-bit oracle in both directions
and all eight optional-output masks; leaf/element totals; ordered-value reconstruction
using an independent bit-at-a-time decoder; exact memory retained through traversal.
Report element-weighted width/shift/reversed/record-kind histograms, cross-word reads,
leaf count and leaf-boundary frequency. Counts are structural potential-path coverage,
not executed branch profiles. Keep raw JSON/stdout/stderr,commands,source/binary hashes.

Prior sampled-PC profiles establish iterator symbol concentration, but do not attribute
cost to score decoding. No cache/cycle/frequency claims; scheduling/frequency unknown.
Reviewer agent failed before startup this round; sequential review only, exact backend/
model/token cost unknown. No acceptance, commits or network publication in this round.
