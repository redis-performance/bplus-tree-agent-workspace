# All three native ARM implementations eligible; discovery not started

Fixed600s correctness job completed392.6s /145 logged commands. Base/A/B/C each pass
original43 tests in native-O3 and ASan/UBSan-O1, exact V2 all-match oracle, scan interval,
wide-ID seeds7/19, live-widen SCAN seeds7/19 and resize-generation suites. Candidate
semantic outputs match baseline per mode/seed. All three designated portable paths
pass V2 in both modes. No candidate source repairs occurred after sealing.

Eight isolated faults detected (four × native/sanitizer): fold omission and missing
tail trigger count/canary assertion, reversed lanes trigger order assertion, overread
mutation triggers count/canary assertion before a protected-edge signal. Therefore
we do NOT claim that this negative run demonstrated a guard-page fault. Positive V2
runs still exercise protected input boundaries/misalignment. Prior SSE2 aligned-load
fault is retained as provenance and was not relabeled as an ARM alignment test.
Fault-only symbolization disabled; positive sanitizer runtime unchanged.

Native A/B/C codegen each contains byte cmeq and shrn instructions (five and two static
occurrences respectively); exact source-linked disassembly retained. This confirms
native vector compilation, not a speedup. Whole.text hashes are distinct, so no whole
binary identity claim is made. Maintenance order remains preregistered B,C,A.

The rebuilt validation baseline .text matches the existing AA baseline exactly.
Original timing binary869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055
and source/referee hashes pass before/after checks. Original timing binary remains
the control; all candidate binaries use identical relative frontend/output paths,
compiler/options/allocator/assertions/hash/referee. Actual binary pins and exact144row
schedule/driver hashes are in comparison-freeze.json. No candidate timing has run.
Root static/finalfreeze review required before the fixed300s discovery phase.
