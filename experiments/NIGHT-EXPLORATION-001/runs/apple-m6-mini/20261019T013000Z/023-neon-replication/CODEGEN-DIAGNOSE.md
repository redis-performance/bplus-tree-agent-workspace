# Static native codegen diagnosis

The actual Apple native binaries activate the NEON matcher in all three candidates. Source selection remains **NONE**. This diagnosis uses retained disassembly and read-only Mach-O bytes; no build, workload, timer, profile or new disassembly was run.

| Variant | ScanSlot instruction lines | Entry-prefix stack bytes | `ldr q` | `cmeq.16b` | `shrn.8b` | `cnt`/`addv` |
|---|---:|---:|---:|---:|---:|---:|
| base | 514 | 528 | 0 | 0 | 0 | 0/0 |
| A | 661 | 544 | 2 | 4 | 2 | 2/2 |
| B | 644 | 544 | 2 | 4 | 2 | 0/0 |
| C | 653 | 544 | 2 | 4 | 2 | 2/2 |

Counts cover the complete unique `_zbtIndexScanSlot` body, including cold/assertion branches and other inlined work. They are static inventory, not runtime instruction counts or costs. Stack bytes sum the initial save and subtraction, not a CFG maximum. The baseline has scalar `fmov`; it has no candidate-style NEON byte compare/narrowing sequence.

Each candidate has two direction-specialized vector load/compare/narrow sequences. A/C mask with `0x1111111111111111`, count matches with `cnt.8b`/`addv.8b`, enumerate with `rbit`/`clz` and clear the lowest set bit. B retains full nibbles, enumerates with `rbit`/`clz` and clears each selected nibble with a variable shift and `bics`; it has no population-count pair. All candidates also contain `shl.16b`/`cmlt.16b` normalization before narrowing.

The saved Apple assembly contains register predicate expansion segments of 30 instructions: one `fmov`, fifteen `mov.b` lane transfers and fourteen scalar extracts/shifts, with predicate preparation outside that segment. This is a precisely bounded sequence, not a full-loop count. The prior corrected ARM diagnosis described a different 35-instruction materialization involving stack-byte stores and a halfword reload. The prior ARM rejection does not establish Apple's cost or explain an Apple result.

All variants retain the source eight-byte SWAR residual and zero-to-seven-byte scalar tail. A/B advance vector chunks using word indices; C uses byte offsets. Retained assembly windows in the JSON locate vector and byte-tail regions; this is not a complete control-flow proof. A and C do **not** coalesce: their ScanSlot bodies contain 661 versus 653 instructions and have different actual byte hashes. All six variant pairs have different ScanSlot and whole `__text` hashes.

The JSON independently records actual Mach-O section bounds, raw binary/section/body hashes, source hashes and source helper lines, retained disassembly hashes, opcode counts, mask windows and symbol alias inventories. All four native binaries match `validation/binary-freeze.json`; source C hashes also match the frozen snapshots. Duplicate outlined labels are preserved and are not paired by ordinal. ScanSlot has exactly one retained body per variant. Whole-text identity is not a runtime equivalence claim; linked addresses and assertion line constants can change bytes.

Participant: `/root/followup_proposal_c`, source preparer and independent static timing reviewer; exact original candidate authors remain the frozen cross-host authors. GPT-6/Codex family; exact serving model, token counts and currency cost unknown. No performance prediction, cycle attribution, source adoption or patch repair.
