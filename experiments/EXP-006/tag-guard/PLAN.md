# Additional bounded-read regression validation

After fixed comparison (no changed timing or acceptance rule): the exact-first-match
oracle used an oversized accessible array. It checks result semantics but cannot prove
absence of unused beyond-span loads. Add a distinct guard-page oracle: place span0..128
against either boundary of one writable page between inaccessible pages; all256tags,
three deterministic patterns. Run control/A/B/C native+ASan with sameflags;4sources,
2builds. Allsource/refereecomparison evidence unchanged. No timings.

A deliberateC fault changes its n>=16loopguard to n>0; require fault detection rather
than calling the source safe from inspection alone. Preserve original candidatepatches.
No new named boundary campaign count; this is EXP-006regression validation.
Children serial<=120s; finish starting experimental children before05:33UTC.
