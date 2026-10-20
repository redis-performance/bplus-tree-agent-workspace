# Iterator — measured profile assessment

Diagnostic profiles, **source NONE**. No timing acceptance or per-operation counter
claim. Exact binary/commands/raw hashes/window order are in [analysis](analysis.json)
and [raw records](results/). All retained windows enter the reported means; a
configuration needs all three L2 windows to qualify for interpretation.

## iterator-100000-forward-integer-7

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    1.07%         2.17%         2.01%
├── Bad_Speculation                   3.20%         2.40%         2.40%
├── Backend_Bound                    11.32%        11.13%        11.86%
│   ├── Memory_Bound                  7.18%         7.09%         7.78%
│   └── Core_Bound                    4.14%         4.03%         4.03%
└── Retiring                         84.41%        84.30%        83.73%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-100000-forward-integer-7-base.record.json) | 3/3 | 5.51 | 1.571 | zbtreeIteratorNext 89.8%, traverse 10.2% |
| [Iterator A](results/iterator-100000-forward-integer-7-itA.record.json) | 3/3 | 5.51 | 1.570 | zbtreeIteratorNext 87.9%, traverse 12.1% |
| [Iterator B](results/iterator-100000-forward-integer-7-itB.record.json) | 3/3 | 5.48 | 1.565 | zbtreeIteratorNext 87.3%, traverse 12.7% |

## iterator-100000-forward-integer-4

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    2.17%         3.30%   unavailable
├── Bad_Speculation                   5.14%         5.15%   unavailable
├── Backend_Bound                     1.20%         1.20%   unavailable
│   ├── Memory_Bound                  0.00%         0.00%   unavailable
│   └── Core_Bound                    1.20%         1.20%   unavailable
└── Retiring                         91.53%        90.37%   unavailable
```

Iterator B TMA is unavailable for interpretation: 2/3 windows qualify; failed scope/quality evidence and all numeric observations remain in analysis.json.

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-100000-forward-integer-4-base.record.json) | 3/3 | 5.85 | 1.569 | zbtreeIteratorNext 92.4%, traverse 7.6% |
| [Iterator A](results/iterator-100000-forward-integer-4-itA.record.json) | 3/3 | 5.76 | 1.566 | zbtreeIteratorNext 92.5%, traverse 7.5% |
| [Iterator B](results/iterator-100000-forward-integer-4-itB.record.json) | 2/3 | 5.79 | 1.564 | zbtreeIteratorNext 92.6%, traverse 7.4% |

## iterator-1000000-forward-integer-7

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    0.70%         1.85%         2.35%
├── Bad_Speculation                   2.80%         2.00%         2.00%
├── Backend_Bound                    21.28%        22.11%        21.60%
│   ├── Memory_Bound                 15.94%        16.27%        16.26%
│   └── Core_Bound                    5.31%         5.85%         5.34%
└── Retiring                         75.22%        74.04%        74.05%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-1000000-forward-integer-7-base.record.json) | 3/3 | 4.89 | 1.570 | zbtreeIteratorNext 90.5%, traverse 9.3%, 0xffffffff85400ef0 0.2% |
| [Iterator A](results/iterator-1000000-forward-integer-7-itA.record.json) | 3/3 | 4.85 | 1.572 | zbtreeIteratorNext 89.7%, traverse 10.3% |
| [Iterator B](results/iterator-1000000-forward-integer-7-itB.record.json) | 3/3 | 4.86 | 1.560 | zbtreeIteratorNext 89.6%, traverse 10.4% |

## iterator-1000000-forward-integer-4

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    2.03%   unavailable         2.73%
├── Bad_Speculation                   4.72%   unavailable         4.72%
├── Backend_Bound                    13.25%   unavailable        13.22%
│   ├── Memory_Bound                 10.52%   unavailable        10.50%
│   └── Core_Bound                    2.66%   unavailable         2.68%
└── Retiring                         80.00%   unavailable        79.33%
```

Iterator A TMA is unavailable for interpretation: 2/3 windows qualify; failed scope/quality evidence and all numeric observations remain in analysis.json.

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-1000000-forward-integer-4-base.record.json) | 3/3 | 5.12 | 1.569 | zbtreeIteratorNext 91.3%, traverse 8.7% |
| [Iterator A](results/iterator-1000000-forward-integer-4-itA.record.json) | 2/3 | 5.09 | 1.561 | zbtreeIteratorNext 91.4%, traverse 8.6% |
| [Iterator B](results/iterator-1000000-forward-integer-4-itB.record.json) | 3/3 | 5.07 | 1.570 | zbtreeIteratorNext 92.1%, traverse 7.9% |

## iterator-100000-reverse-integer-7

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    1.90%         2.22%         3.55%
├── Bad_Speculation                   5.11%         4.40%         4.00%
├── Backend_Bound                     8.57%         9.03%         8.31%
│   ├── Memory_Bound                  5.47%         5.79%         5.42%
│   └── Core_Bound                    3.10%         3.23%         2.89%
└── Retiring                         84.42%        84.43%        84.16%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-100000-reverse-integer-7-base.record.json) | 3/3 | 5.51 | 1.567 | zbtreeIteratorNext 89.8%, traverse 10.2% |
| [Iterator A](results/iterator-100000-reverse-integer-7-itA.record.json) | 3/3 | 5.53 | 1.568 | zbtreeIteratorNext 87.2%, traverse 12.8% |
| [Iterator B](results/iterator-100000-reverse-integer-7-itB.record.json) | 3/3 | 5.51 | 1.570 | zbtreeIteratorNext 86.9%, traverse 13.1% |

## iterator-100000-forward-fraction-7

```text
Pipeline Slots (100%)              Baseline    Iterator A    Iterator B
├── Frontend_Bound                    0.89%         2.09%         1.90%
├── Bad_Speculation                   3.20%         2.40%         2.40%
├── Backend_Bound                    11.26%        11.91%        11.39%
│   ├── Memory_Bound                  7.20%         7.55%         7.49%
│   └── Core_Bound                    4.06%         4.35%         3.90%
└── Retiring                         84.64%        83.61%        84.31%
```

| Build | Qualified L2 windows | IPC | Cycles/reference cycle | Top user-cycle sampled symbols |
|---|---:|---:|---:|---|
| [Baseline](results/iterator-100000-forward-fraction-7-base.record.json) | 3/3 | 5.51 | 1.566 | zbtreeIteratorNext 90.0%, traverse 10.0% |
| [Iterator A](results/iterator-100000-forward-fraction-7-itA.record.json) | 3/3 | 5.47 | 1.571 | zbtreeIteratorNext 87.9%, traverse 12.1% |
| [Iterator B](results/iterator-100000-forward-fraction-7-itB.record.json) | 3/3 | 5.52 | 1.568 | zbtreeIteratorNext 91.9%, traverse 8.1% |

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
