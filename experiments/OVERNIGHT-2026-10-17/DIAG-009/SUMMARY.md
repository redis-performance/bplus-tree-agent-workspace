# DIAG-009 aggregate timer delivery rates

These are delivered sample counts per thread CPU duration, not exact interarrival intervals.
Wall/thread brackets include sampler boundary overhead; dump occurs after endpoints.

| Block | Rate1000 / rate3001 | Rate17011 / rate1000 |
|---|---:|---:|
| 1 | 1.364467 | 0.236440 |
| 2 | 1.344153 | 0.251989 |
| 3 | 1.491548 | 0.236543 |
| 4 | 1.328347 | 0.251557 |
| 5 | 1.379935 | 0.253734 |
| 6 | 1.350436 | 0.241692 |

All controls: True; fixed hypothesis supported: False.
No GHz inference, source speedup or unbiased profile-share claim.
