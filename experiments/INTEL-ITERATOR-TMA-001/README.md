# Intel iterator B — TMA-led parked-work continuation

Status: **PREPARED / baseline qualification pending**. Source adoption NONE.

## Selection

Resume the exact retained **B 32-bit cached-offset patch**, not a new source variant.
The prior [Intel TMA](../TOPDOWN-ASSESSMENT-20261020/README.md) measured Memory Bound
8.55%→16.47% at100K→1M with Frontend Bound<1%. Combined with the historical iterator
hotspot, this supports testing removed offset work/dependent loads. It does not prove
B's mechanism or gain. AMD scan has unresolved binary/timing transfer; Apple decoder
has adverse guards and no comparable TMA. This is a research priority, not acceptance.

## Frozen baseline stage

[Protocol](protocol.json): current tree baseline `c6112e052`, exact archived B patch,
separate source/build directories, Clang18 `-O3`, identical allocator/assertions.
Secondary Intel Sapphire Rapids chosen after checking current fleet main and live SSH:
primary Intel busy; secondary idle with no active containers or conflicting reservation.
CPU2 and NUMA0 bind; sibling50 online, occupancy recorded. No global clock/SMT changes.

New measurement condition: explicit NUMA memory binding plus600ms target windows,
rather than carrying forward the old short controls. This is not a proven noise cure.

A separate referee changes only `--ops` range and adds a pre-timer readiness hook.
The original driver and all semantic checks remain. First validate64 original/new
fixture pairs, a completed >100M-visit boundary, native/sanitizer original43tests and
both retained cache oracles for baseline/B. Wider count arithmetic is range-checked;
uint64 checksum overflow is intentional modulo arithmetic in both referees.

Then baseline L2 TMA:3×10s per size, same executable as timing, CPU2 scope, workload
ready after fixture/oracle/warmup. All four L1 categories and100% event scheduling
required. Long profiles are terminated after capture; they are diagnostic, not timing.

Calibrate once per cell from three fixed10M-visit runs, target600ms using the fastest,
round up to whole traversals, maximum2B visits. Freeze counts before192A/A processes:
eight cells × six blocks × four identical-binary runs. Every block must satisfy±1%,
every window≥500ms, sibling occupancy≤1% over the process envelope, exact fixture/
checksum/owned bytes and CPU2 endpoints. Complete and retain the schedule within900s;
timing/occupancy failures complete the schedule and mean PARK. Process/semantic/affinity
failures stop with partial output retained. No retry or candidate timing.

Candidate comparison, full guards, fresh independent confirmation and matched
candidate TMA require a separate reviewed stage after all prerequisites pass.

## TMA classification

```text
Pipeline Slots (100%) — fresh secondary Intel baseline / B
├── Frontend_Bound     pending / unavailable
├── Bad_Speculation    pending / unavailable
├── Backend_Bound      pending / unavailable
│   ├── Memory_Bound   pending / unavailable
│   └── Core_Bound     pending / unavailable
└── Retiring           pending / unavailable
```

Candidate TMA is not authorized by this baseline-only protocol. Prior profiler-host
numbers motivate selection but do not classify this host/build. Actual results will
replace pending baseline values; missing candidate values remain explicit.

## Review and provenance

Root Codex controller; separate `intel_b_review` agent checks pre-execution and final
raw evidence. Exact serving models/token costs unknown. Existing implementation
population is retained; no new proposal/implementation population claimed.
CPU-perf `library_status`/`ask` consulted this session:0/287 indexed sources, zero
supporting passages. Reviewer checked availability independently and labels root's
ask as shared. Topdown collector pinned71dea5e; pmu-tools2026.4.7.0 staged privately
inside the task directory, without global installation or shared database writes.

Scripts: [prepare](prepare.py), [fixed campaign](campaign.py), [owned run/release](run.sh).
