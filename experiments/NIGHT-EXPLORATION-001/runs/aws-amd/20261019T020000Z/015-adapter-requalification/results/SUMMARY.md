# Size matrix — x86_64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 409.00 | 375.57 | 365.12 | 389.56 | 695.15 |
| lookup-hit | 24.45 | 31.54 | 46.59 | 74.86 | 311.72 |
| lookup-miss | 14.29 | 16.12 | 20.24 | 36.22 | 179.56 |
| rank | 23.18 | 24.88 | 63.60 | 104.13 | 356.34 |
| iterate | 4.06 | 4.22 | 4.17 | 4.27 | 4.47 |
| scan | 18.93 | 22.64 | 53.22 | 66.97 | 92.85 |
| update | 244.30 | 342.05 | 428.61 | 492.06 | 1082.54 |
| delete | 241.60 | 199.41 | 188.91 | 219.98 | 602.15 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 382.90–538.30 | 12.73% | 0.0383 | yes |
| 100 | lookup-hit | 23.82–25.67 | 2.39% | 23.8248 | no |
| 100 | lookup-miss | 13.85–15.81 | 1.72% | 13.8462 | no |
| 100 | rank | 22.48–23.98 | 1.58% | 22.4790 | no |
| 100 | iterate | 3.78–4.67 | 9.45% | 3.7819 | yes |
| 100 | scan | 17.72–20.34 | 1.61% | 17.7174 | no |
| 100 | update | 239.04–295.44 | 1.38% | 239.0405 | no |
| 100 | delete | 226.90–268.70 | 3.02% | 0.0227 | yes |
| 1000 | insert | 365.47–391.21 | 2.21% | 0.3655 | yes |
| 1000 | lookup-hit | 31.13–32.26 | 2.16% | 31.1269 | no |
| 1000 | lookup-miss | 15.78–16.23 | 0.23% | 15.7775 | no |
| 1000 | rank | 24.41–25.07 | 0.89% | 24.4115 | no |
| 1000 | iterate | 4.16–4.25 | 0.43% | 4.1632 | yes |
| 1000 | scan | 21.96–22.97 | 0.97% | 22.0000 | no |
| 1000 | update | 331.79–404.58 | 1.61% | 331.7945 | no |
| 1000 | delete | 196.98–207.18 | 1.73% | 0.1970 | yes |
| 10000 | insert | 360.95–376.40 | 1.96% | 3.6095 | yes |
| 10000 | lookup-hit | 45.99–48.27 | 1.04% | 45.9904 | no |
| 10000 | lookup-miss | 19.97–20.89 | 1.53% | 19.9726 | no |
| 10000 | rank | 62.52–64.82 | 1.43% | 62.5236 | no |
| 10000 | iterate | 4.16–4.20 | 0.54% | 4.1555 | yes |
| 10000 | scan | 52.91–54.26 | 0.64% | 53.2139 | no |
| 10000 | update | 422.90–432.04 | 0.47% | 422.9022 | no |
| 10000 | delete | 187.51–192.60 | 1.04% | 1.8751 | yes |
| 100000 | insert | 384.42–446.99 | 7.06% | 38.4417 | no |
| 100000 | lookup-hit | 73.82–75.45 | 0.28% | 73.8185 | no |
| 100000 | lookup-miss | 35.65–43.14 | 7.64% | 35.6541 | no |
| 100000 | rank | 103.48–106.27 | 0.95% | 103.4774 | no |
| 100000 | iterate | 4.25–4.32 | 0.78% | 4.2548 | yes |
| 100000 | scan | 66.40–68.13 | 0.91% | 68.0669 | no |
| 100000 | update | 489.73–495.34 | 0.29% | 489.7286 | no |
| 100000 | delete | 217.62–222.81 | 1.36% | 21.7618 | no |
| 1000000 | insert | 689.94–703.51 | 0.75% | 689.9395 | no |
| 1000000 | lookup-hit | 298.90–325.99 | 3.06% | 298.8978 | no |
| 1000000 | lookup-miss | 177.97–189.18 | 2.73% | 177.9651 | no |
| 1000000 | rank | 344.11–368.77 | 2.34% | 344.1132 | no |
| 1000000 | iterate | 4.45–4.59 | 0.89% | 4.4514 | yes |
| 1000000 | scan | 91.06–94.96 | 1.61% | 91.2282 | no |
| 1000000 | update | 1073.27–1098.95 | 0.49% | 1073.2704 | no |
| 1000000 | delete | 576.25–611.11 | 2.38% | 576.2479 | no |
