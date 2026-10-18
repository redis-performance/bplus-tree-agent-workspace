# BOUNDARY-020 — active-resize relocation and retired defrag cursor

All eight baseline/EXP-004A/B/C × native/debug or ASan/UBSan cells PASS. Each runs
four fixtures,32complete model checks,284714public exact-value results,4observed
retired-cursor restarts and8completed incremental passes. Across each cell10924
allocation callbacks include9104moves and1820declines; every moved allocation is
released exactly once. Complete outputs and logical digests agree across cells.

Construction naturally triggers resize at1793mixed inline/external members. The
header, ID map, old/new hash buffers and resize metadata are actually relocated
(or explicitly declined). After three defrag steps, deletion retires the saved
defrag cursor's40-member leaf; resumption must first call the allocator on the
current first live leaf. Each interrupted pass finishes. A subsequent uninterrupted
pass visits exactly the pre-enumerated1361page/external allocations per fixture.
The member resize remains active throughout, with cursor/revision unchanged by
relocation and observation. Public lookups happen only after coverage is captured.

Independent sorted-vector checks cover exact scores including signed zeros, binary
lengths/bytes, every seek rank, forward/reverse iteration, scan completeness and
lookup/ranks. Usable-size summation checks complete tree ownership after every
incremental step, separately from callback allocation deltas. Active cloning and
freeing the original before checking the clone add ownership checks. This does
not establish mutation liveness for every possible concurrent sequence.

Both new isolated faults compile and are detected: discarding a relocated active
resize bucket pointer produces ASan use-after-free; treating a missing defrag
cursor as completion fails the restart oracle. Existing source/tests unchanged.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-020/run.py` and
`faults.py`. [Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json),
[fault manifests](faults/manifest.json), raw stdout/stderr, source/binary hashes and
additive oracle patch retained. Exact base commit and uncommitted snapshots are in
manifest; no git retry or source adoption. Original43tests independently passed
all eight unchanged source/build cells in neighboring BOUNDARY-019 this round.

Decision: additive correctness coverage validated; source NONE; EXP-004 A/PARK and
EXP-005 PARK/NONE unchanged. No benchmark, speed claim, new qualification or population.
Review sequential after independent reviewer startup failed. Exact backend/model/
token costunknown; supervisor records CLI usage separately.
