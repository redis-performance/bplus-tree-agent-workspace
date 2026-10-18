# Mixed-width live cursor with separately allocated members

Preregistered additive scope; does not modify earlier snapshots or checks. After natural
inline319-byte construction reaches threshold-32leaf IDs, future append members rotate
320/321/1024/4097bytes. Initial anchor bytes never change. Precompute independent sorted
hash intervals after anchor count is known, before starting live SCAN. All source/allocator
files remain exact frozen control/EXP-004 A/B/C. Seeds67511/67523; three modes as prior
extension (active clone/free-original, move all, decline every third).48run cells, native-
O3/debug and-O1ASan/UBSan;120schild/900smatrix, serial. Fixed matrix stops on a failure.

Retain every original per-call interval, exact-value, continuous-anchor, bounded-cursor,
full ordered/lookup model, sampled-rank/seek, clone and scan check. Require actual mixed-
width active state with external members and incomplete migration before intervention.
Callback key length is independently determined by insertion ID and anchor boundary.
No hardcoded number of members needed to reach natural leaf IDs. Cardinality cap850000.

Structural accounting includes every external member's actual usable allocation. Clone
must own distinct external allocations as well as every page/header/table. Defrag exact
pre-enumerated visit set now includes external pointers; track visited/freed/declined
counts and compare allocator delta at EVERY step. Public defrag returns after each external
member, so bound steps by length+next_leaf_id+1, scanned<=leaf_max+1. Both bounds derive
from local API/source semantics, not failures. Require external-count>0 and actual external
relocation callbacks in each move mode. Initial inline oracles retain their tighter bound.

One isolated sanitizer fault omits the duplicated external-pointer repair, leaving the
clone record referencing the original allocation (repeat ownership-fault type from
BOUNDARY-011, not a new distinct fault). Clone disjointness or post-free access must fail.
All output/hash/commands/patches preserved. No timing/profile/speed claim; suite count23
unchanged. Source NONE, existing performance PARK. Independent review unavailable.
