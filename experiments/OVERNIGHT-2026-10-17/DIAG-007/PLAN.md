# DIAG-007 — fine contiguous-window phase diagnostic

Preregistered 2026-10-17 before build/measurement. The prior reuse diagnostic tested
fresh versus reused fixtures, with checks/output between long windows. This diagnostic
asks a distinct question: does a reproducible early-to-late phase shift remain after
fixed warmup, across fine contiguous windows without intervening validation or output?

Hypothesis: early lookup windows are >=3% slower than late windows in at least two
of four cells, with that direction in at least five of six processes in each such cell.
A cell supports this iff median(first-four mean wall ns/op / last-four mean wall ns/op)
>=1.03 and at least five ratios >1. No alternate direction or window boundaries chosen
post hoc. This diagnostic is not A/A qualification, a source comparison, or a claim
about frequency, caches, topology or residency. Failure means not supported; unavailable
controls mean inconclusive. Source NONE / lookup qualification PARK remain unchanged.

Instrument: a separate diagnostic main over frozen HARNESS-002 helpers/support. One
single-thread tree/process; independent construction/hash seed1301, query seed1409;
100000 members, 10 full hit warmup passes, 16 consecutive windows of 500000 queries
(5 complete query passes/window). Hit/miss x16/320-byte binary members. Store all
observations in preallocated/touched records; compute expected checksums before warmup;
validate counts/scores/memory after all windows, and print only afterward. Capture each
window's wall/thread durations, opaque boundary CPU IDs, reported QoS/relative priority;
effective QoS remains unknown. Outer wall bracket includes all observations/gaps.
No clock estimate, QoS intervention, pinning, additional settling or background sampler.

Fixed schedule: six blocks, four cells/block, rotating canonical order
(hit16,miss16,hit320,miss320) by (block-1)%4. 24 measured processes,384 windows total.
No normal-sized excluded warmup process; small n997/ops1999/4 windows all four cells,
two query seeds and both release/ASan+UBSan builds are prospective smoke exclusions.
All measured windows must exceed10ms and outer-wall minus sum(window-wall) must be
nonnegative and <=1% of outer-wall in every process for the phase criterion to be
interpretable. This is a gap-accounting bound, not proof of instrumentation neutrality.
Every checksum, total count, fingerprint and tree memory must match across like cells.
Each child <=120s; campaign budget240s. Stop on correctness failure/timeout and retain
incomplete evidence. No outlier removal, optional stopping or adaptive counts/thresholds.
No concurrent local build/test/profile/agent computation during measured children.

Report all ratios,16-position means and ranges, thread/wall observations and CPU boundary
changes. Within-process spread, per-CPU groups, first/last association and between-process
means are descriptive only: windows are clustered, not384 independent samples. Never
filter out mismatched IDs, low CPU share or slow rows. Boundary IDs do not identify core
type, exclude intervening migration or support frequency normalization. No speed gate relaxed.

Machine: user-identified Apple M1 ARM64, prior inventory4P+4E/16GiB/noSMT; one thread,
macOS26.3, Apple Clang17; frequency/turbo/effective QoS/residency unknown, no sysctl retry.
C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer; libc allocator, assertions/hash intact.
Exact source base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit uncommitted
HARNESS-002/diagnostic patch; hashes frozen before measurement. Root source/referee intact.

CPU MCP ask and methods/code05/14 consulted. Retrieved Intel/other unrelated passages
are not support. Method05 motivates retaining repeated observations/checksums; method14
uses thread CPU time and boundary IDs and says "nothing pinned". No M4 values copied.
Installed SDK pthread headers re-inspected: CPU number may change before call returns;
QoS getter cannot see overrides. Full retrievals stay ignored scratch; source URLs and
hashes recorded. Reviewer agent startup failed before running; sequential coordinator
review only, no independent participant/model/cost invented. Supervisor tracks CLI costs.
