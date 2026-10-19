# Size matrix — Apple M1

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1K | 10K | 100K |
|---|---:|---:|---:|---:|
| insert | 410.00 | 411.50 | 395.40 | 436.32 |
| lookup-hit | 42.40 | 51.67 | 65.29 | 81.76 |
| lookup-miss | 14.23 | 14.88 | 19.82 | 26.23 |
| rank | 35.68 | 48.41 | 87.37 | 127.19 |
| iterate | 3.95 | 4.52 | 4.44 | 4.51 |
| scan | 23.29 | 40.79 | 60.02 | 71.70 |
| update | 257.29 | 466.05 | 515.88 | 617.52 |
| delete | 340.00 | 273.00 | 269.20 | 316.69 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 390.00–2620.00 | 73.75% | 0.0390 | yes |
| 100 | lookup-hit | 39.62–77.46 | 32.15% | 39.6220 | no |
| 100 | lookup-miss | 13.76–16.12 | 4.00% | 13.7550 | no |
| 100 | rank | 33.20–38.78 | 2.55% | 33.1960 | no |
| 100 | iterate | 3.71–4.22 | 4.86% | 3.7150 | yes |
| 100 | scan | 22.42–25.90 | 2.26% | 22.4170 | no |
| 100 | update | 242.37–263.82 | 2.53% | 242.3700 | no |
| 100 | delete | 290.00–400.00 | 9.72% | 0.0290 | yes |
| 1000 | insert | 401.00–435.00 | 2.61% | 0.4010 | yes |
| 1000 | lookup-hit | 49.94–68.43 | 12.24% | 49.9390 | no |
| 1000 | lookup-miss | 14.31–17.81 | 7.40% | 14.3070 | no |
| 1000 | rank | 45.34–57.27 | 8.93% | 45.3450 | no |
| 1000 | iterate | 4.34–4.99 | 6.65% | 4.3410 | yes |
| 1000 | scan | 34.83–42.58 | 10.86% | 34.8980 | no |
| 1000 | update | 445.71–508.13 | 3.33% | 445.7080 | no |
| 1000 | delete | 266.00–296.00 | 3.85% | 0.2660 | yes |
| 10000 | insert | 387.10–437.80 | 3.89% | 3.8710 | yes |
| 10000 | lookup-hit | 64.39–68.33 | 1.10% | 64.3870 | no |
| 10000 | lookup-miss | 19.31–20.61 | 4.32% | 19.3140 | no |
| 10000 | rank | 85.26–103.44 | 7.99% | 85.2640 | no |
| 10000 | iterate | 4.32–5.02 | 8.67% | 4.3220 | yes |
| 10000 | scan | 58.93–64.37 | 3.70% | 59.2710 | no |
| 10000 | update | 508.10–597.23 | 12.51% | 508.0960 | no |
| 10000 | delete | 261.40–378.80 | 14.23% | 2.6140 | yes |
| 100000 | insert | 419.11–537.22 | 12.35% | 41.9110 | no |
| 100000 | lookup-hit | 78.22–156.74 | 57.67% | 78.2240 | no |
| 100000 | lookup-miss | 24.42–69.45 | 80.53% | 24.4180 | no |
| 100000 | rank | 121.06–226.72 | 41.96% | 121.0550 | no |
| 100000 | iterate | 4.41–4.79 | 1.70% | 4.4120 | yes |
| 100000 | scan | 70.48–82.89 | 6.95% | 72.2530 | no |
| 100000 | update | 607.19–872.80 | 22.60% | 607.1930 | no |
| 100000 | delete | 293.21–576.44 | 31.71% | 29.3210 | no |
