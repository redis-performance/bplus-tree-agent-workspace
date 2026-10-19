# Size matrix — x86_64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 503.68 | 485.53 | 472.53 | 557.98 | 779.74 |
| lookup-hit | 29.89 | 39.73 | 58.08 | 132.10 | 213.14 |
| lookup-miss | 16.08 | 18.51 | 24.03 | 71.19 | 149.40 |
| rank | 26.90 | 37.50 | 78.25 | 173.68 | 297.65 |
| iterate | 4.41 | 4.56 | 4.48 | 4.51 | 5.01 |
| scan | 26.30 | 39.21 | 68.62 | 87.61 | 118.96 |
| update | 336.11 | 510.61 | 562.21 | 734.98 | 1039.10 |
| delete | 282.73 | 243.58 | 236.29 | 354.05 | 571.45 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 481.38–619.93 | 11.78% | 0.0481 | yes |
| 100 | lookup-hit | 29.23–32.07 | 3.64% | 29.2317 | no |
| 100 | lookup-miss | 15.52–17.66 | 1.73% | 15.5198 | no |
| 100 | rank | 26.41–30.11 | 5.01% | 26.4109 | no |
| 100 | iterate | 4.34–5.21 | 6.05% | 4.3446 | yes |
| 100 | scan | 25.11–29.59 | 5.94% | 25.1078 | no |
| 100 | update | 327.41–402.09 | 1.19% | 327.4097 | no |
| 100 | delete | 263.95–323.73 | 8.60% | 0.0264 | yes |
| 1000 | insert | 473.55–495.01 | 1.45% | 0.4735 | yes |
| 1000 | lookup-hit | 38.44–41.17 | 2.94% | 38.4397 | no |
| 1000 | lookup-miss | 17.94–18.92 | 1.14% | 17.9368 | no |
| 1000 | rank | 36.39–39.30 | 4.62% | 36.3927 | no |
| 1000 | iterate | 4.45–4.71 | 4.32% | 4.4513 | yes |
| 1000 | scan | 38.40–41.53 | 2.90% | 38.5161 | no |
| 1000 | update | 502.19–530.31 | 0.95% | 502.1918 | no |
| 1000 | delete | 241.58–247.03 | 0.72% | 0.2416 | yes |
| 10000 | insert | 466.59–481.10 | 1.12% | 4.6659 | yes |
| 10000 | lookup-hit | 57.32–59.05 | 0.54% | 57.3195 | no |
| 10000 | lookup-miss | 23.65–24.51 | 1.29% | 23.6479 | no |
| 10000 | rank | 76.57–78.73 | 0.49% | 76.5737 | no |
| 10000 | iterate | 4.45–4.74 | 2.72% | 4.4482 | yes |
| 10000 | scan | 67.96–69.14 | 0.66% | 68.3556 | no |
| 10000 | update | 558.51–565.05 | 0.16% | 558.5065 | no |
| 10000 | delete | 235.57–239.56 | 0.77% | 2.3557 | yes |
| 100000 | insert | 547.69–630.45 | 7.91% | 54.7691 | no |
| 100000 | lookup-hit | 128.63–137.10 | 1.73% | 128.6294 | no |
| 100000 | lookup-miss | 70.60–75.24 | 3.08% | 70.6044 | no |
| 100000 | rank | 172.42–185.06 | 1.33% | 172.4155 | no |
| 100000 | iterate | 4.48–4.67 | 1.76% | 4.4790 | yes |
| 100000 | scan | 86.63–92.62 | 2.00% | 88.8920 | no |
| 100000 | update | 731.78–741.34 | 0.51% | 731.7847 | no |
| 100000 | delete | 345.19–364.79 | 1.21% | 34.5190 | no |
| 1000000 | insert | 772.08–822.09 | 2.73% | 772.0763 | no |
| 1000000 | lookup-hit | 203.96–217.64 | 0.43% | 203.9558 | no |
| 1000000 | lookup-miss | 148.10–155.53 | 1.99% | 148.1022 | no |
| 1000000 | rank | 295.09–315.94 | 0.58% | 295.0929 | no |
| 1000000 | iterate | 4.99–5.13 | 1.28% | 4.9862 | yes |
| 1000000 | scan | 118.54–119.43 | 0.43% | 118.7368 | no |
| 1000000 | update | 1034.72–1073.03 | 0.42% | 1034.7213 | no |
| 1000000 | delete | 569.34–582.16 | 0.19% | 569.3355 | no |
