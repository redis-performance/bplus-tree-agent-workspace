# Fresh mutation/relocation extension

All eight baseline/EXP-004 A/B/C × native/debug or ASan/UBSan cells PASS the corrected
fixed schedule: eight fresh-seed/policy fixtures each,448model checks and15054526
exact public results per cell. Each cell performs1536mutations and2056defrag steps
while a member resize is observed active,256cursor-leaf retirements,280observed
resets/restarts and24header identity resets. Complete outputs/digests agree.
Both existing BOUNDARY-020 faults are detected again in sanitizer builds. This adds
coverage within the same suite; it does not add distinct faults or performance data.

The first attempt passes three fixtures, then fails joint coverage. Its policy can
decline the header move while the test requires three identity resets; this is an
identified fixture-design inconsistency, not a production finding. The individual
failed counter was not printed, so do not claim it was separately measured. The
second preregistered attempt always moves headers and preserves the same reset
threshold and every other check, while other allocations still decline every third
callback. Original plan/source/snapshot/logs retained. New source prints every
coverage component before the unchanged assertion.

[Corrected plan](PLAN-attempt002.md), [manifest](attempt-002/manifest.json),
[summary](attempt-002/summary.json), [faults](attempt-002/faults/manifest.json),
source revisions and patches retained. Commands: `run.py` (retained failure),
`run-attempt002.py` (PASS), `faults-attempt002.py` (both DETECTED).
Output-label erratum: FIXTURE field `final` prints the quiescent allocation-visit
count, not final member cardinality. Read it as `quiescent_allocations`; no results
were rerun or altered to fix that label. Logical verification checks actual length.

Fresh confirmation is sequential coordinator work, not independent agents. No
source adoption; EXP-004 A/PARK and EXP-005 PARK/NONE unchanged.
