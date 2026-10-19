# ARM frontend diagnostic — measured checkpoint

Native baseline controls completed and passed independent raw-data reconstruction.
All six cells qualify: every ABBA block is within ±1%, and every timing window
exceeds 10 ms. The rejected mask candidate remains rejected; no source is adopted.
Comparison and scoped-profile results are still pending.

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
