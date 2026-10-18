# BOUNDARY-009 — batched-score exactness and output boundaries

New correctness coverage, not timing evidence. Test the unchanged public zbtreeScores
API, with read-only structural observations of natural incremental resize. No private
field is changed. Preregister two hash seeds17/101, mixed binary keys including empty,
embedded NUL and lengths4/7/8/16/319/320/321/1024; finite score extremes/subnormals,
nextafter neighbors and both signed zeros. Count0..16, full exhaustive input hit/miss
bit patterns (sum2^count=131071 batches) on a populated tree before/after mutation.
Expected returned mask derives independently from the live model; hit score bits must
match exactly. Missing-score slots have no specified value and will not be constrained.
Output guards before and after the requested count must remain untouched. Duplicate
members in every slot, zero-count NULL arrays, single/raw lookups (optional NULL score),
clone independence and caller-buffer ownership are also checked.

Build a tree to7169 entries via public insertion; require natural active resize before
any lookup. Run full-size batches while resize is active, then exhaustive stable tests.
Delete one selected key, update selected exact scores, clone/free original and test
again, finally empty the set. Batch lookup can legitimately advance rehash and change
index allocation, so no false memory-invariance assertion during active resize. Verify
logical length, single/raw lookup equivalence and ordered iterator contents after stages.
All checks release/debug and ASan+UBSan, child timeout120s. Preserve any failure.

Two isolated intentional faults chosen before runs: wrong returned bit and wrong output
score slot. Each must build and fail the matching oracle assertion; keep both patches.
These are test-sensitivity controls, not proposed fixes. No source optimisation, external
publication, git retry or independent confirmation. Backend/model/cost unknown. Root
source/referee unchanged, exact frozen snapshots and commands recorded.
