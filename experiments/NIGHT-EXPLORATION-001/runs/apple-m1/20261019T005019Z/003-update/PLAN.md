# UPDATE-001 path decomposition — frozen baseline inventory

Status: referee validated in release smoke (15 cells) and ASan/UBSan smoke
(five 10K cells); no candidate or adoption comparison. Source tree is launch
commit 77d32df82cd5da02b95c6afb6193fcf83f67223f, SHA256
d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
The separate update referee is update-path-bench.c. Its commit is pending after
the earlier worktree index-lock denial; preserve its hash and exact file.

Cases: same score; position preserving 4i+1 ↔ 4i+2; nearby reorder of one
member across its paired anchor 4k+2 using 4k+1 ↔ 4k+3; distant move from
4i+1 to 4(n+i)+1 for the first quarter of members; original +N on every
member. Construction and query permutations use separate fixed seed streams.
Each process checks exact score bits for all members, uniqueness and order by
full iteration, length, and sampled or full public ranks after timing. Existing
upstream and signed-zero oracles cover additional semantic boundaries.

Inventory only: 100/1K/10K/100K/1M × five named cases × seeds 1/2/3,
100,000 operations per process, 75 serial processes, no candidate. Keep each
CSV and stderr. These are batch averages, not latency percentiles or qualified
speed claims. Instrumented source is a separate diagnostic: count successful
in-place updates versus remove/reinsert at the same cells with 20,000
operations, seed 1. Instrumented durations must not enter timing summaries.
Profile 100K and 1M preserve/distant/+N after inventory and inspect the
release update path assembly. Only then choose a candidate hypothesis or NONE.

Before any candidate, qualify this new referee's position-preserving primary
cells at 100K and 1M: three baseline calibration observations per cell with
100,000 pilot operations, seed 1; freeze counts as
ceil(50,000,000 / fastest positive ns/op), capped at 100 million. Then six
same-binary ABBA blocks, discovery seeds 1/2/3 repeated twice, sizes rotated
by block. Every window must last at least 10 ms and every A/A block effect
must stay within ±1% to qualify. Retain all raw rows. This A/A cannot repair
the separate rank precision failure.

No changed referee may enter a candidate comparison until a separate commit
and fresh baseline A/A requalification. This round's inventory is descriptive
and cannot serve as a candidate baseline. Frequency, core residency and
hardware counters remain unknown.
