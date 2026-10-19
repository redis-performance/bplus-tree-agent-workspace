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
