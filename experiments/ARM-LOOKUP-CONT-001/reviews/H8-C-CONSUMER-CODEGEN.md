# H8-C supplemental target consumer code-generation review

**Decision: STATIC ELIGIBLE.** The additional actual ARM GCC15/LTO consumer binaries close the coverage blocker in [H8-B/C ARM review](H8-BC-ARM-CODEGEN.md). That earlier report remains unchanged: its no-admission decision accurately describes the lookup-only evidence available then. This supplement establishes code-generation eligibility, not correctness requalification, measured improvement or acceptance.

Role: independent C reviewer; previously implemented A, not C. The reviewer also authored the descriptor guard harness earlier; this is not an independent review of that harness design. Offline inspection only. No workload execution, timing, fleet access, source modification or publication occurred in this review. The controller's saved commands are six successful compiler invocations, not consumer executions.

## Provenance and exact byte joins

The build-only metadata pins target image `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`. All six recorded commands use that image with `-flto=auto -std=c11 -O3 -g -Wall -Wextra -Werror -fno-omit-frame-pointer`; no new retention, inlining or optimization flag was added. All return codes are0. The three actual harness C files and three build scripts independently rehash to all six metadata entries. Baseline and C source identities remain respectively `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9` and `37f5c33a57120e33a5a0203dc05bfb41f9e528cd5dabef934c66335526b2de0e`, as verified in the preceding review and repeated in these build records.

Every saved actual ELF rehash matches metadata. Mapping all disassembled instruction addresses through ELF64 PT_LOAD segments and comparing the four little-endian instruction bytes verifies **72786 words, zero mismatches**. These are actual executable bytes, not source-generated assembly predictions.

| Consumer / variant | ELF SHA-256 | Verified words |
|---|---|---:|
|guards-base|`b5bfd9166d5bd7d7b2a720f8177a9a8f8e755a5f314c8a547248ca304bc9a146`|15451|
|guards-C|`6ebd31b5bad22eda53b15322fca7fc4fbc9d2736badd3e9aced4cab359883150`|15323|
|descriptor-guards-base|`40ef576e393e6f8822d4acedcde9214c6b81586349c71bcbc2da0bd6dadfbabe`|8034|
|descriptor-guards-C|`89917951f6d7a7d08f23e19e35acd878c454f52915119c5bbc9db903986b36a4`|8034|
|index-guards-base|`b271dcfbe6c48ab94072f800773afb8e2b964a468a6acfc9749aeeaa3a8dfcdf`|13023|
|index-guards-C|`4ba4f949f1893f9b87bb006a1b32647a859a8ff0f5e8bccb4127d697ad46252c`|12921|

Exact archived assembly anchors follow. PCs and one-based lines below refer to the corresponding complete `<consumer>-<variant>-objdump.stdout` capture. Private capture paths are retained separately.

| Capture | Assembly SHA-256 |
|---|---|
|guards-base|`dfebe2bcc091d058b2f80d6c394c9b9ee156cd6b48d384b3e1fa6ff7fb11a0ad`|
|guards-C|`ad4f51b77bf24476ecbcbbb1b0499eda91b2fa8413b4454de85084bcbf519425`|
|descriptor-guards-base|`c7cbe1d90c323e499262e3be095434eb4c0a03aecd433b574c49216f20fd6bba`|
|descriptor-guards-C|`01592b153c26babe9436e24b6bb219dcd199fb94c99990c6534ddb6867c7d2ec`|
|index-guards-base|`9235eafc536f9373bc70202614fc05e65f7bc6c06f234c7e8aae7f292ca9b851`|
|index-guards-C|`5e5c231e6ff48e21b4d1728256c54dacc73e2d652ab2875ec5ff89be5f186933`|

## Generic consumers now present

**Forward/reverse member iteration:** in descriptor-guards C, `run` contains both inlined member-returning iterator directions. Reverse decode loads the header at `408270`, compares253 at `408274`, then254 at `40827c`, and directly loads pointer/non-null/length at `408284/408288/40828c` (lines7874–7881). Forward decode loads the header at `4083fc`, compares253 at `408400`, and branches only for the fallback to `40833c`'s254 comparison; pointer/non-null/length are `408344/408348/40834c` (lines7925–7929). Both ordinary paths skip the fallback. Extended payloads retain the two-byte lengths and+3 address at `408410–408420`. Neither path loads an external hash or tests an optional expected-hash pointer. The generic decode is naturally inlined; no decoder call appears. Comparing the baseline/C `run` bodies confirms the same272 instructions, with only ten differing lines: initialization scheduling and cold diagnostic address/line constants, rather than a new hash-validation chain.

**Rank:** guards C retains both `zbtreeRank` and `.constprop.1`, including current/rehash and narrow/wide leaf lookups. Rank is a member-lookup operation and legitimately passes the member hash into the checked leaf helper; it is not a no-hash decoder consumer. Calls at `409334/409534/409764/409954` and `40b118/40b324/40b5b8/40b740` reach `406080 <zbtScoreLeafFindMember>`. Numeric rank accumulation does not need another member decode. Member retrieval through the iterator is independently covered above. Required lookup validation is therefore retained while generic decoding has no spurious optional validation. Both rank frames remain208 bytes.

**Scan:** index-guards C retains both scan-slot clones and the scan-group caller. Generic external decoding has no expected-hash test. Clone1's two output paths use header/range/extended/pointer at `4059f0/4059f8/405a00/405a08` (lines5278–5284) and `405a74/405a78/405a80/405a88` (lines5311–5316). Clone0's pointer loads `406040` and `4060c0` have the same direct range/extended/pointer shape. Lengths are read at+5 after nonnull validation; ordinary payloads remain+1 and extended payloads+3. Original callbacks remain calls, e.g. `405a30/405aa8`. Scan tag traversal, bounds and callback boundaries are not replaced by a runtime decoder.

**Build:** guards C retains `zbtBuildElementFromLeaf` at `40454c`; index-guards C retains it at `403244`. Guards header/range/extended/pointer/null/length sequence is `404598/40459c/4045a4/4045ac/4045b0/4045b4` (lines3937–3943). No expected-hash test survives. The later `CMP255` and external hash load `4045c8/4045d4` fill the existing build entry's hash/ownership metadata; they are not a redundant lookup classifier or optional rejection. In these artifacts the compiler retains the existing build helper as a callable routine where the baseline could inline it. This is a code-layout/call-placement change to disclose and guard, not a runtime checked-decoder call. The successful helper has no stack allocation; its only cold failure reaches the original pointer assertion. Both leaf-build variants keep80-/128-byte frames.

No generic external decoder is required to reject a hash: its expected hash is absent by design. Demanding a hash comparison before its pointer load would reinstate precisely the optional work C must eliminate.

## Checked lookup paths and frame/call gates

The retained checked leaf helper in each consumer still has one ordinary0–253 classifier, one additional necessary external/extended distinction, and the full-hash rejection before pointer access:

| C consumer | Ordinary / extended classifier | Hash load / compare / reject | Pointer / nonnull / length | memchr / memcmp |
|---|---|---|---|---|
| guards |`406134 /40613c`|`406144 /406148 /40614c`|`406150 /406154 /406158`|`40610c /40616c`|
| descriptor-guards |`406634 /40663c`|`406644 /406648 /40664c`|`406650 /406654 /406658`|`40660c /40666c`|
| index-guards |`404e14 /404e1c`|`404e24 /404e28 /404e2c`|`404e30 /404e34 /404e38`|`404dec /404e4c`|

No lookup pointer read precedes the rejecting branch. The variable memcmp remains length-equality guarded, and memchr retains its bounded remaining-tag length. No checked-decoder call, indirect classifier jump or duplicate marker chain is emitted. The only `zbtPackedDataChecked.part.0` symbol is the nonreturning assertion-failure routine already explained in the preceding review.

| Inspected frame | Baseline → C |
|---|---:|
| Leaf find, all three consumers |128 →128|
| Raw reader and actual no-score clones |176 →176|
| Rank and rank clone |208 →208|
| Scan-slot clones1 /0 |528 /512 →528 /512|
| Scan-group clone |128 →128|
| Leaf-build variants |80 /128 →80 /128|
| Descriptor `run` |160 →160|
| Main guards `run_guard` |432 →432|

Examples: guards general/raw-clone entries move from `409d60/40a660` to `409ea0/40a7a0`, both retaining `stp ... #-176`; index scan entries move from `405928/406028` to `4054e8/405be8`, retaining `sub sp,#0x210/#0x200`. Original raw-to-leaf and rank-to-leaf call boundaries remain. No source or ABI change is needed to obtain this result.

## Footprint and bounded decision

| Consumer | Baseline text | C text | Delta | data/bss, unchanged |
|---|---:|---:|---:|---:|
| guards |70507|70087|−420|752 /40|
| descriptor-guards |38880|38848|−32|744 /40|
| index-guards |62182|61846|−336|760 /17008|

The saved consumer ELFs show no disproportionate text expansion. These section sizes and frame checks are static evidence only. The supplemental binaries have not been executed as part of this build-only capture; this audit neither invents correctness outputs nor treats them as qualified timing artifacts. C may now enter the frozen H8 screening protocol, with the original external/extended and affected-operation guards binding. Its scope remains broader than A/B and its build-helper placement remains a regression risk to measure, not a reason to relax the gates.

## TMA and consultation limits

Qualified ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and every child remain **unavailable** for baseline/C: the historical collector scope/formulas are unqualified and these builds contain no new profile collection. Static instruction/stack observations cannot supply pipeline percentages. No performance improvement is claimed.

Current-session discovery exposed no callable cpu-perf/library_status endpoint. The actual shared H8 consultation, recorded in [H8-selection.md](../H8-selection.md), remains the limited3/287-source,158-passage consultation with an unrelated sampling passage. It is not this reviewer's call or evidence of speed. This supplement resolves the concrete emitted-caller coverage gap using the saved binaries. Exact model/token cost is unknown; detailed provenance remains private.
