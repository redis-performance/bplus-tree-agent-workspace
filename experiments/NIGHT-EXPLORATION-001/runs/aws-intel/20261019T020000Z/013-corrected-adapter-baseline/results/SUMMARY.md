# Size matrix — x86_64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 497.57 | 480.98 | 470.56 | 558.93 | 781.57 |
| lookup-hit | 31.00 | 40.28 | 59.46 | 134.38 | 219.08 |
| lookup-miss | 16.18 | 18.51 | 23.94 | 71.54 | 149.16 |
| rank | 27.09 | 38.52 | 78.49 | 174.79 | 301.96 |
| iterate | 4.04 | 4.07 | 4.05 | 4.14 | 4.57 |
| scan | 23.91 | 35.31 | 67.09 | 86.44 | 116.55 |
| update | 329.13 | 513.88 | 557.48 | 729.79 | 1037.70 |
| delete | 273.45 | 238.29 | 232.11 | 350.16 | 557.22 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 476.37–566.22 | 5.46% | 0.0476 | yes |
| 100 | lookup-hit | 30.60–33.38 | 1.78% | 30.6011 | no |
| 100 | lookup-miss | 15.48–19.23 | 8.10% | 15.4798 | no |
| 100 | rank | 26.60–30.54 | 6.05% | 26.6046 | no |
| 100 | iterate | 3.92–4.75 | 3.11% | 3.9250 | yes |
| 100 | scan | 22.52–26.55 | 2.20% | 22.5216 | no |
| 100 | update | 318.72–396.81 | 1.00% | 318.7226 | no |
| 100 | delete | 250.14–316.82 | 6.84% | 0.0250 | yes |
| 1000 | insert | 471.44–492.33 | 1.40% | 0.4714 | yes |
| 1000 | lookup-hit | 39.40–41.73 | 1.15% | 39.3955 | no |
| 1000 | lookup-miss | 18.04–18.70 | 0.79% | 18.0445 | no |
| 1000 | rank | 36.61–40.67 | 2.35% | 36.6062 | no |
| 1000 | iterate | 3.96–4.38 | 3.99% | 3.9601 | yes |
| 1000 | scan | 33.00–38.28 | 4.50% | 33.0967 | no |
| 1000 | update | 506.58–529.84 | 0.45% | 506.5842 | no |
| 1000 | delete | 236.62–242.42 | 0.93% | 0.2366 | yes |
| 10000 | insert | 465.70–489.37 | 1.49% | 4.6570 | yes |
| 10000 | lookup-hit | 58.60–60.40 | 0.43% | 58.6044 | no |
| 10000 | lookup-miss | 23.78–25.28 | 2.64% | 23.7833 | no |
| 10000 | rank | 76.66–79.93 | 0.67% | 76.6567 | no |
| 10000 | iterate | 3.98–4.94 | 11.92% | 3.9777 | yes |
| 10000 | scan | 66.57–68.02 | 1.05% | 67.1051 | no |
| 10000 | update | 553.68–562.21 | 0.74% | 553.6806 | no |
| 10000 | delete | 230.80–236.03 | 0.66% | 2.3080 | yes |
| 100000 | insert | 544.75–644.68 | 6.75% | 54.4750 | no |
| 100000 | lookup-hit | 130.94–147.23 | 5.68% | 130.9435 | no |
| 100000 | lookup-miss | 71.12–74.97 | 2.07% | 71.1159 | no |
| 100000 | rank | 173.79–182.18 | 2.92% | 173.7937 | no |
| 100000 | iterate | 4.02–4.23 | 0.55% | 4.0173 | yes |
| 100000 | scan | 85.32–100.48 | 9.15% | 87.4682 | no |
| 100000 | update | 728.05–764.86 | 2.63% | 728.0516 | no |
| 100000 | delete | 341.09–378.60 | 4.50% | 34.1095 | no |
| 1000000 | insert | 770.75–797.67 | 2.35% | 770.7528 | no |
| 1000000 | lookup-hit | 209.09–221.31 | 0.39% | 209.0917 | no |
| 1000000 | lookup-miss | 148.30–156.45 | 1.75% | 148.3001 | no |
| 1000000 | rank | 299.51–319.12 | 0.41% | 299.5126 | no |
| 1000000 | iterate | 4.53–4.75 | 4.05% | 4.5302 | yes |
| 1000000 | scan | 116.21–117.05 | 0.23% | 116.4247 | no |
| 1000000 | update | 1034.02–1065.15 | 0.43% | 1034.0219 | no |
| 1000000 | delete | 555.58–567.91 | 0.61% | 555.5783 | no |
