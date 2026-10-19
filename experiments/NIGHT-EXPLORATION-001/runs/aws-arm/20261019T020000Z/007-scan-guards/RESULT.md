# Baseline referee validation: PASS, no timing result

All108 cells (36 combinations × seeds101/102/103) pass separate-TU native,
ASan/UBSan, and the never-timed read-only census. All36 compact nonce fixtures
have retained SHA256 hashes. Eight realistic wrong-output controls fail as expected:
score, length, omitted real member0 including all duplicate callbacks, and member
content, each native/sanitizer. Both unchanged original test builds pass43/43.
There were368 final validation commands, with no baseline or candidate timing windows.
This is local x86_64 baseline correctness evidence, not an ARM or Intel performance result.

All36 descending cases have exactly one naturally reversed leaf containing64 members:
1.5625% at4096 members and0.064% at100000. Every actual physical tag matches its
original hash; high17 fixtures are100% tag17, folded fixtures contain both0 and1 only.
No inspected case has active member rehash or wide leaf IDs. The321-byte cases use
external records. Dense active-resize, broad reversed, and wide-ID performance coverage
remain absent. Existing unchanged tests cover resize/SCAN correctness only; seeREADME.

The first unqualified validation attempt wrongly compared native and sanitizer allocation
sizes; failed evidence and its new-driver correction are preserved. Root also rejected
the original missing-member fault that directly changed a coverage bitmap. Its retained
replacement omits real callbacks without manipulating the bitmap. Neither fix changed
original tests or tree source, and no timing preceded the corrections.

Referee source, original tree/header, fixture manifest and schedule are frozen in
referee-freeze.json. Root reviews this immutable publication before Intel calibration.
Budget300s calibration +900s A/A +900s B comparison, all36 cells/six blocks, seeds101–103.
Target200ms, floor100ms; freeze passes before A/A and never tune duration from A/A results.
A noisy or missing guard blocks acceptance; this validation does not adopt any source.
