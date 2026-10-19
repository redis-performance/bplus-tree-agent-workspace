# ARM iterator frontend diagnostic

The user authorized continuing the optimization effort after the completed ARM mask
rejection. This diagnostic investigates the opposite timing directions in the
original benchmark and HARNESS-004. The rejected candidate remains rejected; no
new implementation or source adoption is authorized by a favorable diagnostic.

Status: **Native controls/comparison complete; matched profiles granted.**
Independent restoration timer11:45UTC and read-only audit11:45:10UTC are armed.
All six native cells qualify; the comparison reproduces primary gains and guard
losses. The corrected matched-profile phase has a separate1,200-second grant. Attempt1 failed before
measurement and automatically restored OSS; its verified handback is retained.
[Results and chart](RESULTS.md), [live status](STATUS.md) and
[profile grant](PROFILE-GRANT.json) track execution.

## Question and falsifiable hypothesis

Does the exact mask rewrite reduce scoped retired instructions in both benchmark
programs, despite their opposite elapsed-time outcomes? The hypothesis is that the
instruction reduction repeats across the two programs, both sizes, and both guard
directions. Any paired instruction non-decrease falsifies that universal direction
claim. Counter validity, exact source/code identity and scope controls must pass
before interpreting it. Instruction counts alone cannot explain cycle differences.

Primary and guard fixtures are deliberately retained, not made interchangeable:

| Property | Original primary | HARNESS-004 mask 4 |
|---|---|---|
| Scores | 0 through N−1 | i−N/2 |
| Allocated member objects | 2N | N |
| Checksum consumer | Numeric double-to-uint64 conversion | Exact IEEE bits plus visited count |
| Warm-up | One shuffled lookup pass | Full outside-timing oracle and three traversal passes |
| Requested visits | 50M | 20M |
| Directions | Forward | Forward and reverse |

Within each frontend, source pairs share fixtures, options, allocator, CPU and
same-session measurement schedule. Cross-frontend comparisons are descriptive;
no single-factor causal claim follows from these confounded programs. New fixture
or caller crossover experiments would require a separate preregistration.

## Preregistered bounded execution

Exact baseline: `13e459ff8800be3f02b6b45c87dd7b0c39453fa9`.
Exact rejected patch SHA-256:
`ca14579cbf4325816d5511697cb0bec5ab0e618ef661830acbc4bfe72a5cc88f`.
The original referee, target source and historical artifacts remain unchanged.

- Six native cells: primary forward / guard forward / guard reverse × 100K / 1M.
- Fresh seeds 1601–1603, six ABBA blocks per cell: 144 baseline-only A/A processes,
  then 144 exact baseline/candidate processes, separately capped at 600 seconds.
- Scoped profile: seeds 1701–1703, the same six modes/sizes, both source variants;
  36 cycle captures and 36 PMU runs, plus known-work, disabled, semantic and
  own-binary mapping controls. All preparation/profiling fits one fixed 1,200-second cap.
- Instrumentation qualification within that cap: 12 source/mode/size cells, three
  blocks per cell; 144 original-binary A/A processes plus 144 original-versus-disabled
  comparisons. Every relevant block must be within ±1% with windows at least 10 ms
  for timing attribution to transfer. Missing/noisy controls mean PARK for that claim.
- Every capture maps sampled tree instructions to its own original and actual
  timing binary; primary maps cannot qualify guard code. Unknown frames, losses,
  warnings, changed callers and raw per-run data are retained.

Native execution freeze fa190bd9b passed independent Intel5fa4ec90c and AMD130d5c904
review before its baseline-only grant. The corrected profile freeze2d4e93924 has separate root/Intel/AMD review and
grant3e04f174b, with allocator modes separated and unscaled stat counters. Each phase requires
fresh exclusivity/identity checks and its entire cap plus margin before the lease
ends. No automatic retry, row removal, threshold change, alternate candidate or
extension based on results. A completed diagnostic can end with NONE for a new
optimization hypothesis if evidence is insufficient.

## Review and publication

The existing ARM worker prepares the protocol; Intel independently audits frontend
comparability; AMD independently audits scope and attribution requirements. Root
reviews and coordinates. These are actual separate agents, not a new optimization
proposal/implementation population. Exact serving models and token/currency costs
are unknown. If a new optimization round becomes eligible, follow both three-agent
population stages in `docs/POPULATION.md` after fresh baseline/profile prerequisites.

[Activity](ACTIVITY.md) · [Status](STATUS.md) ·
[Previous rejection](../ARM-MASK-FOLLOWUP-001/RESULTS.md).

## Independent preparation reviews

[Intel comparability review](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/e345fa9b6/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/030-arm-frontend-comparability/REVIEW.md)
and [AMD attribution requirements](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/d5fc035e0/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/035-arm-dual-frontend-diagnostic-review/REQUIREMENTS.md)
independently confirm the distinct fixtures and missing guard/candidate profiling.
Neither finds a defect invalidating the earlier rejection. The profile's validity
gates must be separate from hypothesis direction: a counter-direction mismatch is
evidence to retain, not a reason to filter or rerun a capture. Untimed leaf-layout
census and source-linked caller maps are required for stronger attribution.

The new release auditor uses a distinct `bplus-front-20261019` namespace. It checks
fresh release markers, matching saved/live coordinator PIDs, inactive owned slice,
zero recursive owned processes and inspection errors. The reviewed attempt2 timer is armed11:45UTC, with a separate read-only audit
scheduled11:45:10UTC. The first acquisition failure and verified automatic restoration
are retained in [the activity log](ACTIVITY.md).
