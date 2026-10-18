# AA-003 descriptive control results

Wall time is primary; identical executable A/B.
No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.
These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.

| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |
|---|---:|---|---:|---|---:|---|
| hit16 | 24 | -3.549 [-9.195, +2.097] | 1524.6 | 0.9998–1.0000 | 14 | no |
| miss16 | 24 | +0.210 [-2.215, +2.634] | 453.4 | 0.9999–1.0000 | 11 | no |
| hit320 | 24 | +0.114 [-0.878, +1.107] | 1806.8 | 0.9939–1.0000 | 17 | no |
| miss320 | 24 | -0.001 [-1.993, +1.992] | 1037.4 | 0.9961–1.0000 | 18 | no |
