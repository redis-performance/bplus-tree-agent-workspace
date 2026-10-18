# EXP-008 implementation C — cutoff 16

Author: C implementation pass. Actual backend/model and token/currency cost:
unknown.

## Chosen hypothesis

This isolated variant implements the chair's one-time count crossover using a
cutoff of 16. For a nonempty logical range of at most 16 scores, it writes each
result with the original `zbtScoreLeafScore` decoder. For a range longer than
16, it calls the frozen EXP-007 B `zbtScoreLeafDecodeRange` helper once. A zero
count returns without reading the leaf or writing output. The helper is in
[`policy.inc`](policy.inc).

The population contract supplies the unchanged EXP-007 B helper before this
file is included. This variant adds only `zbtScoreLeafDecodePolicy`; it does not
edit that helper, the tree source, referee, or build configuration. It adds no
width or orientation branch and no persistent leaf or iterator metadata.

## Expected behavior

The scalar branch avoids entering B's specialized bulk helper for counts 1, 2,
4, 7, 8, and 16. Counts 32 and 96 use B. At the decision boundary, count 16
must use scalar and count 17 must use B. The width 59/61/62/63 crossing cases
remain ordinary count-selected cases; this implementation makes no geometry
exception. The chair's fixed comparison matrix, held-out confirmation, and
acceptance guards decide whether this cutoff is useful. No performance result
is claimed here.

## Risks and review points

- The small-range path calls the original scalar decoder once per score. Its
  machine code depends on natural compiler inlining; this source does not force
  `inline` or `noinline`. Inspect generated code to confirm whether scalar
  decoding is inlined and whether the count branch is evaluated once per range.
- The long-range path enters B's outlined helper. The policy call and B call
  overhead may still erase the gain for ranges just above 16; count 17 and the
  preregistered 16/32/96 cells are important threshold checks.
- `start + i` must remain within the leaf's logical score range, and output must
  be disjoint and large enough for `count`, matching the frozen bulk-helper
  contract. The wrapper does not add bounds checking.
- Correctness must cover zero and partial ranges, reversed leaves, all packed
  widths, maximal legal score shifts, exact finite score bits, and output
  canaries in both release and sanitizer builds. The existing helper's padding
  and packed-load assumptions remain unchanged.
- This helper accepts a range length. It does not change the public scalar
  iterator, which has no batch count, and cannot establish an iterator speedup.

No builds, tests, profiles, or timings were run in this implementation pass.
