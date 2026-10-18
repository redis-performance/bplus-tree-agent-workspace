# BOUNDARY-026 — heterogeneous prefix and duplicate batch lanes

Preregistered before implementation. Add a public-API oracle for empty keys and64
binary prefix families, each with lengths1,2,3,7,8,15,16,17,31,32,63,64,127,128,255,
256,319,320,321,1024,4096. Longer family keys retain shorter key prefixes, including
embedded NULs. Distinct exact finite scores include both signed zeros and extremes.
No NaN. Queries mix variable lengths within a batch and reuse identical member values
both by aliased SDS pointers and independent equal-byte copies. All counts0..16,
all-hit/all-miss/mixed states; check exact hit masks and score bits, outside-count
canaries, null count0, and that input bytes remain intact. Do not assume miss slots
are preserved, since that is not the API contract.

Use an independent live vector and bytewise score/member comparator. Full public
lookup/raw/rank and forward/reverse iteration verify each model, including after
score changes, deletion/reinsertion, cloning and freeing the original. All edits use
public APIs; no private structure manipulation. Full public lookup passes settle
migration before read-only owned-byte guards. No timing claim or active-resize claim.

Freeze root test and four source snapshots from EXP-006(control/A/B/C), identical
referee, allocator and flags. Discovery: native O3 and ASan/UBSan O1 with REDIS_DEBUG,
seeds82603/82611. Fresh confirmation: same matrix, debug-only assertions disabled,
seeds82703/82711. Oracle CHECK and normal serverAssert remain enabled in both modes.
32semantic cells total. Every child<=120s, no new child after06:02UTC; incomplete
stays incomplete. Preserve all failed attempts, patches, stdout/stderr and exact hashes.

Two isolated deliberate controls: reuse lane0 hash for other lanes, and reuse lane0
member length during lookup. Require detection; survival is a coverage gap to retain.
Report these controls separately from the preexisting54distinct boundary fault types
until classification is reviewed; do not inflate that historical count. Sources and
all15optimization patches remain unchanged, no adoption. Sequential adversarial
review only, independent reviewer unavailable; exact backend/model/token cost unknown.
