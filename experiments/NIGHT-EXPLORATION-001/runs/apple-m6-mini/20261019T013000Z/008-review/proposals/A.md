# Proposal A — NONE: geometry does not yet establish a paid dependency stall

Participant `/root/followup_proposal_a`, actual independent proposer. Inherited
backend/model family GPT-6/Codex; exact serving identifier, token usage and monetary
cost unknown. I authored the007baseline census and disclose that prior involvement.
Every proposer receives that same frozen evidence; I did not inspect B/C proposals.
Only this assigned proposal file was written. No source implementation, build,
profile, timing, agent launch, Git operation or shared-memory change was performed.

All thirteen frozen input hashes verified, including baseline C SHA256
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`
at source commit e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf.

**Recommendation: NONE for a new public-lookup source trial from this lens.**
There is a structural opportunity to investigate score/member load overlap, but
there is not yet evidence that a new source ordering removes a material paid stall
rather than performing extra work. The storage census must not be promoted into
cache-latency evidence. This vote leaves all previous objectives/decisions closed.

## Causal path and observed evidence

Baseline release assembly in004's zbtScoreLeafFindMember shows this source path:
memchr finds a tag; the physical index selects a u16 offset; that offset selects the
record; record kind/hash/length checks select member bytes; memcmp establishes
identity; only on success does the original decoder load the packed score and
produce the output. The helper preserves logical/physical orientation handling.
The original decoder, scanner, layout and hashes are outside this trial's allowed
changes. The two prior routes that changed physical decoding or helper exposure
have already failed their dual-primary gates and cannot be recycled as new choices.

The007census confirms separate storage locations. Every observed candidate/match
with nonzero score width has score-word and in-leaf record starts in different
64-byte diagnostic blocks. Mean matched separation is14.84–15.61blocks for16-byte
members and18.04–18.20 for321-byte members. Offset-entry and score starts are also
usually separate. All requested random-built trees are normal orientation and
matched deltas overwhelmingly have6/7bits, with rare8/16/17bit cases. These facts
locate the bytes but say nothing about their residency or load completion latency.
A score word is near the already used leaf header as well as being far from the
record; distance from the record alone is not evidence of a fresh expensive fetch.

The004public-hit profiles show leaf/memchr regions, with memchr57/139sampled PCs at
100K and148/266at1M. They do not distinguish a packed-score stall from record/tag
work, measure branch speculation or assign exact runtime shares. Small-miss profiles
remain insufficient. The release instruction sequence is static order, not evidence
that an out-of-order core waits until the preceding memcmp call has resolved before
issuing all later independent work.

The007request counts also quantify the bill for unnecessary work. Short-key hits
have1.138–1.155tag candidates/query: a score operation placed on every tag candidate
would execute approximately13.8–15.5%more often than the existing exact-match score
read. At321bytes the existing full-hash filter makes only20,003/20,004memcmp calls
for20,003hits even though there are23,056/23,124tag candidates. Work placed before
that filter would partially defeat an already effective rejection. Misses reach
leaf search only0.01550–0.02705times/query and do not read matched scores. These
are operation-count costs, not measured elapsed percentages.

## Why no hypothesis is nominated

The strongest score-read ordering idea would need to overlap an original decoder
read with independent member verification without altering the decoder. It is
conceptually distinct only if it genuinely changes scheduling, rather than merely
removing the already tested physical/logical round trip. The current record lacks
proof of generated scheduling, stall cost and a useful end-to-end bound. It also
lacks reverse/wide-score throughput evidence needed to bound the extra-work cost.
I therefore do not nominate or implement that idea under another name.

In particular, the native geometry does not show cache misses; separate64-byte
virtual blocks are not measured hardware cache lines. Predicted return/branch paths
and compiler scheduling could already overlap some loads. Explicit earlier work
could increase live registers or expand the helper again, repeating the code/frame
pressure exposed in006. None of those outcomes can be ranked from this census.

006A's100K reductions are real exploratory observations, but its1M blocks do not
all meet2%; B/C fail as well. Their normalized lookup instruction streams coincide,
so timing differences do not identify three useful mechanisms. Full candidate guards,
fresh confirmation and matched profiles were never eligible. No subset of those
observations rescues a new universal score-read hypothesis.

## Concrete revisit condition

Before selecting this lens, obtain a separately preregistered baseline diagnostic
that can distinguish member-verification stalls from packed-score work or otherwise
bounds their overlap opportunity. Combine matching release instruction inspection
with a phase-matched profile/causal control; record counter availability honestly.
A hit-localized source-order argument must explain what independent work becomes
available earlier, which extra work occurs on false candidates, and why CPU/compiler
speculation does not already supply the overlap. Retain nullable-output behavior and
long-member filtering. Another geometry sample or unchanged failed A/A is not that
missing evidence. If no such diagnostic is feasible, keep NONE and report the lead.

Any future selected score-read trial retains the original100K+1M public successful
lookup primaries and every101guard. Before implementation it also needs explicit
normal/reversed and narrow/broad finite-score throughput fixtures, including signed
zero, width0/full-width/cross-byte fields and binary member lengths. The existing
semantic oracle alone does not clear those performance guards. No tree-size switch,
cache-line-size assumption, primary relabeling, guard pruning or allocator/assertion
change is supported.

## Budget feasibility and decision criteria

A500ms revision could be a legitimate separately frozen referee, but longer windows
are not an established noise remedy. With101cells and six process-level ABBA blocks,
one full phase requires at least101*24*0.5=1212seconds, or20.2minutes of timed work.
A/A, full discovery guards and fresh confirmation alone require60.6timed minutes;
three two-primary screens add1.2minutes. Reverse/wide additions, independent epochs
for capped mutations, all setup/verification, builds, profiles, review and publication
remain extra. Prior006A/A used250.6timed/545.5wall seconds, so setup cannot be ignored.
The160minute/absolute06:30UTC limit may fit a tightly bounded stronger proposal, but
there is little room for inventing and validating an additional causal diagnostic
inside the same full acceptance campaign. This is a feasibility limit, not proof
that any other proposal cannot fit.

If root selects a stronger proposal, freeze the entire case/epoch count first;
every segment must retain its own duration and owned-memory observations. No source
or count retuning after candidate results. Require >=2% improvement in every fresh
block on both primaries, qualified same-session controls and no >1% guard/memory
loss, plus independent confirmation, matched profiles and adversarial review.
Missing/noisy stages mean PARK/NONE. Stop before06:30UTC or160minutes, whichever is
earlier; do not trade final review time for another exploratory run. For this proposal
there is no implementation population or timing schedule to execute: selection NONE.
