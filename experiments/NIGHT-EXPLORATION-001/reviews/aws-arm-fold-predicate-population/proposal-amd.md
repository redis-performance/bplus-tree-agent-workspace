# Independent AMD proposal: NONE

**Recommendation: select NONE for a new source implementation population from this
packet.** The predicate reconstruction is materially sampled and is avoidable-looking
compiler output, but the current evidence does not support a sufficiently large gain
against unchanged baseline869425... . This is not a claim that a replacement cannot
win. It is a judgment that a positive prediction would currently exceed the evidence.

I read only common immutable packetc3323969a and its already reviewed018/019 evidence,
plus fresh020 control results stated in the packet/root assignment. I did not read
other agents' proposals. I authored prior017 C and independently audited the rejected
raw discovery/static code/profile. That history is disclosed; this proposal is not
blinded to prior results. Root separately chairs the actual independent proposals.

## Evidence and baseline-relative feasibility

Corrected source13e459ff8, baseline869425..., compilerClang18.1.3/-O3, assertions,
allocator and referee remain fixed. Fresh020 baseline controls qualify all six blocks
at100K/1M; this makes a correctly frozen comparison measurable. It supplies no evidence
for the magnitude of an unimplemented replacement. Older failed controls stay final.

All prior variants lost every discovery block. Even B, the diagnostic source rather
than a winner, has median+78.160678% at100K and+55.341943% at1M. To achieve a2% gain
against the unchanged baseline, a replacement derived from B would need to reduce B's
elapsed time by about44.9935% and36.9134% respectively. This is the relevant hurdle;
being faster than rejected B would not satisfy it.

The exact35-instruction reconstruction in each fullchunk is real; both directions
repeat it. Matched samples assign17.669828%/16.866355% of B's timed-call-site period to
those70 addresses, with400/421 events and all preregistered gates passing. The region
is worth understanding, but those shares alone are much smaller than the required
whole-operation improvement from B. Merely as an illustrative, noncausal accounting
exercise, removing those entire fractions from B would still leave about+46.68% and
+29.14% elapsed relative to baseline. Sampling skid, dependency chains, register
allocation and unequal instruction costs make that arithmetic neither a rigorous
bound nor a prediction. They also do not justify assuming the missing recovery.

Static B zero-mask continuation is51 instructions per16bytes versus two baseline
chunks'38. Hoisting a correctly represented fold mask could eliminate much of that
instruction expansion and perhaps its normalization. However, a static count is not
retired work or latency, only one path is counted, and output/residual/decode layout
also changed. The surviving mask extraction, vector-to-scalar transfer and other
changes have no counterfactual cost measurement. The~17% result cannot establish
that these interacting costs disappear with a fold-mask rewrite.

## Ranked alternatives and falsifiable future direction

1. **NONE now.** Preserve the rejected population and profile, and do not spend a new
   implementation/timing population on an unsupported baseline-relative forecast.
2. Deferred source hypothesis: construct one all-zero/all-one byte-vector fold mask
   from tag==1 before the fullchunk loop, then combine exact zero/equal comparisons
   by bitwise masking instead of the source conditional. This is a precise mechanism
   for eliminating repeated predicate unpacking, but it currently predicts recovery
   from rejected B more convincingly than a2% win against baseline. It is not selected
   by this proposal and no code is supplied.
3. Duplicating entire loops for fold versus ordinary tags might avoid predication but
   adds code footprint/control-flow risks and broadens layout changes. It has weaker
   review and attribution clarity; do not combine it with mask-enumeration changes.

The deferred hypothesis is falsified mechanically if the same per-chunk stack
stores/reload, scalar bit extraction and lane reconstruction remain, or equivalent
work is merely moved to each chunk. Elimination alone would not validate performance.
A baseline-relative claim would still require every frozen primary block at both sizes
to meet<=−2%, all qualified guards<=+1%, exact owned-memory parity, independent held-out
confirmation and a matched profile. Any failed primary ends that direction; no B-only
speed comparison, timer retry, alternative fallback, count change or source adoption.

## Risks and bounded evidence requirements if chair selects a source hypothesis

Do not change the baseline/referee/compiler to obtain the desired lowering. Preserve
folded stored0+1 semantics, exact allmatch cardinality and physical order, reversal,
zero-count and misaligned complete-vector bounded reads, word/scalar tails, binary
member lengths, exact finite scores and signedzero, scan/resize/generation/leaf-ID
maintenance, and source-local portable fallback. The same immutable original43 tests,
V2 guard oracle, scaninterval, wide/live-widen and resize suites plus retained fault
controls should run under the previous bounded600s serial validation cap. Forced
fallback is not proof of actual big-endian execution. Static codegen is a prerequisite,
not an excuse to tune flags or variants after timing.

Any later profile must use exact selected timing code or prove instruction mapping,
retain complete unfiltered denominators/losses, distinguish full-process PMU from the
exact-return-PC post-filter, and avoid charging ancestors or baseline offsets to the
candidate. Expected reduction in the predicate region must not be presented as recovered
elapsed cost. Any new performance schedule and guards need a separate immutable plan;
this proposal authorizes no measurements. No new experiment after07:15UTC and no
unbounded work to force a positive result before fleet release08:00UTC.

Actual author: /root/aws_amd, native inherited Codex. Exact backend model identifier,
token usage and monetary cost unavailable/unknown. One real independent proposal;
no invented reviewers, stronger model, or completed skill-panel workflow. SourceNONE.
