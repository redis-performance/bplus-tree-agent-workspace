# Scan — follow-up TMA

Secondary Intel Sapphire Rapids, CPU2/NUMA0, sibling50 offline during capture.
Exact retained Clang18/O3 binaries, source37efd287f and original candidate patches.
Three5s windows per build; means use all15 intervals. Diagnostic only, source NONE.
This new host/SMT condition is separate from earlier captures.

## scan-1000000

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound                   15.15%        18.17%
│   ├── Fetch_Latency                 6.55%         7.47%
│   └── Fetch_Bandwidth               8.61%        10.69%
├── Bad_Speculation                  22.23%        24.34%
│   ├── Branch_Mispredicts           21.85%        23.81%
│   └── Machine_Clears                0.40%         0.43%
├── Backend_Bound                    43.16%        39.36%
│   ├── Memory_Bound                 28.50%        25.31%
│   └── Core_Bound                   14.65%        14.10%
└── Retiring                         19.51%        18.15%
    ├── Light_Operations             18.76%        17.37%
    └── Heavy_Operations              0.77%         0.80%
```

- Baseline: 3/3 windows qualify. [Capture records](results/scan-1000000-base.record.json).
- Scan B: 3/3 windows qualify. [Capture records](results/scan-1000000-scanB.record.json).

## scan-trim-319-zero

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound                   13.19%        13.83%
│   ├── Fetch_Latency                 2.68%         3.03%
│   └── Fetch_Bandwidth              10.51%        10.77%
├── Bad_Speculation                   0.40%         0.53%
│   ├── Branch_Mispredicts            0.00%         0.00%
│   └── Machine_Clears                0.40%         0.53%
├── Backend_Bound                     2.37%         1.71%
│   ├── Memory_Bound                  0.40%         0.40%
│   └── Core_Bound                    1.97%         1.31%
└── Retiring                         84.04%        83.97%
    ├── Light_Operations             79.34%        79.64%
    └── Heavy_Operations              4.70%         4.30%
```

- Baseline: 3/3 windows qualify. [Capture records](results/scan-trim-319-zero-base.record.json).
- Scan B: 3/3 windows qualify. [Capture records](results/scan-trim-319-zero-scanB.record.json).

## scan-resize-319-zero

```text
Pipeline Slots (100%)              Baseline        Scan B
├── Frontend_Bound                   10.00%        12.35%
│   ├── Fetch_Latency                 3.30%         4.93%
│   └── Fetch_Bandwidth               6.60%         7.42%
├── Bad_Speculation                  16.19%        15.45%
│   ├── Branch_Mispredicts           16.00%        15.25%
│   └── Machine_Clears                0.20%         0.20%
├── Backend_Bound                    23.39%        21.76%
│   ├── Memory_Bound                  3.50%         3.10%
│   └── Core_Bound                   19.89%        18.61%
└── Retiring                         50.41%        50.49%
    ├── Light_Operations             48.81%        48.89%
    └── Heavy_Operations              1.60%         1.60%
```

- Baseline: 3/3 windows qualify. [Capture records](results/scan-resize-319-zero-base.record.json).
- Scan B: 3/3 windows qualify. [Capture records](results/scan-resize-319-zero-scanB.record.json).

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
