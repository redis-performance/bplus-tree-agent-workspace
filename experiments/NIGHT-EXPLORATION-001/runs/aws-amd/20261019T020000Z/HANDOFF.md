# AWS AMD native handoff

BUILDER-WRITE-001 REJECT/NONE: 144 processes, all 36 effects slower. A +1.039%/+1.362%, B +1.250%/+1.745%, C +5.777%/+2.766% median elapsed at 100K/1M; no guards or confirmation. All patches/raw rows retained. AMD totals: 2 populations, 0 accepted, 2 rejected, 0 parked. Baseline source unchanged.

Decisions: 002-lowerbound and 004-builder-write implementation-selection.md. Packed-move census in 003-packed-move; scoped FIFO profiler and failures in 002-lowerbound. Root baseline preserved. Current next investigation: constant 64-bit full chunks versus partial-tail packed shifts; no proposal or candidate yet. Intel SSE2 scanners are prior rejections, do not duplicate as new work.
