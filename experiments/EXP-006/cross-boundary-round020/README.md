# EXP-006 cross-boundary compatibility

**PASS: 80 semantic cells and 48 builds. Source adoption NONE; C/PARK unchanged.**
The fixed [plan](PLAN.md) ran exact retained control/A/B/C sources against the frozen
partial-promotion, narrowing and external-relocation oracles. Discovery seed92503
uses debug assertions; held-out92521 removes debug-only assertions but retains all
unconditional checks. Both nativeO3 and O1ASan/UBSan builds pass.

| Oracle | Cells | Checked history |
|---|---:|---|
| Partial promotion | 16 | 18 count/layout clones per cell; exact masks/bits/canaries, external score transfers, liveSCAN and source ownership |
| Widening then narrowing | 16 | Natural width changes, dense ID renumbering,4096 surviving continuous anchors, absent-member lookup |
| External relocation | 48 | Active mixed-width clone, full moves and partial declines; every allocation visit and usable-byte delta |

Logical digests agree across all eight source/build combinations per seed and mode.
Each partial cell reports25 complete models and over21million exact member/score
results; the narrowing cells report3 models, and each external mode reports3 models.
These are oracle counts, not timing results or an exhaustive correctness proof.

All five [preregistered fault transfers](FAULT-PLAN.md) on C are detected:

- Cached member table after promotion: ASan heap-use-after-free in zbtreeScores.
- Last-hit omission: the exact returned-mask assertion fails.
- Outside-count write: the unchanged output-canary assertion fails.
- Stale renumbered leaf ID: the first surviving ID/registry assertion fails.
- Shallow external clone: the external-pointer disjointness assertion fails.

The [fault manifest](faults/manifest.json) retains exact patches, source/binary hashes,
commands and failure logs. These repeat known fault families; none is a production
bug or a new optimization variant. Raw sanitizer paths remain in ignored snapshots;
public stderr replaces only the workspace path. No assertion was weakened.

Reproduction commands used in this round:

```sh
python3 experiments/EXP-006/cross-boundary-round020/run.py
python3 experiments/EXP-006/cross-boundary-round020/faults.py
```

The drivers refuse existing snapshot/output directories and contain historical cutoff
times. Do not rerun them into retained evidence; create a fresh preregistered attempt.
[Manifest](manifest.json) stores full per-child commands, stdout/stderr hashes, source
snapshots and binary hashes. [Round audit](../../OVERNIGHT-2026-10-17/ROUND-020-VERIFY.json)
independently checks the schedule, digests, hashes and patch reconstruction.

This is new EXP-006 coverage of existing BOUNDARY-023/025 families, not a new named
suite, harness, qualification, measurement diagnostic or population. No timing was
collected. The long-key and single-lane performance guards remain unresolved.
