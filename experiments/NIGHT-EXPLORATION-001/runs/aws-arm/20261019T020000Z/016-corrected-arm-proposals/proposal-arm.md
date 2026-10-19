# ARM proposal: exact 16-byte NEON leaf-tag matching

Participant: `/root/aws_arm`, separately authored native Codex agent. Exact serving
model, measured tokens and USD cost are unknown. I read my immutable corrected
baseline packet `9cd8689db` (014 profile/control/assembly and 015 A/A), original
helper source and the required population process. I have not read either peer's
proposal for this round. I know the prior original-adapter investigation and the
Intel SSE2 family; this is not a blind experiment. The original `8fab511e` A/A
failure and NONE decision remain final. No source implementation or timing was
performed for this proposal; the ARM runner is idle.

## Proposed hypothesis and exact scope

On corrected source `13e459ff8800be3f02b6b45c87dd7b0c39453fa9`, replace only the
complete-block path in `zbtLeafTagMatches` with AArch64 NEON exact byte equality
across 16 physical tags, convert comparison lanes to an exact physical-position
mask, and emit positions in the original order. Preserve the bounded remainder and
original portable fallback. This is one all-match scanning hypothesis, not a change
to index bucket lookup, record decoding, hashing, score packing or table layout.

Falsifiable prediction: this reduces the repeated word-mask and candidate-byte
recheck work enough to improve both original SCAN primaries (100K and 1M, 16-byte
members, fixed 5M requested operations) by at least 2% against the same corrected
baseline, with exact tree-owned memory and no qualified guard regression beyond 1%.
AArch64 has no x86-style byte movemask instruction; building the mask is a real
cost and may erase the benefit. The prediction is not a measured speedup.

## Evidence and limits

Fresh controls qualify all six blocks at each size: 100K effects span −0.308% to
+0.398%, minimum 415.775 ms; 1M spans −0.762% to +0.286%, minimum 535.062 ms.
These controls use seeds 401–403 twice under the distinct corrected adapter.

Six timed-scope profile captures have 1,255 and 1,597 events. Source-mapped all-match
plus local setup accounts for 465 events / 36.929% sampled period at 100K, and
524 / 33.128% at 1M. Forward word loops account for 29.631% / 27.657%; word load,
mask and fold-selection scope for 11.041% / 13.446%; byte recheck for 5.067% / 3.175%.
These regions overlap and must not be summed. The 209 mapped instruction words
match between original and diagnostic binaries; none uses SIMD. Output parity and
the disabled PMU control pass. Exact ranges exclude the separate leaf-ID assertion,
resize checks, later decode/hash/callback and the count assertion.

The evidence supports reducing this helper's repeated scalar work. It does not say
all 37% is removable, establish the best NEON mask reduction, or predict a speedup
from sample percentages. Constant/mask setup, loop control and emission survive.
Dense matches can move the bottleneck to emission. PMU skid and period weighting
remain limitations. No old/new adapter performance claim is part of this proposal.

## Ranked alternatives

1. **Exact 16-byte NEON comparison with an exact lane mask — select.** It attacks the
   observed complete-word matching/recheck work together while retaining a narrow
   helper boundary and unchanged data layout. Mask reduction must preserve lane order.
2. **Separate ordinary-tag and folded-tag scalar loops — do not select now.** It may
   remove folded-zero work for ordinary queries, but attacks a smaller portion and
   adds duplicated scalar control flow. Existing code already specializes some paths;
   instruction counts alone would not establish an independent improvement.
3. **NEON any-match prefilter followed by the original scalar helper — do not select.**
   Correctness is simpler, but positive blocks repeat work. An index reference normally
   implies a relevant match somewhere in its leaf; the packet does not quantify enough
   empty 16-byte blocks to justify that added test as the best supported mechanism.
4. **NONE — required fallback** if the chair finds the lane-mask costs, guards or
   validation budget make this mechanism unjustified. Qualified controls permit an
   experiment; they do not obligate implementation or acceptance.

## Semantic and portability constraints

- Only load a complete 16-byte span within `count`; no assumption about padding or
  bytes after the physical tags. Counts 0–96, all alignments and both page edges matter.
- Query tag 1 must match physical tags 0 and 1 exactly. Other queries, including the
  helper's tag-0 oracle case, must retain exact equality. Eliminate borrow-generated
  false candidates only where the new comparison mask is demonstrably exact.
- Enumerate physical matching lanes in ascending order. For a reversed leaf emit
  `count - 1 - physical_position`, preserving the original resulting logical sequence;
  do not sort or reverse the emitted positions again. Write only the returned count.
- Avoid undefined shifts, signed overflow, zero-mask bit-scan calls, unaligned integer
  aliasing and endian-dependent lane extraction. Keep the portable helper unchanged.
  A conservative native guard may require AArch64 NEON plus little-endian lane mapping;
  unsupported targets retain the original fallback, with no new compiler ISA flags.
- No public API, state size, ownership, iterator, invalidation, allocator, assertion,
  hashing or compatibility-adapter changes. Exact tree-owned memory is mandatory.

## Guards, predictions and rejection rules

Use original 43 tests, V2 exact-match oracle and sanitizer builds, plus unchanged
focused 007 and supplemental 011 referee semantics rebuilt against the corrected
adapter. V2 must cover all byte queries, folding, zero spans, misalignment, protected
input boundaries and untouched output slots. Supplemental cases require actual active
old/new resize state, exact signed-zero bits and natural reversed physical coverage.
The 319-byte inline fixture has no complete 16-tag chunk: predict no benefit there,
with tail/setup overhead a particular regression risk. Tiny leaves, dense/folded tags,
reversed output, 8/319/320/321/1024 boundaries and scan during resize remain guards.
Other original operations should remain unchanged, but whole-TU code placement still
requires measurement. Correctness-only passes never establish performance safety.

Before candidate data, the chair must freeze the complete serial schedule, seeds,
budgets, primary criterion, guard qualification and independent confirmation. I propose
requiring at least 2% improvement in every qualified primary block at both sizes; no
average rescue. For each qualified guard every block <= +1% passes, all six > +1%
demonstrate regression, and mixed exceedance means PARK. Any unresolved required guard
or incomplete schedule means PARK, even if the primary lead is clear. The corrected
full baseline currently qualifies only 21/40 cells; those missing controls cannot be
silently waived. No adaptive retuning based on candidate results.

Any semantic failure makes that implementation ineligible. Repeated primary failure
falsifies its performance prediction. A selected survivor needs fresh held-out
confirmation, matched scoped profile evidence of the proposed mechanism, and an
independent adversarial review. A win without a mechanism explanation remains PARK.
Source selection stays NONE until all required gates pass.
