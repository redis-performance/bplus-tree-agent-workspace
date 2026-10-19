# Proposal C — NONE

Participant: `/root/followup_proposal_c`, an actual independent proposal agent.
Visible backend/model family: GPT-6/Codex, inherited from root. Exact serving variant,
per-agent token usage and monetary cost: unknown. This proposal did not read A/B.
Lens: adversarial measurement, semantic/ownership risk, justified specialization and
falsification. No implementation, build, test, benchmark or profile was performed.

## Recommendation

Select **NONE** for a new implementation population from these inputs. Preserve the
two existing exploratory leads and their original REJECT decisions. The evidence
supports investigating them, but does not yet support a distinct specialization
whose discriminator predicts benefit independently of the sizes that happened to win.
This is a proposal-selection decision, not a new experiment result.

I verified the frozen `src/zset_btree.c` SHA256 and all thirteen evidence-file hashes
against `input-manifest.json`; all fourteen match. The source pin is
`e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf`. I read the shared protocol, population
rules, both reports/profiles/selection records, all six patches, update census,
baseline source and retained public release assembly. No timing rows were pooled.

## Why the strongest apparent directions do not yet justify a new hypothesis

| Lead | Supporting observation | Missing discriminator or contrary evidence |
|---|---|---|
| Update repacking at 1M | All six blocks improve for each implementation; medians -7.705%, -8.765%, -9.270%. Early preserve census has 11,058 packing failures in 20,000 calls at 1M versus 1,517 at 100K. | These are existing rejected implementations. A new tree-length threshold would be fitted to the observed crossover, rather than a measured cost boundary. All three fail the 100K primary; B/C regress there in every block. Both A/A cells fail strict precision. |
| Physical-slot lookup at 100K | B improves every block by 3.482–6.243%, with qualified 100K A/A. Baseline assembly visibly computes physical-to-logical-to-physical on reversed leaves. | B already implements this mechanism. A/C implement closely related removal but fail the 100K each-block gate, so the B advantage cannot yet be attributed solely to eliminating that conversion. There is no candidate profile, and 1M effects span both signs beside failed controls. |

The update source already checks both neighbor order and exact packing in
`zbtScoreUpdateInPlace`. All three prior additions enter only after order succeeds
and packing fails. Adding another ordinary eligibility branch around the same
re-encoding is not a demonstrated new mechanism. The census identifies a failure
rate for an early phase, not the distribution of re-encoding cost, available array
headroom or useful phase duration. The long 1M preserve capture has 207 memchr PCs,
87 FindForAdd PCs and 27 UpdateInPlace PCs among 409 samples. Those counts cannot
be treated as exact shares, but they do warn against extrapolating the early
packing-failure count into a persistent update bottleneck. A worthwhile future
update hypothesis needs its transient phase declared explicitly.

For lookup, `zbtScoreLeafFindMember` also serves callers requesting logical position.
Baseline source and assembly establish the conversion opportunity; they do not
establish that width, orientation, length, leaf occupancy or tree size explains B's
distinct 100K result. The hit census shows about 31–32 tag bytes consumed per scan
and 1.14–1.16 full comparisons per query, while the retained samples emphasize
memchr. These observations do not justify replacing memchr or selecting a new
scalar cutoff. An unchanged old B patch or an arbitrary 100K-only switch would not
meet the request for three new implementations of a supported new mechanism.

## Semantic and ownership objections a future specialization must answer

Repacking changes metadata and the locations of offset/tag arrays within one leaf.
Its proof must cover overlapping movement, current allocation headroom before any
write, exact score reconstruction, reverse orientation, maximum propagation and
unchanged member/index references. A guard based on current count alone supplies
none of that proof. Prior private-oracle success supports those exact patches and
fixtures; it does not validate a newly narrowed eligibility rule.

Lookup decoding is lower risk because it does not mutate ownership, but every
combination of optional score/position outputs still matters. Width zero, width 64,
cross-byte spills, reverse-base subtraction, exact finite values and signed zeros
must remain exact. A shortcut using floating equality for no-op updates would
additionally need explicit signed-zero treatment. NaN support is not assumed.
No existing successful check is permission to weaken iterator, rank, SCAN, resize,
binary-length, collision or ownership coverage.

## Bounded evidence needed before reopening

No new implementation experiment is proposed here. If the chair also selects NONE,
retain the remaining overnight budget for the required audit/report. A separate
future evidence phase can be bounded to 90 minutes, with its own preregistration:

1. In the first 15 minutes, freeze one lead and a mechanism-level discriminator
   before collecting new data. For update, define the early mutation phase and
   inspect whether actual pack-failure/repack cost predicts the crossover. For
   lookup, define candidate-versus-control instruction/path observations that can
   explain why the generic reader B differs from A/C without using size as the
   explanation. Choose one lead, not a combined hypothesis.
2. Spend at most 30 minutes collecting the missing bounded census/profile evidence
   on unchanged baseline and retained isolated patches. These are diagnostic
   observations, not a repeat of either failed timing schedule and not adoption.
3. Reserve 25 minutes for exact-source/assembly reconciliation and independent
   semantic/measurement review, then 20 minutes to publish a new proposal or NONE.
   Stop at the bound. Do not turn an incomplete diagnosis into a source selection.

This future diagnostic outline does not satisfy implementation-population or
adoption gates and is not authorization to start it during this proposal step.

## Falsification and acceptance constraints for any later proposal

The proposed causal discriminator must predict behavior in a held-out seed/phase,
not merely identify the already favorable fixture. If its expected path change is
absent in matched candidate profiles/assembly, or if useful end-to-end benefit
does not persist in the declared phase, reject that mechanism. A new result must
preserve the original reports and cannot rehabilitate their failed objectives.

Any eventual specialization needs a new declared primary before coding and all
relevant guard sizes/patterns, including 100K and 1M, five-size update cases,
long/binary members, hit/miss and mixed lookup patterns, mutation/rank/iteration,
SCAN/resize and owned memory. Freeze one source/referee/compiler/allocator and
three isolated implementations, qualify same-session controls, measure serial
ABBA with at least three blocks (six under the current protocol), then use fresh
confirmation seeds and matched profiles. Require >=2% primary improvement in
every fresh block, no guard block above +1%, no >1% owned-memory increase and
independent adversarial review. Noisy guards mean PARK; no guard is dropped.
If the complete matrix exceeds the bounded campaign budget, defer acceptance.
M1 replication stays separate and NOT RUN until performed with matching patch and
referee identity. No source adoption is recommended.
