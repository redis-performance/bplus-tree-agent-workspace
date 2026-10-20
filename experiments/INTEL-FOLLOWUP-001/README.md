# Intel follow-ups

**Offline attribution complete; fresh secondary-host protocol prepared.**
Source NONE. No optimization approved or new population counted.

| Follow-up | Concrete progress |
|---|---|
| Update lookup | All36 old raw profiles redecoded with exact libc/debug identity. At1M same/position, `memchr` implementation13.22%/14.36%, comparison implementation5.22%/5.43% of workload sampled period. |
| Iterator B | Corrected annotation denominators; precise load sites identified for distinguishing leaf-transition dependencies from offset arithmetic. |
| Corrected scan B | Exact primary/guard hot instructions mapped; seven-member guard samples are in scalar-tail/setup paths, not full SIMD chunks. Branch causality remains unmeasured. |

[Offline audit](INDEPENDENT-OFFLINE-REVIEW.md) verifies21,601 samples and365 hot-IP
numerators. [Decoded evidence](offline.json). `memcmp` and `bcmp` share the resolved
implementation; these samples cannot identify one caller's exclusive cost.

**Earlier-sweep corrections:** [host exclusivity and annotation denominator](../INTEL-PARKED-PROFILES-001/CORRECTIONS-20261020.md).
The profiler has another active reservation. Its old capture-quality gates remain
facts, but exclusive-host conditions were not established. Prior leads are provisional.

## Fresh diagnostic plan

[Protocol](protocol.json):16 configurations on the separately checked secondary Intel:
update100K/1M same/position; iterator1M full-output base/B and two missing score-only
pairs; corrected scan1M and two guard pairs. Three5s L2 windows per configuration.
PEBS slow-load and LBR probes precede gated duplicate captures. Unsupported or
unqualified probes are retained, with that method skipped; no retries.

Exact prior binaries, fresh correctness/semantic checks, CPU2/NUMA0. Sibling50 will
be offline only during the owned lease, restored by normal cleanup and an independent
timer. This is a new host/SMT condition, not a causal comparison with old timings.
No per-operation or stationary-state claim without in-window work counts.

## TMA classification

Fresh secondary-host captures have not started:

```text
Pipeline Slots (100%) — each baseline/candidate separately
├── Frontend_Bound    unavailable (pending new collection)
├── Bad_Speculation   unavailable (pending new collection)
├── Backend_Bound     unavailable (pending new collection)
│   ├── Memory_Bound  unavailable
│   └── Core_Bound    unavailable
└── Retiring          unavailable (pending new collection)
```

Actual CPU-perf and topdown MCP consultations are recorded; previous-run MCP queries
are explicitly labelled, not new captures. Root and independent intel_b_review;
model/token costs unknown. [Design review](INDEPENDENT-DESIGN-REVIEW.md).

Execution is bounded by `bplus-intel-followup-001.service` (`RuntimeMaxSec=1620`,
`TimeoutStopSec=15`), an inner1500s timeout and a30min recovery timer.
Private process/cgroup inventory stays off Git.
