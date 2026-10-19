# Pre-execution allocator parity correction

Intel identified that c370e444f grouped tiny native and sanitizer observations together although compat uses malloc_usable_size. The superseding freeze groups both semantic controls and census observations by explicit binary allocator/build mode: native versus ASan/UBSan. Exact within-mode original/disabled and control/A parity still includes owned bytes. No source, seed, count, order, threshold or1200s budget changed; prior freeze remains unexecuted.

A second Intel finding adds --no-scale to the42 perf stat commands before any profile data. This aligns execution with the original no-scaled-estimate requirement; events and fixture work are unchanged. Runtime is explicitly the rounded perf-reported100.00% criterion, not a stronger unobserved nanosecond equality.
