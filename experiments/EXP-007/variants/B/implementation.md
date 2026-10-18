# Implementation B: explicit aligned and noncrossing leaf loops

Author: independent delegated agent `/root/proposal_b`. Exact backend/model and
measured token/currency cost are unknown. No A/C implementation was read. No
build or timing was run by this implementer. The chair owns validation and
source snapshot/patch provenance.

The chosen hypothesis is once-per-invocation leaf-width specialization, tested
as a private bulk helper. `decoder.inc` adds only `zbtScoreLeafDecodeRange` to
an isolated original source copy. The unchanged referee calls that helper and
materializes/checksums the same double array for every implementation, including
the scalar-loop control. This does not change or optimize the scalar iterator.

B uses four geometry paths: zero width, byte-aligned widths, noncrossing
unaligned widths, and crossing-capable widths. Selection occurs before each
loop. The byte-aligned path uses `physical * (bits / 8)` and has no within-byte
shift or ninth-byte check. The other noncrossing path covers widths at most 58
and width 60. The remaining valid widths are 59, 61, 62 and 63; that path retains
the original scalar crossing predicate. Width, mask, base, score shift,
orientation and leaf count are captured once. This implementation does not
introduce direction-specific loops, new encoding, prefetching, intrinsics,
allocator changes or cached iterator metadata.

Semantics remain the original decoder's unsigned arithmetic and ordered-double
bit conversion. Logical positions increase from `start`; reversed leaves map
each to `leaf_count - 1 - logical`. A zero count returns before any leaf or
output access. Width zero repeats the decoded base without touching score data.
The mask handles width 64 explicitly so no C shift-by-64 occurs. The crossing
path retains `shift != 0`; load/endian handling uses the original `memcpy` and
`intrev64ifbe` idiom. Reading a full word at the last score relies on the same
documented leaf allocation padding as the control. Output must be disjoint,
and `start/count` must describe a valid forward logical subrange.

Principal risks are code-size growth and dispatch cost for short ranges, plus
compiler loop versioning that could change gains across contexts. Removing
the branch from source does not establish dynamic instruction savings. Inspect
generated loops, validate native and ASan/UBSan exact bits across widths,
directions, shifts and subranges, and retain aligned and crossing guards. No
performance, portability or production-readiness conclusion is claimed here.
