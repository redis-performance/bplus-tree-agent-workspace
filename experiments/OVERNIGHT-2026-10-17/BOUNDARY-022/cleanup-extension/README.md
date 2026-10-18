# Same-sized cleanup cursor interval — PASS

Attempt002 passes all eight source/build cells, two seeds,10full models and432SCAN
calls each, with119784exact results. Source and destination both have64buckets; at
observation only56of256members are in destination and five leaves remain uncopied.
Per-call intervals/all hints, active cloning, unchanged original ownership/cursor,
and cached-insertion fallback after old-table release all pass. Full output matches.
The isolated equal-mask/skip-destination fault fails interval completeness. One new
fault type,45total; suite count22unchanged. No production bug or speed claim.

Initial failed fixture expected a revision change from ordinary insertions. Source
only changes this revision at index transitions; the corrected new plan checks SAME
revision before triggering insert, then DIFFERENT after actual cleanup starts. Raw
PRE observations show filled479/used255 and equal revisions; cleanup begins at256live.
The original failure and snapshot remain. All production/existing tests unchanged;
other coverage assertions retained. See PLAN.md/manifest.json and attempt-002/PLAN.md,
manifest.json, summary.json, oracle.patch and faults/ for commands, flags and hashes.

Run entrypoints: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-022/cleanup-extension/attempt-002/run.py`
and its `faults.py`. Uncommitted isolated source provenance, sequential review only;
independent reviewer startup failed. Source NONE/prior PARK unchanged. Backend/model/
cost unknown. No new optimization, baseline, harness or diagnostic count.
