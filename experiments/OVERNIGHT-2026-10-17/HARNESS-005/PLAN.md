# HARNESS-005 — monotonic construction and alternating zero fixtures

Separate referee revision, before qualification or any source comparison. Frozen parent
HARNESS-004, baseline source unchanged. Add construction shuffled/ascending/descending
and alternating-zero encoding. New zero keys use big-endian eight-byte IDs so lexical
order equals model order even beyond 255; existing fixture keys remain unchanged.
The zero score model uses exact +/-0 bits alternating by member ID, numeric ties ordered
lexically. Fold score bits with u^(u>>32) before unsigned summation to keep negative-zero
contributions observable for even-sized traversals. This changes timed checksum cost,
so all new timing uses new qualification; older timings are never pooled.

Existing full byte/order/exact score-bit/state-copy/exhaustion sentinel oracles remain.
Each requested output is consumed; no-output case observes count with state checks outside
timing. Fixed three warmup traversals do not establish frequency or placement stability.
Thread CPU, boundary IDs and reported QoS inherited unchanged; effective QoS unknown.

Validation: release and ASan/UBSan builds, original43tests, existing640cells/build;
new 768cells/build: n1/32/97/513,bytes16/320,integer/alternating-zero,threeconstruction
orders,bothdirections,all8masks. Requested2n+1 means3n effective items. Two hash seeds
covered with seed31001 for old cells,31013 new. Count/checksum/fingerprint/bytes checked.
Three isolated sensitivity faults: clear returned negative-zero sign, reverse state
corruption with mask0, length+1 with mask2. No source optimization counted.
Sequential review only: independent reviewer startup failed before execution.
Exact backend/model/cost unknown. Main source and all prior results stay untouched.
