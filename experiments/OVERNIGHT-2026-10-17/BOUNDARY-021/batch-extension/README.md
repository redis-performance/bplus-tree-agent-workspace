# Multi-member batch at natural growth wrap

Final attempt002 PASS: control/EXP-004 A/B/C in native/debug and ASan/UBSan,
four fixtures each (seeds61543/61559 × batch2/batch13). Each cell checks262160natural
resizes, four growth wraps,262188full model states and24254190exact public results.
All output matches. Batch2 creates one new leaf and keeps wrap active; batch13 creates
two new leaves and completes the resize. Both preserve exact values, reference IDs,
generation1, independent model ordering, subtree counts and owned-memory accounting.

Both deliberate faults are detected: allowing generation0, and prematurely marking
batch leaves migrated. The latter previously SURVIVED the singleton test; the new
multi-member fixture detects the lost second member at actual natural wrap. One new
distinct fault type,42total; suite count remains21. No production defect observed.

Initial batch12 attempt FAILS required two-leaf coverage and is retained unchanged.
The compiled header72+12×item332 fits leaf4095. New fixed13-member recipe exceeds
that conservative budget and retains the at-least-two-leaf requirement. No production
assertion or prior test was weakened. See original PLAN.md/manifest.json/raw output,
and attempt-002/PLAN.md, manifest.json, summary.json, oracle.patch and faults/.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-021/batch-extension/attempt-002/run.py`
and its `faults.py`. All exact commands/flags/hashes/stdout/stderr retained. Uncommitted
isolated provenance; sequential review only, reviewer startup failed. Source NONE,
EXP-004 A/PARK and EXP-005 PARK/NONE unchanged; no timing or optimization count added.
