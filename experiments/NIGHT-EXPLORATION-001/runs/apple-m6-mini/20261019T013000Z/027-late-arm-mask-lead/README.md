# Late ARM mask lead — retained for future M6 review

The other campaign reports a primary lead for the exact historical `experiments/EXP-005` A packed-score mask patch on AWS Neoverse V2: median elapsed differences −7.77% at 100K and −7.10% at 1M, with all 12 primary blocks passing. This is not the night's count-one `005-decode` family. The original [result](inputs/RESULT.md), [static review](inputs/CODEGEN-REVIEW.md), [validation](inputs/VALIDATION-RESULT.md), [patch](inputs/candidate.patch) and [root raw audit](inputs/root-raw-audit.json) are pinned by RECEIPT.json.

The ARM decision is PARK / source NONE. Qualified broader and mixed-output guards, fresh confirmation and a matched candidate profile remain missing. A 4→3 static mask instruction change does not establish the cause of a 7% elapsed difference; caller changes and compiler context remain material.

This publication arrived after M6's experimental cutoff. It is an unselected future-review input, not a new M6 proposal, implementation or measurement. No native work ran for this receipt, no source changed and no host timings were pooled. The main README preserves the ARM chart under its separate heading.

Any later M6 work must start from the current corrected source and actual local profile/codegen, then the required independent proposals/chair and fresh qualified controls. Verify that the exact source mechanism exists locally; do not assume the ARM lowering, gain or controls transfer. All M6 guards, memory, fresh confirmation, matched profile and independent/adversarial acceptance requirements remain. No unchanged failed schedule retry is authorized by this note.

The [retained M6 baseline window](M6-BASELINE-MECHANISM.md) confirms the original mask-selection pattern exists in the already validated binary. It includes five lines when counting the constant load and final AND. No modified M6 codegen, native workload or performance inference follows from that static inspection.
