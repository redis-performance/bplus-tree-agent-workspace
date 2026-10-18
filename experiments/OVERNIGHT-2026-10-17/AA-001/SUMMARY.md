# AA-001 descriptive control results

Wall time is primary; identical executable A/B.
No rows removed. 95% Student-t intervals across six ABBA block effects (df=5); independence/normality assumed.
These are local precision controls, not speedups. Frequency/effective QoS and within-window residency unknown.

| Cell | Rows | B/A mean % [95% interval] | Min wall ms | CPU/wall min–max | Boundary IDs differ | Qualified |
|---|---:|---|---:|---|---:|---|
| hit16 | 24 | +0.378 [-1.721, +2.477] | 1519.1 | 0.9999–1.0000 | 12 | no |
| hit320 | 24 | -0.571 [-1.305, +0.162] | 1465.8 | 0.9997–1.0000 | 13 | no |
| miss16 | 24 | -0.120 [-2.552, +2.312] | 449.5 | 0.9989–1.0000 | 7 | no |
| rank16 | 24 | +1.661 [-0.632, +3.954] | 565.5 | 0.9998–1.0000 | 12 | no |
| iterate16 | 24 | +0.017 [-0.073, +0.107] | 220.5 | 1.0000–1.0000 | 3 | yes |
| scan16 | 24 | +0.197 [-0.580, +0.975] | 358.6 | 1.0000–1.0000 | 1 | yes |
| update16 | 24 | +4.602 [-5.182, +14.385] | 558.2 | 0.9999–1.0000 | 13 | no |
| hit321 | 24 | -0.710 [-2.720, +1.300] | 1496.6 | 0.9999–1.0000 | 17 | no |
