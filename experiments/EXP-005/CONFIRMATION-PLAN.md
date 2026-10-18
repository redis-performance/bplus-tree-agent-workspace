# EXP-005 — nonzero packed-score mask

Preregistered before builds/timing. One hypothesis: express the width mask without
baseline conditional-select overhead, preserving the original cross-word branch.
Three sequential proposals/chair above; three isolated implementations from identical
HARNESS-004 baseline, not independent agents. A:UINT64_MAX>>(64-bits);
B:((1ULL<<(bits-1))*2)-1; C:UINT64_MAX>>((-bits)&63). All inside bits!=0, valid widths1..64.
Unsigned overflow in B intentional/defined. Do not combine with EXP-004.

Profile prerequisite: existing EXP-004 control PC captures match baseline src/header;
score-only concentrates in zbtreeIteratorNext, static mask sequence has compare/select.
New baseline AA-009 uses same newly built control: only previously qualified masks0,4,7,
fresh seed20101,n100000,20mitems,integer16,forward,threewarmups,sixABBAblocks=72rows plus
one prospective1m warmup. Precision interval(df5) entirely[-1,+1]%,allwindows>=10ms,
exact/checksum/count/ownedmemory/fingerprint checks. No unchanged failed mask6 A/A.
If primary4 fails, skip candidate timing and PARK; record artifacts/codegen instead.

Control/A/B/C validation: original43tests,128iteratorfixtures/build,mutation012,
packed013 and signed-zero014 suites,release/debug+ASan/UBSan=1096commands total.
Freeze binary/source/referee hashes; main source untouched. Source mask variants
screen on masks0,2,4,6,7,seed20101,3serialABBAblocks each=180rows,rotatedvariant/cells.
Masks2/6 diagnostic only; broader/unqualifiedguards block ACCEPT. Wall ns/item primary,
thread/CPUids/QoS descriptive. Allflags/assertions/allocator identical;memory unchanged.
No exclusions/optional stopping. >=2% primary upperCI gain and qualifiedguard upperCI<=1%
for screening preference; ties favour shortestpatch then A/B/C. NONE if none eligible.

Fresh confirmation is precommitted for ALL3 to avoid optional salvage: masks0,4,7,
seeds20107/20113,3ABBAblocks=216rows. Evaluate primary>=2% and guards<=1% individually;
confirmedguardfailure requires lowerCI>1 on BOTH seeds. Reject implementations that
confirm a guard regression; otherwise PARK missing/noisy evidence. Twelve matched
instrumented100mitem profiles (control/A/B/C masks0,4,7),two400m calibration runs,seed20107,
excluded from speed evidence. Require conservation/cadence controls as earlier sampler.
Static codegen and adversarial sequential review required. Independent review unavailable.

Eachchild<=120s;AA/screen/confirmation budgets600/600/420s. Serial measurements with
allbuilds/tests/agentsidle. No source adoption,commits,pushes or publication. SameM1,
arm64/macOS26.3,AppleClang17,C11,-O3,-g,-fno-omit-frame-pointer,libc,one unpinnedthread;
frequency/effectiveQoS/withinwindowmigration/samplerbias unknown. Allcosts unknown.
