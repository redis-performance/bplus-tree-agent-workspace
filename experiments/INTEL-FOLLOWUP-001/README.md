# Intel follow-ups

**16/16 configurations;48/48 L2 windows qualify. Source NONE.**
Secondary Intel runner restored: OSS running, sibling50 online, capture/recovery units
inactive, no owned workload. [Live release](RELEASE-FINAL.json).

**Best parked lead: iterator B.** At1M full output, Memory Bound34.07→28.15% and
Retiring46.81→53.01%; Frontend pressure increases. This is a profile lead, not a speedup.
Update1M remains≈69% Memory Bound. Scan B has mixed frontend/speculation/memory effects.
[Decisions and next gates](ASSESSMENT.md).

```text
Pipeline Slots (100%)            Iterator base    Iterator B
├── Frontend_Bound                       0.80%         1.63%
├── Bad_Speculation                      1.60%         1.20%
├── Backend_Bound                       50.89%        44.09%
│   ├── Memory_Bound                    34.07%        28.15%
│   └── Core_Bound                      16.82%        15.91%
└── Retiring                            46.81%        53.01%
```

[All iterator classifications](ITERATOR.md) · [Update](UPDATE.md) · [Scan](SCAN.md).
Three5s windows per build, same exact prior binaries/fixtures, CPU2/NUMA0, sibling50
offline during capture. New host/SMT condition; do not pool with earlier measurements.
Ambient Parca remained enabled; CPU/workload accounting passed the1% gate.
Cache-level/DRAM slot breakdown and cycles/op remain unavailable.

PEBS/LBR probes captured samples but **failed scheduling-evidence validation**. Both
retained; no retries/deep repeats. [Gates](PROBE-GATES.json) ·
[Sampling configuration fix to validate next](SCHEDULING-EVIDENCE.md).

Fresh8 native/sanitizer tests,12 cache-oracle checks and48 semantic outputs passed.
[Protocol](protocol.json) frozen in52c039e04; bounded1500s execution with30min recovery.
Actual CPU-perf/topdown MCP use, raw checksums, independent review and activity are retained.
No source adoption, new population or change to34 attempts (18PARK/16REJECT/0approved).

Earlier profiles: exact libc/debug attribution and21,601-sample audit completed.
[Offline review](INDEPENDENT-OFFLINE-REVIEW.md) ·
[Ownership/annotation corrections](../INTEL-PARKED-PROFILES-001/CORRECTIONS-20261020.md).
