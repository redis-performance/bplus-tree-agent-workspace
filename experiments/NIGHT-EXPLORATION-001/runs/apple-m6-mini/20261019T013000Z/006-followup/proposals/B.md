# Proposal B — specialize the leaf-search call boundary

Recommendation: one bounded new experiment, **M6-LOOKUP-CALLER-001**, with moderate
mechanism evidence and uncertain speed benefit. Do not adopt or reopen LOOKUP-001.
If the chair cannot reserve the full qualification/guard/review budget, select NONE.

Participant: `/root/followup_proposal_b`, actual independent proposal agent.
Backend visible to this agent: Codex / GPT-6 family, inherited from root. Exact
serving model identifier, measured token usage and monetary cost are unknown.
No other proposal was read. No build, test, benchmark, profile, implementation or
permission change was performed during this proposal. The only write is this file.

## Frozen evidence and diagnosis

Source: e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf. Read-only SHA256 verification of
`src/zset_btree.c` returned
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`, matching
`input-manifest.json`. I read all manifest-listed update/lookup reports, profiles,
census/selection records and six patches, plus POPULATION.md, shared measurement
rules, and the baseline lookup assembly retained under `004-lookup/profile/`.

The useful evidence is a call boundary, rather than evidence for a faster scanner:

- `zbtIndexTableFind` is already always-inline. The retained release
  `zbtreeScoreRaw.asm` nevertheless calls the generic `zbtScoreLeafFindMember` with
  x5 = zero, i.e. no logical-position output. The read-only path therefore still
  enters a function compiled for both read-only and mutation/rank callers.
- `zbtScoreLeafFindMember.asm` starts with `sub sp, sp, #0x90` and six paired
  register saves, including the frame/link pair. It saves the nullable output
  pointers and tests them later. This is concrete generated-code evidence of a
  144-byte separate frame and generic output handling, not a cycle-cost estimate.
- The caller has its own 176-byte frame. Eliminating the leaf boundary could
  combine register lifetimes and avoid some save/restore work; it could also
  increase spills and instruction footprint. Assembly must decide which occurs.
- Lookup census reports about 1.15–1.17 leaf scans per hit and about 31–32 scanned
  bytes. Thus the generic leaf entry is on the ordinary successful lookup path.
  Baseline hit captures contain 139/266 PCs at 100K/1M, including 57/148 memchr
  PCs. Leaf work is observed, but these are not unbiased time shares and they do
  not prove call overhead dominates.
- LOOKUP-001 B's 100K median -4.80% is a lead for its closed physical-decoding
  experiment, not evidence that this proposal wins. It had no candidate profile;
  1M controls failed. Its patch is not a new implementation here.
- UPDATE-001 long captures also contain substantial lookup work. Any update
  benefit from specialization would be a guard observation, not the primary
  claim. Repacking's 1M direction does not support an index-layout change.

## One hypothesis and exact scope

**For successful public single-query score lookup, exposing the leaf search to
its caller so the compiler can specialize optional outputs will reduce the
generic call-frame/output-bookkeeping cost enough to improve both 100K and 1M
end-to-end lookup by at least 2%, without a >1% guard or owned-memory loss.**

Target only the `zbtScoreLeafFindMember` / `zbtIndexTableFind` call boundary in
`src/zset_btree.c`, with the public `zbtreeScoreRaw` / `zbtreeScore` paths as the
measured entry points. Leave public signatures, layouts, hashing, assertions,
memchr/memcmp, tag/full-member validation, score representation, allocator and
index/rehash traversal semantics identical. Keep the existing score decoder
source unchanged. Do not combine this with physical-decoder B, a new scanner,
prefetch, repacking or a home-filter change.

Three independent implementations should explore only ways to expose that same
call boundary: whole-body forced inlining; a shared inline body plus retained
generic wrapper; and a read-only-specialized wrapper/body with generic callers
retained. These are implementation directions, not prescribed patches. Each
must start from the frozen baseline, not a losing variant. Reject a purported
variant that is merely an unchanged LOOKUP-001 patch. Macro duplication, if used,
must be reviewed for maintenance risk and exact semantic equivalence.

Expected scope: cache-resident successful score lookups have the best chance;
1M pointer chasing can dilute the gain. Misses often never enter the leaf and
should have little direct benefit. Rank, insertion lookup and updates must not
pay a new dispatch penalty. Batch16 can react differently to code size and
register pressure. No layout changes imply identical owned bytes, but measure
and assert it rather than assuming it.

## Preregistered primary, guards and falsification

Use the frozen public lookup referee from LOOKUP-001 with unchanged workload
semantics. Dual primaries remain 100K and 1M hit lookup, 16-byte binary members,
single-query public entry, score requested. This proposal does not narrow the
old primary to its winning 100K observation. Preserve the exact timed checksum
and final-state validation. Report batch-average ns/op, never latency quantiles.

Before implementation, enumerate a fixed guard manifest covering all five sizes
(100/1K/10K/100K/1M), public hit/miss and mixed queries, short/long binary members,
batch1/batch16, all standard operations, all five update patterns, and owned bytes.
Deduplicate identical workloads explicitly; do not omit a size/pattern because
controls are noisy. Use existing validated referees and separate hashes, rather
than changing the historical harness under the comparison. Include score=NULL
API behavior in semantic validation even though timed primaries request scores.

The full guard manifest must fit the fixed phase budgets below before coding.
Otherwise NONE; do not silently shrink it. Performance adoption requires the
shared per-block gates: qualified same-session controls, >=2% improvement in
both primaries in every fresh block, no guard block above +1%, no owned-memory
increase above 1%. Unqualified guards force PARK. Primary failure rejects the
variant; do not retarget to 100K after seeing results.

The mechanism is falsified if generated code retains equivalent separate
leaf-call save/restore and output bookkeeping, or introduces offsetting spills
without another declared mechanism. A timing win with unchanged mechanism stays
PARK. Removal of memchr, changed decoding, altered leaf layout or missing full
member checks is an out-of-scope experiment, not a win for this hypothesis.

## Correctness and adversarial risks

The greatest risk is duplicated semantic logic drifting between output forms.
Exercise every score/position nullable combination, exact finite score bits and
both signed zeros, zero/64-bit and crossing-byte encodings, both leaf orientations,
binary lengths/embedded zero bytes, colliding tags, missing members, external
records, and protected-page boundaries. Reuse the frozen 4,160-cell exact-bit
oracle and original native/ASan/UBSan tests without weakening checks. Preserve
reversed-base and logical-position deliberate fault sensitivity.

Exercise insertion cursors, rank counts, leaf-ID relocation, clones, resize/SCAN
and iterator invalidation through existing frozen tests; generic callers must
retain output and ownership semantics. Beware always-inline expansion into both
old/new rehash table paths, code-size growth and assertion-path duplication.
Retain standard portable C behavior and existing endian conversion. An arm64
result supplies no x86 or actual big-endian execution claim.

## Complete <=90-minute execution design

All minute allocations are hard upper bounds after chair selection. If a phase
cannot complete, preserve partial evidence and PARK; do not borrow final-report
time or skip gates. No agent reasoning/build/test work overlaps serial timings.

1. **0–8 min:** Freeze source, exact referee/guard manifest, host/compiler/flags,
   allocator/assertion settings, discovery/held-out seeds, hashes and phase order.
   Preflight that at most 96 distinct full-matrix cells fit the timer budget.
   This ceiling is a feasibility check, not permission to drop required guards.
2. **8–22 min:** Three actual independent implementations in isolated worktrees
   or permitted isolated copies/builds, followed by native/sanitizer/oracle and
   fault checks. Keep all patches, failures and actual participant metadata.
   Inspect assembly for the declared specialization before timing.
3. **22–35 min:** Baseline-only calibration and a *new preregistered full-matrix*
   same-session A/A schedule targeting >=100 ms per window with fixed operation
   counts, using discovery seeds 1/2/3 and six ABBA blocks. This is not a rerun of
   LOOKUP-001's completed two-cell ~50 ms schedule. Freeze once; never retry a
   failed cell or tune counts after candidate observations. Qualify with the
   unchanged ±1%/10 ms rule. Retain failures as adoption blockers.
4. **35–49 min:** Serial discovery. Screen all three variants on both primaries
   with six ABBA blocks and fixed counts. If none passes, REJECT/NONE and finish
   audit early. If more than one passes, preregister smaller-change preference
   for effects indistinguishable at A/A resolution. Provisionally choose one
   for the complete guard matrix; this is not adoption. A failed guard ends
   this bounded experiment without shopping through more variants. Limit total
   candidate timed work to 300 s, retaining all rows and deterministic rotation.
5. **49–64 min:** For an eligible provisional winner only, fresh confirmation
   seeds 101/102/103, six ABBA blocks for both primaries and every guard. Fixed
   <=300 s timed-work cap. No row removal, optional stopping for a win, reused
   discovery blocks, or acceptance from a partial matrix.
6. **64–76 min:** Matched baseline/candidate public-loop profiles with validated
   sampler controls, retained insufficient captures, and generated-code review.
   Confirm the frame/output mechanism and disclose memchr, code-size and spill
   changes. No PMU/frequency/time-share claim without actual supporting data.
7. **76–86 min:** Independent confirmation audit and adversarial source/semantics/
   measurement review. A fresh-seed run is not another-machine replication.
   Missing independent review prevents acceptance.
8. **86–90 min:** Seal raw CSV/per-run rows, commands/checksums, patches, review,
   decision, remaining gaps and M1 exact patch/referee instructions for root
   publication. Preserve every prior experiment decision. Main tree source stays
   unchanged overnight even if this isolated candidate qualifies.

At 96 cells × 24 windows × 100 ms, a full matrix is about 230.4 s of timed work;
three two-cell primary screens add about 14.4 s. Setup/warmup and profiling are
separate wall-time costs, so the chair must enforce the larger minute bounds.
If calibration requires materially longer windows or setup exceeds the allocation,
PARK rather than reduce coverage. The proposed new A/A schedule can still fail;
that is an informative stop, not grounds for a second qualification attempt.

## Decision weight

Evidence is stronger for a real generic call boundary than for its performance
importance. This is a small, portable experiment with no intended memory trade-off,
but duplicated caller code could negate the benefit. I rank it below a proposal
with a demonstrated dominant mechanism and above an unchanged scanner or a
retrospectively narrowed physical-decode retry. NONE remains preferable to an
incomplete acceptance campaign.
