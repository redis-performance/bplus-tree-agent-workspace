# Scan — measured profile assessment

Diagnostic profiles, **source NONE**. No timing acceptance or per-operation counter
claim. Exact binary/commands/raw hashes/window order are in [analysis](analysis.json)
and [raw records](results/). All retained windows enter the reported means; a
configuration needs all three L2 windows to qualify for interpretation.

## scan-100000

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound                   19.20%        23.15%
├── Bad_Speculation                  33.50%        32.75%
├── Backend_Bound                    19.80%        18.97%
│   ├── Memory_Bound                  9.25%         8.50%
│   └── Core_Bound                   10.55%        10.47%
└── Retiring                         27.50%        25.17%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/scan-100000-base.record.json) | 3/3 | 1.83 | 1.566 | zbtIndexScanSlot 84.6%, zbtIndexScanGroup 6.7%, siphash 6.0% |
| [Scan B](results/scan-100000-scanB.record.json) | 3/3 | 1.66 | 1.567 | zbtIndexScanSlot 85.2%, siphash 5.7%, zbtIndexScanGroup 5.5% |

## scan-1000000

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound                   16.70%        19.19%
├── Bad_Speculation                  23.96%        25.00%
├── Backend_Bound                    39.10%        37.51%
│   ├── Memory_Bound                 24.76%        23.61%
│   └── Core_Bound                   14.34%        13.91%
└── Retiring                         20.20%        18.21%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/scan-1000000-base.record.json) | 3/3 | 1.33 | 1.570 | zbtIndexScanSlot 85.8%, zbtIndexScanGroup 10.0%, siphash 2.7% |
| [Scan B](results/scan-1000000-scanB.record.json) | 3/3 | 1.19 | 1.569 | zbtIndexScanSlot 84.8%, zbtIndexScanGroup 9.2%, siphash 4.7% |

## scan-trim-319-zero

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound              unavailable        12.50%
├── Bad_Speculation             unavailable         0.69%
├── Backend_Bound               unavailable         2.23%
│   ├── Memory_Bound            unavailable         0.40%
│   └── Core_Bound              unavailable         1.87%
└── Retiring                    unavailable        84.61%
```

Baseline TMA is unavailable for interpretation: 2/3 windows qualify; failed scope/quality evidence and all numeric observations remain in analysis.json.

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/scan-trim-319-zero-base.record.json) | 2/3 | 5.41 | 1.561 | zbtIndexScanSlot 69.8%, zbtIndexScanGroup 21.4%, consume 7.2% |
| [Scan B](results/scan-trim-319-zero-scanB.record.json) | 3/3 | 5.38 | 1.571 | zbtIndexScanSlot 66.5%, zbtIndexScanGroup 21.6%, consume 9.4% |

## scan-resize-319-zero

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound              unavailable        11.92%
├── Bad_Speculation             unavailable        15.01%
├── Backend_Bound               unavailable        25.01%
│   ├── Memory_Bound            unavailable         5.90%
│   └── Core_Bound              unavailable        19.11%
└── Retiring                    unavailable        48.05%
```

Baseline TMA is unavailable for interpretation: 2/3 windows qualify; failed scope/quality evidence and all numeric observations remain in analysis.json.

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/scan-resize-319-zero-base.record.json) | 2/3 | 3.12 | 1.573 | zbtIndexScanSlot 50.7%, siphash 34.7%, zbtIndexScanGroup 10.4% |
| [Scan B](results/scan-resize-319-zero-scanB.record.json) | 3/3 | 3.09 | 1.571 | zbtIndexScanSlot 54.0%, siphash 35.2%, zbtIndexScanGroup 7.8% |

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
