# Size matrix — aarch64

Median batch-average ns/op over 24 observations per cell; lower is better.
Three seeds, six same-binary ABBA blocks. These are baseline measurements, not speedups.

| Operation | 100 | 1000 | 10000 | 100000 | 1000000 |
|---|---:|---:|---:|---:|---:|
| insert | 430.89 | 432.20 | 431.01 | 496.20 | 760.92 |
| lookup-hit | 39.85 | 46.47 | 69.02 | 144.00 | 354.18 |
| lookup-miss | 17.43 | 18.10 | 23.74 | 59.53 | 191.37 |
| rank | 37.27 | 46.45 | 87.76 | 176.54 | 412.41 |
| iterate | 3.15 | 3.36 | 3.31 | 3.35 | 3.77 |
| scan | 26.87 | 36.54 | 62.46 | 83.06 | 110.78 |
| update | 317.76 | 439.12 | 507.61 | 648.55 | 1082.97 |
| delete | 267.90 | 247.37 | 244.59 | 324.98 | 597.44 |

## Variation and timing duration

Ranges describe observed batch averages, not per-operation latency percentiles or confidence intervals.
A/A is the difference between identical-binary sides. Large values show noise, not a code change.
Short windows (<10 ms) are flagged for follow-up batching before small optimization comparisons.

| Size | Operation | Min–max ns/op | Largest absolute A/A difference | Shortest window (ms) | <10 ms |
|---:|---|---:|---:|---:|---|
| 100 | insert | 374.77–558.94 | 14.77% | 0.0375 | yes |
| 100 | lookup-hit | 39.73–40.20 | 0.60% | 39.7303 | no |
| 100 | lookup-miss | 16.93–19.08 | 0.30% | 16.9265 | no |
| 100 | rank | 37.08–37.63 | 0.45% | 37.0787 | no |
| 100 | iterate | 3.14–3.18 | 0.21% | 3.1419 | yes |
| 100 | scan | 26.22–30.14 | 1.84% | 26.2219 | no |
| 100 | update | 314.29–368.69 | 0.61% | 314.2882 | no |
| 100 | delete | 240.66–273.96 | 1.16% | 0.0241 | yes |
| 1000 | insert | 423.69–442.37 | 1.88% | 0.4237 | yes |
| 1000 | lookup-hit | 45.63–47.56 | 2.72% | 45.6278 | no |
| 1000 | lookup-miss | 17.66–18.22 | 0.42% | 17.6596 | no |
| 1000 | rank | 44.52–48.37 | 3.74% | 44.5212 | no |
| 1000 | iterate | 3.29–3.48 | 3.30% | 3.2912 | yes |
| 1000 | scan | 35.14–39.22 | 2.81% | 35.2066 | no |
| 1000 | update | 431.22–464.81 | 0.55% | 431.2160 | no |
| 1000 | delete | 243.56–249.82 | 1.22% | 0.2436 | yes |
| 10000 | insert | 427.98–436.84 | 0.73% | 4.2798 | yes |
| 10000 | lookup-hit | 68.35–70.89 | 1.04% | 68.3506 | no |
| 10000 | lookup-miss | 23.61–24.15 | 0.86% | 23.6131 | no |
| 10000 | rank | 85.87–89.90 | 1.00% | 85.8714 | no |
| 10000 | iterate | 3.30–3.34 | 1.01% | 3.2984 | yes |
| 10000 | scan | 62.12–63.58 | 0.55% | 62.4808 | no |
| 10000 | update | 503.04–511.12 | 0.20% | 503.0432 | no |
| 10000 | delete | 242.98–245.51 | 0.42% | 2.4298 | yes |
| 100000 | insert | 492.00–505.47 | 0.84% | 49.1996 | no |
| 100000 | lookup-hit | 142.16–146.07 | 0.72% | 142.1606 | no |
| 100000 | lookup-miss | 58.52–60.70 | 1.11% | 58.5176 | no |
| 100000 | rank | 174.35–179.08 | 0.66% | 174.3526 | no |
| 100000 | iterate | 3.33–3.40 | 1.17% | 3.3322 | yes |
| 100000 | scan | 82.11–84.05 | 0.79% | 84.1711 | no |
| 100000 | update | 646.68–650.60 | 0.35% | 646.6810 | no |
| 100000 | delete | 322.51–327.39 | 0.60% | 32.2514 | no |
| 1000000 | insert | 757.28–765.25 | 0.48% | 757.2839 | no |
| 1000000 | lookup-hit | 350.53–406.37 | 6.97% | 350.5340 | no |
| 1000000 | lookup-miss | 189.51–195.51 | 0.84% | 189.5096 | no |
| 1000000 | rank | 408.71–416.54 | 0.72% | 408.7100 | no |
| 1000000 | iterate | 3.76–3.83 | 0.77% | 3.7555 | yes |
| 1000000 | scan | 109.96–136.61 | 10.33% | 110.1624 | no |
| 1000000 | update | 1077.43–1091.80 | 0.47% | 1077.4266 | no |
| 1000000 | delete | 596.05–599.82 | 0.47% | 596.0466 | no |
