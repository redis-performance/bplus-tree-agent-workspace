# Independent review of ARM exact-mask withdrawal

Root reviewed the retained ARM annotation independently of the implementer on
19 October 2026. Exact backend and token/USD cost are unknown.

The 100K annotation SHA256 is `2a0835b29b2f591d3a7b45802075c4f69b919ba4c1adb5cb9a7bcd130e5a1c7e`.
At 0x3954 the tag word is loaded; 0x3960 shifts the selected byte and 0x3964
compares it with the requested tag. This comparison has 0.00% of local samples,
and its following branch 0.19%. The 19.49% comparison at 0x39bc follows the leaf
ID load at 0x39b8 and feeds the assertion path. It is not the tag comparison.
The corrected report therefore accurately withdraws its original attribution.

Zero samples do not prove zero cost. Likewise, samples following an index load
cannot distinguish arithmetic cost from memory latency and sampling skid. These
observations support **NONE before timing**, not a performance conclusion about
an unmeasured mask patch. The three abandoned patches and failed preparation
attempts remain available; this is not a completed measured population.

[Worker erratum](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/f41ae0ba/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/002-lookup/PROFILE-ERRATUM.md).

No new timing, correctness run or independent PMU capture was performed by this
review. The scope is source/assembly attribution and decision integrity.
