# Round20 sequential adversarial review

This is the coordinator's separate source/coverage pass, not independent review.
Reviewer-agent startup failed before computation; no participant/model/cost is invented.
Exact backend/model/token cost unknown. This review cannot satisfy the independent
confirmation/review acceptance gate. Run outcomes are recorded separately after execution.

The transferred oracles use read-only private-state observations to establish actual
public histories. Their mutation, resize, SCAN, clone and defrag actions call public
standalone APIs. They include src/zset_btree.c themselves; drivers correctly omit a
second compiled implementation. Root source/referee, candidate patches and oracle
parents remain frozen. Fresh debug-off builds retain all unconditional CHECK and
serverAssert checks. No NDEBUG, fast-math, allocator or hash changes are introduced.

Partial promotion checks masks, exact score bits and all outside-count canaries while
migration completes on the last requested lane. Miss score slots are unspecified and
are not incorrectly constrained. Count0 is checked with null pointers. Count1's
alternating layout is a hit only; no mixed-hit claim for that cell. Clones must own
separate member tables/external storage and leave source metadata/accounting unchanged.
Score moves preserve external pointers and signed-zero behavior. Narrowing verifies
surviving IDs are compacted, absent members miss and continuous SCAN anchors survive.
External relocation tests clone, all-move and partial-decline modes while migration
and SCAN remain active. Allocation deltas use actual usable bytes, not presumed equality
across sanitizer/native allocators. Logical digests supplement full assertions, rather
than replacing them. Source/build/seed cardinality is not a count of independent agents.

Coverage limits: predominantly long members do not guarantee16-tag hit leaves; the
new dense extension addresses this by adding short keys while preserving external
score-transfer keys and the original promotion family. It checks the target leaf size
via read-only score seek, not a timing counter. That is evidence about fixture geometry,
with helper-path reach inferred from inspected source flow. All-miss lanes do not
establish a dense hit. Control/C only are planned for that extension; do not generalize
the result to A/B. Root tests and old oracle histories remain separate evidence.

The scalar probe removes only __BYTE_ORDER__ after normal host/system/adapter headers
have been read. Preprocessor equality must demonstrate that B/C helper selection is
the only effect. Other translation units retain host settings. This does not emulate
big-endian storage, ABI, compiler semantics or another CPU; actual portability stays
pending. The source helper uses bounded memcpy word loads, nonzero ctz masks and a
scalar tail. Borrow flags can occur after a matching byte, but little-endian ctz still
selects the first true match. Guard pages test physical span bounds, including zero.
The deliberate zero-span read is isolated and must not be mistaken for a production bug.

All new work is correctness validation. No A/A, speed, frequency, PMU, unbiased profile
share or guard-resolution claim follows from it. EXP-006 long-key uncertainty and
single-lane concern remain, EXP-004's original guard remains unresolved, and EXP-005's
fresh primary failed. Source adoption NONE. All fifteen optimization patches remain.

The additional [static assembly inventory](ROUND-020-STATIC-LEAF-AUDIT.md) is explicitly
post-hoc. C's own frame and static body are larger than control, but called libc frames
and dynamic path frequencies are not accounted for. This is not a speed or peak-stack
claim, and not a causal explanation of the batch-size concern. Counts are not promoted
to a new preregistered diagnostic or used to change candidate selection.

The final generation-wrap transfer preserves the successful attempt002 oracle,
changing only its two seed literals. All original natural-resize counts and batch2/13
leaf-creation checks remain. All four exact sources pass both builds. This is fresh
fixture coverage with REDIS_DEBUG enabled, not independent confirmation or debug-off
wrap validation. No new sensitivity control or named suite is claimed. Same-size
cleanup and other older candidate coverage gaps remain explicitly listed.
