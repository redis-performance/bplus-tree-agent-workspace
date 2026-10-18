# EXP-002 expanded guards — REJECT; selection NONE

This supersedes round6's provisional C preference. All three retained implementations
fail the declared guard policy on fresh fixtures. Main source remains baseline; A/B/C
patches and all losing snapshots preserved. This rejects these implementations under
the no-regression gate,not every possible iterator specialization.

HARNESS-004 is a separate validated/frozen referee. Control/A/B/C each pass original43
tests plus640 mode fixtures in BOTH release and ASan/UBSan (5144 validation commands).
AA-006 qualifies10/14 modes;four mixed-output modes remain diagnostic. Discovery uses
504 fixed serial rows,3ABBA blocks per variant/mode. All counts/checksums/exact score/
member/owned-memory controls pass. All variants retain primary improvement but show
qualified guard regressions. No rows removed,including noisy reverse/long-key cases.

Fresh confirmation uses216 fixed rows,seed9103/9151,3blocks per variant/cell/seed.
No-output guard regression confirms for A/B/C on BOTH seeds;full-output confirms for
B/C. A full-output interval crosses the gate for one seed,so that guard is unresolved.
No tradeoff was declared. Thus REJECT all three;selection NONE. Same coordinator fresh
samples,not independent performance confirmation. No source accepted or deployed.

Eight matched descriptive profiles/two known-function calibrations pass. Saved public
entry codegen shows A retaining generic register saves plus added guard branches;
B/C add a public guard sequence and tail branch before generic fallback. Samples land
in both wrapper and generic helper for B/C guard modes. This supports extra dispatch
on fallback while score-only paths avoid generic saves;not exact cycle attribution,
proof of sole causation,or unbiased time shares. Timer-boundary samples are retained.
Instrumented times never used for source comparison;raw PCs/assembly stay in scratch
with commands/checksums in profiles/manifest.json. Frequency/scheduling remain unknown.

[Plan](PLAN.md),[freeze](freeze.json),[discovery](SUMMARY.md),[fresh plan](CONFIRMATION-PLAN.md),
[fresh result](CONFIRMATION.md),[profiles](profiles/SUMMARY.md),[codegen](profiles/ENTRY-ASSEMBLY.md).
Exact source/referee/binary hashes and all run stdout/stderr in manifests. Base commit
plus explicitly uncommitted snapshots;morning commit provenance review pending.
CPU MCP checker consulted;drop_number caveat retained;no portable performance headline.
Independent reviewer failed startup;sequential adversarial review in ../review/ROUND007.md.
Backend/model/cost unknown;supervisor records CLI tokens. No publishing/git retry/settings
change. Next work should target a new profiled hypothesis or genuinely new guard design,
not repeat the same failed dispatch implementation with only longer timings.
