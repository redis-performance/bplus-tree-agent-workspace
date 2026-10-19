# Size matrix — aarch64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 429.50 | 445.66 | 446.09 | 512.41 | 787.01 |
| lookup-hit | 39.01 | 45.51 | 69.32 | 139.87 | 336.90 |
| lookup-miss | 17.13 | 17.98 | 23.70 | 59.57 | 191.78 |
| rank | 36.75 | 45.84 | 87.13 | 175.64 | 412.77 |
| iterate | 4.57 | 4.76 | 4.66 | 4.81 | 5.14 |
| scan | 27.07 | 36.43 | 63.38 | 84.27 | 112.40 |
| update | 330.28 | 456.40 | 520.51 | 665.28 | 1104.32 |
| delete | 268.94 | 249.92 | 247.98 | 328.82 | 601.81 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 396.00–531.88 | 12.86% | 0.0396 | yes |
| 100 | lookup-hit | 38.88–39.71 | 0.60% | 38.8812 | no |
| 100 | lookup-miss | 16.73–18.63 | 0.19% | 16.7345 | no |
| 100 | rank | 36.60–37.46 | 1.06% | 36.6012 | no |
| 100 | iterate | 4.33–4.74 | 5.81% | 4.3332 | yes |
| 100 | scan | 26.44–29.34 | 0.13% | 26.4419 | no |
| 100 | update | 326.84–381.58 | 0.42% | 326.8375 | no |
| 100 | delete | 245.85–285.98 | 2.37% | 0.0246 | yes |
| 1000 | insert | 436.04–453.54 | 1.77% | 0.4360 | yes |
| 1000 | lookup-hit | 44.97–46.30 | 1.21% | 44.9703 | no |
| 1000 | lookup-miss | 17.61–18.13 | 0.58% | 17.6139 | no |
| 1000 | rank | 44.21–47.01 | 4.94% | 44.2081 | no |
| 1000 | iterate | 4.42–4.89 | 4.89% | 4.4156 | yes |
| 1000 | scan | 34.45–40.21 | 6.51% | 34.5155 | no |
| 1000 | update | 448.54–479.14 | 0.16% | 448.5449 | no |
| 1000 | delete | 247.92–253.67 | 1.07% | 0.2479 | yes |
| 10000 | insert | 443.32–449.81 | 0.59% | 4.4332 | yes |
| 10000 | lookup-hit | 68.65–71.13 | 0.43% | 68.6472 | no |
| 10000 | lookup-miss | 23.58–24.37 | 0.91% | 23.5774 | no |
| 10000 | rank | 85.48–88.44 | 0.50% | 85.4781 | no |
| 10000 | iterate | 4.46–4.81 | 6.69% | 4.4594 | yes |
| 10000 | scan | 63.07–64.36 | 0.33% | 63.4404 | no |
| 10000 | update | 517.70–522.97 | 0.11% | 517.7032 | no |
| 10000 | delete | 246.22–249.98 | 0.28% | 2.4622 | yes |
| 100000 | insert | 510.12–518.88 | 1.00% | 51.0123 | no |
| 100000 | lookup-hit | 137.33–140.87 | 0.54% | 137.3342 | no |
| 100000 | lookup-miss | 58.63–64.81 | 4.65% | 58.6262 | no |
| 100000 | rank | 172.28–178.25 | 0.92% | 172.2751 | no |
| 100000 | iterate | 4.59–4.85 | 2.52% | 4.5943 | yes |
| 100000 | scan | 83.33–85.34 | 1.42% | 85.5182 | no |
| 100000 | update | 663.25–669.07 | 0.28% | 663.2466 | no |
| 100000 | delete | 325.89–330.68 | 0.18% | 32.5891 | no |
| 1000000 | insert | 783.60–823.55 | 2.24% | 783.5966 | no |
| 1000000 | lookup-hit | 333.90–340.93 | 0.64% | 333.8989 | no |
| 1000000 | lookup-miss | 189.48–193.61 | 1.13% | 189.4836 | no |
| 1000000 | rank | 407.28–415.43 | 0.26% | 407.2784 | no |
| 1000000 | iterate | 5.11–5.17 | 0.59% | 5.1091 | yes |
| 1000000 | scan | 111.32–113.93 | 0.82% | 111.5180 | no |
| 1000000 | update | 1097.21–1150.66 | 1.73% | 1097.2125 | no |
| 1000000 | delete | 600.00–615.65 | 1.05% | 600.0028 | no |
