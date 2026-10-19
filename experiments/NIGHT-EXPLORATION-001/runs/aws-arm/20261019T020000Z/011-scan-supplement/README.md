# Supplemental SCAN referee: baseline correctness passed, performance unmeasured

This separate referee covers natural active resize and complete reversal in small
publicly constructed trees at member widths 8, 319, 320, 321 and 1024. It retains
original source8fab511e and its adapter/referee; 007 remains immutable.

Final baseline validation passed 378 commands in34.4s:90 fixture models (30cells ×
seeds201–203), native and ASan/UBSan public/census parity, original43 tests/build,
10 callback fault detections,4 structural negative detections,2 census timing refusals.
All validation has passes0 and zero timing windows; exact two warmup traversals and
full pre/post SCAN/iteration oracles execute outside any clock. The independent
model checks complete live membership, binary bytes, scorebits including signedzero,
legal duplicates and ordered iteration. The Python model manifest independently
hashes key/score sequences; seed metadata plus frozen derivation specifies hash seed.

| Construction | Widths | Members | Reversed members | Old/new live members | Full16 chunks |
|---|---|---:|---:|---|---:|
| Insert lower sentinel, ascending insert, delete minimum |8/320/321/1024|31|31|31/0|1 reversed|
| Same public recipe |319|7|7|7/0|0|
| Reserve4096 then ascending insert |8/320/321/1024|7169|0|7008/161|448|
| Same active-resize recipe |319|7169|0|7152/17|0|

These states hold for all three encodings and all three seeds in both builds.
Chunk counts describe structural availability, not measured helper invocations.
No wide IDs, large reversed tree, dense selected tags, concurrent resize progression,
or combined reversal+resize is claimed. 319-byte inline leaves lack full16 chunks.

Separate public timing TU preserves API boundaries. The read-only census TU includes
original tree implementation only in a diagnostic binary, which rejects timing.
No private writes are used. Exact memory identity is required per timing comparison;
no cross-allocator memory equality is assumed. Assertions/hash/allocator/options stay
fixed within a comparison. The proposed fixed1140s performance schedule and strict
six-block decisions are in PERFORMANCE-PLAN.md; root review/scheduling is pending.
No candidate was measured or selected; this adds no optimization population.

Pre-freeze failures are retained: Reserve on nonempty tree is a no-op and did not
create a settled negative fixture; corrected public Score sweep does. Native/sanitizer
census explicitly proves inactive7169/0 before active-state assertion rejects it.
A deliberate sanitizer failure stalled during exit symbolization; the child timed out.
Partial timeout streams were not saved by that validator and are unavailable. Final
failure handler flushes then _Exit(2); successful processes still free allocations and
retain sanitizer exit checks. Final validator adds timeout evidence capture only;
its positive criteria are unchanged from the completed378-command run.

Author /root/aws_arm, native Codex; exact model and measured token/USD costs unknown.
