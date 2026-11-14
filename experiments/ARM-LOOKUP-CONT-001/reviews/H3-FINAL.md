# H3 independent final review — REJECT, source NONE

Reviewed 14 November 2026. The saved evidence supports rejection of all three H3 variants. No blocking defect was found in the reported rejection or raw-data joins. This review does not authorize adoption, another timing attempt, or closure of the broader campaign.

## Independently reconstructed decision

I reconstructed all 504 measured rows: 216 ARM native, 144 ARM GCC15/LTO, and 144 Intel native. The complete unique grids contain 126 ABBA blocks, six cases and three blocks per variant/case. Each effect was recomputed as `100 * ((B1 + B2) / (A0 + A3) - 1)` using elapsed time. Negative values mean faster. All effects, medians, footprint comparisons and pass/fail bits agree with the saved analyses and [H3 results](../H3-RESULTS.md).

| Cohort / variant | Hit median | Decisive failing blocks, elapsed change |
|---|---:|---|
| ARM native A | −6.007% | None |
| ARM native B | −6.441% | None |
| ARM native C | +1.685% | Hit +1.628%, +1.685%, +1.950%; score +3.329%, +3.301%, +3.430% |
| ARM LTO A | −6.635% | None |
| ARM LTO B | −6.237% | External +1.816%, +1.825%, +1.862% |
| Intel native A | −6.382% | Long +1.379%, +1.564%, +1.472%; external +1.081%, +1.115%, +1.252% |
| Intel native B | −4.183% | Long +1.844%, +1.736%, +1.498%; external +1.438%, +1.208%, +1.226% |

These are 21 failing blocks. A's ARM wins cannot offset its Intel guards; B fails guards on both target LTO and Intel; C fails before portability testing. Both Intel candidates pass the primary threshold even under the stronger 2% discovery interpretation, so a portability-primary interpretation does not alter rejection. Every measured footprint endpoint matches its control. Minimum individual windows are 476.814 ms, 2291.664 ms and 2037.514 ms respectively, all above 250 ms.

I independently rederived the three original control cohorts: renewed ARM native, long-window ARM LTO and Intel native. Their 216 rows / 54 blocks all qualify. Maximum absolute A/A effects are respectively 0.398%, 0.474% and 0.632%, below 1%. These controls join the corresponding exact baseline binaries; they are not interchangeable controls from another compiler cohort.

## Identity, completeness and source scope

Every comparison row joins its process stdout, successful command record, CPU2 affinity command, case, seed 17, registered sweep count, expected operations/hits/score checksum and baseline/candidate ELF hash. Per-process stderr is empty. Native ARM uses the original counts; ARM LTO and Intel use their registered fivefold counts. No measured process stem is duplicated. The command journals preserve two `affinity-zero-work` entries from separate build-only and measure-only invocations; these are zero-work probes, not duplicate measurements or retries.

Public metadata, raw comparisons, analyses and process stdout match the private originals. Original-file manifests match their private inputs; public command journals retain the same records with only the execution-root redaction. I independently hashed all seven measured candidate ELFs and the corresponding baseline ELFs against recorded identities. The built but unused ARM LTO C ELF also matches its recorded hash. [ARM codegen evidence](../H3-codegen.md) records the six ARM candidate identities; Intel identities remain in its cohort metadata.

Applying each published patch in memory to the frozen baseline reconstructs the isolated candidate source exactly:

| Variant | Source SHA-256 |
|---|---|
| A | `9c9b248b0b0a162f8679f8d189ff224652f3bfa5017c2f17e679fee83acaa7c9` |
| B | `5119e918762b2ca1a1943335c2b0729f48f72d5d7d0122a78aa4e0e1dbca8700` |
| C | `d1d8e8211a341a1aeeb488889c7f5b702afef739da682f0c991b41a39e118584` |

The baseline remains `16def20f621e1e9fcb2cd3f2818aea49e23dae9066ebea5fa276e841c5e095c9`, from pinned upstream `ee8e7f70152404649ac947157fd662d11b4a00d5`. All 11 frozen referee/dependency files checked across the three isolated implementations match, including lookup, qualification driver, both output oracles, header, compatibility/vendor inputs and upstream test entry point. No H1/H2 mechanism is stacked.

Source inspection supports the declared bounds: specialization requires length at most eight and an equal inline record length; zero length performs no payload load. A uses bounded first/last copies, B constant-size comparisons, C bounded byte comparisons. Equality remains endian independent, and the generic/external fallback and successful output logic remain intact. Both ARM compiler cohorts emit specialized comparison paths and retain generic fallback calls. Emitted-code differences satisfy a static mechanism gate; they do not prove a cause for any timing result.

Saved correctness logs show 57 native plus 57 sanitizer upstream tests, 36 fixture cells, 90,000 optional-output checks and 45,000 external checks per variant. The supplemental short-member oracles exercise guarded/exact allocations, alignments, boundary lengths and fallback/collision cases with different coverage: A 51,888 checks, B 719,716, C 231,504. These are supporting bounded tests, not exhaustive proof or a substitute for the failed performance gates. This review ran no new candidate executable.

## Chronology and remaining limits

Saved measurement starts are ARM native 02:29:31.557 UTC, ARM LTO 02:40:03.077 and Intel native 02:40:04.667. Intel completes at 02:47:57.539; ARM LTO completes at 02:50:01.813. Thus the ARM target cohort was already active before Intel comparison started and completed about 124 seconds after Intel finished. The saved artifacts contain no Intel LTO comparison, H3 confirmation, subsequent H3 guard trial or selected-candidate profile. This bounded artifact audit agrees with the controller's statement that no new H3 timing followed rejection; it is not a live fleet audit or independent observation of the precise decision instant. Unused builds remain build artifacts.

Under the existing additive convention, this closes one ARM population, not three variants or separate compiler attempts. From the canonical ledger's 41 completed attempts, the proposed totals correctly become **42 completed / 23 PARK / 19 REJECT / 0 approved; ARM 30 / Intel 6 / AMD 6; 25 populations / 5 replications / 12 qualifications**. Existing controls are not recounted. Ledger edits await controller acceptance; other active hypotheses remain excluded.

## TMA classification and review provenance

For ARM baseline and every H3 candidate: **Frontend_Bound unavailable; Bad_Speculation unavailable; Backend_Bound unavailable; Retiring unavailable; children unavailable.** ARM event/formula qualification remains unresolved, and H3 candidate pipeline captures were not collected. Separately qualified [Intel baseline TMA](INTEL-TMA-BASELINE.md) does not establish H3 category deltas. No pipeline-cause or server-performance claim is supported by this rejection audit.

This reviewer did not propose or implement H3, author its lookup referee, or collect its measurements. Earlier roles included H1/H2 review, authorship of separate H2 supplemental guards and hardening of a future H2 confirmation collector; those roles are disclosed and are not represented as independent review of my own work. Detailed execution provenance remains private; model, token usage and cost are unreported. No fleet operations, local timing, source changes, commits or pushes were performed.

Own current tool discovery returned no exposed `cpu-perf` / `library_status` tools. I consumed the controller's explicitly shared [consultation](../CONSULTATION.md), including the H3 bounds/codegen question: server 0.1.1, bundled revision `deb5a0bac467`, 3/287 indexed sources and 158 passages. It supplied no supporting primary passage. I did not make those controller calls and do not claim retrieved authority for the measured result or its cause.
