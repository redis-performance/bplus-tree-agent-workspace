# Update — follow-up TMA

Secondary Intel Sapphire Rapids, CPU2/NUMA0, sibling50 offline during capture.
Exact retained Clang18/O3 binaries, source37efd287f and original candidate patches.
Three5s windows per build; means use all15 intervals. Diagnostic only, source NONE.
This new host/SMT condition is separate from earlier captures.

## update-100000-same

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    3.00%
│   ├── Fetch_Latency                 1.10%
│   └── Fetch_Bandwidth               2.00%
├── Bad_Speculation                  12.60%
│   ├── Branch_Mispredicts           12.47%
│   └── Machine_Clears                0.13%
├── Backend_Bound                    66.75%
│   ├── Memory_Bound                 48.75%
│   └── Core_Bound                   18.00%
└── Retiring                         17.65%
    ├── Light_Operations             16.85%
    └── Heavy_Operations              0.80%
```

- Baseline: 3/3 windows qualify. [Capture records](results/update-100000-same-base.record.json).

## update-100000-position

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    3.41%
│   ├── Fetch_Latency                 1.10%
│   └── Fetch_Bandwidth               2.37%
├── Bad_Speculation                  12.21%
│   ├── Branch_Mispredicts           12.17%
│   └── Machine_Clears                0.10%
├── Backend_Bound                    66.69%
│   ├── Memory_Bound                 48.83%
│   └── Core_Bound                   17.79%
└── Retiring                         17.63%
    ├── Light_Operations             16.90%
    └── Heavy_Operations              0.80%
```

- Baseline: 3/3 windows qualify. [Capture records](results/update-100000-position-base.record.json).

## update-1000000-same

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    1.79%
│   ├── Fetch_Latency                 0.67%
│   └── Fetch_Bandwidth               1.12%
├── Bad_Speculation                   7.02%
│   ├── Branch_Mispredicts            6.95%
│   └── Machine_Clears                0.03%
├── Backend_Bound                    81.72%
│   ├── Memory_Bound                 68.73%
│   └── Core_Bound                   12.97%
└── Retiring                          9.49%
    ├── Light_Operations              9.09%
    └── Heavy_Operations              0.40%
```

- Baseline: 3/3 windows qualify. [Capture records](results/update-1000000-same-base.record.json).

## update-1000000-position

```text
Pipeline Slots (100%)              Baseline
├── Frontend_Bound                    2.19%
│   ├── Fetch_Latency                 0.70%
│   └── Fetch_Bandwidth               1.49%
├── Bad_Speculation                   6.83%
│   ├── Branch_Mispredicts            6.81%
│   └── Machine_Clears                0.00%
├── Backend_Bound                    81.55%
│   ├── Memory_Bound                 68.63%
│   └── Core_Bound                   12.89%
└── Retiring                          9.44%
    ├── Light_Operations              9.04%
    └── Heavy_Operations              0.40%
```

- Baseline: 3/3 windows qualify. [Capture records](results/update-1000000-position-base.record.json).

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
