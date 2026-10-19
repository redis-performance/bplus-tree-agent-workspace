# Focused SCAN guard validation passed

Focused baseline/B validationPASS673 serial commands in312.77s:432 native/sanitizer models,216 census cells,43 originaltests per4builds,16 repeatedfault detections;36 fixturehashes and24 post-validation artifacthashes pass. No focused timing yet; frozen baseline calibration324 one-traversal windows/300s next. Source NONE/PARK unchanged.

Exact ARM referee2ab283daa/root review239ac9730; original8fab511e adapter and selectedB remain fixed. Every full raw model matches acrosssources withinbuildmode, with no native-versus-sanitizer byte equality requirement. Census binaries are separate and never timed. Descending fixtures contain exactly64 reversed members; no active resize,wideIDs or omitted memberlength boundaries are implied. These semantic passes do not resolve24 original guard failures or establish acceptance. Callback costs differ from original count-only scan.

Next phases remain unchanged: calibration300s then AA900s and B900s,full36cells/six blocks,200ms target/100ms floor. Passcounts and exact schedules will be frozen after baseline-only calibration, before AA. No retry/adaptation/extensions.

[Plan](PLAN.md), [validation summary](validation-summary.json), [raw audit](validation-audit.json), [raw commands](validation-processes.json), [all models](validation-cells.json), [post-validation hashes](post-validation-hashes.json). No new optimization population; source adoption NONE.

## Calibration and comparison freeze

Focused baseline calibrationCOMPLETE324 serial rows in178.75s/300s. Raw schedule/CPU2/checksum/ownedbytes auditPASS;24 post-calibration hashes unchanged.36 fixedpasscounts1..942 frozen with both864-process AA/B schedules beforecomparison; allcounts below100000cap. Next baseline AA900s, no adaptation/retry/extension.

[Calibration rows](calibration.json), [audit](calibration-audit.json), [fixed counts](pass-counts.json), [schedule/source freeze](timing-freeze.json), [post-calibration hashes](post-calibration-hashes.json). Some dense cases already exceed the200ms target in a single traversal; counts remain at leastone. No A/A or B focused timing has yet run.

## Focused A/A:22 of36 cells qualify

Focused AA COMPLETE864 rows/216 blocks in611.62s under900s;22/36 cells qualify,14 precision-failed,zero shortwindows. Raw schedule/CPU2/serial/checksum/ownedbytes auditPASS;24 post-AA hashes unchanged. Full frozen864-row B diagnostic next under900s,including everyfailedcontrol label; no adaptation/retry/source switch. Overall PARK/source NONE.

Each cell requires all6 block effects within±1% and every window>=100ms. Maximum observed absolute effect4.264%. Failed controls remain final for this schedule; no candidate comparison can relabel them as qualified. Existing24 unresolved original guards remain separate.

| Members | Bytes | Order | Tag distribution | Qualified | Min..max A/A effect |
|---:|---:|---|---|---|---:|
| 4096 | 16 | shuffled | ordinary | no | -0.756..+1.688% |
| 4096 | 16 | shuffled | dense17 | yes | -0.394..+0.678% |
| 4096 | 16 | shuffled | folded01 | yes | -0.355..+0.372% |
| 4096 | 16 | descending | ordinary | no | -1.303..+1.474% |
| 4096 | 16 | descending | dense17 | yes | -0.031..+0.861% |
| 4096 | 16 | descending | folded01 | no | -1.072..+0.970% |
| 4096 | 16 | equal-score | ordinary | no | -4.264..+1.441% |
| 4096 | 16 | equal-score | dense17 | yes | +0.015..+0.650% |
| 4096 | 16 | equal-score | folded01 | yes | -0.322..+0.773% |
| 4096 | 321 | shuffled | ordinary | no | -1.023..+1.027% |
| 4096 | 321 | shuffled | dense17 | yes | -0.740..+0.194% |
| 4096 | 321 | shuffled | folded01 | no | -0.996..+1.122% |
| 4096 | 321 | descending | ordinary | no | -1.087..+1.215% |
| 4096 | 321 | descending | dense17 | no | -1.878..+1.323% |
| 4096 | 321 | descending | folded01 | yes | -0.473..+0.909% |
| 4096 | 321 | equal-score | ordinary | no | -2.504..+1.050% |
| 4096 | 321 | equal-score | dense17 | yes | -0.469..+0.884% |
| 4096 | 321 | equal-score | folded01 | yes | -0.777..+0.359% |
| 100000 | 16 | shuffled | ordinary | no | -1.132..+1.252% |
| 100000 | 16 | shuffled | dense17 | no | -1.471..+0.083% |
| 100000 | 16 | shuffled | folded01 | yes | -0.460..+0.208% |
| 100000 | 16 | descending | ordinary | yes | -0.954..+0.579% |
| 100000 | 16 | descending | dense17 | yes | -0.058..+0.125% |
| 100000 | 16 | descending | folded01 | yes | -0.242..+0.272% |
| 100000 | 16 | equal-score | ordinary | no | -0.219..+1.713% |
| 100000 | 16 | equal-score | dense17 | yes | -0.072..+0.115% |
| 100000 | 16 | equal-score | folded01 | no | -0.601..+1.272% |
| 100000 | 321 | shuffled | ordinary | yes | -0.683..+0.364% |
| 100000 | 321 | shuffled | dense17 | yes | -0.415..+0.859% |
| 100000 | 321 | shuffled | folded01 | yes | -0.031..+0.397% |
| 100000 | 321 | descending | ordinary | yes | -0.289..+0.488% |
| 100000 | 321 | descending | dense17 | yes | -0.397..+0.249% |
| 100000 | 321 | descending | folded01 | no | -0.146..+1.492% |
| 100000 | 321 | equal-score | ordinary | yes | -0.330..+0.305% |
| 100000 | 321 | equal-score | dense17 | yes | -0.048..+0.149% |
| 100000 | 321 | equal-score | folded01 | yes | -0.073..+0.226% |

[All raw AA rows](aa.json), [per-cell audit](aa-audit.json), [post-AA hashes](post-aa-hashes.json). B timing has not yet started at this publication.

## Full focused B comparison:22 qualified guard passes,14 unresolved

Focused B COMPLETE864 rows/216 blocks in588.46s/900s. All22 baseline-qualified cells pass everyguard block;14 unqualifiedcells remain unresolved. No shortwindows or qualified regression; exactcallbacks/checksum/ownedbytes/CPU2/serial auditPASS.24 focused+22 original post-phase hashes unchanged. Overall PARK/source NONE retains24 original unresolvedcells. Corrected-adapter baseline013 next; supplemental014 after.

All36 cells have negative median elapsed changes in this diagnostic, and every observed B block stays below+1%; the14 failed A/A cells remain descriptive only. Qualified median changes range−20.864% to−0.306%, and the largest qualified block effect is−0.248%. These are this referee’s ID/length/score-consuming callback results, not pooled original count-only SCAN speedups. Some dense workloads include extensive legal duplicate emissions/collision disambiguation; raw normalization uses actual callbacks. No duration change, seed selection, dropped cell, alternate implementation or retry.

| Members | Bytes | Order | Tag distribution | Baseline qualified | Median elapsed change | Min..max block effect |
|---:|---:|---|---|---|---:|---:|
| 4096 | 16 | shuffled | ordinary | no | -1.044% | -2.413..+0.260% |
| 4096 | 16 | shuffled | dense17 | yes | -2.518% | -3.621..-1.857% |
| 4096 | 16 | shuffled | folded01 | yes | -3.494% | -3.780..-2.382% |
| 4096 | 16 | descending | ordinary | no | -8.149% | -8.757..-5.938% |
| 4096 | 16 | descending | dense17 | yes | -2.331% | -3.089..-1.848% |
| 4096 | 16 | descending | folded01 | no | -3.283% | -3.795..-2.597% |
| 4096 | 16 | equal-score | ordinary | no | -1.274% | -2.493..+0.005% |
| 4096 | 16 | equal-score | dense17 | yes | -3.385% | -3.547..-2.004% |
| 4096 | 16 | equal-score | folded01 | yes | -3.845% | -4.781..-3.397% |
| 4096 | 321 | shuffled | ordinary | no | -2.691% | -3.252..-1.494% |
| 4096 | 321 | shuffled | dense17 | yes | -5.211% | -5.794..-4.676% |
| 4096 | 321 | shuffled | folded01 | no | -9.096% | -9.479..-8.243% |
| 4096 | 321 | descending | ordinary | no | -9.796% | -11.515..-8.911% |
| 4096 | 321 | descending | dense17 | no | -5.736% | -6.570..-4.593% |
| 4096 | 321 | descending | folded01 | yes | -9.796% | -10.261..-8.515% |
| 4096 | 321 | equal-score | ordinary | no | -1.081% | -2.372..-0.576% |
| 4096 | 321 | equal-score | dense17 | yes | -4.392% | -6.263..-3.030% |
| 4096 | 321 | equal-score | folded01 | yes | -7.933% | -8.745..-7.768% |
| 100000 | 16 | shuffled | ordinary | no | -3.197% | -3.995..-1.893% |
| 100000 | 16 | shuffled | dense17 | no | -2.164% | -2.413..-2.037% |
| 100000 | 16 | shuffled | folded01 | yes | -15.160% | -15.267..-14.956% |
| 100000 | 16 | descending | ordinary | yes | -9.651% | -10.793..-8.758% |
| 100000 | 16 | descending | dense17 | yes | -2.561% | -2.736..-2.462% |
| 100000 | 16 | descending | folded01 | yes | -16.651% | -16.767..-16.526% |
| 100000 | 16 | equal-score | ordinary | no | -2.792% | -3.590..-1.860% |
| 100000 | 16 | equal-score | dense17 | yes | -0.820% | -1.106..-0.743% |
| 100000 | 16 | equal-score | folded01 | no | -14.756% | -15.065..-14.469% |
| 100000 | 321 | shuffled | ordinary | yes | -8.603% | -8.866..-8.324% |
| 100000 | 321 | shuffled | dense17 | yes | -3.653% | -3.739..-3.371% |
| 100000 | 321 | shuffled | folded01 | yes | -20.864% | -21.045..-20.681% |
| 100000 | 321 | descending | ordinary | yes | -17.449% | -17.674..-16.823% |
| 100000 | 321 | descending | dense17 | yes | -3.799% | -4.759..-3.460% |
| 100000 | 321 | descending | folded01 | no | -24.078% | -24.951..-22.893% |
| 100000 | 321 | equal-score | ordinary | yes | -10.746% | -10.918..-10.076% |
| 100000 | 321 | equal-score | dense17 | yes | -0.306% | -0.443..-0.248% |
| 100000 | 321 | equal-score | folded01 | yes | -19.936% | -20.067..-19.827% |

All673 validation commands,324 calibration rows,864 AA rows and864 B rows are retained separately. Root independently audited AA at a1210ec35; full B is submitted for separate AMD review. The864-row schedules and36 passcounts remain exactly42f77d525.

Coverage limits remain: descending fixtures contain only64 reversed members, no active resize or wideIDs, lengths16/321 and nonnegative scores. Supplemental referee014 is separate and cannot repair original or focused control failures. Corrected adapter013 also remains a separate source baseline; every comparison here uses original8fab511e and exactSSE2B204edc2c. This B differs from separately authored ARM NEON implementationB1788f2b5.

[Raw B rows](b.json), [all effects](b-audit.json), [focused post-hashes](post-b-hashes.json), [original post-hashes](original-post-b-hashes.json). No source adoption or new optimization population.

Independent AMD review223d6d7de reconstructed all2,052 calibration/AA/B processes and432 ABBA effects without using this worker’s audit code. It verified the22 qualified passes,14 retained noisy controls,36 actual fixture files and24 focused+22 original post-phase hashes. See AMD022 in the same campaign. PARK/source NONE remains unchanged.

Final follow-up: `../014-scan-supplement/DECISION.json` rejects the selected old-source Intel SSE2 B replication on a qualified 319-byte signed-zero reversed-leaf guard. Earlier measurements and qualification labels remain unchanged; no A fallback or source adoption.
