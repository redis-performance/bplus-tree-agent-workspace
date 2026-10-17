# Draft experiment queue

| Order | Work | Entry criterion | Deliverable |
|---|---|---|---|
| 1 | Requalify EXP-001 after referee observability improvements | separate harness commit; see local M1 results | CPU/thread timing, calibrated durations, A/A precision |
| 2 | Fill fixture gaps for the observed hot path | evidence from EXP-001 | reviewed referee update and requalified baseline |
| 3 | EXP-002 selection population | qualified baseline + profile | 3 proposals, chair ranking, one hypothesis or NONE |
| 4 | EXP-002 implementation population | selected hypothesis | 3 isolated patches, correctness, serial comparison |
| 5 | Confirmation and review | eligible measured winner | fresh benchmark/profile, review, accept/reject/park |

The [M1 evidence](EXP-001/local-m1-2026-10-17/README.md) prioritises investigation of
leaf-tag scanning for short keys, hashing for long keys, update movement and allocator
size classes. These are proposals for the selection population, not selected candidates.
