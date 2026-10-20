# Intel parked-work profile sweep

**Launcher correction prepared — diagnostic only; source NONE.** Cover all Intel parked families and
unfinished update-path work before choosing another optimization. Historical decisions
remain34 attempts:18parked /16rejected /0approved. This adds no implementation population.

| Work | Coverage | Decision question |
|---|---|---|
| Iterator A/B | Baseline/A/B:100K/1M full and score-only;100K reverse/fraction, exact failing seed1 | Does removed offset work change the pipeline/hotspot, including adverse guards? |
| Corrected scan B | Baseline/B:100K/1M primary; trim319 signed-zero guard and resize319 signed-zero | Where does cost move when SIMD chunks exist versus the seven-member no-chunk guard? |
| Update NONE | Baseline: same/position/nearby/distant/original ×100K/1M | Does lookup still dominate; is an update-only change worth proposing? |

Independent [inventory](INDEPENDENT-INVENTORY.md) separates these from rejected lookup,
iterator C and old-source scan. Corrected-adapter baseline precision debt remains;
profiles do not qualify its30 noisy cells. Original failed schedules remain unchanged.

Attempt1 passed177 build/validation commands and all36 completed semantic cases,
then all36 launches failed before readiness: controller CPU0 affinity restricted
numactl’s default CPU mask. No TMA/counter/sample capture occurred.
[Failure audit](attempt1/INDEPENDENT-AUDIT.json) preserves every failed launch.
V2 adds `numactl --all` before absolute CPU2 placement, verifies unchanged binaries,
and reuses completed preparation. [Corrected protocol](protocol-v2.json).

## Frozen collection

[Protocol](protocol.json):36 configurations, each3×5s L2 TMA,1×5s exploratory L3,
3s cycles/instructions/reference-cycles/branch counters,3s PID-scoped cycles sampling.
Current source37efd287f; exact retained patches, isolated builds, Clang18/O3.
CPU2/NUMA0, sibling50 online. The profiler runner is freshly checked idle; only its
OSS coordinator is stopped under a bounded40-minute job and45-minute recovery timer.

L2 needs five valid intervals/window, four finite slot roots summing100±0.3pp,
100% scheduling, workload affinity/alive, sibling≤1%, workload/CPU accounting≤1%.
Every raw failure is retained; no retry. L3 mixed units/low scheduling stay exploratory.
Counters and samples carry their own scope/return codes. Raw perf data stay outside
Git; commands, sample reports and SHA256 hashes are committed.

Completed original/profile-driver semantic parity, native/sanitizer original tests,
iterator oracles and same-mode baseline/candidate owned-byte parity precede collection.
Allocator-dependent memory is never equated across native and sanitizer builds.
Driver changes only widen work counts and add a readiness hook before measured work;
the original referee files remain unchanged. These are diagnostic binaries, not a
claim that profiles transfer to old timing binaries. Long profile loops terminate
after capture, so completed end-oracles are separate evidence.

Update trees change during the windows. Report window order/elapsed phase; do not
assume stationary state or invent operations completed during a profile. No cycles
or instructions per operation without measured work counts. A different profiler
host cannot causally explain the earlier secondary-host timing failures.

## TMA classification

Pending fresh captures for every cell/build above:

```text
Pipeline Slots (100%) — baseline and candidate separately
├── Frontend_Bound    unavailable (collection pending)
├── Bad_Speculation   unavailable (collection pending)
├── Backend_Bound     unavailable (collection pending)
│   ├── Memory_Bound  unavailable
│   └── Core_Bound    unavailable
└── Retiring          unavailable (collection pending)
```

## Provenance

Root Codex controller and separate intel_b_review agent; actual serving models,
token usage and costs unknown. Own/shared MCP consultations are explicitly labelled.
CPU-perf retrieval currently has0/287 sources indexed and supplies no supporting
passages. Topdown collector source71dea5e, pmu-tools2026.4.7.0; explicit CPU2 scope
bypasses the known PID→CPU0 path. Read-only normalized slot imports will query the
actual MCP; raw units and all original counters remain available.
