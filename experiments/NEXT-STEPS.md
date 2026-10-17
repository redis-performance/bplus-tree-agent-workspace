# Draft experiment queue

| Order | Work | Entry criterion | Deliverable |
|---|---|---|---|
| 1 | EXP-001 baseline qualification | dedicated runner and frozen release build | A/A evidence, profiles, calibrated cases |
| 2 | Fill fixture gaps for the observed hot path | evidence from EXP-001 | reviewed referee update and requalified baseline |
| 3 | EXP-002 selection population | qualified baseline + profile | 3 proposals, chair ranking, one hypothesis or NONE |
| 4 | EXP-002 implementation population | selected hypothesis | 3 isolated patches, correctness, serial comparison |
| 5 | Confirmation and review | eligible measured winner | fresh benchmark/profile, review, accept/reject/park |

Potential later families: score decode/search, member-index probing, split/merge movement,
allocation/occupancy, batch/ordered operations. None is selected before profiling.
