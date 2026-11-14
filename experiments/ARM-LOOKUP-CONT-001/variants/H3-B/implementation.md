# H3-B: constant-size short-inline comparisons

Status: implemented and correctness PASS; performance selection NONE. Independent implementer: implementer `cont_tags`; other H3 implementation trees were not read. Exact model, token accounting and monetary cost are unknown. No commit, push, fleet access or local performance measurement was performed.

Baseline: `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. Source SHA256: `5119e918762b2ca1a1943335c2b0729f48f72d5d7d0122a78aa4e0e1dbca8700`. [candidate.patch](candidate.patch) SHA256: `741215369e55f08de207d183f8a8ac10f7d880945499b5e286eb74639f3c6c8e`. Source/referee/binary hashes are recorded in [manifest.json](manifest.json).

## Implementation and scope

After the original tag match and external full-hash filter, the leaf helper tests `elelen <= 8 && record[0] == elelen`. This proves the actual record is short inline and has the exact query length. A switch uses `memcmp(record+1, ele, N) == 0` with constant N for each length1..8; length0 returns equality without reading either payload. The generic branch retains the original packed decoder, exact length test and variable-length memcmp. It remains necessary for mismatching inline lengths, 16-bit-length records, long inline members and all external representations, including preserved external short members.

Only this comparison region changes. [scope-audit.json](scope-audit.json) verifies byte-identical source outside the leaf helper body, an unchanged leaf prefix through external filtering, and an unchanged successful-output block and loop tail. Helper declarations/boundaries, scanner, metadata layout, hash function, allocator, record encoding and physical/logical result mapping remain the baseline source. There is no H1/H2 combination, cached position, prefetch, batching or explicit SIMD.

Zero length is defined here as exact equality for a proven inline zero-length record. The direct-helper oracle uses non-NULL pointers, including an address at an inaccessible-page boundary, and verifies zero payload access. It does not claim that NULL is now a supported input to public raw hashing APIs. The record's length marker itself must remain readable.

## Correctness

Compiler: GCC13.3.0, Ubuntu `13.3.0-6ubuntu2~24.04.1`. All commands completed with exit0, no warnings and empty stderr. No failed attempts occurred. [run-correctness.sh](run-correctness.sh) reproduces the completed command sequence; no timing modes are invoked.

| Check | Result |
|---|---|
| Upstream suite native O2 / ASan+UBSan O1 | 57/57 +57/57 PASS |
| Existing correctness fixtures | 18 native +18 sanitizer PASS; six cases × seeds17/29/43 |
| Supplied optional-output oracle, ASan+UBSan | 90,000 PASS |
| Supplied external-record output oracle, ASan+UBSan | 45,000 PASS |
| New short oracle on H3-B, native and ASan+UBSan | 719,716 checks per run PASS |
| Same new oracle on unchanged baseline, native and ASan+UBSan | 719,716 checks per run PASS |

Each focused run contains17,496 guarded short cases,9 exact heap-range cases,36 collision chains and11 generic boundary-length cases. It covers:

- Every length0..8; all-zero, all-255 and mixed zero/high-bit byte patterns; every differing byte position on both stored and query sides; length mismatch with matching prefix.
- Independent query/record alignment residues0..15, query buffers immediately after/before inaccessible pages, stored payloads ending immediately before an inaccessible page, and stored markers immediately after an inaccessible page. Each call checks all four optional score/position output combinations. Misses preserve sentinel outputs; hits preserve the exact signed-zero score.
- Exact-size heap allocations for query bytes and the complete inline record at the end of its leaf allocation, allowing ASan to catch sub-page overreads. The required one-byte stored marker is accessible; it cannot simultaneously be protected as if it were outside the record. Therefore the dynamic leading guard is before the marker, while the compiler load-interval audit below proves the comparison itself starts at the payload. Guard pages alone are not claimed to detect a masked one-byte read of that marker.
- Tag values0/255, empty/singleton leaves, both physical orientations, same-tag longer and shorter records before a match, same-length unequal candidates, and same-full-hash unequal external candidates. A different full hash with the same tag points to an inaccessible payload, proving the existing rejection happens before dereference. Synthetic valid external short records, including length0, must still succeed through the generic fallback. Hashes are deliberately supplied to exercise collision logic; no timed fixture or source shortcut uses them.
- Generic lengths9/15/16/253/254/255/256/319/320/321/384, both-side mismatches at every byte and guarded range ends. The fixture asserts short/16-bit marker boundaries;320+ uses external records. The256-byte case is inline. Existing suites/oracles additionally retain mutation, split/merge, rank/iteration, reversed-leaf and external ownership coverage.

Native and sanitizer allocator accounting are not compared across builds or used as local performance acceptance evidence.

## Static feasibility and explicit code-growth risk

The inspected binary is the controller's matched GCC13/O2, no-LTO **correctness** lookup build, not the ARM measurement ELF. [Leaf disassembly](local-leaf-assembly.txt) and [switch table](local-switch-table.txt) establish that each selected constant-size comparison is compiled into bounded loads, with no memcmp call on that comparison path. The generic fallback retains memcmp at `0x41ed`; the leaf helper remains out of line. Length dispatch is an indirect jump through a36-byte table.

The table entries and memory intervals for **each operand**, relative to its payload/query start, are:

| Length | Switch destination | Loaded byte intervals |
|---:|---|---|
| 0 | `0x41fe` | none |
| 1 | `0x4360` | `[0,1)` |
| 2 | `0x4338` | `[0,2)` |
| 3 | `0x4310` | `[0,2)`, `[2,3)` |
| 4 | `0x4378` | `[0,4)` |
| 5 | `0x42e8` | `[0,4)`, `[4,5)` |
| 6 | `0x42c0` | `[0,4)`, `[4,6)` |
| 7 | `0x4298` | `[0,4)`, `[3,7)` |
| 8 | `0x43f8` | `[0,8)` |

Every interval is within the proven byte length; no terminator, alignment padding or adjacent record byte is required. The source uses standard constant-size memcmp equality and imposes no aligned typed-load assumptions. Other compiler/architecture cohorts must independently verify their generated accesses.

There is substantial code growth: matching local symbol metadata gives the baseline helper393 bytes (`0x189`) and H3-B925 bytes (`0x39d`), recorded in the two symbol artifacts. GCC also duplicates tag-loop paths for lengths4/8, despite unchanged scanner source. Those bytes, the indirect dispatch and generic-path branching can cost more than the removed call/decoder work. Static inspection establishes a plausible changed mechanism, not a speedup or superiority over another variant. No instruction-count or timing measurement was collected. Exact ARM/native, ARM/LTO and Intel code generation and qualified comparisons remain separate chair gates.

The shared fresh native profile places only2.82% of whole-process sample period in named memcmp; this variant cannot claim the23.30% historical memchr share as removable work. Unchanged ≥2% primary-per-block and ≤1% guard/memory thresholds still apply. Neither eliminated calls nor passing correctness selects a winner.

## Consultation provenance and TMA

Own fresh tool discovery found no callable `cpu-perf` or `library_status` tools. The coordinator's actual `short-consult/ask` stdio response is shared evidence, not this worker's invocation. Its question explicitly covers the three bounded short-inline spellings, exact source/native profile, preserved memchr/external filter/layout/helper boundary, binary/guard-page/output cases and independent compiler cohorts. Coverage is3/287 linked sources and158 passages, keyword only; no supporting source passage matched. Unread related sources support no claim here.

| Pipeline-slot category | Baseline | H3-B |
|---|---|---|
| Frontend_Bound | Unavailable: no qualified workload-isolated/formula-qualified funnel | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Qualified children are also unavailable. Function samples and static code sizes are not substituted for pipeline-slot shares. Fleet comparison, matched profiles, fresh confirmation and independent review remain outstanding.
