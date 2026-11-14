# H5 final review — REJECT, source selection NONE

The state-separation hypothesis closes without an eligible implementation. **A fails
the ARM GCC15/LTO primary requirement; B fails the static mechanism gate; C fails
the ARM native primary requirement.** Favorable native or Intel results cannot
cancel a target-cohort failure. No unchanged retry, supplemental guard timing,
held-out confirmation, selected profile or adoption is justified for H5.

This is an offline reconstruction of saved evidence, not a new measurement. The
reviewer previously implemented B; B's assembly inspection therefore is not an
independent-author review of B. The A/C performance arithmetic and artifact joins
were reconstructed independently. The benchmark adversarial parity/replicability
checklist was applied by this reviewer; no additional reviewer population is
claimed. No source, collector, fleet state, executable or timing workload was run
or changed during this review.

## Complete rows and gates

Reconstructed all **288 comparison rows**: ARM native A/C144, ARM LTO A72 and Intel
native A72. Each measured variant has exactly six cases × three ABBA blocks × four
slots, with no omitted/extra/reordered row. Raw process stdout equals the recorded
row; stderr is empty; command records show successful CPU2 execution, seed17 and
the declared counts. Every operation/hit/score checksum was recomputed from the
500-member fixture, including zero hits for misses and125250×sweeps for scored
lookups. Every row names the appropriate baseline/candidate ELF hash.

Effects below are `100 × (mean B elapsed / mean A elapsed − 1)` for each block;
negative means less elapsed time. ARM requires at least2% primary improvement in
every block. Intel portability requires no more than1% regression. Every guard
block and owned-memory endpoint is bounded at1%; every window must be≥250ms.

| Cohort / variant | Primary block0 | Primary block1 | Primary block2 | Largest guard regression | Smallest row | Decision |
|---|---:|---:|---:|---:|---:|---|
| arm-native / A | -2.336182% | -2.117361% | -2.129464% | +0.467883% | 492.659ms | screen passes only |
| arm-native / C | -0.464547% | -0.703023% | -0.132524% | +0.919704% | 494.613ms | primary rejects |
| arm-lto / A | -0.529937% | -0.518976% | -0.531170% | +0.561869% | 2375.865ms | primary rejects |
| intel-native / A | -3.410760% | -3.463200% | -3.400314% | +0.058662% | 2122.420ms | screen passes only |

All comparison rows reproduce each case's qualified baseline owned bytes exactly:
**0% memory change**. All non-primary guard blocks pass. Thus C's native rejection
and A's LTO rejection are primary failures, not memory/guard or short-window failures.
The saved analysis agrees with the independently reconstructed arithmetic. No
averaging across blocks, cases or machines was used to rescue a failure.

Rechecked216 relevant A/A rows,72 per cohort, with18 blocks each. Maximum absolute
control effects are0.397978% ARM native,0.474175% ARM LTO and0.631511% Intel native;
minimum windows are495.198ms,2374.481ms and2127.005ms respectively. All controls pass
±1% and reproduce memory. ARM native uses the original counts (hit/score50k,
miss100k, long/external/update20k sweeps); ARM LTO and Intel native use the separately
qualified5× counts. No control from one compiler/host qualifies another.

Evidence: [ARM native rows](../H5/native/comparison.jsonl),
[ARM LTO rows](../H5/lto/comparison.jsonl),
[Intel native rows](../intel/H5-native/comparison.jsonl). Their public copies,
metadata and analyses are byte-identical to the artifacts audited here.

## Source, referee and binary joins

Original source is `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`,
extraction commit `e13d9fc8875a636ca07203b1f3fdd1aa28488bda`, upstream
`ee8e7f70152404649ac947157fd662d11b4a00d5`. Each retained patch was applied in memory
to that original text and reproduced its exact isolated candidate source. Every
frozen referee/dependency file was rehashed in the root and all three isolated
checkouts; none differs from the frozen manifest. Source hashes match native/LTO
build metadata and the actually measured variant selection.

| Variant | Source SHA-256 | Patch SHA-256 |
|---|---|---|
| A | `ef2098f8cedf2aae88e845162d15ef1fd09a9abcaae0e3939d3043594b5a77e0` | `8a23cc2a738a4f06287bf039a9373ba620a809b1cda57c0d93e333c95309ae1f` |
| B | `a2f627b71b398a75a5f793132d2e15de547d3808622f949870c952506eb496fd` | `2f430e19cb95d1b4e3fe418c7c39eb9b5821087d8fc2ba512a0549b293ba1c20` |
| C | `00297055998a105dd8fe4998e1d7b7a388e1a052ac2db661e494bf1f9fb6b850` | `8d1c1336cd16bf3567295001691bd70c8231753d3ca79e29cb41a260d90d1a76` |

All three cohort baseline ELFs were freshly hashed and match baseline metadata,
control metadata and comparison rows. Every measured candidate ELF was freshly
hashed as well. Full saved disassembly instruction bytes were checked against the
corresponding ELF load segments, without running the executable. Matched lines:
ARM native A20536, native C19532, LTO A11993, Intel native A22703.

| Cohort / variant | Fresh actual candidate ELF SHA-256 |
|---|---|
| arm-native / A | `d77de23d4497572501e7e33abcaea6f6aa4631b0151e1482734d62586249f101` |
| arm-native / C | `e6543b401f4d05a08e2fc7bdb33157077a323a0bd4036a4b5087076736647266` |
| arm-lto / A | `036fbc6a4842d53d61ee6669e16e43eee005610f8f3c2805241a2e691920cc29` |
| intel-native / A | `c7b14fe1021005d051aa44d5f67197a0d7b6acaf5ca88ba5255578a2879bdf26` |

Build commands retain the same referee/dependencies and `-O3 -g -Wall -Wextra
-Werror -fno-omit-frame-pointer`; LTO additionally uses `-flto=auto` and the original
immutable GCC15 image. The standalone process contains both fixture and tree; no
network/client/server saturation comparison or latency-percentile claim is made.
Existing correctness evidence remains mandatory; this review did not rerun it.

## Static B rejection and interpretation

The [saved ARM codegen review](H5-ARM-CODEGEN.md) identified A/C's successful stable
path separation in both ARM builds and B's failure. Reinspection confirms native
B's stable kernel reloads `member_rehash` at`5180` and branches at`5184`, then keeps
the migration-generation/leaf-stamp loads at`5188`/`518c`. LTO B repeats this at
`405754`/`405758` with stamp loads at`40575c`/`405760`. Wide-ID paths retain the same
structure. Stable input avoids the conditional stamp loads, but still executes
the redundant state reload/null branch per candidate. The wrapper's dispatch did
not specialize its outlined kernel. B is **static NONE**, with zero timing rows;
its smaller wrapper is not a performance result. This closure's fresh ELF byte
verification covers measured A/C artifacts; B's disposition uses saved full ARM
assembly and its recorded build identities, not a newly fetched B executable.

A's native and LTO stable code both remove the intended state filtering, so its
LTO primary failure is evidence that the mechanism was insufficient under the
registered target test. It does not prove a particular microarchitectural cause.
Likewise C's native primary improvement is too small despite acceptable guards.
The six ordinary cases do not substitute for the separately required active-
resize/displaced-traffic guards. Those, fresh-seed confirmation and matched profiles
were not completed because rejection already resolves selection. The closure
claim is defensible; an adopted speedup or causal bottleneck claim is not.

## Consultation, TMA and audit pins

Own enabled-tool discovery found no callable CPU-perf/library-status tool. The
controller's actual shared raw-state consultation in [H5 selection](../H5-selection.md)
remains shared evidence; coverage3/287 sources and158 passages supplied no supporting
primary passage for a gain. No new consultation is claimed by this reviewer.
Qualified ARM baseline and H5 candidate Frontend_Bound, Bad_Speculation,
Backend_Bound, Retiring and child-category shares are unavailable/uncollected.
Separate Intel evidence cannot establish an ARM cause. No TMA attribution is made.

| Artifact | SHA-256 |
|---|---|
| Frozen referee manifest | `040a22b3603e8c0917eca78f111106b54ad0d4f5f3a41c34c1f40f57f2b57eba` |
| arm-native comparison rows | `eb2b86a422fafbc5ab013f65253c1b5224d9226e5efc196b35edf8780a0fb5d1` |
| arm-native build/run metadata | `0b7c268c6e851e1a6a8171cac9dae15bea6830a2604e22b14b3d6bc98729927e` |
| arm-lto comparison rows | `dc39366c4ef604b07d5774ca510304edb482a2781bbeb3cecdc869b2559bc0c7` |
| arm-lto build/run metadata | `e8a47fb3ef8f9e31067fdb4134c09263c437605bf49de0888cacbea01262c12e` |
| intel-native comparison rows | `9d62094059d06434d18c6dace74b07ab977f3f3af176ab8e5da189c651295ea0` |
| intel-native build/run metadata | `af15ecb23753a267848cc0b9350ecb84fad854fac4aae8226523b685fd00046e` |

Final disposition: **H5 REJECT; source selection NONE.** Preserve all passing and
failing artifacts. This review does not authorize further measurements or publication.
