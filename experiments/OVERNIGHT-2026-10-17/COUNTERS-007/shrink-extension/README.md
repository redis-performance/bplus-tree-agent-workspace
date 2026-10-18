# Separate shrinking-resize branch census

One serial baseline whole-oracle capture PASS. The new public shrinking fixture
enters zbtIndexRehashStep's NULL-cursor fallback eight times: source and clone in
each of four fixtures. The freed-ID branch remains zero. Post-resize free-ID reuse
is observed four times. This separates the legitimate end-of-list recovery route
from an unobserved freed-member-cursor route; it does not prove unreachability.

Commands: `run.py`, `analyse.py`. [Plan](PLAN.md), [manifest](manifest.json),
[summary](summary.json), [mapped branches](shrink-mapped-counts.json). Raw profiles
and full export remain ignored with hashes. This fourth capture is a preregistered
extension after the first three completed; their observations are not changed.
No timings or source acceptance. Same diagnostic count, sequential review only.
