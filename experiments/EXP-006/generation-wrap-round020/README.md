# EXP-006 natural generation-wrap compatibility

**PASS: eight source/build cells and eight builds. Source adoption NONE; C/PARK
unchanged.** Exact control/A/B/C snapshots pass the successful BOUNDARY-021 multi-member
oracle in nativeO3 and O1ASan/UBSan builds, with debug assertions enabled.

The only oracle change is a [seed-only patch](oracle.patch): fixed fresh seeds94503 and
94521 replace the older pair. Each child retains both batch sizes2/13 and all four
fixtures. Every cell passes262,160 natural resizes, four growth wraps,262,188 complete
models and24,254,190 exact public results. Logs observe generation65535→1, one new
leaf with migration still active for batch2, and two new leaves with migration complete
for batch13. Logical digests agree across all sources/builds. No private generation or
ID writes occur, and no original assertion was weakened.

```sh
python3 experiments/EXP-006/generation-wrap-round020/run.py
```

The [plan](PLAN.md), [manifest](manifest.json), [parent hashes](parent.json), source/
binary hashes and per-child stdout/stderr retain the complete record. Driver refuses
existing snapshots and includes the historical cutoff; future work needs new paths
and preregistration. All children finished before06:26UTC. The [round audit](../../OVERNIGHT-2026-10-17/ROUND-020-VERIFY.json)
reconstructs the patch and verifies every wrap/fixture/count/digest and serial window.

This is fresh-seed compatibility coverage of an existing named suite, not a new suite,
population or diagnostic. There is no separate selection/confirmation phase, debug-off
wrap claim, new sensitivity run or timing result. Earlier oracle fault controls remain
separate evidence. The earlier round20 checkpoint and469 sealed files were preserved
before this final bounded extension; the final round report and seal supersede it.
