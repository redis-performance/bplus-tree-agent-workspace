# COUNTERS-010 — observed score-move branches

Both preregistered unchanged-control captures pass their normal oracles. Instrumented
O1/debug execution counts include the whole process, not timed loops. They establish
reachability, not speed, hotness, frequency or a performance precision remedy.

| Observed operation | Inline | External |
|---|---:|---:|
| UpdateScore calls | 260 | 260 |
| In-place updates | 2 | 1 |
| Delete/reinsert path | 258 | 259 |
| External detach calls | 0 | 259 |
| Different old/new leaf after reinsertion | 258 | 258 |
| Copied-target index removal | 9 | 1 |
| Destination-table relabel | 22 | 1 |
| Old-to-new index insertion | 235 | 256 |

IndexMove counts include construction and split maintenance, so the last three rows
are not all attributed solely to top-level updates. The separately recorded source/
target migration markers in BOUNDARY-024 establish the active mutation phase. External
signed-zero handling includes one reinsertion retaining the same leaf ID; pointer
preservation does not imply that all260updates invoked external detach.

The two raw exports and profraw/profdata files stay under ignored scratch with SHA256
in manifest.json. Public inline-counts.json and external-counts.json map each LLVM
branch's file ID to the actual source line, including assertion macro bodies. Exact
commands, source/binary hashes, UTC intervals and stdout/stderr are retained. No
benchmark or other child overlaps a capture. SourceNONE and all existingPARK unchanged.
