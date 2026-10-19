# Focused SCAN guard referee preregistration

Authored by actual participant `/root/aws_arm`, native Codex agent; exact serving model,
token cost and monetary cost unknown. This is an additive referee for the existing AMD
scan population and Intel replication, not a new optimization population. Baseline source
8fab511e0e6ec7d4808546cd50064c6bf299e695. No candidate timing is authorized in this work.

The full matrix is 4096/100000 members × 16/321 bytes × shuffled/descending/all-equal
insertion × unfiltered/high17/folded01 hash distribution: 36 cells per seed. Shuffled
and descending use exact score `id + 0.25`; all-equal uses 0.25 and shuffled insertion.
Members start with an eight-byte big-endian ordinal, followed by an eight-byte nonce,
then deterministic binary bytes (including NUL). IDs guarantee uniqueness and lexical
order independently of hash selection. Original dictGenHashFunction and an explicitly
seeded original SipHash select high-byte17 or high-byte0/1; unfiltered uses nonce0.
No private state is fabricated. Frozen compact nonce files avoid repeated expensive
hash search in each benchmark child; each child reconstructs and rehashes every key
outside the timing window. Generator, seed, fixture bytes and SHA256 are preserved.

Baseline correctness/census first uses seed101 across all36 cells. Seeds102/103 follow
only if fixture intent is supported. Every callback checks independent exact bytes,
length and score bits, with complete member coverage; documented SCAN duplicates are
allowed. Ordered iteration independently verifies total order and completeness. A
second complete oracle after measured work detects mutation. Timing consumes ID, length
and score bits in a checksum and counts actual callbacks; both count and checksum must
match verified untimed traversals. Requested logical members and emitted callbacks are
reported separately. Original43 tests remain unchanged. Additive malformed-output fault
controls must fail. Sanitizer validation covers the same fixture matrix before comparison.

Performance tree and driver are separate translation units, no LTO. A separate diagnostic
binary includes the exact tree source and appends a read-only census wrapper; that binary
is NEVER timed. The same wrapper is used for every source. Census verifies stored physical
tags against original hashes and reports actual reversed leaves/members, external records,
leaf counts, tag histogram and index resize state. Descending must produce at least one
natural reversed leaf; otherwise this guard remains missing and work stops. A tiny reversed
fraction is reported as such, not broad reversal coverage. This matrix does not replace
separate tied-score construction/traversal, active-resize, or original standard guards.

Subsequent runner schedule, requiring root review of the final referee before timing:
for every cell, seeds101/102/103 repeated twice in six ABBA blocks. Baseline-only calibration
uses three one-full-traversal windows per seed/cell; choose one fixed pass count per cell
as ceil(0.200 / minimum observed seconds), bounded [1,100000]. The200ms target
leaves headroom above the100ms qualification floor; if the cap cannot reach the target,
that cell is unresolved. This target is fixed before any calibration or candidate data. Every measured window must
be >=100ms; any shorter cell is unresolved, with no post-result duration retry. Identical
passes apply to baseline/candidate. Two warmup complete traversals and untimed pre/post
oracle are fixed. Same-session baseline A/A precedes candidate comparison; all six paired
elapsed effects must lie within ±1% to qualify. No demonstrated >1% elapsed or tree-owned
memory regression is allowed. Preserve every process row and paired effect; unresolved
noise, truncated schedules, missing cells or failed correctness imply PARK. This is guard
qualification, not a new primary speed gate.

Root approved an explicit additive guard budget before any timing:300 seconds for baseline
calibration,900 seconds for all36-cell A/A,900 seconds for all36-cell B comparison,2100
seconds total. Six blocks and all36 cells remain fixed. Initial local native setup plus
untimed checks totaled15.63 seconds across36 cells, implying375 seconds for864 processes
before warmups and timed windows; a300-second entire phase would be structurally too short.
These budgets do not extend any prior population or standard-guard phase. Freeze
calibration passes before A/A; no A/A-dependent duration changes, retries or extensions.
Partial or noisy phases remain PARK. Intel owns serial timing after reviewed freeze; ARM
performs baseline correctness/census only. No performance claim from validation runtime.
