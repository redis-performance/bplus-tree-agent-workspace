# AWS ARM overnight results

**Source NONE:2 measured populations,0 accepted/1 rejected/1 parked;1 separate iterator
replication PARK.** See the [morning report](MORNING-REPORT.md) for complete decisions,
evidence, patches, baseline identities and remaining gates.

The experiment runner is idle. **Campaign lease ACTIVE until08:00UTC /09:00Lisbon;
actual release and OSS restoration PENDING.** No new experiments are planned.

- [Original baseline](001-baseline/summary.csv):120 processes/960 rows,18/40 qualified.
- [Corrected adapter baseline](013-corrected-adapter-baseline/RESULT.md):120 processes/
  960 rows,21/40 qualified; distinct identity, no old/new speed claim.
- [Decoder](003-decode/RESULT.md):PARK; [iterator replication](005-iterator/RESULT.md):PARK.
- [Corrected NEON](017-corrected-neon/RESULT.md):REJECT; all three fail both primaries.
- [Fold follow-up](021-fold-predicate-review/COMMON-PACKET.md):chairNONE, no implementation.
- [Independent reviews](023-amd-iterator-review/RAW-REVIEW.md), [activity](ACTIVITY.md),
  [status](STATUS.md), [handoff](HANDOFF.md).

Earlier milestone descriptions and superseded states remain in ACTIVITY and Git;
immutable experiment reports and evidence seals are unchanged.

## Additive preparation update — 2026-10-19T06:22:00.520959+00:00

Root requested a separate [corrected ARM score-only iterator diagnosis](024-corrected-iterator/PLAN.md). Plan/execution freeze prepared; no launch, pending root and independent AMD review plus post-ambient idle handoff. Morning results and all prior decisions remain unchanged.

Profile-only024 completed: [immutable result](024-corrected-iterator/PROFILE-RESULT.md),51 commands/6 captures/970 samples, controls pass. No A/A/candidate yet; runner idle for independent raw review and root phase grant.
