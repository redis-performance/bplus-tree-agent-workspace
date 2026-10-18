# Live mixed-width cursor: clone and relocation extension

New correctness scope, same frozen production/allocator/referee. Seeds66509/66523;
control/EXP-004 A/B/C × native-O3/debug and-O1ASan/UBSan × three interventions:
clone-and-free-original, relocate every allocation, decline every third relocation.
48fixed run cells,120schild limit/900swhole serial matrix. Stop/preserve any failure.
New oracle snapshot before build; original BOUNDARY-023 and prior evidence immutable.

Use BOUNDARY-023 construction and every original check unchanged. On FIRST observed
mixed-width state at a nonzero live cursor, before its next call, apply one intervention.
Do not advance rehash through lookup/rank during intervention. Iterate all members both
directions, sampled seek, full parent/subtree/registry/usable-byte accounting before and
after, and require rehash generation/cursor/used counts/widths unchanged. Existing
cursor and initial anchor coverage then continue through migration and to completion.

Clone mode: duplicate while old narrow/destination wide is active; all owned allocation
addresses must be distinct from original; validate both objects without rehash; original
revision/state unchanged. Free original and continue original numeric cursor on same-
encoding clone. Object identity changes; no encoding change. Full postscan verification
still exercises lookup, exact values, all hints, second clone-after-free.

Relocation modes: pre-enumerate every owned allocation into a sorted uintptr set. The
callback must visit each exactly once, preserve full old usable bytes, return new storage
64bytes larger (or NULL every third call), and track actual allocator usable-size delta.
Start must visit five header/registry/source-index/rehash/destination-index allocations;
then a complete uninterrupted public defrag walk, checking cursor/generation/revision,
table stats and exact accounting at every step. No lookup rehash or writes interleave.
Pointer lookups in the expected set use binary search to avoid quadratic checking.
Full structural/model checks only before/after the pass, not after every leaf.
Defrag must finish within next_score_leaf_id+1calls; exact visit and release counts.

Two sanitizer controls on first seed: clone wide table using narrow byte size (new fault),
and omit assignment of relocated destination buckets (repeat BOUNDARY-020 fault).
Compile success and oracle/production-assertion/sanitizer failure required. Keep classifier
errors or survivors. No speed claims, counts stay23suites (scope extension). Independent
review unavailable; coordinator sequential review and fresh seed confirmation pending.
