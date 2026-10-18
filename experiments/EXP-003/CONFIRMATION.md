# Fresh-seed guard confirmation

216 fixed rows; wall time primary;3 ABBA blocks/seed;95% t df2. All rows retained.
Guard rejection requires lower bound>1% for BOTH fresh seeds;no tradeoff declared.

| Variant | Mode | Seed | B/A mean % [95% interval] | Controls |
|---|---|---:|---|---|
| A | f-int16-m0 | 10103 | -0.044 [-0.731,+0.643] | True |
| A | f-int16-m0 | 10111 | -0.003 [-0.186,+0.180] | True |
| A | f-int16-m4 | 10103 | -6.070 [-6.630,-5.510] | True |
| A | f-int16-m4 | 10111 | -5.785 [-6.170,-5.401] | True |
| A | f-int16-m7 | 10103 | +46.183 [+37.696,+54.670] | True |
| A | f-int16-m7 | 10111 | +41.046 [+40.852,+41.240] | True |
| B | f-int16-m0 | 10103 | +0.097 [-0.108,+0.301] | True |
| B | f-int16-m0 | 10111 | +0.095 [-1.171,+1.361] | True |
| B | f-int16-m4 | 10103 | -7.026 [-7.607,-6.444] | True |
| B | f-int16-m4 | 10111 | -7.156 [-8.021,-6.291] | True |
| B | f-int16-m7 | 10103 | +9.537 [+8.582,+10.491] | True |
| B | f-int16-m7 | 10111 | +9.383 [+8.117,+10.648] | True |
| C | f-int16-m0 | 10103 | -0.104 [-0.505,+0.297] | True |
| C | f-int16-m0 | 10111 | -0.053 [-0.896,+0.791] | True |
| C | f-int16-m4 | 10103 | -5.651 [-8.472,-2.830] | True |
| C | f-int16-m4 | 10111 | -5.657 [-6.458,-4.856] | True |
| C | f-int16-m7 | 10103 | +17.050 [+16.373,+17.728] | True |
| C | f-int16-m7 | 10111 | +16.860 [+15.989,+17.730] | True |

Decision: REJECT; selection NONE. Same coordinator,not independent confirmation.
