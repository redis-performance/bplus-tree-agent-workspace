# Round 17 — score movement during mixed-width migration

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
Main source and referee retain their prior hashes. This round adds one boundary suite
with extensions and one execution-count diagnostic. No timing benchmark, harness
revision, A/A qualification or optimization population ran.

Round start 04:43:22 UTC; deadline 05:13:22 UTC; handoff cutoff 05:11:52 UTC. All
experimental children have finished. This is not the final campaign round. The final
worker still owes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work

| Evidence | Passing source/build/seed cells | What it establishes |
|---|---:|---|
| [BOUNDARY-024](BOUNDARY-024/README.md) | 16 | Current-score movement while one SCAN cursor spans natural widening |
| [External extension](BOUNDARY-024/external-extension/README.md) | 16 | External ownership preserved across score changes |
| [Finite ties](BOUNDARY-024/finite-ties/README.md) | 16 | Exact finite extremes, signed zeros, repeated scores and range counts |
| [Neighbor ties](BOUNDARY-024/tie-neighbors/README.md) | 16 | Actual rejection of locally misordered equal-score neighbors |
| [Fresh confirmation](ROUND-017-CONFIRMATION/README.md) | 64 | Fresh seeds with debug-only assertions disabled |
| [Corrected batch promotion](BOUNDARY-024/batch-promotion/attempt-002/README.md) | 8 + 8 fresh | A public batch completes width promotion inside the call |
| [Initial batch recipe](BOUNDARY-024/batch-promotion/SCOPE-NOTE.md) | 8 + 8 fresh | Retained actual schedule; planned ID1 batch input was missing |

There are **160 passing semantic cells**, including 16 retained initial batch cells
with that scope limitation. The final intended fixtures account for **144 cells,
72 of them fresh confirmation**. Every cell runs six independent sorted-model checks.
The initial scope-limited cells are not used to claim the corrected batch coverage.

The new oracle maintains a true current-score vector and orders by numeric score,
then binary member bytes and length. Exact score bits are checked separately. Updates
use fresh successful public FindForAdd positions. Appending stops before scores move
beyond the previous maximum, preserving the append API's ordering precondition.

Inline fixtures perform 258 cross-leaf updates and two exact signed-zero changes.
Both copied-source/uncopied-target and uncopied-source/copied-target cases are observed.
The target classification is recorded before the update; splitting can change its ID.
Every SCAN call checks current bytes, lengths and score bits, independent reversed-hash
interval completeness, legal duplicate callbacks and nonmutation of resize metadata.
All continuously present initial members appear before bounded cursor termination.
Full postmigration lookups, sampled ranks/seeks, parent/subtree/registry relationships
and exact tree-owned usable-byte accounting pass. Rank checking is not exhaustive.

External fixtures check 260 preserved external addresses per cell, with unique buffer
ownership and exact accounting. Execution counts distinguish 259 detach/reinsert paths
from one in-place update. Finite fixtures use explicit ±largest finite, ±smallest
subnormal, ±smallest normal, ±zero, ±1 and ±2^53 patterns; no NaN or infinity inputs.
They check 288 inclusive/exclusive equal-score range counts per cell. Neighbor fixtures
add two same-leaf reorders and raise that count to 336.

The final batch fixture checks counts 0–16, hit masks, exact current hit scores,
duplicated and absent members, and canaries outside the requested output count. Miss
output lanes remain unspecified. It observes one 16-lane call entering with a narrow
current table and wide resize destination, then returning with completed wide current
table. The original live SCAN and external ownership checks remain active.

## Sensitivity and retained limitations

Seven deliberate-fault runs produce six detections, covering five new distinct fault
types: missing moved-member destination insertion, stale packed in-place score bits,
omitted external detach, skipped equal-neighbor ordering, and stale batch table cache.
The batch-cache fault is repeated against the corrected fixture and produces an ASan
heap-use-after-free. These are deliberate faults, not discovered production defects.

The first equal-neighbor fault **survives** in the finite-only fixture. A separate
neighbor fixture forces ID256 to score255 and ID511 to score512, where binary-key
order requires movement, and detects it. Both old and new evidence remain.
[COUNTERS-010](COUNTERS-010/README.md) and its [tie extension](COUNTERS-010/ties/README.md)
complete four captures: the first fixture never executes either lexical neighbor
comparison; the stronger fixture executes and rejects each once. Other captures
confirm in-place, detach/reinsert and index copy/delete/insert/relabel paths. These
are whole-oracle execution counts, not CPU-time profiles, hotness or speed evidence.

The initial batch expression selected ID2 in every repeated lane despite the planned
ID1/2 coverage. Its outputs are retained with a scope note. Attempt002 changes only
that expression, preserves every assertion and parameter, and passes discovery plus
fresh confirmation. The audit reconstructs this one-expression change exactly.
ASan symbolizer warnings remain in fault logs; no permissions were escalated.

Two initial audit failures are retained: the verifier first misread the prior manifest's
seal, then reconstructed its ordering incorrectly. The corrected audit reconstructs
the exact pre-seal hash using the original Path ordering and validates the sealed files.
No experimental child was rerun. [Erratum](ROUND-017-AUDIT-ERRATUM.md) and original
verifiers/stdout/stderr retain the failures. Private absolute paths were curated only
after preserving original stderr and hashes under ignored scratch.

## Commands and verification

Each linked directory contains PLAN.md, run.py, manifests, commands, UTC endpoints,
stdout/stderr, source/binary hashes and patches. The principal invocations were:

```sh
python3 experiments/OVERNIGHT-2026-10-17/BOUNDARY-024/run.py
python3 experiments/OVERNIGHT-2026-10-17/ROUND-017-CONFIRMATION/run.py
python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-010/run.py
python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-010/ties/run.py
python3 experiments/OVERNIGHT-2026-10-17/verify-round017.py
python3 experiments/OVERNIGHT-2026-10-17/audit-round017-candidates.py
```

Extension/fault drivers and their exact compiler/child commands are in their linked
manifests. All commands ran serially; every experimental child was bounded to 120s.
Apple Clang 17 arm64 used native O3 or O1 ASan/UBSan and the unchanged allocator.
The original 43-test suite was not rerun; unchanged round14 evidence is retained.

[Final audit](ROUND-017-VERIFY.json) passes **2,268 hashes, 286 serial command windows,
15 new patch reconstructions and four raw branch mappings**. It verifies all matrix
outputs and the preserved prior evidence. Workspace/pristine-source and whitespace
checks pass. A separate [candidate audit](ROUND-017-CANDIDATE-AUDIT.json) checks 256
frozen files and reconstructs all 12 retained optimization patches. All old evidence
and losing variants remain.

## Decision and handoff

Totals: **6 harnesses, 12 baseline explorations, 30 diagnostics, 24 boundary suites,
53 distinct boundary fault types; 4 sequential populations; 0 accepted, 2 rejected,
2 parked optimizations.** This round adds one suite, one diagnostic and five fault types.
Base commit remains `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c` plus explicitly
uncommitted isolated snapshots. Keep main baseline until separate morning review.

Reviewer-agent startup failed; [adversarial review](ROUND-017-REVIEW.md) and confirmation
are sequential, not independent agents. Exact backend/model/token cost is unknown;
the supervisor records CLI usage separately. CPU MCP ask and benchmark05/14 methods/code
were consulted; irrelevant retrieval was not cited. Its checker returned no_number for
the qualitative no-speedup statement, not measurement approval. No M4 results transfer.

Frequency, effective QoS, within-window migration, qualified performance guards,
independent review and committed provenance remain unresolved. No publishing, protected
git retry, credentials, supervisor/runtime/STOP or permission changes occurred.

Next: preregister [smaller and all-miss batches across promotion](ROUND-017-NEXT-FIXTURE.md).
That is preparation only. Performance needs distinct qualification or a qualified runner;
do not repeat failed timing protocols unchanged or substitute new fixtures for the
original unresolved guard. The final worker still writes the morning report.
