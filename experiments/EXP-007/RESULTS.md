# Result: strong bulk gain, short-range regressions

**PARK the bulk optimization direction; production selection NONE.** B is the
retained diagnostic candidate, but fails the requirements for an all-range
replacement. This is not merely missing precision: its three losing discovery
guards passed same-cell A/A and regressed in every paired block. No source was
adopted and the scalar iterator was not changed.

Fresh-seed B/control results on Apple M1, Clang 17 O3, one unpinned thread:

| Width | Scores per leaf | Control median ns/score | B median ns/score | Paired median time change | Six-block range |
|---|---:|---:|---:|---:|---:|
| 8 | 96 | 1.432 | 0.821 | -42.78% | -43.60% to -41.92% |
| 60 (primary) | 96 | 1.503 | 1.008 | -33.14% | -33.80% to -32.22% |
| 64 | 96 | 1.438 | 0.820 | -43.02% | -44.02% to -42.90% |
| 60 | 1 | 3.035 | 3.667 | +20.79% | +19.70% to +21.45% |
| 63 | 1 | 3.028 | 3.345 | +10.60% | +9.38% to +10.87% |
| 63 | 7 | 1.999 | 2.130 | +6.49% | +6.29% to +7.52% |

Positive means slower. These are forward physical-orientation cases; full results
include both orientations. Both sides decode into the same-sized output array and
checksum every value. This measures cache-warmed bulk work, not per-call scalar
latency, a public iterator, Redis, or a whole-tree throughput gain.

Discovery primary effects were A -34.62%, B -32.78%, C -27.02%. A/C each had seven
guard medians above +1%; B had three, so the preregistered rule shortlisted B.
Fresh data reproduced the three losses and the large full-leaf gains. Some controls
remain noisy: 13/30 discovery and 25/30 fresh A/A cells fail the all-block ±1% rule.
Fresh primary A/A spans -1.02% to +1.92%, much smaller than the observed 33% gain;
this supports the scoped bulk observation but does not waive guard qualification.
Ranges are observed block ranges, not confidence intervals. No rows were removed.
The count-one fixtures use zero deltas by construction and are seed-invariant;
the fresh phase supplies new measurements, not different input values for those
cells. Longer fixtures do contain seeded deltas.

Mechanism evidence: generated width dispatch is outside per-score loops. Noncrossing
paths omit the ninth-byte scaffold; B's aligned path also omits bit-offset arithmetic.
Nonzero decoding remains scalar; vectorized checksums are common to all variants.
B is outlined while control/A/C inline. That context and call overhead plausibly
contribute to the short-range losses; no counter evidence isolates a sole cause.
Baseline and B external sampling succeeded on the actual release binaries. Baseline
samples fell in warm-up; B spans warm-up and timed iterations. They locate active
bulk decode/checksum code but do not provide comparable timed-only cycle shares.

Discovery took 45.09 seconds for 2880 processes; fresh confirmation took 22.56 seconds
for 1440. Total 4320 serial processes and 557280 measured batches, excluding correctness
and sampling runs. The independent raw reconstruction checks 8640 raw file hashes,
all rows, process statistics, 2160 paired effects and frozen source/binary hashes.
Eight release/sanitizer suites plus 272 boundary-base commands pass. Tree-owned leaf
bytes match; the common 96-double stack buffer is part of this new bulk contract,
not an added production iterator allocation. Compiler stack usage can differ.

Both population steps used three actual independent agents; cross-author semantic
and decision reviews are retained. Fresh timings were run by the same coordinator
on the same machine, not an independent-machine replication. Exact model/cost data
are unavailable. Main source/header hashes are unchanged. Optimization experiment
counts now 0 accepted / 2 rejected / 4 parked; six population rounds, five historical
sequential and one real multi-agent round. All 18 optimization patches remain retained.

Next concrete experiment: a hybrid bulk helper with a scalar path for short ranges
and a specialized path for larger noncrossing ranges. Predeclare counts 2/4/8/16/32/96,
crossing/aligned guards and a held-out confirmation before selecting any threshold.
Keep B frozen as the comparison artifact. Only a guard-passing implementation should
advance to a separately designed scalar iterator integration; no automatic per-leaf
cache or public API change is justified by these results.

Evidence: [discovery](discovery/SUMMARY.md), [confirmation](confirmation/SUMMARY.md),
[selection](implementation-selection.md), [assembly review](profile-results/CODEGEN.md),
[adversarial decision review](review/final-decision.md),
[discovery audit](discovery/AUDIT.json), [fresh audit](confirmation/AUDIT.json).
