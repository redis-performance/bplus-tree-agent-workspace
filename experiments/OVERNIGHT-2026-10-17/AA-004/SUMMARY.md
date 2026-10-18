# AA-004 descriptive control results

Wall time is primary; identical executable A/B.
No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.
These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.

| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |
|---|---:|---|---:|---|---:|---|
| hit16 | 24 | -0.977 [-3.039, +1.086] | 1518.3 | 0.9987–1.0000 | 15 | no |
| miss16 | 24 | -0.446 [-1.726, +0.834] | 446.6 | 0.9998–1.0001 | 7 | no |
| hit320 | 24 | +0.213 [-0.651, +1.077] | 1774.6 | 0.9999–1.0000 | 13 | no |
| miss320 | 24 | -0.862 [-4.256, +2.533] | 1079.5 | 0.9999–1.0000 | 12 | no |
