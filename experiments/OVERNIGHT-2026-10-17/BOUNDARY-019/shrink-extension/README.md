# Public shrinking-resize extension

All eight baseline/EXP-004 A/B/C × native/debug or ASan/UBSan cells PASS. Each has
four fresh fixtures,88model checks and574384exact public results. Three1024-member
prefix deletions naturally shrink the index with1024members remaining. Each fixture
observes85partly migrated steps, then an active end-of-list cursor after86lookups.
A clone preserves that sentinel state; one further public lookup independently
completes each tree. Nine later insertions force the expected free-ID reuse.

The isolated scan-orientation fault is detected by the model during shrinking
resize. It is a new distinct fault type within existing BOUNDARY-019, not a new
suite or source bug. Full outputs/digests agree. All old checks remain unchanged.
Commands: `run.py`, `faults.py` in this directory. [Plan](PLAN.md),
[manifest](manifest.json), [summary](summary.json), [fault](faults/manifest.json).
Exact source snapshots, patches, flags, commands, raw logs/hashes retained.
A separate [branch capture](../../COUNTERS-007/shrink-extension/README.md) observes
eight NULL-cursor fallback entries (source and clone across four fixtures), while
the freed-ID condition stays zero. No timing or optimization claim.
