# Live SCAN across natural leaf-ID widening — validated

All16 source/build/seed cells pass: control and EXP-004 A/B/C, native-O3/debug and
ASan/UBSan, two seeds. Each starts392809continuous anchors at observed next leaf ID32735.
At call25, the same nonzero cursor enters actual narrow→wide migration with209copied
members; at call2072migration completes. All16384live calls stay within16384groups.
There are2047mixed-width calls and14312completed-wide calls,425961final members.
These are observed local geometry and operation counts, not portable constants or timings.

Every call checks exact callback values and independently sorted scalar reversed-hash
interval completeness. All initial anchors survive; duplicates are allowed. Three full
ordered/lookup models, sampled rank/seek, subtree/parent/leaf registry and exact usable-
allocation accounting pass, plus static scans at three hints and clone-after-free checks.
Outputs match across all four sources/builds per seed. No production defect observed.

Both planned faults are detected. Omitted-old-table is a repeat type; decoding a wide
SCAN ID as narrow is new. The latter aborts at production `count != 0`; the initial
Python classifier wrongly labelled it SURVIVED because the adapter prints file:line:
expression without the word Assertion. [Read-only audit](faults/audit.json) maps its
stderr to the exact source/adapter; original outputs/manifest retained, no rerun or
weakened checks. This is a classifier correction, not an actual surviving fault.

[Plan](PLAN.md), [commands/hashes](manifest.json), [summary](summary.json),
[oracle patch](oracle.patch), [faults](faults/manifest.json). All children bounded120s
and serial. Uncommitted isolated snapshots, unchanged source/allocator/referee.
Twenty-third suite,46distinct boundary fault types. Source NONE; EXP-004 A/PARK and
EXP-005 PARK/NONE unchanged. Reviewer startup failed; review sequential, backend/model/
token cost unknown. No timing qualification or acceptance gate is closed by this test.
