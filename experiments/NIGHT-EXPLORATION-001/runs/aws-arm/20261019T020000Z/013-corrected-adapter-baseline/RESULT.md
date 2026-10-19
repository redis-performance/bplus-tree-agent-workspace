# Corrected adapter ARM baseline complete

All120 serial CPU2 processes /960 rows /40 cells /240 paired operation blocks completed.
Seven validation stages passed, including original43 tests in release and ASan/UBSan.
Timing phase375.6s; owned1800s job completed427.9s, return0.
Exact detached source13e459ff8800be3f02b6b45c87dd7b0c39453fa9. Binary
330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc. Live post-run source/referee/binary hashes match frozen manifest;
the runner also verifies unchanged hashes before completing.

Shared reviewed auditor50d64664a reconstructs the exact schedule, allraw hashes,
operations, paired checksum/memory/traversals/warmups, CPU2 and allsummary metrics.
21/40 cells meet campaign absoluteA/A<=1% and minimum10ms criteria. 11 have a short
window and15 fail precision; these categories overlap. Complete coverage is distinct
from qualification. Unqualified cells remain unsuitable for small optimization claims.

This is a separate corrected-adapter baseline identity, not an old/new speedup,
optimization population, source acceptance or rescue of historical failed controls.
No measurements are pooled across machines. Original8fab sources/builds/results remain
unchanged. Allraw rows/failures and percell effects are retained underresult/.
Root independent review pending. Backend nativeCodex; exact model/cost unknown.
