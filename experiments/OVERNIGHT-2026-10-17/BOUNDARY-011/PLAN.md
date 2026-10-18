# BOUNDARY-011 — cloning active resize and released leaf IDs

Correctness work, not timing or source optimisation. Two hash seeds43/211; mixed binary
lengths8/16/319/320/321/1024 and exact finite/signed-zero scores. Natural7169-member
growth fixture must still be resizing at clone time, at three public-lookup offsets
0/1/7. Observe private fields only; never force resize or modify private state.
Copy must preserve both table byte contents/width/used/filled, resize cursor/generation,
leaf IDs/free-list links and logical contents, with independent owned allocations.
Enumerate every tree-owned allocation and sum allocator usable sizes to independently
check AllocSize. Across twins, all owned allocation addresses must be disjoint.

Before lookups drain migration, audit cloned representation. Then validate full sorted
iteration, rank, scalar lookup and scan against independent live/score vectors. Mutate
clone via deletion/update/insertion, verify original unchanged; free original, reverify
clone, reinsert deleted entries and empty it. Separate drained fixture deletes a middle
rank interval, requiring a nonempty natural free-ID list before cloning. Exercise
empty, presized-empty and emptied-tree clones too. Both freeing orders covered.

Every suite passes release/debug and ASan+UBSan; children<=120s. Preserve failures;
fixture adjustments require a new snapshot rather than overwriting failed evidence.
Two predeclared isolated faults: omit in-progress resize when cloning; copy external
member pointer without allocating independent storage. Both must build and be detected
by matching ownership/resize assertion (or sanitizer), patches retained. These are
sensitivity controls, not candidates. Root/referee unchanged; uncommitted provenance,
unknown backend/model/cost; sequential audit because reviewer could not start.
