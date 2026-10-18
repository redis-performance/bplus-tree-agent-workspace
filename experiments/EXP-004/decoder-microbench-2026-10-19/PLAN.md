# EXP-004 focused decoder diagnostic — preregistered plan

User authorised building and locally running the focused Lemire-style benchmark.
This is a separate referee/diagnostic, not a new optimisation population and not a
replacement for EXP-004's original score-plus-length iterator guard. The overnight
supervisor remains stopped. Source adoption and EXP-004 A/PARK are unchanged.

Compare exact control and A source hashes from EXP-004/freeze.json, using the identical
new decoder referee. Commit the harness before running the timing matrix. Record its
commit and build/source/binary hashes. Run release and ASan/UBSan functional checks
first and inspect generated `decoder_batch` assembly for retained loads and loops.

Fixed default matrix: widths 0,8,31,57,59,60,61,62,63,64 × two physical directions;
96 scores/leaf × eight leaves, score shift zero, 64 rounds = 49,152 decodes/batch.
Six ABBA blocks, seeds 81031/81041 alternating, 129 samples/process, 16 warmup batches.
First same-binary A/A, then baseline/A. Total 960 serial processes and 123,840 measured
batches. Rotate cell order per block. No overlapping builds/profiles/tests. Each child
has a 30-second limit; the campaign budget is 300 seconds. Partial failures are retained.

Report per-process min/median/p90/max, paired block effects for both minimum and median,
their full ranges, and histograms. Preserve every row, including migrations/outliers.
No pooling inner samples into fictitious independent trials, no significance claim
from a minimum, no outlier exclusion, and no extending sample counts after results.
Compare apparent candidate changes with same-cell A/A variability; if they overlap
substantially, label the result inconclusive. No accepted source decision follows.

Falsifiable question: does removing the extra cross-word condition improve this decoder
loop across its reachable width/offset patterns, or is the effect geometry-dependent?
The observed iterator improvements do not pre-establish either answer. Width zero and
byte-aligned/full-width cases are controls; widths 59,61,62,63 exercise ninth-byte reads.
This experiment does not identify the cause of the original iterator-mode regression.

Local target: Apple M1/macOS/Clang release O3, one unpinned thread, libc allocator;
frequency and effective QoS unknown. Use monotonic elapsed nanoseconds, not estimated
cycles. Hardware counters unavailable on this local path. Linux counter support is
optional and its successful hardware path remains unvalidated here. No Redis server.
