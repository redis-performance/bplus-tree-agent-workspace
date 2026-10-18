# Proposal A: expose the leaf-invariant crossing class to the compiler

Independent proposal by agent `/root/proposal_a`, 2026-10-19. No other proposal
was read. Exact backend/model and token/currency cost are unavailable and remain
unknown. Source reviewed at `4fd3a3fdbce5acca18ee292642a3d80a79f50362`;
production decoder is still the original baseline. No build, timing, or source
mutation was performed for this proposal.

## Evidence and hypothesis

The latest frozen decoder matrix shows EXP-004 A worsening forward width 8 by
15.65%, width 60 by 4.72%, and width 64 by 10.39%. Its static decoder-loop branch
count fell from 29 to 24, so branch count alone is insufficient evidence of gain.
The historical EXP-004 interrupted-PC profiles locate substantial samples inside
`zbtreeIteratorNext`, while its assembly shows inlined score decoding and the
baseline's aligned-offset short circuit. These are historical localization and
code-shape evidence, not current-cycle attribution or proof of the regression's
cause. References: EXP-004 `decoder-microbench-2026-10-19/README.md`,
`codegen/summary.json`, `profiles/SUMMARY.md`, and `profiles/ITERATOR-ASSEMBLY.md`.

Hypothesis: separating non-crossing widths from crossing-capable widths in
`zbtScoreLeafScore` allows a leaf-invariant condition to bypass all ninth-byte
predicate arithmetic on the common class, improving warmed decoder throughput
without changing packed layout or increasing tree-owned memory.

For physical position p, the offset is `(p * bits) & 7`. Only widths 59, 61, 62,
and 63 can satisfy `bits + offset > 64`. Width 58 reaches offsets 0/2/4/6;
width 60 reaches 0/4; width 64 reaches only 0. Widths at most 57 trivially fit.
This is an exact geometry fact, not an inference from sampled fixtures.

## Concrete implementation

Keep zero-width handling, packed load, endian conversion, masking, score shift,
orientation, and ordered-score conversion unchanged. Expose a small inline
crossing-class predicate (`bits > 58 && bits != 60 && bits != 64`) and put the
ninth-byte path exclusively beneath it. Preserve the original conditional
read in the crossing-capable path. Equivalent source forms can be the three
implementation variants; do not mix in mask simplification or member decoding.

Prefer a branch around the ninth-byte block over function-pointer dispatch or
iterator caching for this first bounded test. No header/layout changes are needed,
and the existing referee calls the actual changed production decoder unchanged.

## What once-per-leaf means with the current API

The microbenchmark contains an explicit per-leaf position loop. After inlining,
the compiler can hoist or unswitch the width-class test outside that loop. Inspect
assembly to establish whether it actually does so. A source-level invariant does
not prove that the generated binary dispatches once per leaf.

The production scalar iterator calls `zbtreeIteratorNext` separately per item;
this design still checks the width class per scalar call. It cannot honestly be
called once-per-leaf dispatch in that API. Strict once-per-leaf dispatch there
would require cached iterator mode updated on every seek/start/leaf transition
(still a mode branch each item), or a cached function pointer (an indirect call
each item), or a new bulk API/referee. Those add different hypotheses and should
not be smuggled into this small source experiment. If the chair requires strict
dispatch-once in both contexts, PARK this proposal rather than mislabel it.

## Predictions, risks, and falsification

- Primary: forward width 60 should improve by at least 2% against the original
  baseline when its impossible crossing work disappears. Register the exact
  primary/statistic before timing; do not select whichever width improves most.
- Aligned widths 8/64 and crossing widths 59/61/62/63, in both orientations,
  are mandatory guards. Include width 0 and small/partial counts in correctness.
- Correctness must preserve exact finite double bits, signed zero, full-width
  shifts, bounded ninth-byte reads, and reversed physical positioning. Keep all
  existing checks and run exhaustive widths/offsets plus sanitizers.
- Classification may cost more than the original aligned-offset short circuit;
  code duplication can worsen register pressure or instruction-cache behavior.
  Compiler unswitching may occur only in the synthetic kernel. These are real
  reasons to reject, even if one layout improves.
- Falsify on a qualified primary gain below 2%, a demonstrated guard regression
  over 1%, any semantic/memory regression, or failure to remove the targeted work
  in codegen. Inadequate precision means PARK, not acceptance or endless retries.
- Only a kernel winner advances to the original score-plus-length iterator and
  other iterator guards, with fresh seeds and independent confirmation/review.
  Kernel-only gains cannot clear EXP-004's unresolved original guard.

Recommendation: test this minimal leaf-invariant classification first, with an
explicit compiler-hoisting check. Do not grow iterator state or change the referee
to manufacture amortization before the small experiment establishes a benefit.
