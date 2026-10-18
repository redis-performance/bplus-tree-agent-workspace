# Compact iterator code generation

Read-only extraction from the already captured instrumented-binary disassemblies;
[snippets and hashes](codegen/summary.json). No additional timing or counter run.

The control has two conditional branches around the cross-word packed-score read:
`b.eq` after testing shift zero, then `b.hs` after comparing bits with64-shift.
A uses addition/compare and one `b.lo`; B uses subtract/compare and one `b.hs`;
C uses subtract/compare and one `b.ls`. Each candidate has one fewer static conditional
branch in this function. This is a compiler mechanism observation, not executed branch
counts, branch misses, cycle attribution or proof that one arithmetic form must win.

The complete static iterator bodies contain155instructions for control/A/B and156forC.
Other instruction ordering and addresses differ, so even total instruction count does
not isolate dynamic work. Signal-instrumented binaries are distinct from timing binaries;
the retained source change is the same, but instruction placement can affect behavior.

The prior COUNTERS-005 census of n95/bytes16/alternating-zero/trimmed reports95reversed
members with two-bit scores, in both builds and seeds. This supports a narrow-width
mechanism prediction for the matching public-API recipe; it is not a measured execution
count for these new seeds. Exact-mask sampled profiles now cover the actual compact
guard and show iterator/caller work. They cannot explain exact timing differences or
resolve C's uncertain guard interval. EXP-004 remains A/PARK.
