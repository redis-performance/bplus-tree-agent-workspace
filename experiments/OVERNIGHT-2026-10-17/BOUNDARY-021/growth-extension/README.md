# Natural growth-side wrap — singleton batch extension

PASS for all eight control/EXP-004 A/B/C native/debug and ASan/UBSan cells.
Each cell checks two fresh seeds,131080 natural resizes, two actual growth-side
65535→1 wraps,131094 full model states and12126950 exact public results. Every
low/high phase is checked. A new leaf enters destination generation1 at each wrap.
All complete outputs match. See PLAN.md, manifest.json, summary.json and oracle.patch.
Entrypoints: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-021/growth-extension/run.py`
and its `faults.py`; exact compiler flags, commands, stdout/stderr and hashes retained.

The zero-generation fault is detected at the natural transition. The deliberate
batch-already-migrated fault SURVIVES, with identical output. This is a test-strength
limitation: the singleton batch can take the ordinary single-entry insertion path,
so marking its leaf migrated prematurely does not lose a member. No detection is
claimed and no assertions were changed. A separately preregistered multi-member
extension is needed. These are extensions of BOUNDARY-021, not additional suites or
new distinct detected fault types. Source NONE; prior PARK unchanged. No performance
measurement or source adoption. Provenance remains uncommitted isolated snapshots;
independent reviewer failed to start; review is sequential. Backend/model/cost unknown.
