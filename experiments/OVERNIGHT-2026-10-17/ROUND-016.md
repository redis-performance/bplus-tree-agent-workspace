# Round 16 — live SCAN across natural width and ownership changes

**Source adoption NONE. EXP-004 remains A/PARK; EXP-005 remains PARK/NONE.**
The main source and root referee remain baseline. This round adds one boundary suite
with three extensions and one execution-count diagnostic. No timing benchmark, harness
revision, A/A qualification or optimization population ran.

Round start 04:18:09 UTC; deadline 04:48:09 UTC; handoff cutoff 04:46:39 UTC. Experimental
children have finished. This is not the final campaign round; the final worker still
owes MORNING-REPORT.md before 07:00 UTC / 08:00 Europe/Lisbon.

## Completed work

| Evidence | Passing source/build/seed/mode cells | Scope |
|---|---:|---|
| [BOUNDARY-023](BOUNDARY-023/README.md) | 16 | One live cursor spans actual narrow→wide migration and completion |
| [Clone/relocation extension](BOUNDARY-023/relocation-extension/README.md) | 48 | Active clone/free-original, all-move and selective-decline relocation |
| [External ownership extension](BOUNDARY-023/external-extension/README.md) | 48 | Independently allocated320/321/1024/4097-byte members |
| [Narrowing extension](BOUNDARY-023/narrowing-extension/README.md) | 16 | Bulk deletion compacts IDs and narrows the table without restarting cursor |
| [Fresh-seed confirmation](ROUND-016-CONFIRMATION/README.md) | 64 | Final external/narrowing oracles with debug-only assertions omitted |

All 192 cells pass native/sanitizer semantic checks. Every live SCAN call checks exact
current binary key bytes/length and finite score bits, and completeness for its independent
scalar reversed-hash interval. Duplicates are allowed. Continuous anchors and termination
within the largest observed group bound hold. Full ordered/lookup models, sampled rank/
seek, parent/subtree/leaf registry and exact tree-owned usable bytes pass. Printed digest
covers IDs/scores; key bytes are independently checked but not included in that digest.

Natural widening begins with the same nonzero cursor and stays active for 2,047 calls in
these local fixtures. It is reached through public construction, never private-ID edits.
This round exercises mixed bucket formats, not a new crossing of UINT16_MAX. At the active
state, inline relocation visits 34,955 owned allocations exactly once. External mode adds 3,088
separate buffers; all 38,042 allocations are visited once, including moves and legal declines,
with exact accounting and stable rehash metadata at every public defrag step. Clone
ownership is disjoint before freeing the original and continuing its numeric cursor.

Narrowing retains 4,096 designated continuous anchors. Public deletions compact the first
survivor's leaf ID 32,392 to 0 and reduce next ID 35,497 to 343; index width becomes narrow.
The original cursor terminates in 2,297 calls, below 16,384 largest groups. Every removed member
is separately checked absent. Counts/cardinalities describe local observations, not portable
constants. No production bug or performance improvement is claimed.

[COUNTERS-009](COUNTERS-009/README.md) and its [extension](COUNTERS-009/extensions/PLAN.md)
complete six whole-oracle captures. They confirm actual wide/narrow reads, dual-table scan,
active clone/relocation and external accept/decline branches, plus one dense renumber/rebuild.
These include setup and validation: execution counts are not hotness, CPU time or speed.

## Failures and test sensitivity

All six deliberate faults are detected: three new types (wide SCAN decoded narrow,
truncated wide clone allocation, stale leaf ID after renumbering) and three repeats
(omitted old table, dropped relocated destination assignment, shallow external clone).
The first width-fault classifier wrongly labelled a production abort SURVIVED because
the adapter prints file:line:expression without the word Assertion. The original result
remains; a read-only source/stderr audit proves detection without rerunning the child.

Initial narrowing compilation failed on dereferencing the public void* iterator.leaf.
A separately frozen attempt002 adds only an explicit read-only private-type cast. No
runtime child ran from the failed build, and no oracle condition or threshold changed.
ASan external-symbolizer warnings from deliberate faults remain; no retry/escalation.
The initial workspace audit also found the README linked this report before it existed;
that failure is retained and the report is now written. No experimental child was rerun
for the documentation repair. All raw failures, source snapshots and patches remain.

## Commands and validation

Each linked evidence directory contains run.py, its preregistration, manifest, exact
compiler/child commands, UTC endpoints, stdout/stderr and SHA256 files. Commands run
serially; every child is bounded 120 seconds. Apple Clang 17 arm64 uses -O3/debug or -O1
ASan/UBSan with the unchanged allocator; fresh confirmation omits only REDIS_DEBUG and
changes input seeds. Every oracle CHECK and unconditional serverAssert stays active.
Original 43 tests were not rerun; unchanged source/build evidence from round 14 remains.

The final [read-only audit driver](verify-round016.py) verifies raw file hashes, serial
windows, exact patch reconstruction, prior frozen evidence and source provenance, then
workspace/pristine-source and whitespace checks. [Final audit](ROUND-016-VERIFY.json) passes 1,719 hashes, 277 serial command windows,
11 new patch reconstructions and six raw branch mappings. Workspace/pristine-source
and `git diff --check` pass. A separate [candidate audit](ROUND-016-CANDIDATE-AUDIT.json)
checks 256 frozen files and reconstructs all 12 retained optimization patches.
[Sequential adversarial review](ROUND-016-REVIEW.md) records limits and next evidence.

## Decision and handoff

Totals: **6 harnesses, 12 baseline explorations, 29 diagnostics, 23 boundary suites,
48 distinct boundary fault types; 4 sequential populations; 0 accepted, 2 rejected, 2 parked
optimizations.** This round adds one suite, one diagnostic and three fault types.
Base commit remains `a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c` plus explicitly
uncommitted isolated snapshots. Main source stays baseline until morning review.

CPU MCP ask and benchmark 05/14 methods/code were consulted. Unrelated retrieval passages
were not used as support. Its evidence checker returned no_number for the qualitative
no-speedup statement; this is not measurement approval. No M4 numbering/clock/result
transfer. Exact backend/model/token cost unknown; supervisor records CLI usage separately.
Reviewer startup failed, so all review/confirmation is sequential. Frequency, effective
QoS, within-window migration, qualified performance guards, independent review and
committed provenance remain unresolved.

Next: preregister [score moves during actual mixed-width migration](ROUND-016-NEXT-FIXTURE.md),
using a genuine sorted model with callback-time score bits and observed cross-table leaf
ownership. That recipe is preparation, not a result. Performance needs new justification
or a separately qualified runner; do not repeat failed protocols unchanged. No publishing,
git metadata retry, credentials, supervisor/runtime/STOP or permission edits occurred.
