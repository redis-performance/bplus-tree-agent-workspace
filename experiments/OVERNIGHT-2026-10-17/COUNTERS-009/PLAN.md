# COUNTERS-009 — natural mixed-width cursor/relocation execution counts

Separate diagnostic, no timing/profile-hotness/speed claim. Four fixed serial whole-
oracle captures after BOUNDARY-023 matrices complete: baseline seed65521; relocation
extension seed66509 modes0/1/2. Production/control and all fixture code copied from
successful frozen snapshots, -O1/debug with LLVM instrumentation only.120schildren,
600swhole budget. No tests/builds concurrently with captures. Preserve raw profraw,
profdata and JSON export under ignored scratch with hashes; curate symbol/branch
counts resolving each branch file ID correctly (including macros).

Require every existing C invariant and PASS, including actual natural narrow→wide
transition at nonzero cursor, incomplete then complete migration. Relocation captures
must retain original fixture counters; no pre-encoded IDs. Require positive wide/narrow
ID-read branches, active dual-table scan, and resize completion. Clone mode must reach
active-rehash duplication; both defrag modes must reach active-rehash allocations and
leaf registry repairs, with the declined-return branch present in mode2. Exact static
line mappings fixed from source after inspection before reading results, not chosen
by the largest count. No comparison of count differences as speed or process time.
Failed/incomplete captures remain. Source NONE/PARK unchanged; additional diagnostic
only upon successful verification, no new optimization population.
