# Step 1 chair decision

**Select a one-time per-range crossover:** for non-empty ranges of at most8 scores,
run the original inline scalar decoder loop; for ranges of9 or more, call the frozen
EXP-007 B bulk helper. The source remains an isolated appended helper. The scalar
iterator and public API are outside scope.

Rank A, C, B. A and C independently predict a cutoff below8; C explicitly prioritizes
one-score, seven-score and count-eight edge guards. B proposes16, with a primary at
32/96, but the earlier measured regressions occur at one and seven scores. Its claim
that16 is the right threshold has no direct prior measurement; B's fixed matrix also
makes all three cutoffs indistinguishable on its primary. Preserve B's higher threshold
as dissent, but a crossover closer to the observed short-range failure boundary gives
the current benchmark a falsifiable primary at count16, while preserving bulk work
above8. The predeclared implementation cutoffs are4,8,16; never tune them later.

Geometry crossings (widths59,61,62,63) are not given a special scalar exception.
The tested policy is a simple count threshold. This makes it possible to falsify a
single global crossover if count-seven crossing cases still regress. Do not add a
width table or hybrid policy after observing results.

Proposals were written independently by three actual agents. Shared evidence was
EXP-007's report, codegen and review. The selected hypothesis predicts lower elapsed
time than B at counts1/2/4/7, preserving B's bulk signal at16/32/96. At count8, only
the <=4 variant takes bulk; <=8 and <=16 use scalar. Count16 separates <=8 from <=16.
The primary is width60, forward, count16; secondary primary guard width60, forward,
count96 must retain at least2% gain. All remaining matrix cells are guards.

Chair: /root. Exact backend/model/usage costs for proposers are unavailable. This
selection authorizes only a bounded local diagnostic and does not alter source or
EXP-007's parked decision.
