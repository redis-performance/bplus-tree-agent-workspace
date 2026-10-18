# Fresh-seed guard confirmation

216 fixed rows; wall time primary;3 ABBA blocks/seed;95% t df2. All rows retained.
Guard rejection requires lower bound>1% for BOTH fresh seeds;no tradeoff declared.

| Variant | Mode | Seed | B/A mean % [95% interval] | Controls |
|---|---|---:|---|---|
| A | f-int16-m0 | 9103 | +13.450 [+12.765,+14.135] | True |
| A | f-int16-m0 | 9151 | +13.870 [+11.358,+16.383] | True |
| A | f-int16-m4 | 9103 | -9.966 [-13.546,-6.385] | True |
| A | f-int16-m4 | 9151 | -8.754 [-11.192,-6.317] | True |
| A | f-int16-m7 | 9103 | +3.020 [+0.911,+5.129] | True |
| A | f-int16-m7 | 9151 | +3.392 [+1.998,+4.786] | True |
| B | f-int16-m0 | 9103 | +27.177 [+26.077,+28.276] | True |
| B | f-int16-m0 | 9151 | +26.820 [+25.595,+28.044] | True |
| B | f-int16-m4 | 9103 | -26.032 [-26.390,-25.674] | True |
| B | f-int16-m4 | 9151 | -25.766 [-26.917,-24.615] | True |
| B | f-int16-m7 | 9103 | +14.370 [+9.987,+18.753] | True |
| B | f-int16-m7 | 9151 | +12.731 [+10.047,+15.415] | True |
| C | f-int16-m0 | 9103 | +26.631 [+24.921,+28.341] | True |
| C | f-int16-m0 | 9151 | +27.907 [+24.501,+31.313] | True |
| C | f-int16-m4 | 9103 | -27.431 [-28.758,-26.104] | True |
| C | f-int16-m4 | 9151 | -26.958 [-28.985,-24.932] | True |
| C | f-int16-m7 | 9103 | +13.588 [+12.691,+14.486] | True |
| C | f-int16-m7 | 9151 | +13.101 [+11.408,+14.794] | True |

Decision: REJECT; selection NONE. Same coordinator,not independent confirmation.
