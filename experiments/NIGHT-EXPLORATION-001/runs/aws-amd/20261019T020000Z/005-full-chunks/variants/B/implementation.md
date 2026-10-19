# Sequential isolated implementation B

Precomputed full-chunk count and indexed loops; tail from remainder; exposes count directly to compiler.

Only insert/delete packed score moves plus optional private helper change. Source reset to exact8fab511e for each snapshot, no stacking. Preserve backwards insert end-alignment, forward delete, out-of-field bits, final inserted value/deleted zero, width0/64, little-endian format. Generic reader/writer unchanged. Packed-move oracle and ASan/UBSan required. A/C may lower identically; binary identity will be disclosed. Same native agent, not independent implementers.
