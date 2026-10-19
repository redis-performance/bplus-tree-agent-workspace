# Independent proposal B — NONE

Recommendation: **NONE for a new source optimization from these inputs.** The
generated code exposes a possible scheduling window, but the retained evidence
does not establish a new profitable load-scheduling mechanism at both primaries.
Do not reopen physical decoding, caller inlining or their rejected patches.

Participant `/root/followup_proposal_b`, actual independent proposal agent.
Inherited backend visible: Codex/GPT-6 family. Exact serving identifier, measured
token usage and monetary cost unknown. No A/C proposal was read. Only this assigned
proposal was written; no implementation, build, test, benchmark, profile, agent
spawn, Git or shared-memory action was performed.

## Evidence reviewed before deciding

Read the frozen review input and all listed report/profile/geometry inputs, the
006 101-cell plan and baseline source/assembly. Read-only SHA256 verification passed
for all 13 manifest entries. Baseline source remains
e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf, C SHA256
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.

The baseline `zbtScoreLeafFindMember` instruction sequence is concrete:

1. `memchr` returns a matching tag address.
2. Subtraction gives its physical slot; a dependent 16-bit offset load identifies
   the record, followed by its header/full external hash and member pointer/length.
3. Equal length reaches `memcmp`; only an exact match reaches score decode.
4. The matched-score path reloads score width/orientation, computes its slot's
   packed-word address, reads the word and possibly a ninth byte, then reconstructs
   the exact score using the original decoder.

In the retained leaf assembly, the offset load is at relative instruction region
`aa24`, record-header load at`aa2c`, member comparison call at`a9f8`, and matched
score-word load at`ab44`. These addresses identify ordering within that frozen
binary, not portable addresses or measured latency. The leaf is a separate 144-byte
frame and the caller 176 bytes; changing that boundary is already closed by006.

007 adds useful geometry: every observed nonzero-width candidate/match has its
score-word and record start in different diagnostic64-byte blocks. For16-byte
hits, mean score-word/record separation is about 15 blocks at 100K and 14.9 at 1M.
This means the record address does not identify the score word's storage block.
It does **not** show either access missing a hardware cache, a serialized stall,
a hardware line size, or a profitable prefetch lead time.

Successful queries visit about1.0144–1.01475 leaves at 100K and 1.00770–1.00815 at 1M,
with about 1.15/1.14 tag candidates/query. Most 16-byte candidates therefore incur
a record/full comparison, including the extra false candidates. At 321 bytes the
external full-hash filter rejects almost all extra candidates before comparison:
20,003/20,004 full comparisons for 20,003 hits. Hoisting score-related work before
that filter would introduce work on rejected candidates. Its cost is unmeasured.

Old hit profiles meet their sample minimum and observe the region:100K has 57 of 139
PCs in memchr and 30 in the leaf helper;1M has 148 of 266 in memchr and 27 in the helper.
These sampled symbol PCs cannot assign cost specifically to the final score load,
record-load dependencies or call overhead. Two small-miss captures remain
insufficient. No unchanged recapture or inference from diagnostic timer fields
is justified.

006 matters as a falsification constraint: exposing the leaf body removed calls
but grew caller instructions 345→601 and its frame 176→240. All three read-only
instruction streams coincided and no implementation passed both primaries. A's
1M effects were all negative, but only two blocks reached −2%; that experiment
supplies no license to assume additional source scheduling yields the missing
gain. It also leaves 62 of 101 control cases unqualified at 100 ms.

## Missing causal link

A portable hint or early existing-word load could in principle overlap the score
word with record/member validation while retaining original decoding. I do not
select it as a supported hypothesis here. The prospective word address needs the
memchr slot and width; moving work earlier trades possible latency overlap for
extra false-candidate work, register lifetime, spills and instruction footprint.
The census only establishes separate addresses. It supplies no evidence that the
late word access is the limiting event or that sufficient useful independent work
remains to hide it on this M6 at 100K **and** 1M. Out-of-order execution and platform
memcmp/memchr already complicate any source-order latency claim.

Likewise, prefetching a fixed part of the leaf before the tag is known does not
identify the eventual word for broad widths. Ordinary fixtures overwhelmingly use
6/7-bit scores and zero reversed leaves. Such a guess could accidentally favor
the current geometry while wasting traffic on the required broad/reversed guards.
The existing source already preserves memchr/memcmp and the decoder; deleting or
rewriting those operations is outside this population's scope.

This is a missing mechanism measurement, rather than a claim that load scheduling
can never help. I cannot justify a new end-to-end>=2% prediction at both declared
sizes from geometry alone, so I submit no new implementation population.

## Revisit conditions and retained failure criteria

A revisit needs a new, separately preregistered public-loop diagnostic resolving
which existing dependent loads contribute to the hot path, and a causal test
capable of falsifying the proposed overlap. Hardware counters would help when
actually available, but are not a reason to discover private access or change
permissions. A new sufficiently resolved public self-sampler/assembly analysis
plus a bounded causal diagnostic is another possible route. Its perturbation,
scope and limitations must be retained. A census timing or symbol count alone
does not meet this condition. Preserve both 100K/1M primaries and all prior decisions.

Any eventual score-load proposal must show its intended ordering in generated
code and retain decoder text/algorithm, scanner, layout, hashing and public API.
If the compiler restores the old ordering, if no useful lead window exists, or
if altered code mainly repeats the closed physical-decoder/inlining mechanism,
the new mechanism is falsified before a speed claim. Additional false-candidate
work and nullable score/position outputs need explicit treatment. Score=NULL must
remain valid; finite-score bit patterns, signed zero and all binary lengths,
ownership, leaf IDs, rank, resize/SCAN and iterator checks remain mandatory.

Acceptance would still require both primaries <=−2% in every fresh block, all speed
guards <=+1%, owned-memory increase <=1%, qualified controls, fresh independent
confirmation, matched profile validation and independent adversarial review.
Noisy controls force PARK; no failed cell may be omitted or count-retuned.

## Guard inventory and 160-minute feasibility

Retain the exact 101 case inventory from 006: 40 standard cells, 30 independent query
cells (five sizes plus member-length boundaries), 6 batch1/16 cells, 25 update-pattern
cells. Both100K/1M public successful-score-query primaries remain unchanged.

For a future score-read scheduling hypothesis, throughput guards must additionally
represent verified normal/reversed storage and broad exact finite score widths,
including signed zero behavior, rather than rely only on the private semantic
oracle. A possible *future preregistered* inventory is 24 extra cells: 2 sizes × 2 actual
orientations × 3 finite-score families (zero/equal, narrow, broad) × hit/mixed query.
That is a budgeting example, not a validated fixture plan or permission to assume
descending insertion makes large trees reversed. 007 and historical fixture
experience require verifying actual request-weighted orientation/width first.
If those public histories cannot be constructed/validated within budget, NONE.

With 125 cells, six ABBA blocks and 500 ms windows, a complete phase already contains
1,500timed seconds. All three dual-primary screens add 72 seconds to discovery;
1,572 seconds fits the provisional 1,800 timed cap. Controls, complete discovery
and fresh confirmation together have a 76.2-minute timed-work floor. The proposed
three 2,400 second phase wall caps can consume 120 minutes, leaving 40 of 160 minutes
for proposals/chair, three isolated implementations, new epoch/score fixtures,
fault validation/freezing, calibration, profiling, independent review and sealing.
This arithmetic does not prove impossibility, but does not establish feasibility.

The critical unmeasured cost is new replicated mutation epochs: setup/checking
must remain outside each segment, retain the 64 MiB/replica bounds, record every
segment length, and meet >=10 ms per segment rather than only a 500 ms sum. New broad
fixtures also add preparation and validation cost. Their unknown overhead cannot
be silently charged to spare wall time or covered by dropping guards. Even a
timely new A/A may fail; the old 100 ms schedule cannot be retried unchanged.

Before any future implementation, the chair needs a separately frozen complete
phase-cost/fixture plan that fits both 160 minutes and the absolute 06:30 UTC stop,
including independent confirmation/profile/review. Missing time or any gate
means PARK/NONE. Given the present causal evidence gap, spending that budget on
three source variants is not supported by this proposal.
