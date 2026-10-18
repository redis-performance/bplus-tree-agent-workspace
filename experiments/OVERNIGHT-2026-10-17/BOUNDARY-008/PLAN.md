# BOUNDARY-008 — append-batch flush and temporary-buffer ownership

Standalone read-only structural observations; mutations through public APIs only.
18 fixtures: hash seeds17/101, key distributions8-byte/319-byte/mixed8,319,320,321,1024,
initial existing members0/95/7169, final8193. All scores numerically zero with alternating
signed-zero bits and big-endian member IDs, ensuring strict score/member append order.
Groups0,1,95,96,97,193 then remaining members force empty/partial/count/byte flushes.
Alternate Add and AddWithHash using exact fixture hash. Overwrite reusable caller buffer
immediately after every Add; buffered inline and external members must be copied already.

Verify full iterator/rank/score/raw lookup/scan coverage after every Finish, clone/free
original, and deletion. Empty Finish preserves length and tree-owned bytes. Observe and
require both count-triggered and byte-triggered flushes and at least one Add that begins
with natural active index resize; do not manufacture private tree state or lower checks.
No observation of incomplete batch via other mutating APIs; all buffers finished first.

Release/debug+ASan/UBSan required; each child<=120s. Separate mutation controls: borrowed
inline buffer pointer, omitted final flush. Both must fail. Preserve failures, patches,
commands,source/output hashes. No performance claim or source optimisation. Sequential
review only, backend/model/cost unknown, uncommitted snapshot pending morning review.
