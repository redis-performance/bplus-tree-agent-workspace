# Cross-author semantic review of B/C and the shared referee

Reviewer: agent `/root/proposal_a`, 2026-10-19. I authored variant A, not B/C.
This is cross-author static review, not fully independent performance confirmation.
Exact backend/model and token/currency cost are unavailable. No builds, timing,
or source changes were performed for this review.

Finding: no semantic defect identified in B or C under the documented valid-leaf,
valid-subrange, disjoint-output contract. The shared oracle and output-materializing
control are appropriate for this private bulk experiment. This conclusion does not
replace the native/sanitizer runs or authorize a production/API acceptance.

Reviewed SHA256 values:

| File | SHA256 |
|---|---|
| `variants/B/decoder.inc` | `6da7d81bfd0dfa9828922cd17508403b7ea9a86ea3ac64159dedacf6a02ab4ad` |
| `variants/C/decoder.inc` | `fc542ed01e638a3c871624e7cf257dcce5fe9ebe27e297b159533312b2a8e345` |
| `referee/kernel.c` | `192f6ed26ba49bb1f3e67174d5e7e24482acb8e84b985eef56b6a1c241e2a829` |
| `referee/control.inc` | `5c39ab90b9e87238ffd9b424c7e7371aaf897a93526d3af3e3166b49deb82543` |

## Range, bit, and bounds audit

Both candidates return immediately for count zero. For a valid range, `start + i`
is bounded by leaf count minus one, hence neither logical addition nor reversed
physical subtraction underflows/overflows. Reversed indexing maps logical forward
subranges to descending physical positions using the original rule; neither
candidate changes logical output order.

For width w, reachable offsets are multiples of gcd(w,8), modulo eight. Widths
at most 57 fit even at offset seven; width 58 reaches at most six; width 60 at
most four; width 64 only zero. Thus the crossing class is exactly 59/61/62/63.
B's aligned path and remaining non-crossing path cover every other valid width.
C's `bits > 58 && (bits & 3) != 0` is equivalent over the valid interval 0..64.
Neither classification is promised for corrupted leaf widths above 64.

B special-cases width zero before reading packed data and width 64 before creating
a shifted mask. Its crossing predicate preserves the scalar `shift != 0` condition,
so the ninth-byte assembly shift is 57..63, never 64. C retains the original scalar
fallback on crossing widths and the original guarded mask for other widths. All
score shifts remain within the valid leaf's 0..63 contract; unsigned arithmetic
preserves defined wrapping behavior. No floating-point arithmetic or comparison
is introduced during reconstruction: both preserve ordered conversion, finite
score bit patterns, and signed-zero semantics by inspection.

Every nonzero-width read is the scalar decoder's same eight-byte load at the same
address, and any ninth-byte read occurs only where the scalar permits it. The
original `zbtScoreLeafScoreBytes` supplies eight spare bytes and alignment padding,
so partial/tail ranges do not introduce an overread relative to the original
allocation contract. `memcpy` preserves unaligned-load legality and `intrev64ifbe`
preserves byte order. Actual execution on another architecture is still untested.
Output writes are exactly `out[0..count)`, and no leaf data is written.

## Referee adequacy and limits

Independent bit-at-a-time packing and independently calculated expected IEEE bits
avoid using candidate code to generate expected results. Exact per-element checks
are stronger than the timed additive checksum and would catch permutations or
compensating errors that the checksum alone misses. Every tested partial range
has one leading canary and all remaining trailing slots checked. Full 96-element
output fits in the 98-element validation array and 96-element timed array.

The identical control and all candidates write a `double[96]` before the identical
checksum consumer. Passing the array address through a compiler barrier with a
memory clobber makes these stores observable to the compiler before consumption.
This is an adequate GCC/Clang materialization guard; inspect generated assembly to
confirm stores and subsequent reads survive in each measured binary. It is not
a CPU fence, and that is not required for this single-threaded scratch buffer.
The outer round barrier prevents repeat-invariant fixture load hoisting. Comparisons
remain bulk materialization throughput, not the old scalar kernel or iterator API.

The reviewed self-test covers every width, both orientations, seven leaf counts,
and low/high score-shift choices. The shared range checks use starts 0, midpoint,
and end, each with counts 0, 1 when possible, and the remaining tail. These are
useful boundary checks but are not every legal subrange or every score shift.

Coverage improvements before claiming exhaustive semantics:

- Add explicit exact-bit fixtures for positive/negative zero and subnormal/normal
  boundaries. Random finite values do not establish that these were exercised.
- A separately recorded correctness-only exhaustive subrange sweep is cheap for
  leaves capped at 96 and would cover arbitrary prefix/interior lengths.
- Preserve all native/sanitizer failures and do not weaken the oracle. Tree-owned
  allocation equality follows from unchanged layout/no helper allocation, but
  neither code inspection nor this synthetic test establishes public iterator
  integration, invalidation, mutation, or full-tree performance.

Minor documentation issue: the reviewed `referee/kernel.c` opening comment still
says only EXP-004's source patch differs. This is stale for EXP-007 and should be
corrected with provenance retained; it does not change execution semantics.

I reported the coverage gaps and stale comment to the chair immediately. No timing
result or candidate preference was used to formulate this review.
