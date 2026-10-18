# DIAG-003 descriptive results

Wall time primary; six process blocks, two windows/arm/block. Local diagnostic only.

| Block | R ns/op | I ns/op | R/I | R CV | I CV |
|---|---:|---:|---:|---:|---:|
| 1 | 72.637 | 72.945 | 0.995778 | 0.5712% | 0.2319% |
| 2 | 73.220 | 73.630 | 0.994437 | 0.7842% | 1.6395% |
| 3 | 73.753 | 76.755 | 0.960894 | 0.3597% | 7.7124% |
| 4 | 72.202 | 72.889 | 0.990580 | 0.3561% | 1.4738% |
| 5 | 72.763 | 72.647 | 1.001609 | 0.3759% | 0.1929% |
| 6 | 73.445 | 72.998 | 1.006118 | 0.5915% | 0.7846% |

Median R/I: 0.995107; R lower in 4/6 blocks. Fixed criterion met: False.
24/24 checked rows; tree bytes 2984176; opaque boundary CPU changes 7.
Clock/effective QoS/residency unknown; no causal cache/frequency or portable speed claim.
