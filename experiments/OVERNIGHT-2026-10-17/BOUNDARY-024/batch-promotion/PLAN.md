# Batch lookup spanning natural width promotion

Preregistered new extension at05:00UTC round17, not a timing trial. Use final external
score oracle with all current-value/ownership/live-SCAN checks intact. Replace the
16lookup migration drain with one16lane zbtreeScores call. Require at least one call
that enters with narrow-current/wide-destination resize and returns wide-current with
no resize. Observe states around the public call; this proves promotion inside it.

Each16lane batch repeats ID0 (current exact signed zero), includes IDs1/2 and other
present members plus absent IDs above current n; exact hit mask and score bits for
hits must match independent scores[]. Use20output slots with2leading guards and
canaries after requested count. Miss-lane outputs are unspecified and not asserted.
In the first2mutation gaps run counts0..16, including NULL arrays for count0; this
checks negative/positive zero while migration is active without exhausting it. Free
all temporary keys; private state is read-only. SCAN must remain nonmutating, but
batch lookup is allowed to progress rehash/accounting. No stale iterator reuse.

Discovery seed75503: control/EXP-004A/B/C, nativeO3/debug and O1ASan/UBSan/debug,
8fixedcells. Fresh confirmation seed75521: same8cells but omit REDIS_DEBUG, preserving
all CHECK and unconditional assertions. Freeze distinct snapshots before each matrix;
original test and referee stay unchanged. Serial120schildren, matrixbudget360s each,
no new child after05:09UTC. Stop and retain failures without skipping/repeating cells.

One targeted sanitizer fault after discovery: cache the current table descriptor at
batch entry, then reuse that cached table once normal lookup has completed resize.
This models a stale-table fast-path assumption across promotion. Successful build
plus actual oracle/assertion/sanitizer failure is required; survivor/timeout retained.
No new suite or optimization count. Any detected new fault type is counted separately.
All raw commands, UTC windows, hashes, stdout/stderr, patches retained. SourceNONE/PARK
unchanged. This executes part of the earlier next-fixture preparation; do not claim
exhaustive masks or timing improvement.
