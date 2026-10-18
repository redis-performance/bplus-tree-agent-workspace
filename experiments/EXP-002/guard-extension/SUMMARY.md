# EXP-002 expanded guards

All rows retained; wall time primary. 95% t intervals across3 ABBA blocks (df2).
Unqualified modes diagnostic only. Frequency/effective QoS/within-window residency unknown.

| Variant | Mode | Qualified | Mean B/A % [95% interval] | Controls | Demonstrated regression |
|---|---|---|---|---|---|
| A | f-int16-m0 | True | +13.439 [+13.182,+13.696] | True | True |
| A | f-int16-m1 | True | +0.358 [-0.584,+1.301] | True | False |
| A | f-int16-m2 | False | +3.760 [+2.788,+4.731] | True | False |
| A | f-int16-m3 | False | +3.096 [-0.094,+6.286] | True | False |
| A | f-int16-m4 | True | -10.509 [-11.056,-9.961] | True | False |
| A | f-int16-m5 | False | +5.833 [+2.848,+8.818] | True | False |
| A | f-int16-m6 | False | +2.215 [+0.553,+3.878] | True | False |
| A | f-int16-m7 | True | +3.554 [+3.244,+3.864] | True | True |
| A | r-int16-m4 | True | +62.636 [-54.999,+180.272] | True | False |
| A | r-int16-m7 | True | +1.993 [+1.360,+2.626] | True | True |
| A | f-frac320-m7 | True | -4.149 [-20.845,+12.546] | True | False |
| A | r-wide320-m7 | True | +1.116 [-4.211,+6.443] | True | False |
| A | f-frac320-m4 | True | -10.863 [-11.306,-10.421] | True | False |
| A | f-wide320-m4 | True | -10.686 [-10.805,-10.568] | True | False |
| B | f-int16-m0 | True | +27.145 [+27.057,+27.233] | True | True |
| B | f-int16-m1 | True | +18.237 [+16.185,+20.288] | True | True |
| B | f-int16-m2 | False | +14.703 [+14.466,+14.939] | True | False |
| B | f-int16-m3 | False | +15.519 [+10.969,+20.069] | True | False |
| B | f-int16-m4 | True | -25.302 [-32.769,-17.834] | True | False |
| B | f-int16-m5 | False | +5.470 [+4.384,+6.556] | True | False |
| B | f-int16-m6 | False | -5.274 [-8.078,-2.471] | True | False |
| B | f-int16-m7 | True | +13.365 [+12.687,+14.043] | True | True |
| B | r-int16-m4 | True | +17.665 [+17.540,+17.791] | True | True |
| B | r-int16-m7 | True | +0.927 [+0.599,+1.255] | True | False |
| B | f-frac320-m7 | True | -0.461 [-2.373,+1.451] | True | False |
| B | r-wide320-m7 | True | -0.176 [-5.807,+5.455] | True | False |
| B | f-frac320-m4 | True | -27.739 [-30.045,-25.432] | True | False |
| B | f-wide320-m4 | True | -26.842 [-27.505,-26.178] | True | False |
| C | f-int16-m0 | True | +27.076 [+26.544,+27.608] | True | True |
| C | f-int16-m1 | True | +18.774 [+18.466,+19.081] | True | True |
| C | f-int16-m2 | False | +15.081 [+14.804,+15.359] | True | False |
| C | f-int16-m3 | False | +15.475 [+14.262,+16.688] | True | False |
| C | f-int16-m4 | True | -27.950 [-28.525,-27.375] | True | False |
| C | f-int16-m5 | False | +5.458 [+2.598,+8.317] | True | False |
| C | f-int16-m6 | False | -5.104 [-5.282,-4.927] | True | False |
| C | f-int16-m7 | True | +14.166 [+11.309,+17.023] | True | True |
| C | r-int16-m4 | True | +17.357 [+16.951,+17.764] | True | True |
| C | r-int16-m7 | True | +0.904 [+0.465,+1.344] | True | False |
| C | f-frac320-m7 | True | +0.300 [-3.090,+3.690] | True | False |
| C | r-wide320-m7 | True | +0.397 [-1.175,+1.970] | True | False |
| C | f-frac320-m4 | True | -27.865 [-29.956,-25.773] | True | False |
| C | f-wide320-m4 | True | -28.316 [-28.989,-27.643] | True | False |

Expanded preference: NONE. No source acceptance.
