# Size matrix — Apple M6

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 225.00 | 227.00 | 222.65 | 234.32 | 328.24 |
| lookup-hit | 14.68 | 15.59 | 25.91 | 45.10 | 122.86 |
| lookup-miss | 6.40 | 6.59 | 8.50 | 12.29 | 45.49 |
| rank | 13.42 | 15.00 | 36.29 | 65.49 | 212.00 |
| iterate | 2.02 | 2.24 | 2.20 | 2.15 | 2.22 |
| scan | 11.78 | 15.68 | 25.22 | 46.28 | 52.39 |
| update | 125.84 | 167.70 | 283.21 | 325.00 | 568.73 |
| delete | 205.00 | 167.00 | 157.90 | 169.34 | 330.73 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 210.00–1000.00 | 62.30% | 0.0210 | yes |
| 100 | lookup-hit | 14.49–25.55 | 27.52% | 14.4920 | no |
| 100 | lookup-miss | 5.94–8.56 | 15.44% | 5.9360 | yes |
| 100 | rank | 13.24–15.85 | 6.12% | 13.2420 | no |
| 100 | iterate | 1.74–2.40 | 13.99% | 1.7400 | yes |
| 100 | scan | 11.09–12.93 | 2.80% | 11.0940 | no |
| 100 | update | 119.56–130.10 | 0.83% | 119.5600 | no |
| 100 | delete | 190.00–240.00 | 17.50% | 0.0190 | yes |
| 1000 | insert | 219.00–245.00 | 4.72% | 0.2190 | yes |
| 1000 | lookup-hit | 14.97–16.53 | 2.65% | 14.9660 | no |
| 1000 | lookup-miss | 6.35–6.92 | 3.83% | 6.3500 | yes |
| 1000 | rank | 14.66–15.52 | 2.20% | 14.6600 | no |
| 1000 | iterate | 2.12–2.66 | 11.06% | 2.1180 | yes |
| 1000 | scan | 15.23–16.18 | 1.43% | 15.2570 | no |
| 1000 | update | 160.72–218.46 | 1.87% | 160.7200 | no |
| 1000 | delete | 157.00–173.00 | 1.82% | 0.1570 | yes |
| 10000 | insert | 213.10–238.00 | 5.74% | 2.1310 | yes |
| 10000 | lookup-hit | 25.18–29.19 | 4.90% | 25.1770 | no |
| 10000 | lookup-miss | 8.38–9.04 | 1.54% | 8.3850 | yes |
| 10000 | rank | 33.98–40.23 | 8.24% | 33.9780 | no |
| 10000 | iterate | 2.09–2.61 | 8.44% | 2.0900 | yes |
| 10000 | scan | 21.27–32.32 | 17.86% | 21.4480 | no |
| 10000 | update | 277.36–287.80 | 0.98% | 277.3640 | no |
| 10000 | delete | 151.40–166.10 | 3.21% | 1.5140 | yes |
| 100000 | insert | 228.36–241.11 | 1.49% | 22.8360 | no |
| 100000 | lookup-hit | 43.68–46.14 | 0.83% | 43.6780 | no |
| 100000 | lookup-miss | 11.74–12.68 | 3.31% | 11.7370 | no |
| 100000 | rank | 64.03–68.06 | 1.19% | 64.0270 | no |
| 100000 | iterate | 2.08–2.62 | 11.77% | 2.0750 | yes |
| 100000 | scan | 45.44–47.37 | 0.88% | 46.5860 | no |
| 100000 | update | 317.51–329.66 | 0.86% | 317.5150 | no |
| 100000 | delete | 163.30–179.97 | 2.96% | 16.3300 | no |
| 1000000 | insert | 320.40–331.76 | 1.73% | 320.3960 | no |
| 1000000 | lookup-hit | 120.35–126.79 | 2.10% | 120.3490 | no |
| 1000000 | lookup-miss | 43.64–46.87 | 1.80% | 43.6400 | no |
| 1000000 | rank | 205.00–221.20 | 3.92% | 205.0020 | no |
| 1000000 | iterate | 2.05–2.77 | 16.43% | 2.0510 | yes |
| 1000000 | scan | 50.54–54.89 | 2.84% | 50.6300 | no |
| 1000000 | update | 559.74–585.11 | 1.55% | 559.7440 | no |
| 1000000 | delete | 326.33–336.69 | 1.69% | 326.3350 | no |
