# H6-C: inline-length codebook in record descriptors

Independent implementer: record-codebook. Completed2026-11-14 02:38UTC. Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; source SHA256 `bf2cbbe66b36d178692ba214fd192af1b5dc6b1c67f1619e2d782c839b2da825`. [Patch](change.patch), [manifest](manifest.json). Other H6 implementations were not read.

Each existing uint16 offset entry becomes a descriptor with the same size. Its low12 bits are the record address relative to the leaf; its upper nibble follows this injective policy:

| Code | Meaning |
|---|---|
| 0 | Generic record; use the original decoder/hash path |
| 1–9 | Exact inline lengths0–8 respectively |
| 10–15 | Exact inline lengths12,16,24,32,64,128 respectively |

The encoder examines the already-written physical byte-length marker. External marker255 and16-bit-length marker254 always produce code0, including externally represented short members. The decoder is a16-byte constant table, not a fixture-dependent rule. No leaf or index allocation grows.

On a hinted tag match, lookup decodes the exact length from the descriptor and passes `record+1` to the unchanged length/equality condition and memcmp. Unhinted candidates retain the original external full-hash filter, packed decoder, length check and comparison. The original successful-output block, leaf helper boundary, memchr, hash, score stream and fixed score-data address remain. Source comparison confirms the score write/decode region and table finder are unchanged. No H1–H5 patch is included.

## Descriptor and mutation audit

`zbtRecordOffset` masks addresses; `zbtRecordLengthCode` extracts the nibble; `zbtRecordDescriptor` creates descriptors only after record construction; `zbtRecordDescriptorMove` changes addresses while retaining their codes. A compile-time assertion ties the4095-byte leaf limit to12 address bits. Encoder/movement assertions reject unrepresentable addresses; debug checks validate hinted marker/codebook agreement. Debug lookup checks intentionally read the marker for correctness, while the ordinary O3 build removes that debug check and avoids the marker load on hinted hits.

| Consumer or writer | Treatment |
|---|---|
| `zbtScoreLeafOffset` | Returns only decoded low12 bits, preserving every indirect record consumer's original address contract |
| Leaf membership helper | Loads descriptor, masks address, branches on code; generic external/decoder path remains intact |
| Build, split/merge/rebuild, bulk leaf creation | Moves descriptor construction after `zbtBuildElementWrite`, so no uninitialized marker is inspected |
| Re-encoding in-place insertion | `locations[]` explicitly contains decoded addresses; each descriptor is regenerated from its already-written physical record after the score/array rewrite |
| Fast insertion | Existing uint16 descriptors move unchanged with the original memmoves; the new descriptor is encoded after its record write |
| Live record-byte accounting | Every direct offset load is masked before forming a record pointer |
| Delete/compaction | Deleted-record address, record ordering comparisons and adjustment predicates use decoded addresses; movement preserves the original high nibble and asserts the adjusted address fits |
| Reverse-for-pop | Swaps complete uint16 descriptors and tags, so the code follows its physical record |
| Duplicate/defrag | Existing full-page copy carries descriptors; no cached pointer or fixup is added; external records stay generic and retain the original pointer/ownership repair |

The remaining raw uint16 copies/swaps operate on whole descriptors; they never treat descriptor bits as an address or numeric record order. `record_start` stays a plain offset. Temporary decoded locations are never copied directly back into encoded arrays. Allocator usable capacity is still capped at4095 before constructing records. All original allocation/ownership assertions remain.

## Correctness results

All local execution was correctness-only, with no timing, instruction measurement, profiling or fleet access. Candidate correctness executions all pass. Two focused-test build errors are preserved below; neither changed the candidate source.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed,0 failed | [Log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed,0 failed | [Log](qualification/upstream-sanitizer.log) |
| Native fixture cells | All18 passed | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture cells | All18 passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External-record oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| Descriptor boundary oracle, native O3 | 1,414,196 checks passed | [Result](descriptor-native.json) |
| Descriptor boundary oracle, ASan/UBSan | 1,414,196 checks passed | [Result](descriptor-sanitizer.json) |
| Mutation oracle, native O3 | 7,693 validations,53,527 leaf checks,30 page relocations | [Result](mutation-native.json) |
| Mutation oracle, ASan/UBSan | 7,693 validations,53,597 leaf checks,30 page relocations | [Result](mutation-sanitizer.json) |
| Fixture output/owned bytes | All36 rows exactly match frozen baseline records | [Result](footprint-check.json) |
| O3-Werror build and whitespace | Passed | [Binary hashes](local-binary-sha256.txt); `git diff --check` |

The [descriptor oracle](descriptor_oracle.c) tests every code, generic/unlisted lengths and transitions7/8,14/15,253/254,319/320. Query data is placed at both accessible-page boundaries; record payloads end at an inaccessible page while the leaf base remains aligned and relative capacity stays below4095. Exact ASan allocations vary both payload/query addresses over all16×16 alignments for every coded length. Binary/all-zero data, every mismatch position, unequal-length equal prefixes, same-tag0/255 candidates, both physical orders and all four score/position-output combinations run. Externally represented lengths0..8 and the other coded lengths stay generic and reject same-tag/full-hash mismatches;320/384-byte external cases run too. These artificial external-short fixtures validate the physical-format fallback, while ordinary external allocation ownership is exercised by the supplied and mutation tests.

An empty physical record at offset4094 is tested in an actual4095-byte allocation. Descriptor relocation to the maximum representable address4095 is checked arithmetically for every nonzero code without dereferencing a record outside the leaf cap. No overread or padding assumption is added. Zero-length tests use non-NULL query addresses at allocation/page boundaries; they do not widen public API pointer contracts. The unchanged memcmp is still used.

The [mutation oracle](mutation_oracle.c) checks every live descriptor against its physical record after each operation, verifies decoded accessor agreement and record bounds against `min(usable_size,4095)`, and invokes the existing full tree/index/ownership validator. All16 descriptor values, zero/full-width score encodings and reversed leaves are observed. Four score scenarios, mixed coded/uncoded/empty/binary/external members, insertions, score movement/repacking, deletion/compaction, merge/drain, shrink, duplication, actual page relocation helpers and bulk append are exercised. Native and sanitizer leaf-check counts are reported separately; identical allocation/layout behavior across those builds is not assumed. Branch-level coverage counts are not claimed.

Two harness failures are retained: [descriptor link failure](failures/link0.md) omitted the upstream test globals when REDIS_TEST was enabled; [mutation compile failure](failures/mutation-compile0.md) retained a node accessor absent from this baseline. The failed test sources and available compiler diagnostics are preserved. Test-only corrections added the standard globals and used the baseline `node->isleaf` field. No candidate source or referee was changed to make either test pass.

`qualify.sh` ran with only its `LOG=` destination redirected. [Stdout](qualify.stdout), [stderr](qualify.stderr). Supplied sanitizer oracles used C11/GCC13.3, `-O1 -g -Wall -Wextra -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`. Focused native used `-O3`; focused sanitizer used the same sanitizer flags. Both focused oracles added `-DREDIS_TEST -DREDIS_DEBUG -Werror`, continuation src/compat/vendor headers, standalone compatibility source, SipHash and `-lm`. Production codegen was inspected separately without debug-only checks.

## Static mechanism screen and pending risks

In the [local GCC13.3/x86-64 O3 leaf helper](local-leaf-disassembly.txt), `403c` loads the descriptor, `4044` masks its address, and `404d` extracts the nibble. A nonzero code branches at `4051` to the small codebook path (`3ff0`–`4006`), which obtains length from the constant table and reaches the unchanged memcmp at `4089`. It skips the record-header load at `4053`; that load belongs to code0's original generic path. Memchr remains at `401e`, and the leaf helper is still out of line.

Disposition: **small, reviewable codebook; local mechanism present, exact ARM/LTO screen pending**. The hint removes the dependent record-header/format path, but adds a dependent codebook lookup; it does not eliminate every dependent load. Address masking taxes other member consumers, and descriptor encoding/maintenance can tax mutation. The16-byte constant table adds shared read-only program data, with no per-tree storage increase. None of these static facts establishes a gain.

The exact cohort ELF must retain the intended hinted path before timing. Fixed2% primary and1% guard/memory gates remain. Member iteration/rank/churn and boundary/mixed-length guards require their own frozen qualification before adoption; score-only supplemental guards cannot establish those costs. Fresh confirmation, Intel portability, matched profiles and independent review remain pending.

## Consultation and TMA

Session discovery found no exposed cpu-perf/library_status tools. The actual shared controller descriptor consultation, including library status and the exact offset/encoding/mutation question, was read; it is not attributed as a separate implementer invocation. Coverage:3/287 linked sources,158 passages,0 vectors, bundled list `deb5a0bac467`. No matching passage establishes a gain. Detailed participant provenance is retained privately.

| Category | Qualified ARM baseline | H6-C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Qualified ARM child categories remain unavailable. No collector ran in this implementation session; static dependency inspection is not pipeline-slot evidence.
