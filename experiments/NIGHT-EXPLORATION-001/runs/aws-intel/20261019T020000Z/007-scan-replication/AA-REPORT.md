# Intel original scan A/A — both primary controls qualify

First Intel qualification of this target completed48 same-binary processes and12 ABBA blocks in57.31s, within the fixed300-second cap. Original uninstrumented scan,100K/1M members,16-byte members,5M requested operations,seeds101/102/103 twice. No candidate has been timed and no new implementation population is counted.

| Size | Paired effect range | Minimum window | Qualification |
|---|---:|---:|---|
| 100000 | -0.850..+0.195% | 444.744ms | PASS |
| 1000000 | -0.246..+0.137% | 595.019ms | PASS |

Every block stays within the frozen±1% band and every window exceeds10ms. Audit reconstructs the exact48-row schedule, all12 paired effects, raw CSV identity, serial command boundaries, CPU2 start/end observations, unchanged checksum/actual operation count and exact tree-owned bytes within each block. Original duplicate-emitting scan semantics are preserved; effects use unrounded elapsed_ns/actual emitted operations. No row exclusion, retry, adaptive counts or alternate metric was used.

The timing baseline was freshly built in an isolated8fab511e snapshot using its unchanged Makefile and Clang18.1.3. comparison-freeze.json records exact source/referee/driver/binary hashes and the actual command. Every future variant must compile the same relative source paths and output path under its own isolated snapshot with identical flags/allocator. No sampler is linked into timing. The profile006 executable is separate.

Qualification applies only to these declared scan cases on this Intel host in this session. It does not qualify small/reversed/folded-tag/dense-collision/resize/long-member workloads or other operations, and it does not establish a candidate speedup. Await AMD’s frozen comparison and root decision before any Intel candidate timing. No candidate selection, source adoption or new population follows from controls alone. Raw rows are aa.json and raw/; audit-aa.py produces aa-audit.json.
