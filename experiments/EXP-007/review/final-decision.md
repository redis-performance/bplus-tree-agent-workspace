# Cross-author review of selection and interpretation

Reviewer: `/root/proposal_a`, 2026-10-19. I authored A and cross-review the selection
of B. Exact backend/model/token cost remain unknown. No new build, timing, or source
change was performed. This is independent reasoning over the chair's recorded data,
not an independently operated performance confirmation.

Recommendation: **production selection NONE; retain the bulk opportunity as PARK.**
Explicitly record that B fails the broad all-range guard requirement. Calling B a
rejected universal replacement is justified by qualified discovery regressions;
calling the broader bulk-specialization hypothesis disproven is not. If the ledger
supports only one status, PARK accurately preserves the narrower opportunity, but
the decision must not imply that lack of precision is the only obstacle.

## Selection check

The preregistered shortlist ranks passing semantic candidates by fewest guard
median losses greater than 1%, then primary effect. Discovery reports A/B/C at
7/3/7 such losses, so B is the correct diagnostic shortlist even though A has
the largest primary median gain. Fresh confirmation of B therefore follows the
plan and is not post-hoc selection of the prettiest primary result.

I recomputed six-block effects from process summaries for the primary and three
losing B guards in both phases; reported median effects agree. I also checked
eight raw CSV files (1,032 samples): B's two block-zero processes for width60 at
count96/count1 in each phase. Raw medians match the process summaries. The chair
is responsible for the full raw/hash audit. An initial read-only spot-check script
used the wrong row-kind literal `sample`; inspection established the actual kind
`time`, and the corrected read-only check passed. No measurements were rerun.

| Forward B cell | Discovery median effect | Discovery six-block range | Fresh median effect | Fresh six-block range |
|---|---:|---:|---:|---:|
| Width60/count96, primary | -32.78% | -33.45% to -32.26% | -33.14% | -33.80% to -32.22% |
| Width60/count1 | +21.75% | +20.55% to +22.25% | +20.79% | +19.70% to +21.45% |
| Width63/count1 | +9.93% | +9.11% to +13.00% | +10.60% | +9.38% to +10.87% |
| Width63/count7 | +5.89% | +4.82% to +7.29% | +6.49% | +6.29% to +7.52% |

Negative means less elapsed time. Ranges are observed block ranges, not confidence
intervals. The primary is a compelling repeated same-host signal, but its A/A cell
fails the declared strict qualification in both phases. Do not relabel it a fully
qualified accepted 33% gain or pool the 129 within-process samples as replications.

## The guard losses are substantive

Recomputed A/A failure counts are 13/30 discovery cells and 25/30 fresh cells.
However, all three losing B guard cells **pass discovery A/A**: their six-block
ranges are respectively -0.691%..+0.014%, -0.621%..+0.028%, and
-0.901%..+0.986%. Every corresponding B comparison block is more than 4.8%
slower. Those are demonstrated guard failures under this experiment's own
qualification rule. Fresh A/A no longer qualifies these cells, but fresh effects
repeat the adverse direction and similar magnitudes. Later noise does not erase
the qualified earlier failures.

The useful result is consequently conditional: processing a full warmed leaf can
amortize specialization and produce a large signal; applying this helper to every
range damages the measured short-range cases. Function outlining, dispatch,
metadata hoisting, loop generation, and code placement are confounded within B;
the result does not identify dispatch alone as the causal cost or gain.

## Limits and next narrow direction

This experiment materializes an identical double array in control and candidates.
It does not measure the existing scalar iterator, fix EXP-004's mixed-output guard,
or establish whole-tree performance. The host is unpinned M1 with unknown dynamic
frequency/effective QoS and within-window migration. Same-host fresh seeds are not
another machine, compiler, or independently operated run. Static codegen can verify
the intended control flow, but cannot supply hardware-cycle causality. Preserve
all candidate patches and primary/guard data without changing adoption criteria.

The next narrow experiment should test an explicit caller-side crossover policy:
retain the original scalar range loop for short requests and use specialization
for full-leaf requests. Preregister a small count sweep including 1,7,intermediate,
and96 values on both crossing/non-crossing widths, select a threshold only on
discovery, and confirm on fresh seeds/counts. This is a new candidate, not an
amendment that rescues B under the old plan. Avoid claiming that seven is already
the correct threshold or that a public iterator should cache a full leaf. First
establish the bulk crossover; then separately design a caller that can consume it.

Do not rerun the same failed precision schedule indefinitely. The retained primary
signal is strong enough to motivate this distinct bounded experiment; it is not
permission to drop the existing short-range guards or integrate the API now.
