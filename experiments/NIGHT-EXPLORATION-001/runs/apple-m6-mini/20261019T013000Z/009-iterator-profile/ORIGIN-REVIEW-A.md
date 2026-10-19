# Intel iterator cache origin review — no semantic blocker found

Reviewer `/root/followup_proposal_a`, actual independent reviewer, inherited
GPT-6/Codex family; exact serving model/token/monetary cost unknown. Read-only review
only: no build, timing, profile, source mutation, Git write or agent launch. Only
this report and its JSON companion were written. M6 baseline profiling by B is a
separate gate; this review does not choose an optimization hypothesis.

## Exact origin and applicability

Pinned fetched origin commit c3e5882ca5ff3b04f65769d4ba49e4347d1f6351 on
origin/exploration/aws-intel-20261019T020000Z. Campaign path is
experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/004-iterator.
Its source/header equal the M6 baseline byte-for-byte: C d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2,
header496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83.
Every exact published A/B/C patch passes `git apply --check -` against the untouched
M6 baseline. Independent in-memory application reconstructs every published source
and header SHA. The JSON records all inspected input hashes and patch identities.
No patch was applied to any on-disk source. Initial report lookup used nonexistent
RESULTS.md; README.md is the actual origin report. That read error is recorded.

The origin explicitly labels BOTH population stages as three sequential passes by
one native worker. These are historical implementations, not three independent
Intel authors. Reviewing or reconstructing them locally supplies no independent
implementation authorship. Intel's bounded screen remains PARK/NONE; it ended at
566/576 processes, with141complete blocks and two trailing rows. C is rejected;
A/B are conditional leads. No Intel result is attributed to M6 and no timing is
recomputed or extended by this review.

## Mechanism, state size and semantic requirements

All variants lazily cache only the per-leaf member-offset-array base when `ele` or
`len` is requested. They keep the original packed member decoding, physical-position
conversion, score decoder, tag scanner, hashing, tree layout and ownership. The
repeated count*score-width/score-array-size computation can be bypassed after cache
initialization; whether that matters on M6 awaits its baseline profile.

| Variant | Cached value | Published64-bit iterator bytes | Trade-off |
|---|---|---:|---|
|Baseline|none|16|leaf pointer + logical position|
|A|pointer to offset array|24|+8bytes per live iterator|
|B|uint32 relative offset|16|uses existing64-bit padding|
|C|uint16 relative offset|16|uses padding; explicit leaf-bound static assertion|

These sizes are published Intel measurements plus conventional64-bit layout
reasoning, not a new M6 measurement. On a conventional ILP32 ABI the baseline would
be8bytes and A/B/C would generally be12; no32-bit build was run. A's +8-byte iterator
state is separate from tree-owned memory and must be explicitly declared before
measurement. B/C's same size is not binary-header compatibility with previously
compiled callers: every referee/caller must be rebuilt against its own header.

For B/C, zero is a safe unset sentinel: the offset array begins after the nonempty
leaf header even with score width0. Its byte displacement fits the current<=4095-byte
leaf bound. C asserts that bound against UINT16_MAX. All variants preserve the
existing aligned uint16 offset-array access. There is no new allocation or ownership
transfer. Pointer-cache A remains valid only while the original leaf allocation
remains valid; a relative offset does not make B/C's iterator leaf pointer survive
relocation or mutation.

All11leaf assignments reset the cache:

| Entry/transition | Reset paths |
|---|---:|
|SeekRank failure and success|2|
|SeekScore empty, reverse success, forward success, notfound|4|
|SeekLex success and notfound|2|
|Start, including empty|1|
|Next transition to previous/next leaf, including EOF|2|

SeekLex sentinel success delegates to resetting Start; sentinel/ordinary failure
uses its reset label. Next on a null leaf returns without reading cache. Within a
leaf, changing iteration direction needs no reset because only the common offset
base is cached; logical position and physical orientation are still computed each
step. Output masks can change between steps: masks without member/length outputs
leave cache unused, and later materialization initializes it lazily. Copies of a
valid iterator must copy the entire struct; leaf, logical position and cache then
remain consistent and advance independently. External manual partial writes to
leaf/position are not a new supported reinitialization API.

Mutation invalidates the iterator and returned member pointer under the original
contract, even if a particular in-place update happens not to relocate its leaf.
Tests must reinitialize through Start/Seek after mutation or defragmentation;
exercising stale cached state after mutation is invalid usage. A clone requires its
own newly initialized iterator. Failed seeks/end calls must preserve the original
return/output behavior, including not writing nullable outputs on EOF. No blocking
semantic defect was found in these exact patches by static inspection.

## Novelty and oracle evidence

I compared all retained EXP-002 and EXP-004 source diffs. EXP-002 specializes forward
score-only dispatch/helper structure; EXP-004 changes the packed decoder's overflow
predicate. The Intel cache changes persistent per-iterator metadata and initialization
paths and leaves both of those mechanisms untouched. It is a distinct hypothesis,
not a relabeled rejected decoder/dispatch patch. This compares source mechanisms;
it does not assert any unrecorded M6 measurement of those historical variants.

Published original oracle coverage: poison iterator state before all entry points;
all masks; both directions; copies; successful/failed rank/score seeks; equal-score
lexical bounds and sentinels; multi-leaf traversal; binary16/321-byte inline/external
members; ties and exact signed zeros; empty trees. It claims28,192state checks/build,
43original tests/build and1,920fixture cells/source across native/sanitizer builds.
The additive oracle retains original checks and adds direction toggles on the current
position plus mutation followed by explicit reinitialization:89,428total state checks
per source/build. Its loops and expected-state model were inspected here; they were
not executed again. Deliberate B omissions of successful-rank reset and forward-leaf
transition reset are reported detected by ASan/UBSan. The initial invalid unequal-
score SeekLex expectation is retained in attempt001-oracle rather than suppressed.

Important coverage limits: iteration reverse direction is not proof of reversed
physical leaf storage. The random257-member oracle has no explicit verified
reversed-leaf recipe. The named wide fixture2^53+2*i does not prove packed64-bit
width coverage: nearby ordered doubles can still pack narrowly. Broad finite-score
and width/offset geometry require observed fixture coverage. These are missing
coverage/guard gates, not demonstrated production defects in the cache patches.

## Required performance guard inventory

Correctness checks and throughput guards are different deliverables. The semantic
oracle above cannot clear a performance guard. The origin timing matrix has only
eight contracts/sizes (mask7forward/reverse integer, mask4forward integer and
mask7forward fraction at100K/1M); it does not supply the complete inventory below.
Before code, root must fix a bounded complete matrix/interaction coverage and count
its calibration/control/discovery/confirmation cost. No cell may disappear for noise.

1. Keep both full-outputmask7, forward integer,16-byte primaries at100K/1M. Reproduce
   the exact timed consumer contract: origin reads first member byte, length and
   exact score bits, with full byte verification outside timing. A full-member-byte
   timed consumer is an additional contract, not a silent replacement.
2. Materialization/direction/score basis at both primary sizes: all8masks ×2directions
   ×4score families (integer, fraction, observed broad finite widths, equal/signed
   zeros). This alone is128cells, including the2primaries. Masks0/4 are essential:
   cache reset stores/state size can regress them despite no cache initialization.
3. Length/materialization boundaries:8/16,253/254 length-prefix boundary,
   319/320/321 inline/external boundary and1024bytes; member-pointer-only, length-only,
   combined and scored outputs in both directions. Add a variable-length binary
   fixture covering empty/1-byte members, prefixes and embedded NULs; a singleton
   empty key is feasible, whereas100K distinct empty keys are not.
4. Small and transition sizes:0/1/2,31/32/33,63/64/65,95/96/97,100/129/257,1K/10K.
   Include all masks/directions where initialization and boundary costs dominate.
   Empty/end tests use call/lifecycle operation counts, not division by zero items.
   Require actual differing offset-array geometry across leaf transitions.
5. Physical orientation and score geometry: verified public-history fully reversed
   small leaves and mixed-orientation multi-leaf trees in both iterator directions;
   width0, narrow, byte/cross-byte and observed broad/full-width finite scores,
   including signed zero and finite extremes. Verify physical coverage untimed;
   do not infer it from direction or an encoding name.
6. Lifecycle throughput: Start/first Next, warm Next, repeated short runs, successful/
   failed rank/score/lex seeks, inclusive/exclusive/sentinel bounds, empty/EOF Next,
   warmed-copy then advance, changing masks/directions, and reinitialization after
   mutation/defrag/clone. Lex seeks use equal-score trees. Timed copied-state costs
   must expose A's larger struct rather than treating copies as free setup everywhere.
7. Retain the existing101 standard/lookup/batch/update guards and tree-owned memory
   checks. Add small/large range-deletion costs: the implementation uses iterator
   setup internally, and ordinary whole-tree delete is not equivalent. Record
   per-iterator bytes/max live states separately; identical tree-owned bytes alone
   do not erase A's state-size trade-off.

All semantic modes need independent byte/length/exact-score/current-position oracles,
output canaries, copies and reset-sensitive fault controls before any timing.
Throughput matrices then require matching-header builds, qualified same-session
controls, six serial ABBA blocks, held-out confirmation, profile validation and
adversarial review. The factored inventory is intentionally not a claim that128
cells suffice: length/small/orientation/lifecycle/noniterator families add work, and
interaction coverage must be frozen explicitly. If the complete feasible matrix
cannot fit the remaining campaign/deadline, prepare/PARK rather than shrink guards.
