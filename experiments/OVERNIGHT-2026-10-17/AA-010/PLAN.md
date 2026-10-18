# AA-010 — preregistered HARNESS-005 qualification

Frozen HARNESS-005 baseline release binary/source hashes. M1 arm64/macOS26.3, Apple
Clang17 C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer,libc,one unpinned thread.
Clock/frequency/effective QoS and within-window migration unknown. No M4 transfer.

Eight fixed cells, all n100000,bytes16,20m effective items,3warmup traversals:
integer ascending forward mask4; integer descending forward mask4;
integer descending reverse mask4; alternating-zero ascending forward mask4;
alternating-zero descending forward mask4; alternating-zero descending reverse mask4;
alternating-zero descending forward mask6 and mask7. Seeds31031 and31043.
Six serial ABBA blocks per cell/seed, rotated cells and seed order by block:384rows.
One prospective1mitem whole-binary warmup, kept separately. No row exclusions,
thresholdchanges or optional stopping. All children120s; total budget600s. If a child
fails or budget expires, preserve partial rows and PARK incomplete cells.

Wall ns/effective item primary. Each block100*(meanB/meanA-1);95%t df5 interval must
be entirely[-1,+1]%, every window>=10ms, all count/checksum/exact oracle/owned memory/
fingerprint/seed/construction invariants hold. Treat normal-independent-block assumption
as a limitation. Thread-time interval and wall/thread ratios/CPU boundary IDs reported
only as scheduling observations. Cannot infer stable frequency from them.

Both seeds must qualify for a cell to be used as new EXP-004 performance guard. Otherwise
PARK it. This fixture changes checksum code and does not replace/qualify original mask6.
No source acceptance from new guards alone. No builds/tests/agents during measurements.
