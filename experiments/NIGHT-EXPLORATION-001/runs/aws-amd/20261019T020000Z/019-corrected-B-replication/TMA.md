# TMA classification

Supplement added 20 October 2026; historical decisions and raw evidence are unchanged.

## AMD-CORRECTED — AWS AMD

[Historical report](RESULT.md): **Rejected**.

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
