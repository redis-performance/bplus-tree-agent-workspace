# Corrected-adapter baselines: M6 and three AWS architectures

Four independent audits reconstruct **480 serial processes, 3,840 raw rows and 160
host/case/size cells**, with 24 observations per cell. Each host completed seven
native/sanitizer validation stages. These are coverage baselines; qualification is
limited as shown below. No optimization has been adopted.

![Corrected-adapter M6, Intel, AMD and Graviton baselines](corrected-adapter-baseline.png)

Dots are median batch-average ns/op; whiskers show the observed minimum and maximum.
They are not per-operation latency percentiles or confidence intervals. Lower is less
time. All eight operations use the original five sizes, 16-byte members, one million
requested operations, seeds 1–3 and six same-binary ABBA blocks. Insert/delete execute
one operation per member; scan reports actual callbacks, including legal duplicates.

## Qualification

A case qualifies only when every A/A block stays within ±1% and every timed window
is at least 10 ms. The three outcome columns below are disjoint; a short case is
listed as short even if it also fails precision.

| Host | Qualified | Short window | Other noisy | Independent audit |
|---|---:|---:|---:|---|
| Apple M6 | 5/40 | 14/40 | 21/40 | [Raw reconstruction](../reviews/corrected-apple-m6-baseline-audit.json) |
| AWS Intel | 10/40 | 11/40 | 19/40 | [Raw reconstruction](../reviews/corrected-aws-intel-baseline-audit.json) |
| AWS AMD | 11/40 | 11/40 | 18/40 | [Raw reconstruction](../reviews/corrected-aws-amd-baseline-audit.json) |
| AWS Graviton | 21/40 | 11/40 | 8/40 | [Raw reconstruction](../reviews/corrected-aws-arm-baseline-audit.json) |

## Source and machine identity

The tree, benchmark loop, compatibility adapter, Makefile, vendor inputs and analyzer
are byte-identical across these runs. AWS uses exact source13e459ff8; M6 source7f299a5f5
differs only in two Linux affinity metadata lines in the runner. The corrected adapter
annotates the panic function's existing non-returning behavior; assertions remain intact.
[Complete source parity](source-parity.json), [exact runner diff](runner-metadata-only.diff),
[pinned published summaries and hashes](sources.json).

M6 uses Apple Clang21 on macOS without CPU pinning. AWS uses Clang18.1.3 on Linux,
pinned to CPU2: Intel Sapphire Rapids, AMD Zen5 and ARM NeoverseV2. Compiler, OS,
affinity and machine differences are confounded; this chart does not isolate an
architecture effect or establish a candidate gain. Host observations are never pooled.
The old-adapter [five-host chart](../baseline-charts/m1-m6-baseline.png) remains unchanged.
No corrected M1 baseline is present, and no old M1 rows are inserted here.

## Measured medians

Values below are batch-average ns/op, including cells that are not qualified. Use
qualified same-host comparisons for optimization decisions; do not infer acceptance
from these medians.

### 100,000 members

| Operation | Apple M6 | AWS Intel | AWS AMD | AWS Graviton |
|---|---:|---:|---:|---:|
| Insert | 234.32 | 558.93 | 389.56 | 496.20 |
| Hit lookup | 45.10 | 134.38 | 74.86 | 144.00 |
| Miss lookup | 12.29 | 71.54 | 36.22 | 59.53 |
| Rank | 65.49 | 174.79 | 104.13 | 176.54 |
| Forward iteration | 2.15 | 4.14 | 4.27 | 3.35 |
| Scan | 46.28 | 86.44 | 66.97 | 83.06 |
| Score update | 325.00 | 729.79 | 492.06 | 648.55 |
| Delete | 169.34 | 350.16 | 219.98 | 324.98 |

### 1,000,000 members

| Operation | Apple M6 | AWS Intel | AWS AMD | AWS Graviton |
|---|---:|---:|---:|---:|
| Insert | 328.24 | 781.57 | 695.15 | 760.92 |
| Hit lookup | 122.86 | 219.08 | 311.72 | 354.18 |
| Miss lookup | 45.49 | 149.16 | 179.56 | 191.37 |
| Rank | 212.00 | 301.96 | 356.34 | 412.41 |
| Forward iteration | 2.22 | 4.57 | 4.47 | 3.77 |
| Scan | 52.39 | 116.55 | 92.85 | 110.78 |
| Score update | 568.73 | 1037.70 | 1082.54 | 1082.97 |
| Delete | 330.73 | 557.22 | 602.15 | 597.44 |

## Reproduce the plots

```sh
python3 scripts/plot-host-baselines.py experiments/NIGHT-EXPLORATION-001/corrected-adapter-charts
```

The script verifies all 160 summary cells, each source SHA256, and all 24-observation
counts before rendering combined and individual PNG/SVG files with shared per-panel
limits. It performs no new benchmarking. Root visually inspected the combined PNG;
original chart bytes were checked unchanged. Individual plots also name the corrected
adapter in their footer. Native serving models and token/USD costs remain unknown.
