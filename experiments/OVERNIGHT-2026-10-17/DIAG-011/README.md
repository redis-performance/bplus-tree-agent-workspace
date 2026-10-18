# DIAG-011 — caller hypothesis unsupported

144fixed rows complete;all count/checksum/member/score/state/owned-memory controls pass.
The preregistered mask6 interaction criterion passes one seed and fails the other;
therefore unsupported. No optional stopping or noisy-row removal. EXP-004 A/PARK stays.
The altered caller does not qualify or replace HARNESS-004,does not clear its guard,
and cannot be used to accept the candidate. No source timing gate relaxed.

Eight matched descriptive profiles/two calibrations pass. Codegen reveals an additional
premise error:Clang already unswitches the dynamic mask6 loop,so its per-element body
contains NO output-mask tests. The fixed caller changes registers/callsite/layout and
surrounding code;this experiment does not isolate a predictor/cache mechanism. Keep
this negative result and do not repeat the same test as a branch-removal remedy.
[Assembly audit](profiles/CALLER-ASSEMBLY.md),[profile summary](profiles/SUMMARY.md).

384validation fixture processes plus4builds pass across control/A release/sanitizers.
Original plan/progress label overstated cardinality192perbuild;explicit listed matrix
has96. [Pre-timing erratum](VALIDATION-ERRATUM.md) records the arithmetic correction;
no listed fixture removed or check weakened. Full original oracle unchanged.
[Plan](PLAN.md),[timing results](SUMMARY.md),[commands/hashes/raw](manifest.json),
[freeze](freeze.json),[patch](caller.patch). Structural16th additional diagnostic.
Root and retained candidates unchanged. Exact backend/model/cost unknown,review
sequential. Clock/frequency/effective QoS/residency/sampler bias unknown;no speed headline.
