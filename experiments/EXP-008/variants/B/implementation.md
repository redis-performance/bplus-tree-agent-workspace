# Variant B — scalar through eight scores

This implementation uses the selected one-time count crossover. For `count <= 8`,
it writes each result with the original scalar `zbtScoreLeafScore` decoder. For larger
ranges, it calls the frozen EXP-007 B helper `zbtScoreLeafDecodeRange` once. A zero
count takes the scalar path and performs no writes. It adds no geometry-specific branch,
state, allocation, or public API change.

The scalar loop computes `start + i` for each requested score; as with the referee
helper, callers must provide an in-range span. The bulk path retains the frozen helper's
existing boundary and output semantics. This policy does not establish that eight is a
performance win: count 16 is the separating primary, while counts 1/2/4/7/8 and the
crossing-width cases can falsify the hypothesis.

No builds, correctness runs, profiles, or timings were performed for this proposal
implementation. Exact model/backend and token cost are unknown.
