# Proposal A — NONE for a new packed-score/mutation implementation

Participant: `/root/followup_proposal_a`, an actual independent proposal agent.
Visible backend/model family: GPT-6/Codex, inherited from the root. Exact serving
variant, token usage and monetary cost: unknown. No other proposal was inspected.
Only this assigned proposal file was written. No implementation, build, test,
benchmark, profiling, agent launch, permission change or Git write was performed.

## Frozen input and recommendation

Source commit: `e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf`.
Observed `src/zset_btree.c` SHA256:
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
The source matches the common manifest; all thirteen listed evidence hashes were
verified. I read AGENTS.md, shared memory, docs/POPULATION.md, the common review
input, shared measurement rules and the listed update/lookup reports and patches.

**Vote: NONE.** The retained mutation observations support a useful investigation
of representation-changing updates, but do not yet support selecting a genuinely
new packed-score mechanism with a defensible end-to-end gain and full validation
inside ninety minutes. This is a proposal-stage recommendation, not a reversal of
any completed experiment and not a claim that the lead is false.

## What the evidence establishes

`003-update/PROFILE.md` and `census.json` identify a concrete format constraint:
order-preserving updates fail exact packing 1,517/20,000 times at 100K members and
11,058/20,000 at 1M. Neither preserve cell has a neighbor-order failure. Same-value
updates already succeed in place in every size. Nearby/distant/plus-n initially
fail neighbor order, so a score-repacking optimization cannot remove those moves.

The three retained update patches already exploit the natural allocation-saving
mechanism: after neighbor checks pass, re-encode scores in the existing allocation
when metadata fits before `record_start`, preserving member records and leaf IDs.
Their measured 1M reductions are consistent across blocks: medians 7.705%, 8.765%
and 9.270%. However, at 100K A is unresolved near zero and B/C regress in every
block, with medians +1.694%/+1.992%. Both update A/A cells fail strict qualification
(maximum absolute effects 1.1722% and 1.5527%). These are exploratory measurements,
not a shortlist or an adoption result.

The long preserve profiles weaken an assumption that score recoding dominates the
public operation. At 100K, 51/128 sampled PCs are in memchr, 22 in FindForAdd, 17 in
LeafFindMember and 12 in UpdateInPlace. At 1M those counts are 207/409, 87, 48 and 27.
These are descriptive sampled PCs, not unbiased time shares. They nevertheless
show that lookup remains prominent after amortization. Existing evidence does not
separate one-time format transitions from later steady representation reuse.

`004-lookup/RESULTS.md` supplies a stronger qualified-size lead outside this lens:
physical-slot B reduces 100K time in every block, median 4.800%, against maximum
0.745% A/A variation. Its 1M result remains unresolved and the declared dual-primary
experiment is correctly rejected. It has neither candidate profile validation nor
complete guards. I do not nominate the unchanged patch as a new implementation.

## The genuinely new mechanism considered, and why it is not nominated

Exact target: `zbtScoreUpdateInPlace`, `zbtScoreLeafPackScore`, the packed bit helpers
and a new cold repacking helper in `src/zset_btree.c`; no header or layout changes.
The unmeasured idea is to transcode existing packed integer deltas directly when a
new score only requires lowering the shift and/or widening the packed field while
retaining the base. Existing C first decodes every score to double and then encodes
it again; the new mechanism would operate on raw physical-slot deltas, preserve
metadata/member ownership, and retain the normal fallback for rebasing or lack of
headroom. This would be distinct from applying the existing C patch unchanged.

The mathematical opportunity is real: with a retained base and a lowered shift,
an old raw delta can be left-shifted into the new representation. But the available
census does not count how many packing failures satisfy that restricted case,
how often the conservative width envelope fits the allocation, or how expensive
full decoding/re-encoding is relative to the avoided removal/reinsertion. The
profiles do not establish that reducing this extra recoding work can recover the
100K guard loss or produce >=2% in the full public 1M loop. Increasing operation
counts would also change how strongly the transient is amortized; it must not be
presented as an unexplained precision cure.

A tree-size threshold at 100K/1M would be especially poorly justified. The mechanism
is a leaf-format property, while the observed cut points also reflect cache and
access history. No evidence establishes a portable threshold or supports using a
size check to hide a failed guard. A new 1M objective could be legitimate if declared
before measurement, but the 100K cell and every other relevant guard would remain.

## Revisit conditions and correctness obligations

Before another implementation population, obtain a separately preregistered,
bounded diagnostic that records packing-failure reason, old/new width and shift,
orientation, available headroom, and failure frequency by sweep phase for the
unchanged five patterns and five sizes. Match scoped baseline profiles to the
public timed phase, retaining FindForAdd, target computation and checksum work.
Do not rerun the completed A/A schedule unchanged or reuse its timings as controls.
That diagnostic is a future action for the chair to authorize, not work performed
by this proposal agent and not a proposed ninety-minute adoption campaign.

A subsequent real trial would need 100K and 1M preserve cases retained explicitly,
all five patterns at 100/1K/10K/100K/1M, long binary keys, lookup/rank/iteration and
memory guards. Freeze exact source/referee/flags/allocator and fixed counts before
three isolated implementations. Controls, serial ABBA discovery, fresh confirmation,
matched candidate profiles and adversarial review remain mandatory. Missing/noisy
guards mean PARK; no demonstrated >1% guard or owned-memory regression is allowed.

Direct packed transcoding adds risks beyond the existing patches: shift-by-64 UB,
zero-width handling, full-width/cross-byte fields, overlap while widening in place,
both orientations, tail padding, metadata movement and rollback before any write
on insufficient headroom. Exact finite bits including signed zero, tie ordering,
external member ownership, leaf IDs, subtree maxima, iterators and SCAN all remain
obligations. A raw-delta oracle alone cannot establish those public semantics.

There is no evidence-based reason to promise that completing those new mechanism,
qualification, correctness and independent acceptance gates will fit ninety minutes.
Record the lead and proceed with another proposal only if its evidence is stronger;
otherwise preserve source NONE and finish the audit/report.
