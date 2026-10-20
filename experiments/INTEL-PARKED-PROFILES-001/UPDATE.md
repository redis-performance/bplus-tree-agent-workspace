# Update — measured profile assessment

Diagnostic profiles, **source NONE**. No timing acceptance or per-operation counter
claim. Exact binary/commands/raw hashes/window order are in [analysis](analysis.json)
and [raw records](results/). All retained windows enter the reported means; a
configuration needs all three L2 windows to qualify for interpretation.

## update-100000-same

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    2.92%
├── Bad_Speculation                  13.29%
├── Backend_Bound                    64.99%
│   ├── Memory_Bound                 47.07%
│   └── Core_Bound                   17.97%
└── Retiring                         18.75%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-100000-same-base.record.json) | 3/3 | 1.15 | 1.562 | zbtreeFindForAdd 42.7%, zbtScoreLeafFindMember 23.6%, main 8.5% |

## update-100000-position

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    3.36%
├── Bad_Speculation                  12.60%
├── Backend_Bound                    65.98%
│   ├── Memory_Bound                 47.99%
│   └── Core_Bound                   17.95%
└── Retiring                         18.03%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-100000-position-base.record.json) | 3/3 | 1.11 | 1.564 | zbtreeFindForAdd 39.3%, zbtScoreLeafFindMember 24.0%, main 9.4% |

## update-100000-nearby

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                   13.59%
├── Bad_Speculation                  15.52%
├── Backend_Bound                    37.57%
│   ├── Memory_Bound                 26.00%
│   └── Core_Bound                   11.64%
└── Retiring                         33.32%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-100000-nearby-base.record.json) | 3/3 | 2.07 | 1.567 | zbtreeFindForAdd 21.9%, zbtScoreInsertAt 15.2%, zbtScoreLeafFindMember 11.4% |

## update-100000-distant

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                   15.82%
├── Bad_Speculation                  15.02%
├── Backend_Bound                    29.11%
│   ├── Memory_Bound                 18.32%
│   └── Core_Bound                   10.79%
└── Retiring                         39.97%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-100000-distant-base.record.json) | 3/3 | 2.50 | 1.563 | zbtScoreInsertAt 18.0%, zbtreeFindForAdd 12.9%, zbtScoreLeafLowerBound 12.3% |

## update-100000-original

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                   15.85%
├── Bad_Speculation                  14.81%
├── Backend_Bound                    29.31%
│   ├── Memory_Bound                 18.73%
│   └── Core_Bound                   10.58%
└── Retiring                         40.02%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-100000-original-base.record.json) | 3/3 | 2.51 | 1.568 | zbtScoreInsertAt 18.7%, zbtreeFindForAdd 14.5%, zbtScoreLeafBuild 10.8% |

## update-1000000-same

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    1.79%
├── Bad_Speculation                   7.47%
├── Backend_Bound                    80.71%
│   ├── Memory_Bound                 68.12%
│   └── Core_Bound                   12.56%
└── Retiring                         10.04%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-1000000-same-base.record.json) | 3/3 | 0.62 | 1.569 | zbtreeFindForAdd 48.7%, zbtScoreLeafFindMember 20.6%, 0x0000000000198427 9.7% |

## update-1000000-position

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    1.90%
├── Bad_Speculation                   7.39%
├── Backend_Bound                    80.99%
│   ├── Memory_Bound                 68.15%
│   └── Core_Bound                   12.78%
└── Retiring                          9.72%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-1000000-position-base.record.json) | 3/3 | 0.61 | 1.569 | zbtreeFindForAdd 45.1%, zbtScoreLeafFindMember 18.9%, 0x0000000000198427 10.5% |

## update-1000000-nearby

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    9.67%
├── Bad_Speculation                  11.75%
├── Backend_Bound                    55.43%
│   ├── Memory_Bound                 44.58%
│   └── Core_Bound                   10.85%
└── Retiring                         23.15%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-1000000-nearby-base.record.json) | 3/3 | 1.36 | 1.563 | zbtreeFindForAdd 33.2%, zbtScoreLeafFindMember 10.0%, zbtScoreInsertAt 8.9% |

## update-1000000-distant

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                   11.15%
├── Bad_Speculation                  11.92%
├── Backend_Bound                    48.84%
│   ├── Memory_Bound                 37.56%
│   └── Core_Bound                   11.29%
└── Retiring                         28.09%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-1000000-distant-base.record.json) | 3/3 | 1.77 | 1.569 | zbtreeFindForAdd 22.3%, zbtScoreInsertAt 11.7%, zbtScoreLeafLowerBound 10.3% |

## update-1000000-original

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                   11.09%
├── Bad_Speculation                  11.79%
├── Backend_Bound                    49.18%
│   ├── Memory_Bound                 37.89%
│   └── Core_Bound                   11.33%
└── Retiring                         27.89%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/update-1000000-original-base.record.json) | 3/3 | 1.75 | 1.575 | zbtreeFindForAdd 25.0%, zbtScoreInsertAt 12.6%, zbtScoreLeafBuild 9.7% |

[Next experiment and missing evidence](ASSESSMENT.md).

## Collection limits

Topdown71dea5e / pmu-tools2026.4.7.0, Intel Sapphire Rapids profiler, CPU2/NUMA0,
sibling50 online; Clang18/O3, source37efd287f and exact retained patches. See
[protocol](protocol-v2.json) and [build identities](results/build-sha256.json).
Each L2 mean uses15 one-second intervals when complete. L1 shares sum approximately
100%; displayed rounding and child-model residuals are retained, not rescaled.

L3 data are retained separately. Mixed `% Stalls`, `% Clocks`, `% Uops` and estimated
slot units are not a partition of total pipeline slots. Low scheduling prevents
reliable deeper causal attribution; cache/DRAM slot shares remain unavailable unless
separately qualified. IPC and cycles/reference-cycle are interval ratios, not speedups
or cycles per operation. Samples cover user-mode cycles for the workload PID; sample
shares exclude kernel execution and are not TMA slot shares.

Each workload starts after construction/oracle/warmup readiness. Profile loops terminate
after capture; their final completed-work checksum is uncollected. Completed original,
diagnostic and sanitizer semantic checks are separate evidence. Update workloads
mutate state throughout successive windows; no stationary-state assumption is made.
[Per-window means and elapsed phases](window-phases.json) retain the ordered observations.
Existing timing failures and old-source rejections remain unchanged.
