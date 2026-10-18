# Static decoder loop inventory

The two `.s` files are excerpts of `decoder_batch` from the release build's generated
assembly. Debug-location, CFI and DEBUG_VALUE lines were removed, and trailing
whitespace trimmed. They are for inspection, not standalone assembly units.
`summary.json` records both full assembly and excerpt hashes.

The baseline has 252 static instruction lines and 29 conditional branches; A has
247 and 24. Both retain packed loads and nested round/leaf/position loops; neither
contains a direct call. These counts include all paths and are not dynamic executed
instructions, CPU cycles, cache misses or a performance prediction.

Rebuild full assembly with `make decoder`; inspect
`build/decoder/{base,A}/kernel.s`. Compiler versions and build paths can change
assembly text/hashes. Recorded timing binaries are identified by `local-m1/build.json`.
