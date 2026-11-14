# H2-B: same-footprint cached score-array displacement

Independent implementation by Codex worker `cont_metadata`, completed2026-11-14 01:35UTC. Exact model, token and monetary costs unknown. Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`; no other H2 implementation tree was read. Source SHA256 `6fe9446feddd804c5161d745b63dcfaa959e5b49803b6b29b7c8e2b11049d2ed`. [Patch](change.patch).

The node's former separate leaf Boolean, external Boolean and score-shift bytes become one explicit flags byte: bits0–5 hold shift0..63, bit6 marks a leaf and bit7 marks external ownership. The resulting two bytes hold `uint16_t score_bytes`. The full eight-bit `moved_out` and16-bit `index_resize` fields are preserved. Explicit masks/accessors avoid C bitfield layout assumptions. Compile-time assertions require node24 and leaf-data offset56 on the target ABI; the current64-bit build passes. Other ABIs remain untested.

`zbtScoreLeafOffsets` now reads cached `score_bytes`, so offsets and tags no longer require count×score_bits decoding/rounding during lookup. Packed arrays, records, allocation formulas, member-index semantics and the original leaf match helper remain unchanged. A source comparison confirms the entire original `zbtScoreLeafFindMember` body is unchanged. No H1, scanner, equality, hash, prefetch or batching patch is included.

## State and field audit

| Path | Cache/flag handling |
|---|---|
| Leaf build, including split/merge/rebuild and bulk append | Header is zeroed; leaf flag and shift are installed; count/width determine cache before any array accessor. External-record writes set bit7 without disturbing shift. |
| Re-encoding in-place insertion | New count and width are selected; cache is installed before rewritten arrays are accessed. Shift setter preserves both flags, including an external flag just set by the new record. |
| Fast insertion | Old cache remains valid while old arrays and packed bits are read. Explicit new-array pointers use the already computed new size; count and cache are committed together after movement. |
| In-place deletion | Old cache locates old arrays. Explicit new pointers handle movement; cache is committed with reduced count before return/path updates. |
| Reversed leaves/pop | Reversal changes base/order, not count or width; cache remains valid. Subsequent deletion updates it through the audited deletion path. |
| Position-preserving score update | Width and count stay fixed, so cache stays valid. Any fallback movement/rebuild uses the audited paths. |
| Copy and defrag | Full header/page copying carries cache and flags. All former node-type/external checks now use accessors; no relocation-sensitive pointer is cached. |
| Inner nodes | Existing zero initialization leaves the leaf flag clear. Inner count changes do not maintain the leaf-only cache. |

All four direct leaf count assignments and both score-width assignments were inspected. All direct old `isleaf`, `score_shift` and `has_external` accesses were migrated, including the existing test checker's representation access, without weakening its checks. `moved_out` saturation and resize-ID maintenance are unchanged. A cached displacement's maximum is776 bytes under the current96-member/64-bit limits, well within uint16. A correctness-only oracle checks the cache formula after mutations; no invariant calculation was inserted in the timed lookup path.

## Correctness and code generation

All local execution was correctness-only. No local timing, instruction measurement, profiling or fleet access occurred. No failed builds or tests occurred in this variant.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed,0 failed | [Log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed,0 failed | [Log](qualification/upstream-sanitizer.log) |
| Native fixture verification | All18 cells passed | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture verification | All18 cells passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External-record oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| Focused native metadata oracle | 7,693 tree validations;100,285 leaf checks;54 page relocations;256 flag/shift combinations | [Result](metadata-native.json) |
| Focused ASan/UBSan metadata oracle | Same checks passed | [Result](metadata-sanitizer.json) |
| Frozen fixture output/owned bytes | All36 rows exactly match baseline records | [Result](footprint-check.json) |
| O3 build with `-Werror`; whitespace | Passed | [Binary hashes](local-binary-sha256.txt); `git diff --check` |

The [focused oracle](metadata_oracle.c) tests all shift0..63 values under all four flag combinations, retaining maximal moved_out/index_resize values. Its real trees exercise ascending/descending/equal/wide finite scores, infinity transitions, binary members of12/256/384 bytes, insertion, repeated score movement, deletion/merge, shrink, alternating edge pops, duplication with external ownership, actual page relocation helpers and bulk append. Full tree/index/ordering/ownership checks and leaf-cache checks run after every mutation. It explicitly verifies that zero-width, width64 and reversed leaves were encountered. This complements the supplied optional-output/signed-zero/external oracles.

The existing `qualify.sh` ran unchanged except for redirecting its `LOG=` destination into this variant's `qualification/` directory. [Stdout](qualify.stdout), [stderr](qualify.stderr). Native qualification uses `-O2`; sanitizer qualification uses `-O1 -fsanitize=address,undefined -fno-sanitize-recover=all`. Both supplied oracles used the same sanitizer flags. The focused oracle used native `-O2` and sanitizer `-O1`, plus `-DREDIS_TEST -DREDIS_DEBUG -Wall -Wextra -Werror -g -fno-omit-frame-pointer`, the continuation src/compat/vendor include paths, standalone compatibility source, SipHash and `-lm`. No referee input was changed.

Static inspection of a separate local GCC13.3/x86-64 O3 binary confirms the intended address change: [leaf disassembly](local-leaf-disassembly.txt) loads count at `38c9` and cached uint16 displacement at `38ce` (node offset22), then combines them into tag addresses at `38de`–`38e5`. It does not load score width or multiply/round for those addresses. This is not an ARM performance result; the parent must inspect exact fleet ARM code. The original out-of-line match helper remains, as required by this isolated hypothesis.

## Risks and pending gates

The cache can become stale if a future count/width mutation bypasses maintenance. Packed flags can add masking work to scored lookup, tree navigation and mutation. Same header size and exact correctness fixture footprints do not establish fleet guard results. A useful reduction in address dependency may still fall below the2% primary threshold or lose more than1% on a guard; no acceptance claim is made. Fresh matched ARM measurement, memory checks, profiles, independent confirmation, Intel guards and review remain pending under H2's frozen protocol.

## Consultation and TMA

Own exposed-tool discovery found no `cpu.perf` / `library_status` tools. This worker read the parent's actual shared stdio metadata consultation (`library_status`, `ask`), rather than claiming those calls. Bundled library `deb5a0bac467`,3/287 sources,158 passages,0 vectors; no passage matched the precise metadata hypothesis. The ask supplied NeoverseV2/GCC13/noLTO, the exact address chain, the three independent cache/layout alternatives, native profile localization and fixed speed/guard/memory gates. No unread source is cited as support. The direct source and assembly establish the dependency; controlled fleet measurements must establish whether removing it helps.

| Category | Qualified baseline | H2-B |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No collector ran in this worker session. Earlier CPU-wide labels lack qualification; child categories remain unavailable. Neither static instruction inspection nor hotspot samples supply a pipeline-slot classification.
