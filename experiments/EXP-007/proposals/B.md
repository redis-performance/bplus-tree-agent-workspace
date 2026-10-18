# Proposal B: width-class specialization without persistent iterator state

Independent Step 1 proposal, 19 October 2026. Author: delegated agent
`/root/proposal_b`. Backend/model and measured token/currency costs are unknown;
the session identifies Codex but supplies no reliable exact model identifier.
No other proposal was read. No build, timing, or production-source edit was made.
Inspected repository HEAD: `4fd3a3fdbce5acca18ee292642a3d80a79f50362`.

## Evidence and scope

The original decoder remains the control. The latest [focused results](../../EXP-004/decoder-microbench-2026-10-19/README.md)
show EXP-004 A slowing forward width 8 by 15.65%, width 60 by 4.72%, and width
64 by 10.39%, despite fewer static conditional branches. The control's aligned
offset branch can skip further crossing-predicate arithmetic. This motivates
removing unnecessary crossing work, not asserting that fewer branches cause a win.

The historical [baseline profile audit](../../EXP-004/baseline-profile-audit.json)
places 64 of 104 descriptive interrupted-PC samples in the decoder and 12 in
its crossing scaffold. The [iterator assembly](../../EXP-004/profiles/ITERATOR-ASSEMBLY.md)
contains that scaffold. These are evidence of reachable hot code, not unbiased
cost attribution or fresh counter measurements. The kernel's generated unrolling
and checksum chains differ from the scalar iterator's context.

## One falsifiable hypothesis

Specializing on the leaf's width class makes the compiler omit the ninth-byte
path for noncrossing layouts, improving decode throughput without additional
tree-owned memory. The exact target is `zbtScoreLeafScore` and a small internal
inline decode helper in `src/zset_btree.c`.

For width `b`, reachable bit offsets are `(physical_position * b) & 7`. A ninth
byte is possible only at widths 59, 61, 62, and 63. Widths at most 58 cannot
cross: the 58-bit case reaches at most offset 6. Width 60 reaches only 0 or 4;
width 64 only 0. The remaining zero-width path stays intact.

Preferred minimal implementation: dispatch by this width class to a helper
whose constant `may_cross` argument eliminates the crossing scaffold in the
simple path. Keep the original predicate in the crossing-capable path. Keep
base arithmetic, direction, masking, endian conversion, and zero-width behavior
unchanged. This is one width-specialization hypothesis; do not combine it with
mask changes, prefetch, vectorization, or persistent metadata.

The compiler may unswitch this dispatch out of a leaf loop when the helper
inlines. Inspect assembly to establish whether it actually does. In the existing
scalar iterator this is still a width decision per call: no claim of once-per-leaf
reuse is justified. The extra dispatch can lose, especially for already cheap
aligned inputs, and is a valid reason to select NONE.

## Bulk helper versus iterator cache

A true once-per-leaf implementation belongs naturally in a bulk leaf decoder:
choose the path, then run its loop over that leaf. This is the most direct way
to test the user's proposed amortization, but the existing frozen kernel calls
the scalar decoder. Introducing a bulk helper requires a separately committed
and requalified referee adapter. Control and candidate must both materialize
the same output array and checksum it identically; comparing a direct checksum
control with an output-writing candidate would confound the experiment. The
new benchmark establishes bulk decode performance only, not scalar iterator gain.

A persistent iterator cache could carry the width class, mask, base and pointers
between calls, but the current public iterator holds only `leaf` and `pos`.
Every start, seek and leaf transition would need initialization. A cached flag
still costs a dispatch per score, and a function pointer adds an indirect call.
A decoded-score cache additionally adds storage, speculative decode work for
short scans and mixed-output calls, and new lifetime/invalidity risks. This
proposal prefers the small source helper over that larger state change. If the
chair requires literal once-per-leaf dispatch, choose the bulk diagnostic first
and keep scalar integration as a separately qualified follow-up.

## Predictions and rejection conditions

- Noncrossing widths should improve if the compiler moves classification out
  of the loop; widths 60, 8 and 64 are explicit guards against the previous failure.
- Crossing widths 59/61/62/63 may be unchanged or slightly slower from dispatch.
  Any demonstrated guard regression above 1% fails the normal speed gate.
- Zero-width and short leaves may expose setup cost. Include counts 1, 7 and 96,
  both physical directions, and nonzero score shifts where valid.
- There should be no change in tree-owned allocation or iterator size. A bulk
  adapter's temporary output memory must be identical across variants and reported.
- Inspect code before interpreting timings: if no scaffold is removed or the
  supposedly hoisted classifier remains in the inner loop, the proposed mechanism
  is unsupported even if a noisy timing result happens to improve.

Freeze primary and guards before timing; my preferred discovery primary is width
60, forward, 96 scores, against the original control. Require at least 2% gain,
qualified A/A, serial ABBA with at least three blocks, no demonstrated >1% guard
regression, then independent seeds for confirmation. All other original iterator
guards remain binding for production adoption. Noise means PARK, not widening
the gate or repeating trials until a favorable result appears.

## Correctness and portability risks

Preserve unsigned shifts and the `bits == 64` masking exception: never shift a
64-bit value by 64. The crossing helper must retain its `shift != 0` protection.
Retain `memcpy` loads and endian handling, reversed physical position mapping,
exact finite score bits and signed zero. Exhaustively cover widths 0 through 64,
all reachable offsets, both directions, valid score shifts and final positions;
run native plus ASan/UBSan checks. The original allocation includes the decoder's
read allowance; a new bulk loop must not assume extra padding beyond that contract.

This proposal changes no source storage, member layout, rank metadata or public
iterator API. A local M1 result stays scoped to its compiler and machine. It
cannot close EXP-004's unresolved mixed-output guard by substituting a bulk win.
