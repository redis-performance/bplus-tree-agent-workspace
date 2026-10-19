# Cross-author caller-specialization review

Reviewer `/root/followup_proposal_c`, GPT-6/Codex family; exact model, token usage
and monetary cost unknown. I authored variant C, so this is independent review of
A/B only. Observations about C are disclosed self-review; root must independently
review C. No build, executable test, benchmark, profile or agent launch occurred.
Only this review and `review-caller.json` were written.

**A/B source review passes with measurement prerequisites. No adoption is approved.**
All three patches reconstruct their isolated sources from the frozen baseline, and
all preserve the decoder text and original scanner body. Their reported validation
logs and binaries match their sealed hashes. All five initial driver findings below
were corrected before freeze and verified by static inspection of the revised
driver. One cumulative wall-budget interpretation remains noted at the end.

## Semantic and hypothesis review

A changes only the original helper's declaration to force inlining. Its scanner
body, logical-position calculation, conditional score store and conditional position
store are byte-identical. There is no floating arithmetic transformation, new read,
allocation, index update or ownership operation. Existing tests check exact score
bits, signed zero, both physical orientations, width-zero/full-width/spill cases,
collision handling, misses and all optional-output combinations. I find no new
semantic defect in this source change. Generated-code growth remains a performance
risk in every caller using this helper.

B renames the same unchanged body to an always-inline implementation and retains a
noinline generic wrapper. Its index caller uses that wrapper when `score_pos` is
non-NULL and otherwise passes literal NULL to the inline body. The NULL-output
dispatch exactly matches the prior optional-output semantics: any valid non-NULL
position pointer still receives the same logical index, while a NULL pointer never
requires a position store. `score` remains independently nullable. The generic
wrapper adds no operation beyond invoking the original body. The existing original
physical oracle still exercises that body via the wrapper. I find no new semantic
defect in A/B and no combined hypothesis or old physical-decoder patch reuse.

C preserves the original generic helper and duplicates a position-free read-only
body. Inspection confirms its original logical-position-to-decoder expression is
retained. Its supplemental oracle adds read-only checks without deleting original
assertions; frozen oracle results remain separate. This is structurally plausible,
but my authorship prevents calling this independent validation. Duplication adds
maintenance risk absent from A/B. Root owns that final independent assessment.

All source changes operate within the one selected caller-exposure hypothesis.
Allocator, hash, layouts, public signatures, ordering, leaf IDs, traversal and decoder
source remain unchanged. No signed-zero equality shortcut or NaN assumption was
introduced. Semantic tests do not demonstrate that insert, update, rank, deletion
or batch performance is preserved; the full guards remain necessary.

## Evidence and generated code

I independently checked all three patch reconstructions, baseline source hash,
shared header, support/referee hashes, binary hashes and 318 recorded stdout/stderr
hashes: 106 for A, 102 for B, 110 for C. No log or binary hash mismatch was found.
All recorded command return codes are zero. Source-included physical-oracle build
commands link no second `src/zset_btree.c`. Reported native/sanitizer coverage is
43 original tests, 20 public lookup cells and 4,160 physical-oracle cells per build;
this review did not rerun them. Two newer root files are absent from every isolated
tree and from the source pin; they are not candidate changes. The JSON explains
the initial failed `git show` for that absent pinned path and subsequent absence
verification with `git ls-tree`.

Read-only `otool -tvV` inspection of existing validation binaries finds:

| Function / static observation | A | B | C |
|---|---:|---:|---:|
| ScoreRaw instructions |601|601|601|
| ScoreRaw frame bytes |240|240|240|
| ScoreRaw memchr / memcmp sites |2 / 2|2 / 2|2 / 2|
| Scores batch instructions |770|770|770|
| FindForAdd instructions |1,007|704|704|
| Rank instructions |710|443|443|
| Generic leaf helper emitted |No|Yes|Yes|

All three ScoreRaw instruction streams are identical after normalizing relocation,
page/literal addresses and source-line immediates passed to panic. The operation
sequence and local control-flow targets are preserved by that comparison. This
does **not** assert byte-identical binaries, equal code placement, equal runtime,
or whole-program equivalence. B/C retain the same generic-call structure in rank
and FindForAdd; A exposes those bodies too. UpdateScore itself remains 438 static
instructions in all three, but its preceding public FindForAdd path changes in A.
The batch path changes in every variant, so its guards are material.

The frozen baseline ScoreRaw is 345 instructions with a 176-byte frame and two calls
to a separate 144-byte leaf frame. All candidates eliminate those calls while
growing the caller and its static stack-access sites. This establishes exposure,
not useful speed. A primary timing difference among A/B/C cannot establish three
distinct ScoreRaw instruction mechanisms. Code layout and broader caller effects
are plausible remaining differences. Equivalent measurements should favor smaller
source; full guards may still distinguish A's broader exposure from B/C.

Validation binaries have a build-path difference: A/B compile the frozen frontend
as `referee/lookup-bench.c`; C uses its longer campaign-relative path. The differing
`__FILE__` strings affect literal layout. These validation binaries must not become
the comparative timing binaries. Root confirms the common driver rebuilds every
variant/control using the same frontend source path and matching file/debug prefix
maps, which addresses this concern before timing. Panic source-line constants still
differ because production patches add different numbers of lines.

## Plan and initial driver review

The plan contains exactly 101 unique cell IDs: 40 standard, 15 independent lookup,
15 extra lookup lengths, 6 batch and 25 update-pattern cells. Both declared primary
IDs are present. No operation family is silently deduplicated. Six ABBA blocks give
2,424 processes for a complete matrix. At the nominal 100 ms/window that is 242.4
timed seconds; three dual-primary screens add 14.4 seconds, totaling 256.8 seconds
against the 300-second discovery cap. This is an estimate with 43.2 seconds of
margin, not a guarantee: calibration uses the fastest observation, traversal rounds
operations upward, and fixture/setup time is additional. Actual limits and complete
coverage must determine whether the campaign finishes or parks.

The inspected driver has correct mean-B/mean-A effects, per-block checksum/count
equality, every-block strict A/A bounds, minimum-window checks, primary/guard gates
and owned-memory gates. Controls use the unchanged source, counts come only from
baseline calibration and are shared, and raw rows are retained. Missing profile,
confirmation or independent review remains disqualifying for adoption. Noise in any
guard cannot be cured by dropping that cell. Phase reports are measurements rather
than an automatic adoption decision; root must check all prerequisites together.

Initial pre-freeze driver findings sent to root:

1. Budget and deadline checks only before a child allow the final child to exceed a
   bound while a phase still records complete. Clip child timeouts to remaining
   deadlines and check actual totals immediately after each row.
2. Preserve a command record and partial stderr on TimeoutExpired, in addition to
   retained partial stdout. A timeout is evidence, not a missing command.
3. Validate emitted seed, requested operation count, member length, replicas and
   batch size. Expected operations depend on the referee: n×replicas for standard
   insert/delete, rounded complete traversals for iteration, the verified emitted
   scan count for scans, and requested operations for ordinary lookup/update/batch.
4. The original per-variant screen function executes all six blocks before another
   variant. Explicit per-block variant rotation must implement the frozen schedule.
5. Apply the cumulative discovery timing budget through all screens, not only when
   the later guard phase adds previous screen totals.

These are orchestration findings, not production-source failures. Static follow-up
inspection confirms all five corrected: child timeouts are clipped, timeout command
evidence is retained, per-referee output assertions are present, post-row bounds
prevent an over-bound phase from recording complete, and `screens()` rotates
ABC/BCA/CAB by block with one cumulative timed budget. The old single-variant screen
entry is rejected. Root reports all 32 common builds and common native/sanitizer
semantic checks passed; this reviewer did not execute those checks.

One budget interpretation remains: guards include prior screen timed seconds but
start a new 900-second wall allowance. If PLAN's 900-second wall phase applies to
the whole discovery comparison, deduct the single shared screen-phase wall duration
from the guard allowance. Every screen JSON stores that same common duration, so
use one value rather than summing it three times. Root received this note before
freeze. The JSON retains the revised driver hash and the exact static-review scope.
This review approves no uninspected later revision and claims no driver execution.

All review reading and static inspection are finished. No test, build or profile
work remains active in this agent; root can proceed with its final freeze and
serial measurements after resolving the stated wall-budget interpretation.
