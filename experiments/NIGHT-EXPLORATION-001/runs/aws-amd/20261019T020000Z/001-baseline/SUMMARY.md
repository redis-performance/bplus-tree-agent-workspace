# Size matrix — x86_64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 402.10 | 368.58 | 359.99 | 385.01 | 700.16 |
| lookup-hit | 24.97 | 32.17 | 45.99 | 71.40 | 296.79 |
| lookup-miss | 13.94 | 15.82 | 19.98 | 35.72 | 179.61 |
| rank | 23.43 | 24.99 | 63.10 | 103.67 | 355.49 |
| iterate | 4.15 | 4.52 | 4.39 | 4.51 | 4.59 |
| scan | 19.40 | 23.46 | 54.89 | 68.40 | 95.60 |
| update | 253.72 | 338.85 | 419.91 | 492.17 | 1099.21 |
| delete | 250.05 | 201.66 | 189.70 | 220.36 | 611.89 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 386.20–458.10 | 4.41% | 0.0386 | yes |
| 100 | lookup-hit | 23.94–25.81 | 1.89% | 23.9376 | no |
| 100 | lookup-miss | 13.60–15.29 | 1.11% | 13.5950 | no |
| 100 | rank | 22.18–24.05 | 2.17% | 22.1825 | no |
| 100 | iterate | 3.82–4.54 | 7.96% | 3.8150 | yes |
| 100 | scan | 18.75–21.34 | 3.57% | 18.7489 | no |
| 100 | update | 247.74–307.41 | 1.43% | 247.7416 | no |
| 100 | delete | 232.40–268.00 | 3.39% | 0.0232 | yes |
| 1000 | insert | 362.29–380.49 | 2.00% | 0.3623 | yes |
| 1000 | lookup-hit | 31.71–33.01 | 1.35% | 31.7146 | no |
| 1000 | lookup-miss | 15.48–15.98 | 0.36% | 15.4791 | no |
| 1000 | rank | 24.51–25.80 | 1.60% | 24.5096 | no |
| 1000 | iterate | 4.43–4.57 | 1.07% | 4.4255 | yes |
| 1000 | scan | 22.83–24.53 | 1.77% | 22.8789 | no |
| 1000 | update | 331.45–390.45 | 1.03% | 331.4514 | no |
| 1000 | delete | 198.02–208.62 | 1.41% | 0.1980 | yes |
| 10000 | insert | 356.26–374.19 | 2.30% | 3.5626 | yes |
| 10000 | lookup-hit | 45.47–47.17 | 1.13% | 45.4706 | no |
| 10000 | lookup-miss | 19.67–20.43 | 1.24% | 19.6718 | no |
| 10000 | rank | 62.28–64.44 | 1.16% | 62.2809 | no |
| 10000 | iterate | 4.36–4.54 | 1.96% | 4.3580 | yes |
| 10000 | scan | 54.31–55.43 | 0.22% | 54.6296 | no |
| 10000 | update | 417.47–427.17 | 0.80% | 417.4701 | no |
| 10000 | delete | 187.80–193.15 | 0.83% | 1.8780 | yes |
| 100000 | insert | 380.90–441.12 | 6.59% | 38.0901 | no |
| 100000 | lookup-hit | 70.64–72.17 | 0.49% | 70.6368 | no |
| 100000 | lookup-miss | 35.13–40.81 | 6.79% | 35.1344 | no |
| 100000 | rank | 102.66–106.21 | 0.65% | 102.6590 | no |
| 100000 | iterate | 4.48–4.67 | 1.64% | 4.4831 | yes |
| 100000 | scan | 67.85–69.65 | 0.96% | 69.5597 | no |
| 100000 | update | 489.52–497.95 | 0.91% | 489.5189 | no |
| 100000 | delete | 218.08–222.91 | 1.17% | 21.8076 | no |
| 1000000 | insert | 691.07–706.24 | 0.87% | 691.0687 | no |
| 1000000 | lookup-hit | 289.04–308.38 | 1.57% | 289.0377 | no |
| 1000000 | lookup-miss | 177.82–188.66 | 2.57% | 177.8176 | no |
| 1000000 | rank | 346.84–375.64 | 2.59% | 346.8377 | no |
| 1000000 | iterate | 4.55–4.71 | 1.36% | 4.5538 | yes |
| 1000000 | scan | 94.14–97.43 | 1.51% | 94.3006 | no |
| 1000000 | update | 1085.07–1122.67 | 0.63% | 1085.0678 | no |
| 1000000 | delete | 556.04–620.68 | 4.83% | 556.0434 | no |
