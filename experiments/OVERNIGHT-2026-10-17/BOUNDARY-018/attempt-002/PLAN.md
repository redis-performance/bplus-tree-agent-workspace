# BOUNDARY-018 — leaf-ID registry state machine

Preregistered additive private-invariant oracle. Existing public-API natural-ID tests
exercise wide trees; this isolates the free-ID registry across all selected growth
boundaries and the explicit rule forbidding ID reuse while a member rehash exists.
No benchmark or synthetic state is represented as a public tree fixture.

Two fixed seeds51109/51131; sizes0,1,15,16,17,31,32,33,255,256,257,32767,32768,
32769,65519,65520,65535,65536,65537. Construct registry only, no member entries.
Independent pointer-vector and explicit free-ID stack model: sequential new IDs,
shuffled one-in-three releases, replacement of live IDs, allocation while an active
rehash marker exists, releases during rehash, complete LIFO reuse after rehash ends,
and final drain. Validate all live pointers and the complete free list at phase and
growth boundaries, no cycles/duplicates, no active-rehash reuse, retained highwater,
unchanged capacity/owned bytes when IDs are reused, and actual usable-size accounting.
Synthetic leaf structs are independently allocated; only registry table ownership
belongs to the tested set. Never dereference marker pointers or scan a synthetic tree.

Control/EXP-004A/B/C, release/debug andASan/UBSan; eight isolated cells must pass and
logical digest agree. Two isolated sanitizer faults: allow reuse during active rehash;
truncate free-list links to16bits. Ensure each fault is detected by semantic check,
not merely compiler warning. Freeze exact files/patches/commands and keep failures.
Child120s, wholematrix400s; no measurements overlap. Source/adoption NONE, no population
or timingclaim. Backend/model/costunknown; review sequential after reviewer failed.
