# Dense short-leaf promotion extension

**PASS: all eight control/C source/build/seed cells. Source adoption NONE; C/PARK
unchanged.** NativeO3 and O1ASan/UBSan discovery93503 and fresh debug-off93521 pass.

The original partial-promotion oracle mostly used long members and did not require
a hit leaf with16 tags. This [separate fixture](PLAN.md) adds small islands of16-byte
members while preserving every external key used by the score-transfer checks. It
keeps the original18 promotion cases and adds18 dense-query cases. Each dense hit
requires length16 and a target leaf with at least16 members, observed through read-only
score seek before the public batch call. No tree metadata is privately written.

Each cell passes36 promotion cases/264 requested lanes,68 dense-hit leaf observations,
43 full models,258 cross-leaf score moves,260 external pointer-preservation checks,
and both signed-zero updates. The liveSCAN and clone ownership/accounting checks
remain intact. Reported exact member/score results are36,945,138 for discovery and
36,944,373 for confirmation; all source/build logical digests agree per seed.
All-miss cases make no dense-hit claim; count1 alternating is a hit only.

The [oracle patch](oracle.patch) reconstructs exactly from the frozen BOUNDARY-025
source. Main source, original oracle and all candidate patches remain unchanged.
The larger expected matrix counts strengthen the checks; no existing assertion was
removed or weakened. A/B were not run against this new fixture.

```sh
python3 experiments/EXP-006/dense-promotion-round020/run.py
```

[Manifest](manifest.json) retains source/oracle/binary hashes, complete commands and
stdout/stderr for every child. Drivers refuse existing snapshots and have a historical
cutoff; use new evidence directories for future trials. The [round audit](../../OVERNIGHT-2026-10-17/ROUND-020-VERIFY.json)
recomputes all matrix shapes, digests, hashes and the parent patch.

This is a BOUNDARY-025 extension, not a new named boundary suite or performance
diagnostic. Dense target geometry is observed; helper-path reach follows from source
inspection, not a scoped execution counter or timing profile. No performance guard,
portability or independent-review gate is cleared by this result.
