# EXP-005 width-mask screening

All rows retained; wall time primary. 95% t intervals across3 ABBA blocks (df2).
Unqualified modes diagnostic only. Frequency/effective QoS/within-window residency unknown.

| Variant | Mode | Qualified | Mean B/A % [95% interval] | Controls | Demonstrated regression |
|---|---|---|---|---|---|
| A | f-int16-m0 | True | +0.131 [-0.255,+0.517] | True | False |
| A | f-int16-m2 | False | -0.213 [-0.496,+0.070] | True | False |
| A | f-int16-m4 | True | -2.008 [-3.983,-0.033] | True | False |
| A | f-int16-m6 | False | +2.203 [+1.045,+3.360] | True | False |
| A | f-int16-m7 | True | -0.491 [-0.907,-0.075] | True | False |
| B | f-int16-m0 | True | +0.042 [-0.542,+0.626] | True | False |
| B | f-int16-m2 | False | +0.088 [-0.437,+0.613] | True | False |
| B | f-int16-m4 | True | -0.791 [-1.771,+0.188] | True | False |
| B | f-int16-m6 | False | -1.139 [-1.479,-0.799] | True | False |
| B | f-int16-m7 | True | -0.378 [-1.120,+0.363] | True | False |
| C | f-int16-m0 | True | -0.069 [-0.222,+0.085] | True | False |
| C | f-int16-m2 | False | +0.424 [-1.694,+2.543] | True | False |
| C | f-int16-m4 | True | -3.030 [-3.233,-2.826] | True | False |
| C | f-int16-m6 | False | +1.741 [+1.527,+1.954] | True | False |
| C | f-int16-m7 | True | -0.767 [-0.833,-0.700] | True | False |

Expanded preference: C. No source acceptance.
