# Round6 — selected iterator candidate remains PARK

Round2026-10-17 23:57:50 to2026-10-18 00:27:50 UTC; not the campaign's final round.
Active experiments finished; handoff saved before final90s. Root src and HARNESS-001
referee remain byte-identical. No publishing,git retry,settings/runtime/STOP changes.
Backend/model/token cost unknown; supervisor records actual CLI usage separately.

## Completed work

- DIAG-010:96 fixed serial requested-QoS rows, all controls pass; primary repeatability
  hypothesis unsupported. No remedy/new lookup A/A; source selection initially NONE.
- BOUNDARY-011:12 clone fixtures/build,74 full model checks,22 clone audits,6 active-resize
  clones,10 free-ID clones,274718 allocation observations. Release/debug+ASan/UBSan pass.
  Both faults detected. Fault-driver expected pointer assertion but earlier accounting
  assertion caught shallow ownership; original driver failure retained/read-only audited.
- PROFILE-003:12 fixed traversal captures and two known-function calibrations pass;
  all symbols resolve. Scan hot zbtIndexScanSlot; iteration hot zbtreeIteratorNext.
- AA-005:96 fresh uninstrumented traversal rows; iterate16/320 qualify,scan16/320 PARK.
  This provides a scoped iterator target/guard, not whole-suite qualification.
- EXP-002: three separate sequential proposal passes and chair, then three isolated
  implementations of one hypothesis. No independent agents; reviewer startup failed.
  Forward score-only dispatch isolation selected.64 validation commands pass control/
  A/B/C release+sanitizers with43 original tests,lexical masks and score-boundary oracles.
  72 fixed screening rows:all three pass gates; C selected via overlap/smaller-patch rule.
  24 fresh-seed confirmation rows pass; four matched profiles resolve all samples.
  Codegen removes generic register saves from C hot path. Final **PARK**, no source accepted.

Campaign totals:3 general harness revisions,6 baseline explorations,14 additional
measurement/path/profile diagnostics,11 boundary suites/22 detected fault controls.
1 population round (both stages, sequential fallback). Optimisations0 accepted/0 rejected/
1 parked. Qualifying/PARK baseline cells are separate from optimisation counts.

## Evidence and commands

Canonical experiment [EXP-002](../EXP-002/README.md); all proposals/chair decisions,
implementation notes,A/B/C patches,exact freeze/source/binary hashes,run manifests,
stdout/stderr,screening/fresh confirmation and matched profile summaries preserved.
Main remains baseline. Worktree/git metadata denial from earlier round not retried;
isolated snapshots under scratch,explicit uncommitted provenance until morning review.

DIAG-010 prepare.py/validate.py/test_qos.py/run.py/analyse.py; BOUNDARY-011 run.py/
faults.py plus fault-review.json; PROFILE-003 prepare.py/validate.py/run.py/analyse.py;
AA-005 run.py/analyse.py. EXP-002 prepare.py/validate.py/run.py/analyse.py/confirm.py/
analyse-confirm.py/profile.py/analyse-profile.py. Exact commands/flags in manifests.
No measured child failed or timed out. No removed rows,optional stopping or gate changes.
Prospectively excluded binary warmups DIAG-010 and AA-005 each separately retained.

verify-round006.py checks root/source/referee/raw hashes,serial schedules,recomputes
candidate block effects/intervals,checks correctness/fault records and sample conservation.
This is a sequential evidence audit, not independent experiment confirmation. CPU MCP
ask and05/14 methods/code consulted; SDK requested-QoS API inspected. Checkers consulted
for QoS/profile/candidate claims; drop_number limits retained, no portable performance
headline. Full retrievals stay ignored scratch; curated metadata/hashes saved locally.

## Remaining uncertainty and next concrete action

C is a promising local candidate, not accepted. Generic reverse/full-output paths now
pay dispatch; their performance may regress. Add a separate frozen iterator-mode fixture
covering both directions and all optional-output masks, score encodings and leaf
boundaries. Validate/requalify before comparing retained C/control, with fresh seeds.
Preserve A/B losing patches and root baseline. Independent performance/reviewer
confirmation and morning commit provenance remain mandatory. Frequency/effective QoS/
within-window residency and sampler bias unknown; current evidence is M1-scoped.

Do not rerun DIAG-010/failed lookup matrices unchanged. Traversal scans still PARK;
profiling does not cure noise. Final campaign worker must write MORNING-REPORT.md by
2026-10-18 07:00UTC/08:00Lisbon. No morning report written early this nonfinal round.
