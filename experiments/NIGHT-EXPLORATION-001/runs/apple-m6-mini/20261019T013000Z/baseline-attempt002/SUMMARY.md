# Size matrix — Apple M6

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 235.00 | 234.50 | 229.30 | 239.51 | 335.40 |
| lookup-hit | 14.23 | 15.13 | 26.61 | 44.66 | 121.45 |
| lookup-miss | 6.29 | 6.63 | 8.46 | 12.14 | 45.60 |
| rank | 13.24 | 14.86 | 35.50 | 64.92 | 208.22 |
| iterate | 1.98 | 2.50 | 2.42 | 2.39 | 2.47 |
| scan | 11.73 | 15.68 | 25.84 | 46.06 | 52.09 |
| update | 133.29 | 179.55 | 293.36 | 332.67 | 577.93 |
| delete | 190.00 | 170.00 | 160.40 | 170.91 | 334.02 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 210.00–770.00 | 51.02% | 0.0210 | yes |
| 100 | lookup-hit | 14.07–20.63 | 19.86% | 14.0750 | no |
| 100 | lookup-miss | 6.01–7.55 | 8.99% | 6.0060 | yes |
| 100 | rank | 13.08–14.35 | 3.66% | 13.0790 | no |
| 100 | iterate | 1.94–2.53 | 9.86% | 1.9360 | yes |
| 100 | scan | 11.16–13.29 | 2.40% | 11.1560 | no |
| 100 | update | 126.39–138.39 | 1.48% | 126.3870 | no |
| 100 | delete | 180.00–250.00 | 13.33% | 0.0180 | yes |
| 1000 | insert | 223.00–264.00 | 7.76% | 0.2230 | yes |
| 1000 | lookup-hit | 14.59–16.17 | 3.20% | 14.5880 | no |
| 1000 | lookup-miss | 6.34–7.16 | 3.97% | 6.3450 | yes |
| 1000 | rank | 14.55–15.59 | 3.40% | 14.5540 | no |
| 1000 | iterate | 2.36–2.69 | 6.07% | 2.3590 | yes |
| 1000 | scan | 15.41–16.00 | 0.97% | 15.4410 | no |
| 1000 | update | 172.36–230.10 | 1.22% | 172.3610 | no |
| 1000 | delete | 161.00–192.00 | 6.49% | 0.1610 | yes |
| 10000 | insert | 221.70–237.00 | 2.75% | 2.2170 | yes |
| 10000 | lookup-hit | 24.84–30.47 | 6.39% | 24.8420 | no |
| 10000 | lookup-miss | 8.19–8.70 | 3.85% | 8.1900 | yes |
| 10000 | rank | 34.20–40.38 | 6.94% | 34.1950 | no |
| 10000 | iterate | 2.36–2.64 | 6.27% | 2.3610 | yes |
| 10000 | scan | 21.52–31.59 | 16.11% | 21.7160 | no |
| 10000 | update | 288.95–297.83 | 0.43% | 288.9510 | no |
| 10000 | delete | 153.20–165.60 | 1.14% | 1.5320 | yes |
| 100000 | insert | 235.22–246.89 | 2.00% | 23.5220 | no |
| 100000 | lookup-hit | 43.74–45.28 | 0.89% | 43.7450 | no |
| 100000 | lookup-miss | 11.82–12.45 | 1.64% | 11.8240 | no |
| 100000 | rank | 62.47–67.06 | 3.43% | 62.4700 | no |
| 100000 | iterate | 2.33–2.65 | 5.85% | 2.3250 | yes |
| 100000 | scan | 45.16–46.82 | 1.30% | 46.2990 | no |
| 100000 | update | 326.65–335.37 | 0.90% | 326.6530 | no |
| 100000 | delete | 165.46–179.40 | 3.59% | 16.5460 | no |
| 1000000 | insert | 329.17–357.14 | 3.10% | 329.1650 | no |
| 1000000 | lookup-hit | 118.70–125.40 | 2.30% | 118.7040 | no |
| 1000000 | lookup-miss | 44.31–48.29 | 1.12% | 44.3130 | no |
| 1000000 | rank | 192.48–216.58 | 4.20% | 192.4810 | no |
| 1000000 | iterate | 2.36–2.69 | 4.47% | 2.3630 | yes |
| 1000000 | scan | 50.34–54.63 | 4.41% | 50.4290 | no |
| 1000000 | update | 569.22–595.56 | 1.60% | 569.2210 | no |
| 1000000 | delete | 329.46–344.76 | 2.24% | 329.4620 | no |
