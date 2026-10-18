# DIAG-005 descriptive results

Six balanced process blocks; all cells use320-byte members. Wall time primary.
Interaction = (ascending/shuffled under coupled queries)/(ascending/shuffled under independent queries).

| Block | Seed | AS ns/op | BS ns/op | AI ns/op | BI ns/op | Coupled ratio | Independent ratio | Interaction |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 211 | 360.003 | 301.342 | 361.677 | 361.736 | 1.194666 | 0.999836 | 1.194861 |
| 2 | 211 | 360.831 | 298.683 | 360.777 | 360.775 | 1.208072 | 1.000005 | 1.208066 |
| 3 | 307 | 361.164 | 300.258 | 362.893 | 361.069 | 1.202848 | 1.005052 | 1.196802 |
| 4 | 307 | 358.921 | 299.658 | 358.092 | 362.792 | 1.197771 | 0.987045 | 1.213492 |
| 5 | 401 | 363.011 | 317.845 | 370.067 | 359.697 | 1.142100 | 1.028829 | 1.110097 |
| 6 | 401 | 359.870 | 299.085 | 360.119 | 362.804 | 1.203239 | 0.992599 | 1.212210 |

Median interaction 1.202434; above one in 6/6 blocks. Fixed criterion met: True.
All48 counts/checksums/structure/fingerprint controls pass. Boundary CPU changes: 33.
Frequency/effective QoS/residency unknown. No causal cache mechanism, source speedup or qualification claimed.
