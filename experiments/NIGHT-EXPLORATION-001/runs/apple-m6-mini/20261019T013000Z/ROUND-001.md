# Round 1 — M6 rank population rejected

The launcher-completed five-size baseline was reused. The new rank referee passed
138 native/sanitizer checks and detected a rank fault. Public self-profiling located
ancestor accumulation, and actual release assembly showed Clang already vectorizes
it. No explicit SIMD assumption was used. Private census and timings were labelled
separately from the public API; they were never subtracted as component estimates.

One calibrated A/A schedule completed 72 serial processes / 216 batches. All three
cells failed the ±1% rule; no schedule was repeated. Three sequential proposal
passes and chair chose unconditional shorter-side summation for one exploratory
screen. Three isolated implementation copies passed native and ASan/UBSan upstream
tests plus targeted semantic checks, with identical referee hashes. All patches
are preserved. The screen completed 216 serial processes / 648 batches.

Every candidate regressed the 100K primary in every block: median effects +3.808%,
+3.425%, +3.871%. Their 1M negative signals remain inside observed control variation.
Select NONE and reject this policy for the declared two-primary objective. Tree-owned
bytes match. Logical summands decrease, but all three static rank bodies grow; the
exact branch/cache cause is unmeasured. No fresh confirmation, full candidate guard
campaign, independent review or adoption profile validation is claimed.

[Results](002-rank/RESULTS.md), [population decision](002-rank/implementation-selection.md),
[self-review](002-rank/review.md) and [raw/source audit](002-rank/final-audit.json).
Source and historical referee hashes remain unchanged. All recorded experimental
commands are serial; the audit explicitly retains the brief calibration-summary
overlap and unknown background activity. External sample attach failure and helper
missing-include build failure are preserved. No permissions were changed.

Publication acknowledgements: baseline 48b00870, referee ca5cacfb, profile/counts
210c06a2, controls b5ebd930, chair fedb7d41, comparison freeze 3102530f, rejection
23df69a3. Final audited handoff publication follows this report. The coordinator is
the sole Git writer; this worker did not add, commit or push. Shared logs/counts/
memory are updated. Recorded branch totals: eight populations, 0 accepted / 3 rejected /
5 parked, 24 patches and 11 harnesses. Concurrent M1 night counts remain separate.

Next round resumes UPDATE-001 from [HANDOFF.md](HANDOFF.md). No experimental children
remain. Saved before the required round-end margin. Exact serving model and measured
token costs unavailable; both populations used sequential fallback, not agents.

Publication update 2026-10-19T02:01:23.704328+00:00: corrected request r1-final-audit-handoff-cache-fixed-20261019T015855Z timed out after 120 seconds with no matching acknowledgement. Last ack is the earlier bytecode-cache rejection; see PUBLICATION-TIMEOUT.json. Final audited report/logs remain local and publication is unresolved. Last successful decision commit is23df69a3. The corrected request remains pending; check it before a new round publication. No Git writes or permission changes were attempted. Continue useful bounded UPDATE-001 preparation; do not claim unpublished provenance is acknowledged.
