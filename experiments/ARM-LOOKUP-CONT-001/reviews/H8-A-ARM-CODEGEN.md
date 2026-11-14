# H8-A independent ARM emitted-code audit

Role: execution-owner review, independent of candidate implementation. Read-only audit of actual saved ARM ELF bytes and complete disassembly; no workload execution or performance measurement.

**STATIC ELIGIBLE.** Both actual compiler cohorts retain leaf128-byte and raw176-byte frames. Eligibility admits only a properly qualified screen; it is not a speed or acceptance result.

| Artifact | ELF SHA-256 | Verified instruction words |
|---|---|---:|
|baseline-native|`2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf`|20264|
|baseline-lto|`77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`|12025|
|H8-native|`b4656e11b498f7cce4933c8bd38940c8883fc67a828c87a34b8cbe4caaea1519`|20256|
|H8-lto|`9305171dfab56897a01e2a202ed786700c4ba81793d292c4a5c02b82a5c22316`|12017|

Every four-byte instruction word in the complete saved disassembly was compared with the corresponding PT_LOAD bytes of its actual ELF. All words match. Candidate and baseline hashes match retained build metadata. This establishes the emitted-code identity; it does not measure instructions retired.

| Cohort / function | Entry instruction | Frame bytes |
|---|---|---:|
|native / `zbtScoreLeafFindMember.constprop.0`|`37d0:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|native / `zbtScoreLeafFindMember`|`3950:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|native / `zbtreeScoreRaw`|`c1a0:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|
|native / `zbtreeScoreRawWithHash`|`c994:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|
|lto / `zbtScoreLeafFindMember`|`4032c0:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|lto / `zbtreeScoreRaw`|`405f00:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|
|lto / `zbtreeScoreRaw.constprop.0`|`406800:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|

Native leaf clone at37d0 and general helper at3950 retain their128-byte frames. Ordinary-byte classification is `cmp #253` at3898 /3a1c; the fallback external check is at38a0 /3a24. External full-hash loads and comparisons at3900/3904 and3a98/3a9c reject before pointer loads at390c and3aa4. The target helper at4032c0 uses `cmp #253` at403374, with ordinary branch at403378 and fallback classifier at40337c. External hash4033ec/4033f0 rejects at4033f4 before pointer4033f8.

Ordinary records use one representation comparison instead of two. Extended records retain two; external records add one comparison (one to two), within the frozen allowance and still subject to the external timing guard. The target keeps bounded memchr at40334c and length-guarded variable memcmp at40339c. The outlined call at403430 is the original assertion-failure path, not a runtime decoder. No indirect jump table or whole-leaf inlining appears. Raw and no-score raw remain176 bytes; native prehashed raw also remains176. Source, record layout and output semantics are independently covered by [the source audit](H8-A-CODE.md).

ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable: no qualified candidate pipeline-slot profile exists. Static word counts and frame inspection do not replace these metrics. The controller consultation and its limited retrieved material are recorded in the population selection; this audit makes no new consultation or causal attribution.
