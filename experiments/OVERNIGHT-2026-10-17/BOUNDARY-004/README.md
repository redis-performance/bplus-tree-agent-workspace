# BOUNDARY-004 — relocation API ownership/accounting validated

Four fixtures (seeds11/29, mixed binary lengths and colliding tags) pass release/debug
and ASan/UBSan. Reuses the unchanged BOUNDARY-001 sorted-vector oracle. Each build
completes2673 full model checks,2119 allocation moves,568 declined moves and2079
explicit Step releases. Start callbacks separately release moved plain allocations.
No Redis server/defragmenter integration or mutable source change.

Relocation changes addresses and usable allocation sizes; uninterrupted passes verify
exact tree allocation deltas after every slice. Lookup, exact finite score bits,
binary bytes, rank/seek, iteration and scan remain valid. Bounded inter-slice edits,
delete-all/refill, cursor reset and clone-after-original-free exercise lifetime paths.
An uninterrupted final pass after reset verifies completion; arbitrary concurrent
mutation liveness or exhaustive movement of every allocation is not claimed.

Both preregistered fault controls detected: missing leaf ID repair yields ASan
heap-use-after-free; missing allocation adjustment fails the exact size-delta assertion.
ASan's external symbolizer could not start for the intentional UAF; the address report
and binary-relative frames remain saved. Baseline sanitizer runs are clean.

[Plan](PLAN.md), [oracle patch](oracle.patch), [commands and hashes](manifest.json),
[mutation plan](MUTATION-PLAN.md), [fault evidence](mutations/). Four baseline commands
(two builds/two runs) succeed, each child bounded120s. Source selection NONE, no speed
claim or optimisation/population count. Review was a sequential coordinator pass;
agent startup unavailable. Backend/model/cost unknown. Uncommitted morning-review draft.
