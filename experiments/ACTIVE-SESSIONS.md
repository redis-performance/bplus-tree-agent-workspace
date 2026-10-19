# Active optimization sessions

M6 updated 2026-10-19T08:38:59.265187+00:00. Shared coordination index, first recorded 19 October 2026 at 08:17 UTC. Read each linked status before starting overlapping work. Source acceptance and host measurements are separate; baseline timings never qualify another host. Each owner updates its own status and publishes it to main. This index does not assert a fleet-wide lease or replace per-run exclusive-runner checks.

| Session / host | Observed state | Owner and canonical status |
|---|---|---|
| EXP-009 / local Apple M6 | PARK; fresh controls100K6/6,1M3/6; native lease released; raw audit/decision review complete | Interactive M6 root; [live status](EXP-009/STATUS.md), [result](EXP-009/RESULTS.md) |
| ARM-MASK-FOLLOWUP-001 / remote Graviton | ACTIVE ARM-only lease, hard stop 10:15 UTC; PARK after11 required control precision failures; fixed diagnostics continuing | AWS controller / ARM operator; [status](ARM-MASK-FOLLOWUP-001/STATUS.md), [plan](ARM-MASK-FOLLOWUP-001/README.md) |
| Apple M1 | Last confirmed checkpoint consumed M6 at 06:50 UTC, no further source experiment queued | [Pinned consumption receipt](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/85afa6c7b798130452ca9dbd63082337e8bd78b7/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/026-m1-gate-confirmation/README.md) |
| Intel / AMD | Overnight work closed, runners released; no new lease in the ARM-only follow-up plan | [AWS handoff](NIGHT-EXPLORATION-001/AWS-MORNING-REPORT.md) |

The completed overnight M6 campaign remains closed with source NONE. EXP-009 is newly authorized work with fresh corrected-adapter profiles/controls and separate counts. No CPU-specific or input guard is accepted merely because a scoped timing lead exists.
