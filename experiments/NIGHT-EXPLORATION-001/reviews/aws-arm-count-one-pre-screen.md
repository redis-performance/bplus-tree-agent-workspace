# Independent ARM count-one pre-screen review

Root reviewed the three patches and frozen source/referee independently of the ARM
implementer. Exact serving model and measured token/USD cost are unknown.
Reviewed worker revision: `0ce43c0e`. No source is adopted by this review.

| Variant | Patch SHA256 |
|---|---|
| A | `85f68745655b2675bcfc0611977ed733a0288eeaa4d6ff80c4bbf99495e86548` |
| B | `1951336e9c1006d7cff9fcc739590e5fd639fe0ba9a1afb19bc37613eb0bb52b` |
| C | `18eb57f8137bc72520c4ce7eb7ceaf5e3d0949864d2deb09e9bdef1fd8185179` |

All frozen file hashes match root's copies, including the unchanged extraction,
EXP-007 B bulk helper, EXP-008 policy/kernel, scalar control, shared driver,
allocator, hash implementation and decoder tests.

No semantic or bounds blocker was found. A branches in the policy; B explicitly
returns for zero count before selecting one scalar result; C branches inside the
private bulk helper after its existing zero-count return. Each calls unchanged
zbtScoreLeafScore for exactly one valid logical position. All counts above one
retain the frozen bulk decoder. Existing preconditions require a valid subrange
and disjoint output storage; these patches do not introduce wider accesses,
new shifts, persistent state or an aliasing assumption.

The frozen referee independently packs bits and checks exact output bits, finite
values, both zero encodings, reversed leaves, empty/partial ranges and sentinel
output bounds. Its common materialization and round barriers preserve the output
contract. This review inspected those checks; it did not rerun correctness tests.

Measurement restrictions remain decisive. Both primary controls fail strict A/A:
bulk −4.74%..+5.85%, root −0.35%..+1.32%, with approximately 12–14ms minimum
windows and a fixed driver cap. Only the preregistered bounded exploratory screen
is supported. A nominal 2% lead is insufficient here. Large consistent effects
could motivate a separately declared confirmation, but do not resolve qualification.
The initial 29-cell screen is not the full guard matrix.

The bulk control is an unadopted experimental helper, while the separate root
control applies the unchanged scalar decoder to the same outputs. Relative-bulk
improvement is conditional on that helper and is not a public-tree gain. Count-one
fixtures are seed-invariant in their decoded deltas (the generator sets position
zero's delta to zero); repeated seeds are repeated measurements, not independent
input diversity. The call/inlining mechanism must be checked in generated code.
