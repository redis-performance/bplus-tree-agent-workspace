# Independent ARM participant proposal: NONE for this measured round

Actual author `/root/aws_arm`, native Codex agent. Exact serving model, token cost and
monetary cost unknown. Read only the shared AMD009-delete packet at a04b9f69d, its
linked census summary and baseline8fab511e source, plus root's shared control update.
No AMD/Intel proposal or chair decision was read. Prior context includes the chair's
assignment naming the conditional offset-adjust loop; this is separately authored,
not blind to the common operational discussion. No candidate code was written.

The mechanism is supported enough to retain a falsifiable hypothesis: replace each
conditional offset store with an unconditional value-preserving update, computing an
unsigned addend of either zero or deleted_bytes. On this exact Clang18/Zen5 build this
may let the compiler emit compare/mask/add plus contiguous vector stores instead of
SIMD comparisons feeding individual conditional scalar stores. Restrict the change to
the final compact_records loop. Do not fuse earlier relocation, modify compact_records,
change the score decoder, allocator, flags or tree representation.

The packet attributes101/1844 same-IP samples (~5.50%) at1M to the exact loop ranges;
this is coarse evidence of cost, not a cycle-perfect speed ceiling. The100K range has
only7 samples, too few for precise headroom. The observer shows roughly67.6 offsets
per compacting call, about49.5% adjusted, about98.6% mixed loops, and88.6% of offsets
inside full16-lane groups. Those support testing branch removal but do not establish
branch misprediction, store bottlenecks or any particular speedup. Rewriting source
alone is not enough: compiler output must actually eliminate the conditional-store
sequence before any performance interpretation.

Risks: unconditional stores nearly double written offsets in the average loop; this
can cost store throughput despite removing branches. Offsets are ordinary owned
uint16_t cells, but use explicit unsigned comparisons and defined narrowing of the
existing size_t addend; do not reinterpret signed16-bit lanes or assume offset bounds
without proving them. The loop follows overlapping offset relocation and tag copying:
keep those operations ordered, avoid unproved restrict annotations, and remain inside
count. Validate compact_records=false score updates, external ownership, reversed leaves,
short/tail counts and every unchanged offset. A portable C formulation is preferable
before architecture intrinsics; assembly may still choose the old code.

Counterfactual preregistered prediction: if the compiler emits contiguous vector stores,
the loop's matched-profile share should fall and both original delete primaries should
improve at least2%, with no demonstrated >1% original-operation or owned-memory guard
regression. Reject if emitted code is unchanged, correctness differs, either qualified
primary fails the speed gate, or a qualified guard regresses. Park on unresolved precision;
never turn the census into a performance result.

Decision for the present round is NONE, because the fixed fresh1M A/A already failed
(+0.527,+0.520,+0.499,+4.682,+3.035,+1.087%), while100K qualified (max0.742%). The chosen
dual-primary acceptance is unreachable with these controls, and no retries or operation
adjustments were authorized. Preserve the supported mechanism for a future independently
qualified campaign; do not force three measured implementations tonight merely to fill
a population. This decision creates no candidate, measured population or timing claim.
