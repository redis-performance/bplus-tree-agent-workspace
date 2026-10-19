# ARM independent proposal: unswitch folded-tag selection outside the vector loop

**Proposal:** one source-only hypothesis: for complete native AArch64 16-byte tag
chunks, select ordinary exact equality versus folded0/1 matching once before entering
the chunk loop. Each selected loop must have no per-chunk scalar-to-vector fold
predicate reconstruction. Preserve exact physical lane order and the original word/
scalar residual and portable fallback. Compare any resulting implementation against
unchanged8694/source13e, never merely against rejectedB.

This is a hypothesis worth a tightly gated implementation check, not a predicted
winner. If ordinary-loop code generation does not acquire a clear instruction-path
advantage over the baseline, select NONE before timing. All prior017 results remain
REJECT; this proposal does not relabel that population.

## Evidence and burden of proof

The immutable c3323969a packet supplies qualified fresh701–703 controls, the complete
017 rejection, exact018 assembly, and independently reconstructed019 profiles. B was
55–79% slower than baseline. Its explicitly reconstructed predicate accounts for only
16.87–17.67% of timed sampled period. Simply subtracting that fraction would not
establish recovery of the prior loss, much less a2% improvement. I do not use that
fraction as a projected speedup or a maximum possible recoverable cost.

The reason to consider this distinct source form is broader generated-code behavior:
the rejected B forward zero-mask path has51 instructions per16bytes versus38 for two
baseline8-byte chunks.35 instructions reconstruct the fold predicate, after which the
vector results are normalized through `shl`/`cmlt` before `shrn`. A source branch that
makes ordinary equality unconditional within its loop could eliminate both conversion
and unnecessary normalization while retaining the intended wider comparison. That
would be a materially different instruction path, not an assumption that the exact
17% sampled region maps one-for-one to elapsed time.

An additional read-only inspection of the same019 sample classifications found the B
forward loop-continuation address0x10588 holds35.64%/27.85% of timed sampled period and
match-loop entry0x10654 holds13.07%/11.18% at100K/1M. Those are sampled instruction
locations, not proof those simple instructions themselves cost that much. Skid,
branch/dependency stalls and attribution overlap prohibit assigning these percentages
to fold reconstruction or promising their removal. This observation increases the
need for matched profiles after any survivor; it is not an additional timing result.

## Mechanism and alternatives ranked

1. Select ordinary versus folded matching outside the complete16-byte chunk loop.
   Ordinary matching uses direct equality against the requested high tag; folded
   matching returns every physical byte equal to0 or1. Extract and enumerate an exact
   lane mask in ascending physical order and apply the existing reversed mapping.
   Preserve bounded loads and unchanged8-byte/scalar tails. Prefer the already
   understood whole-nibble extraction/clear form so the compiler need not synthesize
   the A/C forward popcount loop; that is a maintenance/codegen constraint, not a
   claim that rejectedB won performance.
2. Hoist an explicit full-byte vector fold mask and retain one branchless chunk loop.
   This is shorter source, but the current compiler may recreate the same boolean
   narrowing/expansion; I rank it below explicit invariant dispatch for falsifiability.
3. NONE if static lowering or any required control fails. A new compiler/ISA flag,
   changing the referee, eliminating correctness checks, or reducing the regression
   threshold is outside this proposal. Retrying rejected017 is not an alternative.

No code is supplied here. Independent implementers may differ naturally in spelling,
but should implement the one chair-selected mechanism, not three unrelated targets.

## Before-timing stop criteria

Use the exact source/compiler/options and identical frontend paths. Native disassembly
must show no35-instruction fold reconstruction in the ordinary16-byte loop, no per-lane
predicate stores/reload/insertion chain there, and no A/C-style population count to
control its mask iteration. A continuing forward zero-mask ordinary chunk should take
at most20 instructions per16bytes, counted explicitly with branch boundaries, versus
baseline38. This is a static screening condition, not a speed model. If the compiler
merges the loops back into the rejected form or the instruction advantage is absent,
stop that implementation without performance timing; do not retune flags or source
based on timing. The chosen20-instruction threshold is proposed before new code/data.

Full native and sanitizer correctness remains required, including the unchanged43
checks and V2 oracle, designated portable fallback, page-edge/misaligned complete
chunks, every fold/ordinary tag and zero spans, reversed positions, residual tails,
member/score/signedzero semantics and resize/generation tests. Preserve deliberate
fault controls without claiming a cardinality abort is a page-fault demonstration.

## Predictions, guards and rejection

Ordinary16-byte fixtures should show the clearest generated-code reduction. Dense
ordinary/folded distributions may expose output-mask iteration rather than scan cost;
folded cases could lose from duplicated code or entry dispatch. Short leaves below16
must enter the unchanged residual path before vector setup. Reversed leaves must keep
physical enumeration and logical conversion; active resize, long keys, width boundaries
and tree-owned memory remain mandatory guards. Code duplication and register pressure
can erase the expected static gain, and the compiler may still change later decoding.
The portable path must stay semantically and structurally unchanged.

A fixed discovery requires at least2% improvement in every preregistered primary block
at both100K/1M against unchanged8694, qualified controls and exact semantic/memory
parity. Otherwise REJECT/NONE; no claim that merely being faster than rejectedB is
useful. A survivor still needs fresh independent confirmation, all required qualified
guards (mixed/noisy/incomplete means PARK), matched profile and adversarial review.
A matched profile must verify actual source-linked ordinary-loop code and whether the
predicate overhead disappeared; sampling alone cannot substitute for end-to-end gain.
No candidate switching after later failure, no retries/exclusions, and no new experiment
after07:15UTC. Even a correct and smaller loop may simply fail the benchmark.

## Provenance

Actual author /root/aws_arm, separately authored without reading current Intel or AMD
proposals. I authored rejected017 A and the shared guard/profile orchestration, and
am not blind to that history, root discussion, or peers' already sealed017 patches.
I read the common packet and original source plus018/019 immutable evidence; the
additional top-IP inspection used only existing samples. Native Codex agent; exact
model, measured token usage and monetary cost unknown. No new source or timing.
