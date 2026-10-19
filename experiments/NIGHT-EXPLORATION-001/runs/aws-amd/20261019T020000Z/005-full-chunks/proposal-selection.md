# FULL-CHUNKS-001 proposal selection

Three sequential passes by the same native agent; these are not independent agents. Root reviewed the direction independently. Exact backend/model and token/USD costs unavailable.

1. Split full 64-bit packed-move chunks from the partial tail. Profile support: fresh timed-region 1M-update captures at 100K/1M show packed reads/writes under insertion and deletion; at 1M insertion write/read samples are 2.44%/0.63%, deletion writes 3.04%. Census shows 76.14%/76.13% of update chunks are full; insert/delete ~80%. Baseline assembly retains dynamic width min/masks on all iterations. Expected modest instruction reduction, risk code growth and no elapsed benefit. No layout or allocator change.
2. Byte-aligned memmove. Earlier matched census found only 23.24%/1.79% of moved bits eligible at short-pass 100K/1M updates, making generality/headroom weaker. Overlap library dispatch also adds cost. Defer.
3. Eliminate duplicate score-encoding selection during leaf rebuild. Scoped builder evidence shows some duplicated computation but construction only 4.30% at full-pass 1M. Larger signed-zero, finite-score and assertion semantic proof; prior builder metadata specialization just lost. Defer.

Chair: select proposal 1 only, one falsifiable hypothesis: constant-width full-chunk loops reduce elapsed update time at both 100K and 1M by at least 2% in every paired block. Preserve generic helpers, overlap direction, tail and final write/zero semantics. No helper SIMD, byte-aligned path, metadata caching, or encoding change.
