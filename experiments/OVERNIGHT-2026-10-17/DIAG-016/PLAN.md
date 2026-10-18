# DIAG-016 — coordinator bookkeeping policy

Preregistered before measurement, round13. One hypothesis: deferring hash/JSON
manifest work from after every predecessor/target pair until after its four-pair
ABBA block attenuates the previously observed predecessor contrast while improving
SAME/SAME placebo precision. This tests the complete coordinator policy, not a
frequency/cache/core mechanism, and cannot qualify a source guard by itself.

Frozen HARNESS-006 binary and original ambient allocator. Target size95, bytes16,
trimmed, forward, alternating-zero, mask6; SAME predecessor identical, OTHER integer
mask0. Each child requests20m items (20000065 effective;210527 traversals), warmup3.
Two policies: pair serialization (hash four files and write cumulative manifest after
each pair), block serialization (same work deferred until all four pairs complete).
Raw child output goes directly to files in both policies. A minimal append-only
pair journal is flushed in both policies for crash recovery. This is not power-loss
durability; no fsync. Precompute all commands/file paths before the warmup. Record
coordinator process CPU and monotonic times at launch/return, both predecessor-to-
target and previous-target-to-next-predecessor gaps, plus timed bookkeeping spans.
Those boundaries include parent subprocess wait return and are NOT actual child exits.
The cumulative manifest grows; order rotates to limit, not eliminate, growth/time
confounding. No row removal or post-hoc normalization by coordinator time.

Fresh seeds47111/47123. Four cells pair-contrast, block-contrast, pair-placebo,
block-placebo; rotate cell order each block and alternate seed order. Six ABBA blocks
per seed/cell. A=SAME, B=OTHER in contrast; both SAME in placebo.192 target +192
predecessor rows, plus one prospective1m target warmup. Child120s/total400s bounds;
fixed schedule; no optional stopping or additions. All agents idle, serial execution,
no build/test/profile overlap. No source/referee change or population is needed.

Wall ns/item primary. Per block effect=100*(meanB/meanA-1), df5 Student-t95% interval.
Thread effects descriptive. For each seed compute paired effect(block)-effect(pair)
interaction with same interval. Support requires all checks/counts/fingerprints/tree
bytes unchanged, all targets>=10ms, both pair-contrast upper bounds<-1%, all block-
contrast and block-placebo bounds within[-1,+1]%, both block contrast means at most
half the corresponding pair contrast magnitude, and interaction lower bounds>1%.
Pair-placebo precision is reported without requirement because existing precision
is unresolved. Manipulation check: median coordinator CPU between steps2..4 decreases
by>=25% in block policy for each seed/protocol (step1 crosses cell boundary).
If any required criterion fails: unsupported; invalid controls: invalid/PARK. No
policy adoption even if supported; requires separately preregistered fresh confirmation.

Backend/model/token cost unknown. Independent reviewer startup failed; sequential
review only. Existing EXP-004 A/PARK and EXP-005 PARK/NONE remain unchanged.
