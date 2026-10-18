# Growth-side natural wrap extension — preregistered round 15

Correctness only. Source selection NONE; existing optimization PARK decisions unchanged.
Freeze control and EXP-004 A/B/C from their exact recorded base commit and SHA256 snapshots.
Run each native -O3 debug and -O1 ASan/UBSan, serially, child timeout120s; total budget900s.
No source/allocator/referee changes. New oracle is separate from the retained low-water
oracle. All failures retained; missing coverage fails rather than mutating private fields.

Seeds61511/61519. Reserve29 on an empty set; build29 ascending319-byte binary members
with exact finite half-integer scores (negative zero for member0). Exactly32770 cycles
per seed: shrink to8 then grow to29. Settle each observed resize using anchor lookups;
require sequential nonzero16-bit generation,65535→1 naturally, exactly65540 resizes and
one growth-side wrap per seed. Full independent sorted-vector, both-direction iterator,
seek-rank, scan, lookup/rank, subtree/leaf-ID and owned-memory checks at EVERY low and
high water, before/after and clone. No sampling of phase models.

At the actual growth wrap, before lookups consume it, require destination larger than
source, length29 and uncopied live leaves. Verify the full non-mutating iterator/scan
model. Append one extra member29 with public append-batch API to guarantee a new leaf;
require a new live leaf ID, migrated tag1, and an actual destination-table reference
for its hash/leaf ID while wrap remains active. Verify again without consuming rehash.
Then settle and verify all30 members; remove extra maximum member29 before continuing
normal high-water checks. Require exact public values and unchanged memory accounting;
physical IDs are observations, not cross-allocator equality requirements.

Fault controls in isolated sanitizer copies: (1) permit resize generation0 (repeat of
BOUNDARY-021 fault); (2) mark newly batch-built leaf as already migrated during active
resize (existing append-batch fault type if previously covered). Both must build and fail
an explicit assertion/sanitizer finding, not time out. No performance or source acceptance.
Independent reviewer startup failed; subsequent review is sequential, not independent.
