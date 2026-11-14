# H8-B/C ARM emitted-code admission review

**B: STATIC ELIGIBLE for the original qualified screening protocol. C: NO ADMISSION — target generic-caller coverage is incomplete.** B meets the lookup code-shape gates in both actual ARM toolchains. C meets those same lookup gates, but the target LTO lookup ELF omits iterator, rank and scan consumers required by [H8-selection.md](../H8-selection.md). Native evidence cannot substitute for their target code generation. This is a coverage blocker, not a measured rejection or proof of a C defect.

Role: independent reviewer of B/C; the reviewer implemented H8-A and does not review A here. Read-only source/ELF/disassembly audit. No workload execution, timing, fleet access, source edit, compiler change or publication occurred. Eligibility establishes no speedup and does not waive correctness, A/A, guard, confirmation or independent review requirements.

## Exact identity and assembly validation

Frozen baseline: extraction `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`, source SHA-256 `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`. Rehashed isolated sources match both build cohorts: B `24151adc87c1c7c7262adfc360b2b2e7ae662320050c60f1014889bf7c8f5040`; C `37f5c33a57120e33a5a0203dc05bfb41f9e528cd5dabef934c66335526b2de0e`. Reviewed [B patch](../variants/H8-B/candidate.patch) and [C patch](../variants/H8-C/source.patch); neither stacks earlier mechanisms.

All six actual saved ELF hashes match build metadata. Independently parsed their ELF64 program headers, mapped each disassembled instruction address to its PT_LOAD file offset and compared all four instruction bytes. All96731 machine words match, with zero mismatches. Source association comes from the rehashed source and retained build metadata; byte validation independently establishes that the inspected assembly describes the actual saved ELF.

| Cohort / artifact | Actual ELF SHA-256 | Verified words |
|---|---|---:|
| native base | `2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf` |20264|
| native B | `d5bdbfe282f01bc29ff1520cf75365ac780cf13416e55d764299f7e53d4c6bd6` |20272|
| native C | `47071bd029d907da775dd55c2abaaf41e21f8a21e894f6a596d0904079343174` |20328|
| lto base | `77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb` |12025|
| lto B | `b9789ab86976ff0f29667d8449a92dd08948e9858b38abb62a27b3ad11bcbd35` |11921|
| lto C | `ac80bc78a94591d8ba12209db82d6a8f788e9b38f321389670e3ed320e596068` |11921|

Assembly anchors below identify the exact archived full captures. Candidate line numbers refer to the corresponding `assembly-B.stdout` / `assembly-C.stdout`, including its leading header. Private locations and machine identifiers are unnecessary to reproduce the static reasoning.

| Capture | Assembly SHA-256 |
|---|---|
| native base | `6e71c5dbba16d8192449f76513b16ccaafd92bfd57f62a9dc499a1904fa242a0` |
| native B | `d8ade6fb3b36a1057c65e629c9f922bd88c4ad8fe4fc3d29d072452eea7f2a72` |
| native C | `a1b781858dc1b5863e277a725bd32eec9f19c451521f7f6aab273c768e0a98ac` |
| lto base | `d7a70495c2fa10cc5c5238a605bffc5c464c7a708001244225a7d85fdf840d40` |
| lto B | `313451f017faa1ac42a9d0e186024a9f470a55099c88db124df6d68871a61d09` |
| lto C | `35c328da9bb40957b553b80ce0d25b6ffaf39832465ad66f7bee06c899971054` |

The published [native baseline](../H2-profiles/arm-native-base/assembly.stdout) and [LTO baseline](../H2-profiles/arm-gcc15-lto-base/assembly.stdout) supply the original code. Private provenance retains the byte-verification records.

## Ordinary classifier, external ordering and bounded equality

| Capture / helper | Header load → sole ordinary classifier | Necessary fallback classifier | External hash reject → pointer load | memchr / memcmp |
|---|---|---|---|---|
| Native B clone |`2784 → 2788` (`CMP253`), lines1903–1904|`2790` (`CMP254`)|`2798` load hash, `279c/27a0` compare/reject → `27a4` pointer|`2764 /27c0`|
| Native B general |`2918 → 291c`, lines2006–2007|`2924`|`292c`, `2930/2934` → `2938`|`28f8 /2954`|
| Native C clone |`2ccc → 2cd0`, lines2245–2246|`2c70` reached only from `2cd4 B.HI`|`2c78`, `2c7c/2c80` → `2c84`|`2cac /2cf0`|
| Native C general |`2e38 → 2e40`, lines2338–2340|`2e48`|`2e50`, `2e54/2e58` → `2e5c`|`2e18 /2e74`|
| LTO B |`404c70 → 404c74`, lines4426–4427|`404c7c`|`404c84`, `404c88/404c8c` → `404c90`|`404c4c /404cb0`|
| LTO C |`404c70 → 404c74`, lines4426–4427|`404c7c`|`404c84`, `404c88/404c8c` → `404c90`|`404c4c /404cac`|

Every ordinary record byte0–253 is loaded by the original one-byte load and takes exactly one representation comparison before the existing length comparison. B's native clone branches to the common ordinary decode; C's clone falls through. This is layout, not a difference in domain coverage. No subsequent external/extended marker check or nullable-result test survives on the ordinary path. Length0 stays valid; the variable memcmp receives zero only after the unchanged length-equality check.

The complete representation comparison count is:

| Physical representation | Baseline | B/C | Delta |
|---|---:|---:|---:|
| Ordinary0–253 |2|1|−1|
| Extended-inline254 |2|2|0|
| External255 |1|2|+1|

Thus the external case adds exactly one necessary classifier, within the frozen static allowance; it is not a redundant marker chain. There is no header255 retest after proving the range is254/255 and excluding254. The unchanged1% external guard remains binding.

Extended paths retain a bounded two-byte length load at record+1 and payload record+3: native B `2800–2804` / `29a4–29a8`, native C `2d30–2d34` / `2ec4–2ec8`, LTO B `404d00–404d04`, C `404cfc–404d00`. External lookup first loads the original four-byte full hash at+1; mismatches branch back to the next-tag search **before** any pointer read or nonnull assertion. Matching hashes alone reach the original eight-byte pointer at+13, nonnull assertion, then eight-byte length at+5. No new/wider record load appears.

memchr still searches the remaining bounded tag range and advances by found+1 after rejection. memcmp remains a variable-length library call guarded by stored/query length equality. Payload address selection and original score/logical-position output blocks remain. Source patches do not change those outputs; the emitted helpers retain their score and position writes. There is no indirect jump table and no checked-decoder call in any lookup helper. Only original calls to memchr, memcmp, score extraction and the assertion panic appear.

The symbol `zbtPackedDataChecked.part.0` in C is **not a runtime checked decoder**: native `2660–267c` and LTO `4031e8` are the outlined, nonreturning null-pointer assertion failure path, equivalent to baseline `zbtPackedData.part.0`. It contains no record classification or optional-hash dispatch. The actual decoding is naturally inlined.

## Leaf boundaries and all actual raw frames

| Reader | Baseline frame | Native B entry / line / frame | Native C entry / line / frame |
|---|---:|---|---|
| Leaf clone |128|`26c0` /1854 /128|`2bf0` /2190 /128|
| General leaf |128|`2850` /1956 /128|`2d80` /2292 /128|
| Raw |176|`c1e0` /11894 /176|`c0f0` /11834 /176|
| Prehashed raw |176|`c9d4` /12407 /176|`c8e4` /12347 /176|

| Target LTO reader | Baseline entry / frame | B and C entry / line / frame |
|---|---|---|
| Leaf |`404bc0` /128|`404bc0` /4382 /128|
| General raw |`405f20` /176|`405f20` /5642 /176|
| No-score raw clone |`406820` /176|`406820` /6220 /176|

No additional raw/leaf stack subtraction changes these totals. Native raw and prehashed functions still call the leaf clone; both target raw functions still call the leaf helper. Hashing, index probing, rehash-step and assertions remain separate calls with the original boundaries. The LTO lookup artifact has no separate prehashed raw symbol; every actual retained raw function was inspected. There is no whole-leaf inlining or new runtime decoder boundary.

## C generic consumers: evidence and explicit gap

The source passes literal NULL through the original `zbtPackedData` wrapper. The following actual **native** generic paths remove optional expected-hash validation: ordinary comparison is followed by the extended test and then directly by external pointer/non-null/length loads. No external hash eligibility comparison intervenes.

| Consumer | Actual generic decode PCs |
|---|---|
| Member-returning iterator |`zbtreeIteratorNext`: ordinary `13c68`, extended `13c70`, pointer `13c78`, length `13c80`; lines19784–19790. Both directions share this decode before advancement. |
| Lexical seek with optional rank output |`zbtreeIteratorSeekLex`: `13974`, `1397c`, pointer `13984`, length `1398c`; lines19591–19597. |
| Build from live leaf |`zbtBuildElementFromLeaf`: `3a80`, `3a88`, pointer `3a90`, length `3a98`; lines3138–3144. |
| Scan callbacks |`zbtIndexScanSlot`: `55d4/55dc/55e4` and `565c/5664/566c`; clone `6bd8/6be0/6be8` and `6c5c/6c64/6c6c`. |

The later external-marker check and hash load in the build consumer preserve existing ownership/build-entry bookkeeping; they are not optional expected-hash validation. Likewise the normal member-to-rank API legitimately uses the checked leaf lookup; numeric rank traversal itself does not decode a member, while member retrieval after seek-rank uses IteratorNext. These distinctions prevent counting necessary behavior as a failed optimization.

Target C retains `zbtBuildElementFromLeaf` and its leaf-build callers. Its ordinary classifier `403258`, extended classifier `403260`, pointer `403268`, assertion `40326c`, and length `403270` (lines2732–2738) show the optional validation eliminated there too. However, the actual target lookup ELF retains **no iterator, rank or scan symbols/caller paths**. Their omission through whole-program optimization is not evidence that optional checks disappear when those operations are built and used.

Accordingly C has **no timing admission from this audit**. Resolving it requires separately retained actual native/target consumer executables covering member-returning forward/reverse iteration, rank/seek member use, build and scan, with the same source/compiler/flags, verified binary/disassembly identities, and inspection of each generic decode. Do not alter the lookup fixture or use forced retention/optimization flags to make the measured binary pass. No such supplemental build or execution was performed here. Native C text growth also deserves affected-operation review; it is not alone declared disproportionate by an invented threshold.

## Footprint and admission limits

| ELF | text bytes | Delta from cohort baseline | data /bss |
|---|---:|---:|---:|
| Native baseline |95143|—|856 /40|
| Native B |95143|0|856 /40|
| Native C |95559|+416|856 /40|
| LTO baseline |56539|—|744 /40|
| LTO B |56091|−448|744 /40|
| LTO C |56091|−448|744 /40|

No record/leaf/index layout change is present. Text-size equality or reduction is not a measured latency improvement. This review does not repeat the retained correctness oracles. B is eligible only for the frozen, properly qualified screen; external/extended/collision guards can still reject it. C remains blocked on generic target coverage. Neither result is acceptance or a measured population outcome.

## TMA classification and consultation

| Pipeline category | Qualified ARM baseline | B | C |
|---|---|---|---|
| Frontend_Bound and children |Unavailable|Unavailable|Unavailable|
| Bad_Speculation and children |Unavailable|Unavailable|Unavailable|
| Backend_Bound and children |Unavailable|Unavailable|Unavailable|
| Retiring and children |Unavailable|Unavailable|Unavailable|

The saved ARM collector scope/formulas remain unqualified, and this static audit collected no candidate profiles. Classifier counts cannot supply a100% pipeline-slot decomposition. Independent Intel categories do not fill the ARM gap.

Current-session tool discovery exposed no callable cpu-perf/library_status endpoint. The actual controller mask-classifier consultation in [H8-selection.md](../H8-selection.md) is shared provenance, not this reviewer's call:3/287 indexed sources,158 passages, one unrelated register/stack-sampling passage. It establishes neither speed nor causality. Static eligibility and the C coverage blocker follow the frozen gates and byte-verified emitted code. Detailed provenance stays private; exact model/token cost is unknown.
