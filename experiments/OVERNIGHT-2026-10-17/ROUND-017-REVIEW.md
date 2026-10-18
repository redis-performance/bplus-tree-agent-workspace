# Round 17 — sequential adversarial review

Reviewer-agent startup failed before execution: the thread-store could not load its
model context. This is a separate coordinator review pass, not independent-agent
confirmation. Exact backend/model and token cost are unknown; the supervisor records
CLI usage separately. No new proposal or implementation population was run.

The public API contracts were inspected before implementation. Append must receive
an absent member ordered after everything present. The new fixture stops appending
as soon as widening starts, before moving scores beyond the previous maximum. Every
UpdateScore immediately follows its own successful FindForAdd. Iterator score seeks
between those calls do not modify the tree. Nothing reuses a position, iterator or
member pointer after a mutation. Private fields supply coverage/accounting observations;
all construction and mutation uses public APIs.

The old ID-order oracle cannot validate these score moves. Each new oracle maintains
an independent current-score array and sorts IDs by numeric score, then full binary
key bytes and length. Exact bits are checked separately, so signed zeros compare equal
for order while remaining distinct values. No NaN or infinity enters the API. The
finite extension uses explicit binary64 patterns. New scalar equal-score counts cover
all inclusive/exclusive endpoint combinations; full ranks remain sampled, not exhaustive.

All mutations happen between SCAN calls. Callback expectations use current model scores.
The immutable scalar reversed-hash ordering provides each call's expected interval;
callback epochs allow duplicates. All initial members remain continuously present and
must appear before the original cursor terminates within the largest observed group
bound. Newly appended members whose interval already passed are not continuous anchors.
The test shares the production hash algorithm for classification; it is not an
independent SipHash test. The cursor interval invariant is specific to this algorithm,
not a constraint on every possible future opaque-cursor design.

Migration coverage is observed after the source lookup, which itself advances resize.
The prospective destination is the score successor (or last leaf) immediately before
UpdateScore. A split may change its ID. The ownership matrix therefore describes
observed source/prospective-target states, not an assertion that the old entry was
simply relabelled in a narrow table. Separate execution counts inspect the actual
copy/delete/insert/relabel branches. Full lookup/rank passes are delayed until after
migration so verification cannot silently drain the active window. Read-only sorted
models run at explicit active boundaries.

The external extension fixes key lengths before insertion. It enumerates every external
buffer for unique ownership and exact usable-byte accounting. Pointer preservation
across an update is a current implementation transfer invariant, not an additional
public API requirement for future implementations. The execution census distinguishes
in-place preservation from detach/reinsert. The clone is validated after freeing the
original; this adds sanitizer ownership sensitivity but does not prove general leak
freedom. Memory checks are structural accounting, not a measured source memory guard.

The first equal-neighbor fault survives honestly. Generating repeated final scores
is insufficient to test rejection of a locally misordered equal neighbor. The separate
neighbor fixture changes ID256 to score255 and ID511 to score512, where little-endian
binary keys reverse the nearby numeric-ID ordering. It retains the original finite
oracle unchanged and forces same-leaf movement. No timing threshold or existing test
is weakened. Original failures, survivors and exact fault patches remain evidence.

Coverage captures include setup and all oracle phases. They are execution counts,
not CPU-time profiles, hotness, clock estimates or evidence of speed. CPU MCP benchmark
05/14 methods and code were consulted; unrelated ask retrieval was not cited as support.
Its evidence checker found no performance number in the qualitative no-win claim.
No M4 numbering, frequencies or measurements transfer to this M1.

Fresh debug-disabled confirmation changes input seeds and omits only REDIS_DEBUG;
all oracle CHECKs and unconditional serverAssert checks remain. This broadens semantic
coverage but cannot close performance qualification, independent review, or committed
provenance. Main source stays baseline for morning review. All twelve optimization
patches and earlier raw evidence must remain intact. Source selection stays NONE,
EXP-004 A/PARK and EXP-005 PARK/NONE.

The late batch extension observes promotion inside a16-lane public call and respects
unspecified miss outputs. The initial lane expression failed to include ID1; its
16passing cells retain that scope limitation. The one-expression corrected fixture
passes16more cells and repeats the stale-cache UAF detection. No broader count/layout
promotion coverage is claimed. Audit reconstruction failures were corrected read-only;
all original failed logs remain and no experimental child was rerun.
