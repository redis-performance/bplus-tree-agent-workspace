# Sequential adversarial review

This is a separate coordinator pass. Reviewer agent startup failed before running;
no independent-agent review or confirmation is claimed. Exact backend/model/cost unknown.

Semantics: only tag-position search changes. All candidates return the earliest matching
physical tag and leave full hash, packed length, byte comparison, physical/logical mapping,
score decoding and external ownership untouched. Zero-length search performs no load.
Repeated tags and false-positive zero-byte borrow bits are covered by exact first-match
oracles. Cloads a second8-byte word only after n>=16;8-bytecleanup requires n>=8;
scalar tail checks remaining bytes. memcpy avoids alignment/aliasing UB. ctz only runs
on nonzero masks. Little-endian assumption is guarded, scalar fallback otherwise.
Other architectures and actual big-endian execution are unmeasured.

Memory/ownership: no tree allocations or stored layout change. Exact tree-owned byte
checks pass all timing rows; guard-page tests separately protect helper input spans.
The original oversized tag-array oracle alone was insufficient to detect unused
out-of-bounds loads; new protected-page coverage plus a detected n>0fault addresses
that gap. Raw-query guard tests and original ASan/UBSan suites are unchanged.

Measurement: baselineA/A qualifies the chosen mixed and long-key cells, not single-lane
or all-short guards. Fixed serial3-blockscreening and6-blockfresh confirmation retain
all observations. The long guard fails its fresh uncertainty gate; no normalization,
row removal, continuation, or relabelling makes it pass. Screening single-lane regression
is an additional substantive concern. Do not claim Cwins overall or accept on primary only.

Mechanism/maintainability: source growth, loops and scalar tails increase complexity.
Assembly and profiles verify removal of generic memchr, but neither proves frequency
stability or unbiased time fractions. Byte scanA demonstrates that removing a call can
lose performance. UnrolledC retains a scoped experimental preference only. Keep all
losing patches and baseline; no upstream action or root source replacement.
