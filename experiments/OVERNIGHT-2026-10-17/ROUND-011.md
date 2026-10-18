# Round 11 — allocator provenance and compact iterator guards

**Source adoption: NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.** Main tree,
header and root referee retain their previous hashes. No new optimization population
was started. This round extends existing candidates with separately qualified fixtures.

Round started at 02:12:26 UTC; deadline 02:42:26 UTC, handoff cutoff 02:40:56 UTC. The last
profile ended at 02:34:30 UTC. Remaining work was read-only auditing, documentation and
handoff. This is not the final campaign round; the final worker still writes
MORNING-REPORT.md before 07:00 UTC / 08:00Europe/Lisbon.

## Completed work

COUNTERS-006 isolates the prior native/sanitizer physical-layout discrepancy. Its fixed
factorial crosses ambient/exact/16-byte-rounded allocator capacity, O1/O3 and native/
ASan+UBSan: twelve allocator unit cells and twelve full semantic cells pass. Each semantic
cell checks 1,940 fixtures, 289,060 model states and 86,570,560 exact-score results. Fixed capacity
policies produce identical physical outputs across compiler/build cells, while capacity
intervention changes orientation counters. The preregistered structural hypothesis is
supported; this is not a timing or memory-efficiency result.

Six exploratory trace cells reproduce the selected fixtures and expose different usable-
capacity compaction decisions immediately before orientation diverges. The traces were
selected after discovery, and are labelled accordingly. Fresh-seed confirmation then
tests baseline and all three retained EXP-004 variants under both controlled policies
and both build types: all sixteen cells pass 1,980 fixtures each, including every size 0..96
plus 97/513. Each checks 325,860 model states and 163,246,200 exact-score results. Within each
capacity policy all eight complete outputs match. Controlled adapters remain diagnostic
only; their metadata/slack accounting never replaces the timing allocator or memory guard.

HARNESS-006 separately adds compact sentinel-delete, clone and refill histories using
the public API. Existing traversal/checksum/oracle/memory checks remain. Release and
ASan/UBSan each pass 2,560 fixture cells, the original 43 tests and five invalid-input checks:
5,136 validation commands with expected outcomes. Three deliberate length/sign/state
faults are detected. The frozen baseline receives six descriptive profiles and two
known-function calibrations; all controls pass.

AA-011 retains 384 timing rows plus one prospective warmup. Five of sixteen cell/seed
combinations qualify; only alternating-zero trimmed forward score-only qualifies on
BOTH seeds. Seven compact cells PARK. The initial analyser mistakenly retained the old
fixture's literal 200 traversals. Its code and outputs remain. A separate corrected analysis
uses the already preregistered ceil(20m/95) rule:210527 traversals, 20000065 effective items.
No measured child was repeated, no row removed, and no threshold or oracle weakened.

EXP-004's compact extension passes 1,770 validation commands across all retained variants.
All 72 screening rows, four prospective binary warmups and 72 precommitted fresh-seed rows
complete with exact memory/checksum/count/fingerprint equality. A and B pass the added
guard on both fresh seeds; C is inconclusive on one. No confirmed regression rejects a
variant. A/PARK remains: this guard cannot substitute for the original mixed-output guard.
Twenty candidate/control profiles plus four calibrations pass, including a separately
planned exact-mask set. Static code inspection confirms one fewer conditional cross-word
branch per candidate, without claiming executed branch counts, cycles or intrinsic ranking.

DIAG-013 tests a distinct compact warmup intervention, keeping measured work fixed.
All 192 rows plus one prospective warmup complete. Longer warmup halves absolute A/A bias
in three of four pairs, but only one long-policy interval qualifies; all four were required.
The remedy criterion is unsupported. No warmup policy adopted or baseline gate repaired.

## Commands and evidence

Commands ran locally and serially where measured. Exact argument vectors, flags, seeds,
stdout/stderr, file/binary hashes and timestamps are in the manifests linked below.

- COUNTERS-006 `run.py`, `analyse.py`, `trace.py`, `audit-trace.py`, `fresh.py`: complete;
  all semantic/unit controls pass, structural predictions supported on the tested matrix.
- HARNESS-006 `create.py`, `validate.py`, `faults.py`, `profile.py`, `analyse-profile.py`:
  all expected validation/fault/profile outcomes pass.
- AA-011 `run.py`, `analyse.py`, `analyse-corrected.py`: 384 rows complete; original stale
  count analysis retained, corrected qualification gives one jointly eligible guard.
- EXP-004/compact-guards `prepare.py`, `validate.py`, `profile.py`, `analyse-profile.py`,
  `run.py screen`, `analyse.py screen`, `run.py confirm`, `analyse.py confirm`,
  `profile-exact.py`, `analyse-profile-exact.py`: complete; A/PARK unchanged.
- DIAG-013 `run.py`, `analyse.py`: 192 rows complete; fixed remedy criterion unsupported.
- `verify-round011.py`:PASS, 72 wall/thread intervals recomputed from raw rows;
  758 measurement/profile windows serial and 7,017 timestamped nonmeasurement commands
  disjoint. Root hashes, retained sources, identical referees and raw-output hashes pass.
- `python3 scripts/check-workspace.py --pristine-source` and `git diff --check`:PASS.
  Final public-curation and SHA256 records accompany this report.

[Allocator diagnostic](COUNTERS-006/README.md),[new referee](HARNESS-006/README.md),
[qualification and erratum](AA-011/README.md),[compact guards](../EXP-004/compact-guards/README.md),
[warmup diagnostic](DIAG-013/README.md),[audit](ROUND-011-VERIFY.json),
[sequential adversarial review](ROUND-011-REVIEW.md),[method record](ROUND-011-METHOD.json).
Large/raw profile and method outputs remain under ignored scratch with recorded hashes.
No private hostnames, credentials or full agent transcripts are published.

## Decision and handoff

Totals: **six harness revisions, twelve baseline explorations, twenty-one additional
diagnostics, fourteen boundary suites / 28 distinct boundary fault types; four sequential
population rounds; zero accepted, two rejected and two parked optimizations.** This
round retains 720 measured rows, six prospective warmups, 26 profiles and six calibrations.
All measured children completed; the analysis error and every earlier failure remain.

Exact backend/model/token cost are unknown; supervisor usage is separate. Independent
reviewer startup failed before execution, so confirmation and review remain explicitly
sequential. Frequency/effective QoS, within-window migration and sampler bias remain
unknown. CPU MCP ask and methods/code 05/14 were consulted; tangential ask passages were
not cited as causal evidence. Evidence checker returned drop_number; no portable speed
headline or M4 measurement is transferred. Base commit remains
a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicit uncommitted snapshots/patches/SHA256;
committed acceptance awaits morning review. No git retry, publishing, permission change,
runtime/STOP edit, detached process or source adoption.

Next concrete action: preregister a controlled-capacity mutation oracle with mixed finite
scores around packed-width and split/merge thresholds, extending this round's alternating-
zero capacity result. Retain the independent scalar/public-API model and fault controls.
Alternatively design a new compact process/block-position diagnostic from AA-011 and
DIAG-013 raw position rows; do not rerun the failed longer-warmup schedule unchanged.
Do not pool old/new checksum-harness timings or replace the unresolved original mask6
guard. Both population stages remain mandatory for any new optimization hypothesis.
