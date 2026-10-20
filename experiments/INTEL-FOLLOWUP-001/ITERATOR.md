# Iterator — follow-up TMA

Secondary Intel Sapphire Rapids, CPU2/NUMA0, sibling50 offline during capture.
Exact retained Clang18/O3 binaries, source37efd287f and original candidate patches.
Three5s windows per build; means use all15 intervals. Diagnostic only, source NONE.
This new host/SMT condition is separate from earlier captures.

## iterator-1000000-forward-integer-7

```text
Pipeline Slots (100%)              Baseline    Iterator B
├── Frontend_Bound                    0.80%         1.63%
│   ├── Fetch_Latency                 0.40%         0.40%
│   └── Fetch_Bandwidth               0.40%         1.31%
├── Bad_Speculation                   1.60%         1.20%
│   ├── Branch_Mispredicts            1.60%         1.20%
│   └── Machine_Clears                0.00%         0.00%
├── Backend_Bound                    50.89%        44.09%
│   ├── Memory_Bound                 34.07%        28.15%
│   └── Core_Bound                   16.82%        15.91%
└── Retiring                         46.81%        53.01%
    ├── Light_Operations             44.81%        51.03%
    └── Heavy_Operations              2.00%         2.08%
```

- Baseline: 3/3 windows qualify. [Capture records](results/iterator-1000000-forward-integer-7-base.record.json).
- Iterator B: 3/3 windows qualify. [Capture records](results/iterator-1000000-forward-integer-7-itB.record.json).

## iterator-100000-forward-integer-4

```text
Pipeline Slots (100%)              Baseline    Iterator B
├── Frontend_Bound                    2.11%         3.28%
│   ├── Fetch_Latency                 0.70%         0.30%
│   └── Fetch_Bandwidth               1.41%         2.91%
├── Bad_Speculation                   5.15%         5.15%
│   ├── Branch_Mispredicts            5.10%         5.10%
│   └── Machine_Clears                0.10%         0.10%
├── Backend_Bound                     1.15%         1.17%
│   ├── Memory_Bound                  0.00%         0.00%
│   └── Core_Bound                    1.15%         1.17%
└── Retiring                         91.63%        90.41%
    ├── Light_Operations             86.53%        85.72%
    └── Heavy_Operations              5.10%         4.70%
```

- Baseline: 3/3 windows qualify. [Capture records](results/iterator-100000-forward-integer-4-base.record.json).
- Iterator B: 3/3 windows qualify. [Capture records](results/iterator-100000-forward-integer-4-itB.record.json).

## iterator-1000000-forward-integer-4

```text
Pipeline Slots (100%)              Baseline    Iterator A
├── Frontend_Bound                    1.85%         2.67%
│   ├── Fetch_Latency                 0.70%         0.30%
│   └── Fetch_Bandwidth               1.15%         2.33%
├── Bad_Speculation                   4.73%         4.73%
│   ├── Branch_Mispredicts            4.62%         4.43%
│   └── Machine_Clears                0.18%         0.34%
├── Backend_Bound                    12.90%        12.51%
│   ├── Memory_Bound                  8.52%         8.21%
│   └── Core_Bound                    4.38%         4.30%
└── Retiring                         80.53%        80.09%
    ├── Light_Operations             76.23%        75.79%
    └── Heavy_Operations              4.30%         4.30%
```

- Baseline: 3/3 windows qualify. [Capture records](results/iterator-1000000-forward-integer-4-base.record.json).
- Iterator A: 3/3 windows qualify. [Capture records](results/iterator-1000000-forward-integer-4-itA.record.json).

## Interpretation limits

Ambient Parca remained running as disclosed in preflight; this is not proof of zero
shared-resource interference. CPU2/workload accounting passed the1% gate.

Four roots sum to100% within the preregistered tolerance; rounding and child-model
residuals are preserved. L1/L3/DRAM slot breakdown is unavailable: no qualified L3
capture. Memory Bound alone does not identify DRAM or a source instruction.

PEBS/LBR probes failed the scheduling-evidence gate; both were retained and deeper
captures skipped. Their samples do not support mechanism claims. No in-window
operation counts or acceptance timings: fractions cannot establish cycles/op or a
speedup. Updates evolve across windows; phase and raw interval order are retained.
Completed original/profile/sanitizer semantic checks are separate from profile loops,
which terminate after collection without a final completed-work checksum.

[Raw analysis](analysis.json) · [Assessment](ASSESSMENT.md) · [Probe gates](PROBE-GATES.json)
