# Multi-member batch at natural growth wrap — new preregistration

Responds to retained singleton migration fault survival; does not rerun or alter that
result. New seeds61543/61559, batch sizes2 and12, four fixtures per source/build cell.
Control/EXP-004 A/B/C native-O3/debug and-O1ASan/UBSan, serial,120s children,900s total.
Same frozen source/referee/allocator; source baseline preserved. Full sorted-vector
models at EVERY low/high phase of32770shrink/grow cycles per fixture. Observe natural
65535→1 growth wrap,65540resizes per fixture, no private mutations or counter injection.

At wrap, append members29..29+batch_count-1 with exact finite half-integer scores and
319-byte binary keys. Batch2 must form one new leaf; batch12 must form at least two
new leaves (conservative builder budget), otherwise missing coverage FAILS. Record old
live IDs before append; enumerate all newly live IDs after and require all new leaves
have migration tag1 and all appended members have actual hash/ID references in the
wrapped destination, or the current table if public insertion completed that resize.
Verify every appended member through the independent public model; finish resize and
remove extra maxima, then continue original29/8cycle. Require a still-active destination
for batch2; allow completed migration for batch12. No change to existing assertions.

Both earlier fault controls are repeated against new multi-member fixture. The previously
surviving batch-marked-migrated fault must now fail: copying the entire leaf is necessary
when AppendBatchFlush indexes only its first member. Both controls must compile and fail
explicit correctness/assertion/sanitizer checks, not timeout. Preserve all outcomes.
This is correctness coverage; no timings, optimization acceptance or independent-agent
claim. Counts remain one BOUNDARY-021 suite; newly detected distinct faults counted once.
