# COUNTERS-007 — recovery-path execution counts

Three serial baseline whole-oracle Clang coverage captures PASS, with unchanged
source and binary hashes and semantic PASS output. These are execution counts,
not CPU-time profiles, cycles, performance fractions or timing-qualification evidence.

| Observed path | Lifecycle | Relocation | Fresh mutation |
|---|---:|---:|---:|
| Repair member cursor on leaf removal | 2 | 0 | 0 |
| Reuse free ID after resize | 4 | 0 | 0 |
| Allocate while free IDs deferred | 16 | 0 | 116 |
| Freed-ID member cursor condition | 0 | 0 | 0 |
| Member cursor NULL fallback | 0 | 0 | 0 |
| Retired defrag cursor recovery | 0 | 4 | 256 |
| Defrag tree identity reset | 0 | 8 | 32 |

This confirms the coverage distinction: public leaf retirement repairs the member
cursor, whereas defrag's caller-owned cursor can retain a retired ID and restarts.
The member-cursor defensive fallback is unobserved in these schedules; zero is not
proof of unreachability or permission to remove the check. In particular, append
construction migrates the final leaf early, so these captures also miss the normal
end-of-list sentinel route. A public shrinking-resize fixture is a concrete next
coverage question, because its untouched last leaf may migrate at the end.

Commands: `python3 experiments/OVERNIGHT-2026-10-17/COUNTERS-007/run.py` then
`analyse.py`. [Plan](PLAN.md), [manifest](manifest.json), [summary](summary.json),
per-case mapped function/branch records and exact source snippets retained. Raw
profraw/profdata/full exports remain in ignored scratch with SHA256 in manifest.
All three include construction, model helper calls, mutations, cloning and cleanup.
No test/build overlaps a capture. Flags match across captures; no source counters
or code edits are inserted. The oracles differ, so counts are not normalized claims.

Curation note: the original *-source-lines.json helper assumed every branch location
was in the tree file; macro expansions also refer to compat/server.h. Retain those
first files, but use *-mapped-counts.json, which resolves each LLVM file ID before
reading its source line. Counts themselves and all executions are unchanged.

Decision: coverage census complete, additional diagnostic27. Source NONE; existing
PARK decisions unchanged. No new optimization, population, harness or baseline count.
Review sequential; exact backend/model/token costunknown.
