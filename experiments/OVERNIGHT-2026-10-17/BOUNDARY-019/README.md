# BOUNDARY-019 — public leaf retirement, deferred IDs and reuse

Validated in all eight baseline/EXP-004A/B/C × native/debug or ASan/UBSan cells.
Each runs four fixtures,32complete model checks and293132exact public results,
observing16new leaf allocations during active resize,2cursor-leaf retirements and
4post-resize ID reuses. Complete outputs/logical digests agree across all cells.
Both deliberate faults are caught: premature reuse (previously tested synthetically)
and incorrect cursor repair (new fault type). Source adoption NONE; prior PARK stays.

All mutations use public APIs. Independent sorted-vector order/score model checks
both iterator directions, every seek rank, binary lengths/bytes, signed-zero bits,
lookups/ranks after capture, scan completeness, clone ownership and free-ID topology.
Independent usable-size summation verifies exact ownership. Observation-only checks
also assert they did not advance rehash or alter allocation/revision state.

Each fixture naturally reaches resize at1793members, deletes one12-member leaf,
then uses44insertions to create4new IDs while the retired ID stays free. Public
lookups finish rehash; another12insertions cause the expected free-ID reuse with
unchanged highwater. These are coverage counts, not timing results or guarantees
for all allocator layouts. The same coverage assertions hold separately per cell.

Attempt001 fails its incorrect assumption that removing the cursor leaf leaves a
stale cursor. zbtScoreRemoveLeaf explicitly repairs it. All failed files/logs remain
at this directory's root; the corrected [plan](PLAN-attempt002.md), snapshot and
[manifest](attempt-002/manifest.json) are separate. This does not establish public
reachability of the stale-cursor fallback in zbtIndexRehashStep. A fault-generation
preflight also fails before execution because three source text matches existed,
not two; corrected generation selects the unique removal function. Both scripts
and the failure record remain. No production assertion or existing test weakened.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-019/run.py` (retained
failure), `run-attempt002.py` (PASS), `faults-attempt002.py` (preflight failure),
`faults-attempt003.py` (both DETECTED), `original-tests.py` (all43original tests PASS in each of8cells).
Exact commands/flags, timestamps, stdout/stderr, source/binary hashes and additive
oracle patch are retained. Source commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c
plus explicitly uncommitted snapshots. No git retry or main-source change.
Review is sequential; independent agent startup failed before execution. Exact
backend/model/token costunknown. No benchmark/profile/qualification gate is closed.
