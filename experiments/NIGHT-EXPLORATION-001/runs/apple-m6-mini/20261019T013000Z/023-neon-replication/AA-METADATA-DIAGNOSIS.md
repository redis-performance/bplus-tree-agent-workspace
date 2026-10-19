# Existing A/A clock and endpoint metadata

No workload ran. The primary wall-clock decision remains PARK; thread time is descriptive and does not qualify or rescue any control.

| Size | Block (zero-based) | Wall difference | Thread-clock difference |
|---:|---:|---:|---:|
| 100,000 | 0 | -0.144456% | -0.145508% |
| 1,000,000 | 0 | -0.855922% | -0.818856% |
| 1,000,000 | 1 | -1.466505% | -1.440359% |
| 100,000 | 1 | -0.139086% | -0.137738% |
| 100,000 | 2 | +0.039017% | +0.037245% |
| 1,000,000 | 2 | +0.807465% | +0.809337% |
| 1,000,000 | 3 | -0.772759% | -0.753726% |
| 100,000 | 3 | -0.161814% | -0.169229% |
| 100,000 | 4 | +0.314195% | +0.298564% |
| 1,000,000 | 4 | +1.641393% | +1.587803% |
| 1,000,000 | 5 | +0.304408% | +0.264510% |
| 100,000 | 5 | -0.050548% | -0.054749% |

20/48 runs have different CPU endpoints. Observed IDs are 6 and 7; endpoints do not establish full residency or the number of migrations. Every QoS endpoint pair is user-interactive/user-interactive.

The same two 1M blocks have thread-clock differences of −1.440359% and +1.587803%. The two clock brackets differ slightly, as documented in the frozen benchmark. These observations establish no frequency, cache, preemption or scheduler cause. No alternative metric gate, count change or retry is proposed.
