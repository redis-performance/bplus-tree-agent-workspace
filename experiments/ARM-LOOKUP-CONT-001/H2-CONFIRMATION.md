# H2-B held-out confirmation admission

Only B remains eligible. Independent readiness review reconstructs all 1,056 original A/A and B rows across six-case and supplemental workloads, checks source/referee/provenance, and independently hashes all four lookup candidate ELFs. Code audit and ARM/Intel discovery guards pass. Selection remains NONE pending this phase and final profile/raw review.

Confirm the principal ARM GCC15/LTO target on fresh seeds29 and43. Each seed runs all six original cases (72 A/A, then72 comparison rows only if all controls pass), followed by all five affected-operation guards (60 A/A, then60 B rows only if all controls pass). Thus each seed has264 planned rows and both have528. Reuse exact frozen baseline and candidate ELFs; no rebuild, count, fixture, source or gate changes.

Order: six cases seed29, five guards seed29, six cases seed43, five guards seed43. Stop admitting subsequent confirmation phases after any failed qualification/comparison or process failure. Retain every attempted phase, including partial/failed rows. Original native and Intel cohorts provide separate portability/guard evidence; do not pool their timings with this target confirmation.

The six-case collector was hardened before any confirmation ran. Its new A/A controls qualify the self-contained runner. Original comparison collector and measurements remain untouched. Reviewed pins:

- Six-case self-contained collector: `1491e9dd9fede0f5c62ce5e04169a62b48626f04f56b799e6e47e3c1f7e2237b`.
- Guard confirmation driver: `72a0d1771c830becf95a8f7439378b9f88b2c689c214dcd8d2b7b2a386841a67`.
- Original guard collector with explicit C exclusion: `a1ddc7e99f7a03076757dd64f263a3c3dd6d4fc0501dc516a83a6a1306c09704`.

Both wrappers derive deterministic origin+seed output directories and prohibit failed-phase retries. Per-process source/ELF, lease, coordinator and isolation checks are mandatory. A passed seed does not compensate for a failed seed or guard. Full acceptance still requires both seeds/all11cases, matched ARM profiles and final independent evidence review.

No pipeline measurements are collected by these wrappers. ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable without qualified event/formula evidence; Intel lookup TMA is reported separately for its own hardware/scope.

## Additional independent-host confirmation

Before any new Intel held-out process, also admit the same two-seed/all11case confirmation on the independently qualified Intel GCC15/LTO cohort. It uses its own immutable ELFs, fresh A/A and original portability bounds (all cases no>1% regression; no mandatory2% Intel speedup). This parallel cohort tests whether the guard behavior persists under independent seeds on another architecture. No timing is pooled with ARM. Failures remain evidence and cannot be waived by the target result. This adds no new source population or baseline qualification ledger entry; it is confirmation of the same H2-B candidate.
