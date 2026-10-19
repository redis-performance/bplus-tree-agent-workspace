# ARM frontend diagnostic — measured checkpoint

Fresh measurements reproduce the opposing frontend results. The primary improves,
but all four selected guard cases regress in every ABBA block. All six baseline
cells qualify, so these guard losses are demonstrated regressions. The rejected
mask candidate remains rejected; no source is adopted. Matched profiles are now
granted under a separate fixed cap; their results are pending.

## Fresh native controls

Exact historical binaries, CPU2, seeds1601–1603 repeated twice, six ABBA blocks per
cell. All144 processes completed in91.589 seconds. Root verified297 sealed files,
exact source/binary identities, checksum and tree-owned memory joins, and the
separate post-run idle proof. Intel independently reconstructed the same outcome.

| Frontend / direction / size | Largest absolute A/A effect | Shortest window | Qualification |
|---|---:|---:|---|
| primary-forward-100000 | 0.690% | 166.363 ms | PASS |
| primary-forward-1000000 | 0.369% | 186.611 ms | PASS |
| h4-forward-100000 | 0.233% | 64.721 ms | PASS |
| h4-forward-1000000 | 0.552% | 72.563 ms | PASS |
| h4-reverse-100000 | 0.844% | 62.676 ms | PASS |
| h4-reverse-1000000 | 0.403% | 74.581 ms | PASS |

[Root raw audit](NATIVE-AA-ROOT-AUDIT.json) ·
[Immutable operator evidence](https://github.com/redis-performance/bplus-tree-agent-workspace/tree/70103fb6a/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/030-frontend-diagnosis).

## Exact native comparison

Same-session baseline/A ABBA with the same fresh seeds and exact historical binaries.
All 144 comparison runs completed; root and independent Intel06a776000 reconstructed
every row, baseline join, checksum, tree-owned memory and source/binary identity.
The separate post-run check found the runner idle with protected identities intact.

| Frontend / direction / size | Median elapsed change | All six blocks | Qualified A/A |
|---|---:|---|---|
| primary-forward-100000 | -7.775% | -7.786% to -6.972% | PASS |
| primary-forward-1000000 | -7.194% | -7.455% to -6.896% | PASS |
| h4-forward-100000 | +2.903% | +2.770% to +2.943% | PASS |
| h4-forward-1000000 | +2.953% | +2.628% to +3.245% | PASS |
| h4-reverse-100000 | +8.431% | +8.077% to +8.473% | PASS |
| h4-reverse-1000000 | +3.141% | +2.552% to +3.277% | PASS |

Negative means faster; positive means slower. These are scoped frontend comparisons,
not an architecture ranking or a causal explanation.

![Fresh native controls and exact-mask comparison](charts/native-frontend-comparison.png)

[Comparison raw audit](NATIVE-COMPARISON-ROOT-AUDIT.json) ·
[Independent comparison review](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/06a776000/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/031-arm-native-raw-review/native-comparison-121e9643a/REVIEW.md).

## Interpretation limits

The primary and guard frontends have different score distributions, checksum
consumers, warm-up, allocation histories and requested visits. Their effects are
reported separately. Assembly confirms the guard's mask selection already occurs
outside its repeated loop; this rules out that particular per-visit branch premise,
not the other possible causes. Actual IteratorNext bodies contain114 instructions
in control and113 in the candidate; static counts do not measure dynamic work.

The preregistered profile will test whether retired instructions decrease for all
18 paired fixtures. Any valid non-decrease falsifies that universal direction;
invalid or missing counters make it inconclusive. Timing attribution additionally
requires own instrumentation controls and exact code/scope validation. No favorable
counter direction can waive the earlier qualified guard regressions.

The [actual cpu-perf MCP consultation](CPU-PERF-CONSULTATION.json) returned reference
leads but no source passages; the Arm manual was unavailable to its fetcher. Its
heuristic metadata audit is not a replacement for raw-data verification. Frequency,
DVFS/turbo and SMT observations during these windows remain unknown. No vendor
mechanism or portable performance claim is inferred from these results.
