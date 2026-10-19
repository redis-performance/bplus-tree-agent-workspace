# Size matrix — unknown (sysctl unavailable)

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 425.00 | 419.00 | 400.00 | 489.02 | 814.90 |
| lookup-hit | 43.26 | 52.25 | 66.37 | 121.26 | 293.74 |
| lookup-miss | 14.50 | 15.54 | 20.11 | 36.60 | 128.65 |
| rank | 35.95 | 46.88 | 88.56 | 178.24 | 480.32 |
| iterate | 4.04 | 4.57 | 4.51 | 4.58 | 4.86 |
| scan | 23.34 | 37.72 | 61.59 | 75.24 | 153.10 |
| update | 258.99 | 461.65 | 529.84 | 733.07 | 1277.59 |
| delete | 310.00 | 276.00 | 271.80 | 383.79 | 763.82 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 400.00–2070.00 | 65.74% | 0.0400 | yes |
| 100 | lookup-hit | 40.38–75.45 | 28.96% | 40.3820 | no |
| 100 | lookup-miss | 13.88–16.80 | 2.39% | 13.8770 | no |
| 100 | rank | 34.21–38.99 | 1.45% | 34.2100 | no |
| 100 | iterate | 3.78–4.30 | 3.54% | 3.7830 | yes |
| 100 | scan | 23.00–25.91 | 0.85% | 23.0050 | no |
| 100 | update | 246.49–273.08 | 1.89% | 246.4870 | no |
| 100 | delete | 280.00–450.00 | 11.43% | 0.0280 | yes |
| 1000 | insert | 408.00–462.00 | 4.37% | 0.4080 | yes |
| 1000 | lookup-hit | 50.92–58.80 | 4.82% | 50.9180 | no |
| 1000 | lookup-miss | 15.08–16.54 | 4.82% | 15.0820 | no |
| 1000 | rank | 44.53–54.58 | 10.35% | 44.5260 | no |
| 1000 | iterate | 4.43–5.22 | 5.47% | 4.4310 | yes |
| 1000 | scan | 33.78–41.49 | 8.96% | 33.8430 | no |
| 1000 | update | 450.79–517.82 | 3.18% | 450.7890 | no |
| 1000 | delete | 268.00–300.00 | 2.79% | 0.2680 | yes |
| 10000 | insert | 392.10–488.30 | 11.03% | 3.9210 | yes |
| 10000 | lookup-hit | 65.12–85.16 | 10.46% | 65.1160 | no |
| 10000 | lookup-miss | 19.69–23.39 | 7.79% | 19.6930 | no |
| 10000 | rank | 86.46–174.24 | 31.47% | 86.4570 | no |
| 10000 | iterate | 4.41–5.11 | 8.41% | 4.4060 | yes |
| 10000 | scan | 60.35–153.19 | 43.91% | 60.7140 | no |
| 10000 | update | 517.34–674.75 | 8.93% | 517.3410 | no |
| 10000 | delete | 267.50–339.60 | 10.31% | 2.6750 | yes |
| 100000 | insert | 424.29–1031.61 | 48.55% | 42.4290 | no |
| 100000 | lookup-hit | 79.86–348.55 | 29.21% | 79.8550 | no |
| 100000 | lookup-miss | 24.90–114.91 | 40.64% | 24.8970 | no |
| 100000 | rank | 121.50–420.87 | 73.05% | 121.5040 | no |
| 100000 | iterate | 4.50–5.19 | 7.57% | 4.5010 | yes |
| 100000 | scan | 72.22–107.91 | 28.34% | 74.0370 | no |
| 100000 | update | 632.99–1209.35 | 17.46% | 632.9940 | no |
| 100000 | delete | 301.87–1230.07 | 45.49% | 30.1870 | no |
| 1000000 | insert | 739.86–964.07 | 6.16% | 739.8560 | no |
| 1000000 | lookup-hit | 265.82–331.76 | 11.10% | 265.8230 | no |
| 1000000 | lookup-miss | 117.70–156.64 | 10.62% | 117.7040 | no |
| 1000000 | rank | 451.01–533.10 | 5.12% | 451.0150 | no |
| 1000000 | iterate | 4.76–5.18 | 2.57% | 4.7620 | yes |
| 1000000 | scan | 133.50–222.83 | 24.89% | 133.7450 | no |
| 1000000 | update | 1155.53–1396.10 | 4.52% | 1155.5250 | no |
| 1000000 | delete | 714.01–1139.31 | 21.56% | 714.0120 | no |
