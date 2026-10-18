# AA-012 — public batched lookup qualification

Preregistered before any measurement; only run after HARNESS-007attempt002 passes
all validation and sensitivity controls. Exact frozen baseline source, allocator,
Apple Clang17 flags C11O3-g-Wall-Wextra-Werror-fno-omit-frame-pointer-DREDIS_DEBUG.
Local Apple M1 arm64, one unpinned thread, actual core/frequency/effective QoS unknown.
Wall ns/requested member is primary; thread time and boundary IDs are explanatory only.
Timed scope includes batch assembly, API call, exact hit-mask check and checksum.

Five cells: hit16bytes/batch16 (primary); hit16bytes/batch1; hit320bytes/batch16;
miss16bytes/batch16; mixed16bytes/batch16. n8192, exactly2million requested members
per process,3fixed warmup passes. Seeds80703/query80719 and80711/query80723.
Six ABBA blocks per cell/seed, same binary for A and B, rotate cell order byblock
and alternate seed order byblock:240rows total. One prospective warmup100koperations
on primary/first seed, retained but excluded beforehand. All children serial<=120s,
wholetrial360s. Complete schedule or PARK incomplete, no optional stopping/exclusions.
No builds, tests, profiles, agent tasks or coordinator analysis during measured runs.

For each cell/seed, block effect100*(meanB/meanA-1). Two-sided95%t(df5) interval
must fit wholly in[-1,+1]%, every measured wall interval>=10ms, all count/checksum/
mask/fixture/memory invariants pass. Use unrounded elapsed_ns/effective operations.
Both seeds must pass for joint qualification. Thread effects separately computed,
never substituted. Normal independent-block assumptions are limitations. No source
comparison authorized by failed cells; qualification does not replace any original guard.
No thresholds/blocks/counts changed after outcomes. Preserve every row and stderr.
