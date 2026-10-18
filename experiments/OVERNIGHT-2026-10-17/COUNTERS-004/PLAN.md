# COUNTERS-004 — real monotonic signed-zero layouts

Before timing, enumerate physical layout of HARNESS-005 integer/alternating-zero fixtures.
48cells/build: n4096/100000,bytes16/320,seeds31031/31043,threeconstructionorders,
twoencodings. Bothrelease/debug and ASan/UBSan. Unmodified tree in a separate census
translation unit; independent bit reader + exact model bits + all output masks/directions.
Within-process owned bytes unchanged; cross-build compare all structural fields except
owned usable bytes (allocator differs). No timing or frequency claim.

Falsifiable coverage prediction: every descending integer and alternating-zero fixture
contains at least one reversed physical leaf; alternating-zero fixtures contain both
zero signs and a nonzero packed width. Preserve counterexamples, no fixture replacement.
All96children<=120s, serial; no benchmark overlap. Count as one structural diagnostic.
