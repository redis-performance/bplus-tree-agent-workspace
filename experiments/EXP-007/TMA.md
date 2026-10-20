# TMA classification

Supplement added 20 October 2026; historical decisions and raw evidence are unchanged.

## EXP-007 — Apple M1

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

No compatible slot-classification capture is retained for this Apple experiment. Linux Intel/Neoverse measurements cannot fill these values. Collect matched baseline/candidate counters on the stated architecture before assigning a TMA mechanism.

