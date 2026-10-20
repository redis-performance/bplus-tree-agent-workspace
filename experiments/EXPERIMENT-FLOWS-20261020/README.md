# Experiment flows by architecture

[TMA classification for every experiment](../TMA-COVERAGE.md) · [Fresh Intel pipeline trees](../TOPDOWN-ASSESSMENT-20261020/README.md)

**33 experiment attempts: 17 parked, 16 rejected, 0 approved.**

| Target | Attempts | Parked | Rejected | Approved |
|---|---:|---:|---:|---:|
| ARM (M1, M6, Graviton) | 24 | 14 | 10 | 0 |
| Intel | 4 | 2 | 2 | 0 |
| AMD | 5 | 1 | 4 | 0 |

![Architecture overview](overview.png)

[All attempts](all-attempts.svg) · [New populations only](all-populations.svg) · [ARM](arm.svg) · [Intel](intel.svg) · [AMD](amd.svg) · [Replications / preflights](followups.svg)

## Counting rules

- One main-chart ribbon = one recorded attempt: new population, exact-patch replication or qualification. Variants A/B/C remain within a population. Labels POP / REP / AA identify the kind.
- ARM includes Apple M1, Apple M6 and AWS Graviton. Intel and AMD identify separate x86-64 targets.
- M1’s 9 and M6’s 12 ledger totals share seven M1 experiments (EXP-002–008). Count those once: **9 + 12 − 7 + 8 AWS = 22**. M6 adds five new populations.
- Approved means an adopted source optimization. Passed tests, accepted plans and merged harnesses do not qualify.
- The 11 follow-ups (**8 parked / 3 rejected**) are now included in every main/architecture chart, and also have a detail chart. Thus Intel shows both original populations plus its scan replication and corrected-source preflight: **4 attempts**. Historical implementation-population totals stay **22 = 9 parked / 13 rejected / 0 approved**. A failed preflight is parked, not a rejected candidate.
- Follow-ups retain their own source and host scope. The ARM mask and original Intel scan replays progressed from PARK to REJECT; their parent experiments retain their original decisions.
- Baseline runs, profiles, oracle suites, offline diagnoses and proposal-only NONE reviews are supporting work, not additional three-way optimization decisions. See the [full log](../EXPERIMENTS.md). M6’s EXP-004 decoder replay is diagnostic only; EXP-008 replay selected NONE, so neither is relabelled as an accepted/rejected/parked population.

[How to advance the parked work](../PARKED-NEXT-STEPS-20261020/README.md).

## Candidate populations

| Architecture / host | Experiment | Outcome | Decisive limit |
|---|---|---|---|
| ARM / Apple M1 | [EXP-002 · Score-only iterator](../EXP-002/README.md) | Rejected | Fresh no-output guards regress. |
| ARM / Apple M1 | [EXP-003 · Outline member decode](../EXP-003/README.md) | Rejected | Fresh full-output guards regress. |
| ARM / Apple M1 | [EXP-004 · Cross-word predicate](../EXP-004/README.md) | Parked | Guard precision remains unresolved. |
| ARM / Apple M1 | [EXP-005 · Packed-score mask](../EXP-005/README.md) | Parked | Fresh primary confidence gate fails. |
| ARM / Apple M1 | [EXP-006 · Inline tag search](../EXP-006/README.md) | Parked | Provisional C; no accepted source. |
| ARM / Apple M1 | [EXP-007 · Bulk score decoder](../EXP-007/README.md) | Parked | Short-range guard regressions block universal adoption. |
| ARM / Apple M1 | [EXP-008 · Short-range fallback](../EXP-008/README.md) | Parked | No cutoff qualifies; short-range regressions. |
| ARM / Apple M1 | [M1-RANK · Shorter-side rank](../NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/002-rank/RESULT.md) | Rejected | No consistent dual-size gain. |
| ARM / Apple M1 | [M1-DECODE · Count-one decoder](../NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/005-decode/RESULT.md) | Parked | No qualified A/A cells; guard losses. |
| ARM / Apple M6 | [M6-RANK · Shorter-side rank](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/002-rank/RESULTS.md) | Rejected | No dual-primary winner. |
| ARM / Apple M6 | [M6-UPDATE · Update repacking](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/003-update/RESULTS.md) | Rejected | 100K primary fails. |
| ARM / Apple M6 | [M6-LOOKUP · Physical-score lookup](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/RESULTS.md) | Rejected | 100K-only lead; dual-primary gate fails. |
| ARM / Apple M6 | [M6-DECODE · Count-one decoder](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/005-decode/RESULTS.md) | Rejected | Universal guards fail. |
| ARM / Apple M6 | [M6-CALLER · Lookup caller specialization](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/006-followup/RESULTS.md) | Rejected | No implementation clears both sizes. |
| ARM / AWS Graviton | [ARM-COUNT1 · Count-one decoder](../NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/003-decode/RESULT.md) | Parked | Failed precision; identical candidate code and guard concerns. |
| ARM / AWS Graviton | [ARM-NEON · Bounded NEON scan](../NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/MORNING-REPORT.md) | Rejected | All three corrected-adapter implementations slower in every primary block. |
| Intel / AWS Intel | [INTEL-LOOKUP · First-match SSE2 lookup](../NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/002-lookup/implementation-selection.md) | Rejected | Every primary block slower. |
| Intel / AWS Intel | [INTEL-ITERATOR · Iterator offset cache](../NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator/README.md) | Parked | Noisy control and incomplete fixed schedule. |
| AMD / AWS AMD | [AMD-LOWERBOUND · Lazy lower-bound decode](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/002-lowerbound/implementation-selection.md) | Rejected | Dual-primary speed gate fails. |
| AMD / AWS AMD | [AMD-BUILDER · Leaf builder metadata](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/004-builder-write/implementation-selection.md) | Rejected | Every primary block slower. |
| AMD / AWS AMD | [AMD-CHUNKS · Full packed-move chunks](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/005-full-chunks/implementation-selection.md) | Rejected | No primary block reaches 2%. |
| AMD / AWS AMD | [AMD-SCAN · SSE2 all-match scan](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/008-scan-tags/implementation-selection.md) | Parked | 1M control fails; guards and profile validation unresolved. |

## Replications and qualification attempts

| Architecture / host | Follow-up | Outcome | Parent / decisive limit |
|---|---|---|---|
| ARM / Apple M1 | [Initial baseline qualification](../EXP-001/README.md) | Parked | Only 1/41 cells qualifies. |
| ARM / Apple M1 | [Lookup precision preflight](../EXP-009-M1-AA-001/RESULTS.md) | Parked | A/A passes 1/6 at 100K, 2/6 at 1M. |
| ARM / Apple M6 | [EXP-007 bulk replay](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/MORNING-REPORT.md) | Parked | EXP-007: Short windows and failed controls; conditional private lead. |
| ARM / Apple M6 | [NEON replay preflight](../NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/023-neon-replication/RESULTS.md) | Parked | ARM-NEON: Two 1M controls fail; candidate not timed. |
| ARM / Apple M6 | [Guarded lookup preflight](../EXP-009/RESULTS.md) | Parked | M6-LOOKUP: Three 1M controls fail; candidate not timed. |
| ARM / Apple M6 | [Clock-bracket preflight](../M6-CLOCK-BRACKET-001/RESULTS.md) | Parked | M6-LOOKUP-AA: New harness validated; only 2/6 1M controls pass. |
| ARM / AWS Graviton | [Intel iterator replay](../NIGHT-EXPLORATION-001/AWS-DECISIONS.md) | Parked | INTEL-ITERATOR: Both primary controls fail. |
| ARM / AWS Graviton | [EXP-005 mask follow-up](../ARM-MASK-FOLLOWUP-001/RESULTS.md) | Parked → Rejected | EXP-005: Nine qualified guard cases regress; later diagnostic leaves REJECT unchanged. |
| Intel / AWS Intel | [SSE2 scan replay](../NIGHT-EXPLORATION-001/AWS-DECISIONS.md) | Parked → Rejected | AMD-SCAN: Qualified supplemental small-leaf guard regresses. |
| Intel / AWS Intel | [Corrected scan preflight](../NIGHT-EXPLORATION-001/AWS-DECISIONS.md) | Parked | INTEL-SCAN-REPLAY: Known guard A/A fails before candidate timing. |
| AMD / AWS AMD | [Corrected SSE2 replay](../NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/019-corrected-B-replication/RESULT.md) | Rejected | AMD-SCAN: Only 2/6 blocks per size meet 2% gate. |

## Reproduce

```sh
python3 experiments/EXPERIMENT-FLOWS-20261020/render.py
```

Requires Matplotlib. PNG and SVG exports come from [experiments.json](experiments.json); each of its 33 records pins its evidence SHA-256. [Validation](VALIDATION.json) checks source hashes, unique IDs, parent references and totals. Widths count experiments, not speedup, benchmark runs or probability.

Source snapshot: `63d1f03868039605514002ac7f3abcc95757bf5d`. Original campaign decisions remain unchanged. The [previous full README](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/63d1f03868039605514002ac7f3abcc95757bf5d/README.md) retains the historical presentation; detailed reports and images remain in place.
