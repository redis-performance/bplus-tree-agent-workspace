# H3-C: bounded XOR/OR equality for proven short inline records

Independent implementer `cont_metadata`; completed2026-11-14 01:51UTC. Exact model, token and monetary costs unknown. Base `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`. No other H3 implementation was read. Source SHA256 `d1d8e8211a341a1aeeb488889c7f5b702afef739da682f0c991b41a39e118584`; [patch](change.patch), [manifest](manifest.json).

After the original tag match and external-hash filter, `elelen <= 8 && record[0] == elelen` proves a short inline representation with equal length. The candidate accumulates `record[i+1] ^ ele[i]` into an unsigned OR for `0 <= i < elelen`. Equality is the zero accumulator. Length0 performs no payload/query reads. Every other representation or length follows the original packed decoder, length comparison and memcmp condition. The original successful-match logical mapping and optional-output statements are unchanged.

The patch changes neither the leaf helper boundary nor tag scanning, hashing, layouts, metadata derivation or allocation. It includes no H1/H2 code, explicit SIMD, prefetch or batching. The compiler may vectorize the source loop under the frozen O3 flags; no architecture intrinsic is used.

## Correctness

All execution below was correctness-only; no local measurements, instruction measurements, profiles or fleet activity were performed. No failed candidate tests/builds occurred.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed,0 failed | [Log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed,0 failed | [Log](qualification/upstream-sanitizer.log) |
| Native fixture cells | All18 passed | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture cells | All18 passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External-record oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| Focused native O3 oracle | 231,504 checks passed | [Result](short-native.json) |
| Focused ASan/UBSan oracle | 231,504 checks passed | [Result](short-sanitizer.json) |
| Fixture outputs and tree-owned bytes | All36 rows exactly match frozen baseline records | [Result](footprint-check.json) |
| O3-Werror build and whitespace | Passed | [Binary hashes](local-binary-sha256.txt); `git diff --check` |

The [focused oracle](short_oracle.c) directly exercises the changed leaf helper. Protected mappings place query buffers at both accessible-page boundaries and inline record payloads at the end of their accessible page. Exact-sized allocations under ASan cover all16×16 independent modulo16 payload/query alignments with no readable tail padding. Every length0..8 is tested with all-zero and mixed binary/high-bit content, each possible single-byte mismatch and all four optional-output combinations. Generic inline lengths9,15,16,253,254,255,256,319 receive guarded-boundary/all-mismatch checks too, including unequal-length queries sharing the same prefix.

Forced same-tag candidates use tag0 and255: a generic-length mismatch and a same-length unequal candidate precede the match. Reversed leaves verify physical-to-logical mapping. These are deliberately forced helper-level collision cases, not claims of finding actual SipHash collisions. Artificial external records with lengths0..8 exercise the original fallback even for short query lengths; external320/384 cases also run. Matching and mismatching full hashes with the same high-byte tag verify the existing external filter and untouched failure outputs.

For zero length, the focused inline test can place the query address at a protected-page boundary or allocation end: the specialized helper does not read it. This is a helper-level no-read check, not an extension of the public API to NULL or otherwise unsupported pointer arguments. The record marker remains readable and must equal zero. Supplied oracles retain their signed-zero, reversed, long-inline and real external ownership coverage.

`qualify.sh` ran with only its `LOG=` destination redirected into this variant's `qualification/`; its test commands/referee inputs are unchanged. [Stdout](qualify.stdout), [stderr](qualify.stderr). Both supplied oracles use C11/GCC13.3, `-O1 -g -Wall -Wextra -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`. Focused native uses `-O3`; focused sanitizer uses the same sanitizer flags, adding `-Werror`. All use the continuation src/compat/vendor include paths, standalone compatibility source, SipHash and `-lm`. The native focused guard test therefore checks the O3 optimized comparison as well as the sanitizer build.

## Static mechanism screen

The [local GCC13.3/x86-64 O3 disassembly](local-leaf-disassembly.txt) retains the original out-of-line leaf helper. The short branch at `3de0`/`3ded` checks the bound and actual marker. Zero length branches directly to original output materialization at `3ee8`–`3eeb`. Lengths1–7 become an unrolled scalar XOR/OR chain beginning `3f91`: there is no comparison-loop backedge or generic comparison call in that path. Length8 uses exact eight-byte loads followed by a compiler-generated vector reduction at `3ef7`–`3f65`. The generic memcmp call remains at `3e85` and memchr remains at `3e26`.

Disposition: **locally passes the mechanism screen, conditional on exact ARM codegen**. For the ordinary short lengths, eliminating the generic decoder/call and its preservation work is a plausible reduction; it is not measured here. The unrolled length checks, larger helper body and especially the length8 widening/reduction are credible costs and may make this implementation lose. There is no hidden short comparison loop/call to excuse, but the actual ARM build can still fail the static eligibility screen. If that happens, preserve this artifact as ineligible rather than bundling a different comparator or H1/H2 fix. No relative performance ranking is asserted from these local instructions.

The unchanged2% primary and1% guard/memory gates remain. The parent must inspect exact candidate assembly and use matched fleet controls, profiles, confirmation and Intel guards before any acceptance. The small baseline memcmp self share limits confidence; memchr's larger share is not attributed to this patch.

## Consultation and TMA

Own exposed-tool discovery found no `cpu.perf` / `library_status` tools. This worker read the parent's actual shared stdio `short-consult` library_status/ask responses, not calls made by this worker. The precise ask covered NeoverseV2/GCC13 plus separate GCC15/LTO and Intel cohorts, the actual-marker proof, the three comparators, external filtering and required guard-page/zero/binary/output coverage. Bundled library `deb5a0bac467`,3/287 sources,158 passages,0 vectors; no relevant source passage supports a speedup. Unread leads are not treated as citations. Source safety and emitted code support testing the mechanism, while actual fleet evidence must decide benefit.

| Category | Qualified baseline | H3-C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No collector ran in this worker session; qualified children are also unavailable. Neither hotspot samples nor static code inspection establishes a slot-based resource diagnosis.
