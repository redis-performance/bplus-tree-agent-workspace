# DIAG-001 descriptive results

Identical lookup code; process/fixture reuse diagnostic, not speedup or A/A qualification.

| Block | Fresh CV % | Reuse CV % | Reuse/fresh mean | Reuse last/first | Half CV? |
|---|---:|---:|---:|---:|---|
| 1 | 0.487 | 0.549 | 1.0022 | 1.0121 | no |
| 2 | 0.891 | 3.982 | 1.0136 | 1.0046 | no |
| 3 | 1.172 | 0.774 | 1.0107 | 1.0147 | no |
| 4 | 1.955 | 0.693 | 0.9901 | 0.9996 | yes |
| 5 | 0.728 | 0.527 | 1.0038 | 1.0158 | no |
| 6 | 0.633 | 0.515 | 1.0070 | 0.9846 | no |

All 72 windows retained; invariants stable: True. Criterion met in 1/6 blocks; hypothesis supported: False.
Frequency, effective QoS, within-window residency and the causal contribution of each reuse effect remain unknown.
