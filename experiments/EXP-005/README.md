# EXP-005 — packed-score mask arithmetic

**PARK; confirmed source selection NONE.** Screening provisionally preferred C, but
fresh primary improvement does not meet the fixed confidence-bound requirement on
either seed. Main source stays baseline. No adoption or portable performance headline.

Three sequential proposals/chair and three isolated implementations test one mask
expression hypothesis over HARNESS-004. These were not independent agents. All1096
validationcommands pass originaltests,128modefixtures/build,mutation012,packed013 and
signed-zero014 in release/debug+ASan/UBSan. AA-00972rows qualifies0/4/7.180screeningrows
and216freshrows retain allcontrols. Unqualifiedmask6 remains an adverse diagnostic.

Twelve matchedprofiles/twocalibrations pass. Static A/C iterator code removes one mask
instruction; their hotinstructions match after panic-literal relocation normalization.
Fullbinaries differ. No intrinsic C superiority or causalcycle claim follows.
[Plan](PLAN.md),[chair](selection.md),[screening](SUMMARY.md),[fresh](CONFIRMATION.md),
[decision](implementation-selection.md),[review](REVIEW.md),[profiles](profiles/SUMMARY.md),
[assembly](CODEGEN.md),[freeze](freeze.json). Allpatches/rawrows retained.

Uncommitted exactsnapshots; independent confirmation/review and broaderguardprecision
pending. Model/backend/cost unknown;supervisor usage separate. Local M1/macOS26.3,
AppleClang17,-O3,C11,libc,oneunpinnedthread;frequency/effectiveQoS/residency/samplerbias
unknown. MCPchecker consulted(drop_number),not a performancecertificate. Revisit with
new evidence or independently controlledrunner,not unchanged seed/count retries.
