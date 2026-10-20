# Intel iterator B — TMA-led qualification

**PARK / source NONE.** Fresh baseline passes46/48 control blocks. Two100K guards
fail the frozen±1% precision gate: integer reverse **−1.631%**, fraction forward
**−1.160%** (both first block, seed1). Both primary cells pass6/6. No B timing,
retry, source adoption or new implementation population.

Selected the exact retained **B32-bit cached-offset patch** because prior Intel TMA
showed increasing Memory Bound with size and the historical iterator profile located
offset work. B preserves16-byte iterator state. This prioritizes a falsifiable test;
baseline TMA alone cannot establish B's benefit or mechanism.

## Measured outcome

| Baseline cell |100K blocks passed|1M blocks passed|
|---|---:|---:|
| Integer forward, full output (primary)|6/6|6/6|
| Integer reverse, full output|5/6|6/6|
| Integer forward, score only|6/6|6/6|
| Fraction forward, full output|5/6|6/6|

All192 fixed runs completed, with exact fixture/checksum/owned-byte parity, CPU2
endpoints,≥500ms windows and≤1% sibling occupancy. Failed rows remain included.
Independent reconstruction: [audit](independent-audit.json), [review](FINAL-REVIEW.md).
Raw rows, process envelopes and original automated decision: [results](results/).

Baseline and B pass original43 tests natively and under ASan/UBSan, plus both cache
oracles in both builds. The additive long-window referee passes64 original/new fixture
pairs, a completed100,000,001-visit request and11 parser boundary cases. Original
source/referee files are unchanged; [build hashes](results/build-sha256.txt).

## TMA classification

Baseline on **secondary Intel Sapphire Rapids**, three10-second L2 captures per size.
Means of30 one-second intervals; percentages are shares of total pipeline slots.

```text
Pipeline Slots (100%) — baseline 100K
├── Frontend_Bound           1.10%
│   ├── Fetch_Latency        0.30%
│   └── Fetch_Bandwidth      0.80%
├── Bad_Speculation          3.20%
│   ├── Branch_Mispredicts   3.10%
│   └── Machine_Clears       0.00%
├── Backend_Bound            12.09%
│   ├── Memory_Bound         7.80%
│   └── Core_Bound           4.29%
└── Retiring                 83.61%
    ├── Light_Operations     80.51%
    └── Heavy_Operations     3.10%
```

```text
Pipeline Slots (100%) — baseline 1M
├── Frontend_Bound           0.75%
│   ├── Fetch_Latency        0.40%
│   └── Fetch_Bandwidth      0.45%
├── Bad_Speculation          2.80%
│   ├── Branch_Mispredicts   2.70%
│   └── Machine_Clears       0.00%
├── Backend_Bound            22.37%
│   ├── Memory_Bound         16.50%
│   └── Core_Bound           5.87%
└── Retiring                 74.07%
    ├── Light_Operations     71.37%
    └── Heavy_Operations     2.70%
```

L1 sums100.00% and100.00%; raw interval sums stay within0.3pp. Child estimates can
differ from their parent by rounding/model residuals; none are rescaled. L3 cache/DRAM
breakdown is uncollected. Candidate B Frontend_Bound, Bad_Speculation, Backend_Bound,
Retiring and all children are **unavailable**: qualification stopped before comparison.

Memory Bound rises7.80%→16.50%; this supports investigating dependent memory work.
It does not attribute the two guard-control failures, which used different workloads.
Retiring is useful work under this model, not proof that instructions cannot be removed.

Tool: topdown-profiler71dea5e + pmu-tools2026.4.7.0; same baseline executable as
A/A (`dc323d69…b86a8`), CPU2 collector scope, NUMA0,16-byte members, integer forward
full output, seed7103. Workload reaches fixture/oracle/warmup readiness before capture.
Run IDs/raw hashes and all means/ranges: [TMA summary](tma-summary.json).
Actual [MCP funnel calls](topdown-mcp-calls.json) use an isolated slot-only database;
`% Slots`/`% Slots <` are canonicalized to `%_Slots`, without changing values. MUX and
other denominators are excluded. [Reproducer](consult_topdown.py).

All six captures pass100% event scheduling, exact four-root classification, workload
alive/CPU2 affinity and workload-versus-CPU accounting≤1%; maximum error0.1954%,
sibling occupancy≤0.0944%. Long profile processes terminate after capture, so their
full20B-visit post-run checksum is uncollected; timing processes complete their checks.

**Analysis correction:** toplev's advisory watchdog warning precedes its CSV header.
The frozen collector mistakenly treated that warning as the header and marked all
profiles invalid. Independent analysis starts at the actual header and checks unchanged
gates. Original false flags remain in `results/RESULT.json`; no capture was rerun,
watchdog setting changed or threshold relaxed. The real A/A failures still require PARK.

## Next gate

Do not repeat this unchanged schedule or time B using only the favorable cells.
First preregister a diagnostic for the two failing guards: capture frequency/residency,
cycles/instructions and CPU-versus-wall accounting around identical windows, including
fixed cold-start and steady-state controls. Both failures happened in the first block;
that observation alone does not establish warmup or frequency as the cause. A validated
measurement change must requalify all eight cells before a separately reviewed B stage.
Acceptance still needs full guards, matched B TMA, held-out confirmation and review.

## Execution and provenance

Current fleet main and live SSH checks found primary Intel busy and secondary Intel
idle with no containers/reservation conflict. The bounded owned job stopped only the
secondary OSS coordinator, then restored it. [Live release proof](RELEASE.txt):
coordinator RUNNING, owned service/recovery timer inactive, no owned workload.

[Protocol](protocol.json) and harness committed/pushed as `b1aacd747` before execution:
baseline source`c6112e052`, exact historical B patch, separate builds, Clang18`-O3`,
identical allocator/assertions. New condition: NUMA0 binding and600ms calibration target;
no clock/SMT/global package changes. Counts frozen before A/A; no prior timing reused.
[Inputs](input-manifest.json), [tools](tool-manifest.json), [pre-review](PREEXEC-REVIEW.md).

Root Codex controller plus independent `intel_b_review` agent; exact serving models,
tokens and currency costs unknown. No new proposal/implementation population.
CPU-perf`library_status`/`ask` used this session:0/287 indexed sources, zero supporting
passages; [consultation](CONSULTATION.json). [Activity](ACTIVITY.md).
