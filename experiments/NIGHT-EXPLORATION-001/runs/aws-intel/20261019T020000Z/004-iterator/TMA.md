# TMA classification

Supplement added 20 October 2026; historical decisions and raw evidence are unchanged.

## INTEL-ITERATOR — AWS Intel

[Historical report](README.md): **Parked**.

```text
Pipeline Slots (100%) — historical baseline / candidates
├── Frontend_Bound     unavailable
├── Bad_Speculation    unavailable
├── Backend_Bound      unavailable
│   ├── Memory_Bound   unavailable
│   └── Core_Bound     unavailable
└── Retiring           unavailable
```

No matching TMA slot capture is retained for this historical experiment. Timing, instruction counts and sampled hotspot shares do not supply this classification. Collect matched baseline/candidate counters on the stated architecture before assigning a TMA mechanism.

**New baseline diagnostic, 20 October:** [measured Intel L2 trees](../../../../../TOPDOWN-ASSESSMENT-20261020/README.md#tma-classification). Different profiling runner/build; these values do not retroactively classify the historical B candidate.
