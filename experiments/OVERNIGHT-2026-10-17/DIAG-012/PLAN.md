# DIAG-012 — controlled iterator address placement

Preregistered before any layout timing. Baseline control ONLY; not an implementation
population or source acceptance comparison. The prior caller experiment changed
register allocation and surrounding code. Here freeze HARNESS-004 unchanged C files,
compile the tree once to arm64 assembly, and insert a fixed total 64 bytes of unreachable
padding split before/after zbtreeIteratorNext. Offsets 0/16/32/48 move only that function
while preserving later symbol addresses and caller instruction semantics. No padding
executes. Validate linked symbol addresses and relocation-normalized instructions of
iterator and caller before timing. If that isolation fails, record and stop timing.
Do not infer a specific instruction-cache or predictor mechanism from a placement effect.

Validation: every layout runs 128 original iterator fixtures (n129; binary lengths16/320;
integer/fraction/wide/zero;forward/reverse;all8masks), plus original upstream tests.
The C is unchanged and already sanitizer validated. Additionally run each layout under
ASan/UBSan from separately emitted sanitized assembly over the same128fixtures.
Freeze hashes and exact commands. Read actual local assembly/APIs, do not copy M4 data.

Fixed timing matrix: seeds19103/19139; n100000; integer scores;16-byte members;forward;
20m emitted items;3warmup traversals. Six serial ABBA blocks for each pair of placement0
versus16/32/48 and masks4/6/7 =432rows. Add placement0/0 A/A for mask6 at both seeds,
six blocks=48rows. Total480rows. Rotate the ten cells per block, seeds outermost;
ABBA uses identical fixture/memory/checksum and unchanged source. Prospective single
1m-item warmup per binary retained separately. Children<=120s,total timing budget600s.
No builds/tests/agents during measurement; all rows/failures retained, no optional
stopping or outlier exclusions. Wall time primary; thread time/IDs/QoS descriptive.

Primary falsifiable criterion: both mask6 placement0/0 controls have 95% t(df5) block
ratio intervals entirely in[-1,+1]%, and placement16 versus0 has same-sign mean effect
of magnitude>=2%, with its interval wholly above+1% or below-1%, on BOTH seeds.
Only that preselected offset establishes the primary hypothesis;32/48 and4/7 are
secondary descriptive coverage. Failed A/A means primary PARK, even if large exploratory
effects occur. This does not qualify HARNESS-004 source comparisons, clear EXP-004
mask6, or justify padding as an optimization. EXP-004 remains PARK.

M1/arm64/macOS26.3,AppleClang17,C11,-O3,-g,-fno-omit-frame-pointer,libc,one unpinned thread;
frequency/effective QoS/within-window migration unknown. Uncommitted snapshots over
base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c. Independent reviewer startup failed;
sequential coordinator audit only, exact backend/model/cost unknown. MCP ask returned
irrelevant passages; not cited as support. Methods/code05/14 consulted for observability,
with no transfer of machine numbers. Main source/referee and prior evidence unchanged.
