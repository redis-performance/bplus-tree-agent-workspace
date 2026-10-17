# Experiment log

Append-only decisions and evidence; correct earlier records with a dated addendum.
Preparation and baseline qualification do not count as accepted optimisations.

| ID | Date | Purpose | Status | Decision |
|---|---|---|---|---|
| [PREP-001](PREP-001/README.md) | 2026-10-17 | Extract standalone tree, validate adapter, prepare microbenchmarks and population protocol | COMPLETE | No source optimisation |
| [EXP-001](EXP-001/README.md) | 2026-10-17 | Qualify standalone baseline, A/A precision and profiles | PLANNED | NOT RUN |

Accepted: **0**. Rejected: **0**. Parked: **0**. Population rounds executed: **0**.

## 2026-10-17 — EXP-001 local M1 addendum

User authorised local benchmarks and CPU Performance Engineering MCP exploration.
[Run and findings](EXP-001/local-m1-2026-10-17/README.md): 144 serial processes, 984 rows,
four sampled profiles, generated-code inspection and allocator/clock probes. All checksum
checks pass. Baseline qualification PARKED: only 1/41 cells meets the preregistered gates;
frequency and placement remain unmeasured. Short-key leaf-tag scanning, long-key hashing
and the allocator's 320/321-byte size class are documented follow-ups. No source candidate,
population decision or accepted optimisation. Optimisation counts above remain unchanged.
