# EXP-002 fixed implementation comparison

Frozen base HARNESS-003 commit a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit
uncommitted referee; target pinned a7ecd959374d66847c095250bf2d373edf7316c5. Four isolated
snapshots control,A,B,C under scratch/exp-002, identical referee/support/compiler/hash/
allocator. Only iterator function/local dispatch helpers may differ. No main edits.

A inline early fast path; B noinline specialized and generic helpers with public dispatch;
C inline specialized path and noinline generic helper. Same selected hypothesis: remove
generic optional-output handling overhead from forward score-only iteration. All reuse
unchanged score decoder and generic fallback. Distinct implementations, sequential passes,
not independent agents. Preserve all patches, failures, source/binary hashes and outputs.

Build baseline/all variants release -O3 and sanitizer -O1/address,undefined with original
assertions. Run43 original tests plus existing lexical output-mask and score-boundary
oracles in both builds. Any failure ineligible; no weakened check. Benchmark release only.

Fixed primary iterate16 and guard iterate320,100000 members,50000000 operations each,
seed4109/query4201 matching qualified AA-005,independent query order,10warmups. Three
serial ABBA blocks per variant/cell; A label baseline,B label candidate. Rotate variants
ABC/BCA/CAB by block, alternate cells by block.72 rows total. Same-session baseline rows
for every variant. No excluded binary warmup. Each child<=120s,matrix<=300s; no overlap
with builds/tests/profiles/agents. Preserve every row/failure, no optional stopping.

Wall ns/actual visit primary. Per candidate/cell three block effects100*(B/A-1),95%
descriptive t(df2,t4.302652729911275). Screening requires whole primary interval<=-2%,
guard upper interval<=+1%, exact equal owned bytes/count/checksum/fingerprints,24 rows
per candidate,>=10ms each. No passing candidate =>NONE. Passing candidates ranked by
primary mean, overlapping intervals prefer smaller patch. Screening is not acceptance:
reverse/output-mode guards, fresh-seed confirmation, matched candidate profiles,
independent review and morning commit/source review remain mandatory, otherwise PARK.

Baseline AA-005 iteration both cells qualify; PROFILE-003 descriptive symbols and
baseline disassembly saved. Frequency/effective QoS/core residency unknown. One local
M1 thread,Clang17/C11/debug symbols/-fno-omit-frame-pointer/libc. No timing cross-machine.
