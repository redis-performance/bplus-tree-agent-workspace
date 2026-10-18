# AA-002 descriptive control results

Wall time is primary; identical executable A/B.
No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.
These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.

| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |
|---|---:|---|---:|---|---:|---|
| hit16 | 24 | -0.167 [-1.790, +1.455] | 4788.1 | 0.9992–1.0000 | 20 | no |
| miss16 | 24 | +0.991 [-1.298, +3.280] | 2068.4 | 0.9828–1.0000 | 14 | no |
| rank16 | 24 | +0.149 [-0.199, +0.498] | 2010.7 | 0.9996–1.0000 | 21 | yes |
| hit320 | 24 | -0.558 [-2.284, +1.168] | 2378.8 | 0.9731–1.0000 | 18 | no |
