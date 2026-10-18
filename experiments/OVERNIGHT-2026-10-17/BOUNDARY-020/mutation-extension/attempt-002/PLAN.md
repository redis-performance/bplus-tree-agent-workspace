# Fresh-seed mutation extension (same boundary suite, not a timing campaign)

Preregistered before execution. Four fresh seeds60317/60331/60343/60353 × two
move/decline policies, eight fixtures per cell, all four frozen sources/bothbuilds.
Generalise the verified read-only model to interleave256fixed public mutations and
defrag slices, starting at natural resize with>=128uncopied leaves(max65536members).
Require>=16mutation operations and>=16defrag slices while resize actually active
in every fixture. No lookup-based full verifier before transition coverage captured.

Eight-operation repeating schedule: insert unique raw member, finite-score update
using successful FindForAdd, single delete, defrag-only, active-state clone/read-only
model/free, retire saved defrag-cursor whole leaf if still live, second finite-score
update, insert. Keys have319/320/321/1024bytes; updates cycle -DBL_MAX,-DBL_MIN,
negative smallestsubnormal,-0,+0,positive smallestsubnormal,DBL_MIN,DBL_MAX. Each
lookup is a public operation and its rehash progress is observed, never hidden.
Fresh sorted-vector verification every16steps; pointer/parent/ID/accounting check
after every step. Header/index relocation at steps64/192 also tests state.tree reset.
Require actual retired-cursor recovery and header-reset recovery, no private writes.
A final fresh quiescent defrag pass must visit every live node/external allocation
exactly once, then clone and full lookups/ranks validate independent ownership.

Retain initial/dynamic physical counters and per-fixture logical digests. Since
cursor deletion is physical-history-dependent, require per-fixture reference-model
success; report cross-build differences rather than imposing unplanned equality.
Child120s; matrix600s; preserve failures, no timing measurements. Repeat the existing
two BOUNDARY-020 faults in baseline sanitizer extension to show new schedule detects
them. No new boundary-suite or distinct-fault count, source NONE/PARK unchanged.

## Attempt002 amendment, before execution

Attempt001 completes firstthree fixtures then fails joint coverage in seed60331,
decline policy. Inspection shows a planned DefragStart can decline moving the
header itself; requiring three state.tree resets from that policy was unjustified.
The original plan/source/logs/snapshots remain. Attempt002 strengthens the callback
intervention: always move the set header at initial/step64/step192 DefragStart,
while retaining every-third declines for all other allocations. Keep the original
>=3header resets and all other coverage assertions. Print each component before
assertion. This is revised fixture preparation, not a production fix or relaxed
threshold; no timing evidence is involved.
