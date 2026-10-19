# Cross-host SCAN inventory — no hypothesis selected

The only exact native candidate family here that can plausibly be evaluated as the same mechanism on M6 is the corrected ARM16-byte NEON all-match family. It was severely rejected on the ARM runner. The corrected AMD and proposed Intel runs use an SSE2 patch; unchanged on M6, that patch selects its portable fallback and does not replicate native SSE2 work. No source adoption, new proposal, population or launch follows from this inventory.

This is a read-only inventory of90 pinned Git blobs, six exact retained patches and their in-memory reconstructed target hashes. Git operations were show/ls-tree only. No network fetch, SSH, checkout/worktree modification, build, test, profile or benchmark ran. Complete hashes, copied public inputs and pinned public URLs are in SOURCES.json and INVENTORY.json. Timing reports are read as reported evidence; I did not independently recompute all remote raw rows. Preliminary broad tree listings were truncated, then replaced by explicit host/campaign paths; all90 catalogued blobs were read completely.

| Host | Exact pinned evidence commit | Current corrected SCAN state at that pin |
|---|---|---|
| ARM | a9b2127ec505978c711f2f24650dde8eff7ee3f5 | Corrected NEON A/B/C REJECT; later fold-predicate chair NONE |
| AMD | af2131b804b94acad96f6de47f7a243d4fca4ca8 | Exact corrected SSE2 B fails both every-block primary gates; source NONE |
| Intel | a8d051d0bef1363f09ab2981f410e2d1ffbaf5b1 | Corrected exact-B guard-first plan prepared; no corrected candidate run at that pin |

## Identity trap: branch root versus actual corrected snapshots

All three pinned branch roots have unchanged target C d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 and H496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83, but their root compat files still have the legacy79b3/adf0 identities. The actual corrected campaigns run detached source13e459ff8800be3f02b6b45c87dd7b0c39453fa9, explicitly sealed in their manifests. That commit's actual Git blobs, the ARM/AMD campaign freezes and current local M6 files agree exactly: header468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7 and adapterc9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3. Eleven original source/referee/vendor files were checked against current M6. Do not build a branch-root legacy adapter while calling it corrected.

The unchanged benchmark frontend is b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde. The V2 bounded all-match oracle is b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded. Original tests, allocator, hash and scan interval/wide/live-widen/resize-generation referees remain separate frozen dependencies. All cross-host effects must stay host/session/compiler/adapter scoped; no old-adapter control or speed observation qualifies the corrected M6 runner.

## Candidate families and authorship

These are actual separate native authors, not three sequential passes by one author. Exact serving models, token usage and monetary costs are unknown. Sealed provenance records no peer-patch reads before submission; the original SSE2 proposal process disclosed prior operational influence about a different memchr direction, so it was not a blinded experiment. Exact implementation hashes and provenance URLs are retained, rather than inferring independence from code differences.

| Family / variant | Actual author | Patch SHA256 | Reconstructed target C SHA256 |
|---|---|---|---|
| Corrected NEON A | /root/aws_arm | 42fed5c2de1a863f0f1a415d2a348694bfb8f773ef2ffbff562c2472d2b76b53 | 0f8568f36ea0ed3d48c13906302c2df6983d6271568b88e0b5c380f7ce2070eb |
| Corrected NEON B | /root/aws_intel | 978134f54562ab6cff239bfbd15152cfc08e8defb19aa71c8cae122ceb870eac | 1788f2b5e48ef74440079a9a3da67a67a3b5b5bae1d18f617d42784b10ba8825 |
| Corrected NEON C | /root/aws_amd | 7335e122597ba6fa74cee42f13e5ee3ecbb52753efb7c56a8abdf7a4775f27e8 | 1600c035103a0dd30b49a5a266da73707963039647443ffd3ee88cd5f6827fe2 |
| Original SSE2 A | /root/aws_amd | 8c55d42ea53a6f689a53668c8cffcf9a7e01d274d3fcf9306ff154b1f8aa3547 | 30306a73d024ddcb986387ec91f1d1d8746697890e1b22a7f04de10afe029974 |
| Original SSE2 B | /root/aws_intel | bd93f3922c72c4f1e8776a897e80321e3380345ee4dbd37d6d62e99683f4a644 | 204edc2ccd40e42dff5d9d794e499422247f5e68db798f93b7af633636c16e23 |
| Original SSE2 C | /root/aws_arm | b4780cb8998db2931a63533849c658551a676c064be0071f23fd608b98e4f41a | 364b78b368a4b4100ca7339b07100947b5670bf21d6dcbf60195be4f84f63b0a |

All six change only target C, in zbtLeafTagMatches and local capability/include guards. Both families compare every complete16-byte chunk exactly, fold physical tags0+1 for query1, enumerate all physical matches in ascending order and retain reversed logical mapping and bounded residuals. This is distinct from M6's completed rank/decode/update/caller/lookup families and the private packed-score decoder repetitions. It is not a first-match member lookup optimization, and the rejected lookup SIMD evidence cannot stand in for this all-match SCAN contract.

NEON guards require little-endian AArch64 with __ARM_NEON and arm_neon.h. A/C retain one bit per nibble; B clears a complete matching nibble. A/B force-portable macro is ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE; C uses ZBT_FORCE_PORTABLE_LEAF_TAGS_C. SSE2 guards require __SSE2__ and emmintrin.h; fallback macros are respectively ZBT_FORCE_PORTABLE_TAG_MATCHES, ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE and ZBT_LEAF_TAG_MATCHES_SCALAR. Unsupported architecture/fallback checks are correctness evidence only. No extra ISA flag is allowed merely to force a timing result. Apple Clang21 native guard activation and emitted NEON code have not been checked by this inventory.

## Corrected ARM: exact failed family, valid baseline controls

[The immutable ARM plan](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9b2127ec505978c711f2f24650dde8eff7ee3f5/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/017-corrected-neon/PLAN.md) uses Clang18.1.3/C11/O3/g/frame pointers, unchanged assertions/hash/allocator, CPU2 and no added ISA flags. A separate O1 ASan/UBSan path preserves checks.145 correctness commands passed in392.6s under600s: all four sources' original43 tests in both modes, V2, scan interval, wide/live-widen seeds7/19, resize generation, all designated portable paths, and eight isolated negative controls. The overread negative hit a cardinality assertion; it was not demonstrated as a guard-page signal.

Fresh baseline A/A at100K/1M,16-byte members,5M requested SCAN operations, seeds401/402/403 twice, six ABBA blocks, qualified both sizes with minimum415.775/535.062ms.48 rows took61.95s under300s. These are ARM controls, not M6 qualification.

[Discovery rejected all three](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a9b2127ec505978c711f2f24650dde8eff7ee3f5/experiments/NIGHT-EXPLORATION-001/runs/aws-arm/20261019T020000Z/017-corrected-neon/RESULT.md):144 rows/36 blocks in215.635s under300s, same5M/16bytes/seeds. A median effects were+100.169%/+69.898%; B+78.161%/+55.342%; C+100.075%/+69.457% at100K/1M. Every variant failed every primary block. Maintenance order B,C,A did not make B a winner. Source NONE; no held-out confirmation triggered.

Later exact-binary diagnosis identified changed predicate construction and other codegen/context costs, without proving a removable bottleneck. A fresh fold-predicate packet obtained good controls but its chair selected NONE, not a replacement patch. This cannot justify repairing the failed variants in a supposed exact replication. A different Apple compiler/host is a possible new-host falsification question, not evidence that any variant will win.

## Corrected AMD and Intel: same SSE2 B, different decisions

AMD's [corrected baseline controls](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/af2131b804b94acad96f6de47f7a243d4fca4ca8/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/017-corrected-scan/RESULT.md) qualify both sizes: max absolute A/A0.504394%/0.889833%, minimum338.039/434.076ms. Baseline profile diagnosis is separate from legacy008's failed1M control and elapsed/cycle discrepancy. Corrected exact-B validation passed60 commands/151.55s under600s. [Its48-row corrected comparison](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/af2131b804b94acad96f6de47f7a243d4fca4ca8/experiments/NIGHT-EXPLORATION-001/runs/aws-amd/20261019T020000Z/019-corrected-B-replication/RESULT.md) took52.61s: medians−1.848286%/−1.785198%, only2/6 blocks at each size met−2%. Advancement rejected, source NONE; no guards/confirmation/profile allowed after that failure. It was an exact retained-source replication, not another three-implementation population.

Intel's old-adapter exact B had primary leads and independent fresh primary confirmation, but was later REJECTED by a qualified trim/319-byte/alternating-signed-zero guard: all six blocks regressed+1.566%..+6.877%, median+4.931%. That fixture has seven members and no full SIMD chunks; altered compiler context still matters. No inference that corrected noreturn removes the regression is justified.

Intel's corrected baseline A/A qualifies both sizes (ranges−0.121..+0.288% and−0.040..+0.196%; min436.623/582.990ms). Its [current exact-B plan](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/a8d051d0bef1363f09ab2981f410e2d1ffbaf5b1/experiments/NIGHT-EXPLORATION-001/runs/aws-intel/20261019T020000Z/017-corrected-scan-replication/PLAN.md) remains preparation only. It requires600s correctness,60s fresh guard calibration,120s guard A/A and120s B guard, with seeds701–703, minimum100ms and every block±1%/≤+1%. Any failed/noisy guard blocks later primaries. Only after separate review may48 primary rows run under300s. Fresh801–803 confirmation remains reserved. No corrected candidate result or eligibility is invented from the plan.

## Bounded M6 feasibility, without choosing a hypothesis

A separately reviewed exact ARM NEON source-family replication is mechanically plausible on M6 with unchanged target/referee bytes and all original variants preserved. An initial bounded validation/control/discovery envelope is600+300+300=1200seconds, before orchestration/reviews; the reported ARM elapsed values are not M6 predictions. Linux taskset/perf/ELF tooling and CPU2 placement cannot be copied as if they were macOS controls. A platform owner, actual Apple compiler/ISA/codegen identity, identical per-variant flags/paths, semantic/fault coverage, fresh M6 A/A and all original windows/counts/seeds/gates must be frozen first. This inventory authorizes no implementation or launch.

Every primary block at both100K/1M must improve at least2%, every window at least10ms and every fixture/checksum/callback/owned-byte identity match. A/A requires all six effects within±1%. Missing/noisy controls mean PARK; the failed remote candidates remain rejected irrespective of M6. A survivor would still require fresh501–503 A/A+comparison, full corrected original5sizes×2member-lengths×8operations guards, original focused and supplemental fixtures, all applicable existing M6 guards, matched profile and independent confirmation/adversarial review. None may be omitted to fit time. Full acceptance feasibility before07:15UTC is unproven; no M6 runtime or qualification evidence supports promising it. An exact SSE2-native M6 replication is NONE because the architecture selects fallback. A new NEON rewrite or combination would be a distinct hypothesis/population, not exact B replication.

The current M6 SCAN sample concentration reported by the driver is a location observation; this inventory does not convert it into cost, expected gain or a causal recommendation. Root's common packet and actual independent proposals/chair must decide whether an exact family replication, a distinct supported hypothesis or NONE is warranted.

Participant: /root/followup_proposal_c, inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown. Public URLs are immutable commit/path references; no network receipt was checked. No source selected or adopted.
