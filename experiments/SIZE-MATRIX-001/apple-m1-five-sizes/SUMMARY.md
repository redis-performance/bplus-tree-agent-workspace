# Size matrix — Apple M1

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 415.00 | 412.00 | 398.65 | 436.87 | 733.75 |
| lookup-hit | 42.80 | 51.88 | 65.78 | 83.93 | 259.18 |
| lookup-miss | 14.44 | 15.12 | 19.85 | 26.11 | 113.56 |
| rank | 35.54 | 47.77 | 87.30 | 126.82 | 439.36 |
| iterate | 3.96 | 4.53 | 4.43 | 4.51 | 4.80 |
| scan | 23.50 | 39.20 | 60.65 | 72.21 | 130.88 |
| update | 259.76 | 465.18 | 520.10 | 630.56 | 1149.43 |
| delete | 310.00 | 275.00 | 270.25 | 310.25 | 699.15 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 400.00–1290.00 | 52.35% | 0.0400 | yes |
| 100 | lookup-hit | 40.40–50.02 | 10.26% | 40.4020 | no |
| 100 | lookup-miss | 13.89–16.08 | 2.32% | 13.8940 | no |
| 100 | rank | 33.94–38.21 | 3.48% | 33.9370 | no |
| 100 | iterate | 3.79–4.24 | 2.78% | 3.7870 | yes |
| 100 | scan | 22.94–25.44 | 1.24% | 22.9380 | no |
| 100 | update | 241.64–265.90 | 0.54% | 241.6400 | no |
| 100 | delete | 290.00–450.00 | 22.58% | 0.0290 | yes |
| 1000 | insert | 407.00–433.00 | 3.21% | 0.4070 | yes |
| 1000 | lookup-hit | 51.10–52.91 | 1.91% | 51.1050 | no |
| 1000 | lookup-miss | 14.63–15.65 | 1.99% | 14.6300 | no |
| 1000 | rank | 43.83–53.00 | 7.71% | 43.8290 | no |
| 1000 | iterate | 4.42–4.79 | 2.49% | 4.4250 | yes |
| 1000 | scan | 34.95–42.66 | 8.43% | 35.0190 | no |
| 1000 | update | 445.62–529.05 | 6.80% | 445.6240 | no |
| 1000 | delete | 268.00–298.00 | 4.04% | 0.2680 | yes |
| 10000 | insert | 393.10–533.90 | 10.31% | 3.9310 | yes |
| 10000 | lookup-hit | 64.98–87.46 | 4.16% | 64.9830 | no |
| 10000 | lookup-miss | 19.68–22.70 | 3.39% | 19.6830 | no |
| 10000 | rank | 85.95–93.68 | 3.44% | 85.9500 | no |
| 10000 | iterate | 4.39–4.59 | 2.23% | 4.3910 | yes |
| 10000 | scan | 59.79–63.16 | 2.50% | 60.1370 | no |
| 10000 | update | 513.63–594.04 | 10.91% | 513.6330 | no |
| 10000 | delete | 266.90–400.40 | 16.15% | 2.6690 | yes |
| 100000 | insert | 421.28–558.00 | 9.39% | 42.1280 | no |
| 100000 | lookup-hit | 79.11–178.56 | 30.64% | 79.1120 | no |
| 100000 | lookup-miss | 24.56–64.15 | 54.45% | 24.5610 | no |
| 100000 | rank | 117.38–256.55 | 46.01% | 117.3830 | no |
| 100000 | iterate | 4.49–4.87 | 4.63% | 4.4860 | yes |
| 100000 | scan | 71.63–86.54 | 14.18% | 73.5050 | no |
| 100000 | update | 598.85–926.94 | 13.43% | 598.8460 | no |
| 100000 | delete | 294.55–527.66 | 12.82% | 29.4550 | no |
| 1000000 | insert | 703.17–1043.19 | 14.61% | 703.1670 | no |
| 1000000 | lookup-hit | 248.61–285.51 | 7.07% | 248.6110 | no |
| 1000000 | lookup-miss | 110.12–163.15 | 19.04% | 110.1160 | no |
| 1000000 | rank | 420.18–564.74 | 23.16% | 420.1780 | no |
| 1000000 | iterate | 4.74–5.53 | 7.36% | 4.7370 | yes |
| 1000000 | scan | 120.85–197.48 | 30.83% | 121.0540 | no |
| 1000000 | update | 1110.42–1621.99 | 21.65% | 1110.4230 | no |
| 1000000 | delete | 667.28–1079.58 | 26.05% | 667.2820 | no |
