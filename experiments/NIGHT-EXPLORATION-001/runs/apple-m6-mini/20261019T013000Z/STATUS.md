# M6 scoreboard — all queued comparisons complete, source NONE

Updated 2026-10-19T03:04:04.162366+00:00, round5 ends03:08:25UTC. Campaign ends08:00UTC/09:00Lisbon;
no experiments after07:15UTC. Last experimental child2026-10-19T03:00:37.811992+00:00;
none active. Baseline source/referee hashes unchanged.

| Target | Decision | M1 action |
|---|---|---|
| Baseline | COMPLETE/reused | baseline-attempt002;120 processes/960 rows |
| RANK-001 | REJECT/NONE | Skip exact candidates;002-rank/RESULTS.md |
| UPDATE-001 | REJECT/NONE | Skip exact candidates;003-update/RESULTS.md |
| LOOKUP-001 | REJECT dual primary/NONE |100K B exploratory only;004-lookup/RESULTS.md |
| DECODE-001 | REJECT universal policies/NONE | Count1 lead only;005-decode/RESULTS.md |
| ITERATE-001 | SKIPPED | Optional slot used by decoder |
| Fresh confirmation | NOT ELIGIBLE | No discovery survivor |

DECODE hypothesis **M6-DECODE-COUNT1-001**: original scalar at count1, frozen
EXP-007 B otherwise. Exact patches/source/referee/binary identities in
[comparison-freeze](005-decode/comparison-freeze.json).

| Candidate | Primary median | Six-block range | Uncapped qualified guard losses (any block) | Guard losses in all six blocks |
|---|---:|---:|---:|---:|
| A | -16.914% | -20.263..-0.192% | 21 | 8 |
| B | -29.952% | -34.328..-27.469% | 24 | 9 |
| C | -30.160% | -36.649..-21.475% | 22 | 10 |


All three have repeated >1% losses in uncapped qualified guard cells. Primary
A/A fails (−6.331..+1.195%);53/176 numerical qualifiers,41 capped cells.
No fresh confirmation, selected-candidate profile, independent confirmation or
independent review. Native/sanitizer decoder checks pass; two faults detected.
Baseline primary profile sufficient; three guard captures insufficient, no rerun.
Audit17424 rows/4224 effects/3 patches/17467 serial windows verifies executable
freezes and records a documentation filename collision before timing. All evidence
and initial failure retained. Original tree baseline validation reused.

Published: prior handoff a8633cde; referee80177d1e; chair e62f839d; candidates6e9e4ec8;
calibration7c671a8b; A/A b0aee748; A87c3305f8; B9df7bb2e9; C4a884419d.
Decision/audit/report publication follows. Coordinator alone writes Git.
No Git write, denial retry, permission change, sysctl retry or upstream action.

Launcher-verified Apple M6, Clang21. Frequency/DVFS/residency/migration/PMU unknown.
Cached M1 4c48fa7e context only; no fresh fetch after DNS failure, no host pooling.
Both population steps used three sequential passes, not independent agents.
11 populations(9 sequential+2 multi-agent),0 accepted/6 rejected/5 parked,
33 patches/14 harnesses; M1 night counts separate. Actual CLI usage inUSAGE.json;
exact backend/model/currency cost unknown. SeeMORNING-REPORT.md andHANDOFF.md.
