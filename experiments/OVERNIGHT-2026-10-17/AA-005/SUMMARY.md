# AA-005 descriptive control results

Wall time is primary; identical executable A/B.
No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.
These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.

| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |
|---|---:|---|---:|---|---:|---|
| iterate16 | 24 | +0.404 [+0.009, +0.798] | 220.6 | 0.9982–1.0000 | 4 | yes |
| scan16 | 24 | -0.475 [-2.253, +1.303] | 718.1 | 0.9999–1.0000 | 8 | no |
| iterate320 | 24 | +0.021 [-0.454, +0.496] | 221.0 | 0.9992–1.0000 | 5 | yes |
| scan320 | 24 | -0.428 [-1.337, +0.480] | 665.8 | 0.9999–1.0000 | 12 | no |
