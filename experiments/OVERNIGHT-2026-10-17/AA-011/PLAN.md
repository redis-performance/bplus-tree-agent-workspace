# AA-011 — compact-history precision qualification

Preregistered before any timing. Use frozen HARNESS-006 baseline release binary and
unchanged source/allocator/compiler flags. Apple M1 arm64, Apple Clang17, C11 -O3 -g
-Wall -Wextra -fno-omit-frame-pointer; one unpinned thread. Frequency, within-window
migration and effective QoS unknown. Boundary CPU IDs and thread time are descriptive.

Eight cells, all n95, 20m requested items rounded up to whole traversals, three warmups:
integer trimmed forward mask0; integer trimmed forward mask4; integer trimmed reverse4;
integer trimmed-cycle forward4; alternating-zero trimmed forward4; alternating-zero
trimmed reverse4; alternating-zero trimmed forward6; wide trimmed forward7 bytes320.
All other cells bytes16. Seeds41031/41043. Six ABBA blocks per cell/seed, rotated cells
and seed order by block =384 rows. One prospective 1m-item whole-binary warmup retained.
All children <=120s; total600s. Complete fixed schedule or PARK incomplete cells.

Wall ns/effective item primary. Per block100*(meanB/meanA-1);95%t df5 must lie wholly
within[-1,+1]%,every wall window>=10ms, exact semantic/checksum/effective-count/unchanged
memory/fingerprint invariants. Both seeds must qualify for a new guard. Retain all rows,
no exclusions or optional stopping, no threshold changes. Normal-independent-block
assumption remains a limitation. Report thread effects separately. No timing from sampler
or source-included structural binaries. No builds/tests/agent computation during timing.

New compact cells add coverage, cannot replace any original unqualified guard or primary.
No acceptance from this qualification alone. No unchanged failed duration/QoS retry.
