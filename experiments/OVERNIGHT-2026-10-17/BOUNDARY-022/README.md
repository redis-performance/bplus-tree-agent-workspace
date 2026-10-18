# Colliding SCAN cursor intervals — PASS

All eight control/EXP-004 A/B/C native/debug and ASan/UBSan cells pass. Each runs two
seeds,20full model states and684SCAN calls, including128active-growth and128active-
shrink calls. All logical digests match. Colliding folded tags0/1 and254/255, actual
probe displacement across home groups and wraparound are observed. Every SCAN call
checks exact current members and completeness in its independent scalar-reversed
hash interval; duplicates remain legal. Full iterations retain all128continuous anchors.

Both faults are detected: missing displaced probe tail and collapsing colliding leaf
matches. See faults/manifest.json and raw errors. These add one suite and two new fault
types:22suites/44distincttypes total, including the batch extension's new fault. No
production defect, timing measurement, source adoption or noise remedy is claimed.
Source NONE; EXP-004 A/PARK and EXP-005 PARK/NONE unchanged.

PLAN.md preregisters seeds, bounds, coverage and all gates. manifest.json freezes exact
base/source hashes and records commands/flags/stdout/stderr. summary.json records
logical equality; oracle.patch preserves the test. Entrypoints: `python3
experiments/OVERNIGHT-2026-10-17/BOUNDARY-022/run.py` and its `faults.py`. Uncommitted
isolated snapshots remain pending morning review; independent reviewer startup failed,
so review is sequential. Backend/model/cost unknown. No existing checks changed.
