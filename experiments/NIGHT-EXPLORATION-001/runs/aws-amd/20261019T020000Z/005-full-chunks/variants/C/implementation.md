# Sequential isolated implementation C

Private inline full64-copy helper centralizes compile-time width; peeled loops and generic tail.

Only insert/delete packed score moves plus optional private helper change. Source reset to exact8fab511e for each snapshot, no stacking. Preserve backwards insert end-alignment, forward delete, out-of-field bits, final inserted value/deleted zero, width0/64, little-endian format. Generic reader/writer unchanged. Packed-move oracle and ASan/UBSan required. A/C may lower identically; binary identity will be disclosed. Same native agent, not independent implementers.
