# Fresh corrected-baseline codegen review A

PASS for source identity, retained validation summary and the requested static mechanism observation. The physical→logical→physical conversion sequence remains present in the **fresh corrected-adapter native release**, not merely in historical004 assembly. This establishes an emitted source/compiler mechanism, not a bottleneck, cost, speed prediction or selected hypothesis. Fresh scoped profiles and same-session A/A remain prerequisites.

Reviewed build evidence: [build manifest](../bench-results/build/build-manifest.json), [actual release codegen](../bench-results/build/release-codegen.json), status, selected original test/oracle outputs and the63-command journal. Build publication is main73bc2b87d. I performed only file reads, hashes and pure Python; no external program, native binary, build or timing was invoked.

## Identity and recorded checks

Current C/H match d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. Adapter H/C are corrected468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7 /c9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3. Lookup, physical oracle and sampler hashes match their manifest entries:7569d802357a8ca937ba8eaa668f9fe2c17652b6cd8b957d952129b6cab87cf5 /ac37c96fd1b583a6c74f8be083e3f68bff9a74989929cdc4fddcce8d8177f59a /18033d406b2bc4ff97d9c956ecf0d7081f6d1cbfb34db89ed5b94f6f09c267f1. All eight produced binary hashes match the manifest.

The native lookup SHA is40eb0740bbd8fcde7f340a636cdd00c70fe3f7c02bcc60c5a3bd793525d742e7; the separate profile binary isdc7f8abe4a302d2e56eeafc786f97d3091134e937426058be8c31c44c5cc2825. They must not be treated as identical executables. Retained Apple Clang21.0.0 targets arm64-apple-darwin27.0.0. Native options are C11/O3/g/Wall/Wextra/Werror/frame pointers/no-LTO; sanitizer uses O1 plus ASan/UBSan and no recovery. Includes, tree source, corrected adapter, SipHash and `-lm` are explicit in commands. No extra ISA option or disabled assertion is introduced.

All63 command records have expected codes, no timeout, direct reaping, empty owned groups and safe release. The two original-test outputs each report43 passed/0 failed. Native and sanitizer physical oracles each report4,160 cells and515,840 exact-score/position/output checks. Summary retains36 smoke checks (hit/miss/mixed × six lengths × two modes) and eight invalid-CLI checks. These are baseline correctness/build checks, not a full candidate guard screen or performance qualification. Build wall11.090947 seconds is orchestration metadata; smoke elapsed/rate fields are unused here. This bounded review is not a second complete raw-output audit.

## Actual helper dataflow

Fresh `_zbtScoreLeafFindMember` contains142 static instruction lines and a144-byte entry allocation; `_zbtreeScoreRaw` has491 lines and a160-byte entry allocation. These counts include static alternatives/error code and say nothing about executed instruction counts or cycles. I checked the helper instruction lines against the retained actual native otool stream (SHA1b0272ee00a594f9aa21188b06695e47acced78d1ded5e8c62dac4cb218ed920).

The physical tag index is held in `w27`. The leaf count is recovered into `w12`; reversal is loaded into `w10`. Helper-relative byte offsets below come from this fresh release:

| Offsets | Actual sequence | Meaning |
|---|---|---|
| +0x154..+0x168 | reversal load; `mvn w8,w27`; add count; compare; `csel w8,w27,w8,eq` | Logical position is physical for forward leaves, count−1−physical for reversed leaves |
| +0x16c..+0x178 | load/check optional score pointer; load/check score width | Score decoding is conditional; width zero skips delta loads |
| +0x17c..+0x188 | `mvn w11,w8`; add count; compare reversal; `csel w11,w27,w11,eq` | Decoder reconstructs physical position; forward alternative already selects original physical `w27` |
| +0x18c..+0x1a0 | multiply position by score width, derive byte/bit offsets, load/shift packed word | Reconstructed position reaches the packed score read |
| +0x1f4..+0x1fc | compare reversal, conditional negate delta, add score base | Reversed score-base subtraction is distinct and remains semantically required |
| +0x210..+0x214 | optional position check/store | The logical position is still supplied to callers that request it |

The two inverse-mapping arithmetic sequences survive in emitted code. This is not two out-of-line decoder calls: the logical decoder is inlined inside the generic leaf helper. `ScoreRaw` still calls that helper from its two table paths and supplies a literal NULL position (`x5=0`) at both sites. The generic helper therefore retains logical-position computation even for public score lookups. Memchr/memcmp and packed-record/external-hash validation remain present.

This does not show that a guarded physical decoder will improve both primary sizes, preserve other caller codegen, or eliminate any measured stall. Corrected adapter/compiler/frontend context differs from historical004/006. Historical gains, instruction counts, controls and losing decisions are not transferred to this baseline. No source or hypothesis is selected by this review.

Review file SHA-independent evidence pins: build manifest8c126f54ffd2530aa184d3272610cb1f05198183787bd7da57358526fa13f61f; release-codegen80ce637d77d6af4cb6efe767397b3d6acf30104b7993b57d94769de5e758ec48. Participant `/root/followup_proposal_a`, inherited Codex/GPT-6 family; exact serving model/token/currency costs unknown. Only this new review file was written. All work is finished; idle for root's fresh profile/qualification phase.
