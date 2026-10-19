# Independent AMD full-chunk pre-screen review

Root reviewed the three patches independently of the implementer against source
8fab511e. Exact model and token/USD cost are unknown. Review is static; native and
sanitizer validation remain the worker's separate gate before timing.

| Variant | Patch SHA256 |
|---|---|
| A | `061fd7b68d5f0a90798452226d6004d8b9c0d7fa65e7b2ea0aba366ed0082528` |
| B | `b3aa2c05c34fdbf3436aae2920475f30bbebca0f60dd0cb0a3dab01335df2ff3` |
| C | `f0fceda724d8bafaec5e3fb34bbe3d0458e157c0c6c0dc1e63e3bf1bfae33fe2` |

No bounds, overlap-direction or semantic blocker found. Let R be the original
number of moved bits, q=floor(R/64) and r=R mod64. Insertion copies full fields at
insert_at+R−64, insert_at+R−128, …, insert_at+r, then the r-bit prefix. This exactly
matches the original backward sequence; it does not accidentally copy the prefix
first. A/C decrement the remaining count, while B indexes the same q positions.
Deletion copies from low to high at destination+64j for j=0..q−1, then the r-bit
tail. The final deleted field is still cleared using the unchanged generic writer.

All full copies still use the existing read/write helpers at constant width64.
C only wraps those calls; it adds no wider load or store. The ninth-byte crossing
path and shift-by64 protections therefore remain unchanged. Every partial width
is1..63, making A/C's size_t-to-unsigned narrowing safe. Zero-width early returns
are preserved. Valid leaves bound R by96*64 bits, so B's indexed arithmetic cannot
overflow. A/C's deletion loop maintains moved<=remaining, preventing subtraction
underflow. No allocation, leaf count, ownership, hashing or layout changes occur.

The frozen packed-move oracle is directly relevant: it compares all824 bytes
against an independent bit-at-a-time, out-of-place reference across widths0..64,
all insertion/deletion positions for varied counts, dirty surrounding bytes and
multiple seeds. Decoder and public score-boundary tests supplement it. Static
inspection finds no widening of access beyond the original helpers; the oracle's
large buffer alone would not establish exact short-allocation read bounds.

A and C may produce identical generated code. If so, record that equivalence;
their separate measurements are not independent mechanism confirmation. Fresh
A/A reportedly qualifies both fixed one-million-update primaries. The paired
screen must still meet both gates; full guards, independent fresh confirmation
and mechanism profiles remain necessary for any later acceptance.
