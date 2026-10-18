# AA-007 — wall-time precision

Fixed six-block A/A; all rows retained. 95% t intervals assume independent normal block effects.
Frequency, effective QoS and within-window placement unknown. No source speed claim.

| Cell | Rows | B/A mean % [95% interval] | Qualified |
|---|---:|---|---|
| f-int16-m0 | 24 | -0.059 [-0.383,+0.266] | True |
| f-int16-m1 | 24 | +0.806 [-0.938,+2.551] | False |
| f-int16-m4 | 24 | -0.086 [-0.255,+0.084] | True |
| f-int16-m7 | 24 | +0.024 [-0.443,+0.492] | True |
| r-int16-m4 | 24 | -0.607 [-1.282,+0.067] | False |
| r-int16-m7 | 24 | -0.639 [-1.678,+0.400] | False |
| f-frac320-m7 | 24 | -0.046 [-1.261,+1.168] | False |
| r-wide320-m7 | 24 | -0.286 [-0.689,+0.117] | True |
| f-frac320-m4 | 24 | +0.332 [+0.022,+0.641] | True |
| f-wide320-m4 | 24 | -0.038 [-0.577,+0.500] | True |
