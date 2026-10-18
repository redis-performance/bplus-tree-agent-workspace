# Fresh guard-regression confirmation

Written after504-row discovery but before any fresh confirmation/profile outcome.
All A/B/C show qualified no-output/full-output regressions;primary improvements remain.
Expanded preference NONE. Confirmation addresses selection over modes/variants with
fresh fixed seeds9103,9151,not additional discovery rows. Same frozen executables.

For every variant A/B/C and each seed:three ABBA blocks for f-int16-m0 (no output),
f-int16-m4 (primary),f-int16-m7 (full output).100000 entries,20m items,3 mode warmups.
216 fresh serial processes total. Outer seed order9103,9151;variant rotation ABC/BCA/CAB
by block;mode order0,4,7 rotated by block. No binary warmup excluded. Children<=120s,
total<=420s;no concurrent local tests/builds/profile/agent work. Preserve all rows/failures.

Same memory/checksum/fingerprint/count controls and>=10ms windows. Per variant/cell/seed
three effects100*(candidate/control-1),95%t df2,t4.302652729911275. A guard regression
confirms only if lower interval>+1% for BOTH seeds. Primary speed gate unchanged upper
interval<=-2%. Any confirmed guard fails candidate regardless primary. If all three
confirm a guard regression,REJECT these three implementations under declared no-tradeoff
gate and selection NONE. This rejects represented implementations,not every possible
future specialization. No winner=>no acceptance;independent acceptance requirements stay.

Separate descriptive profile/codegen phase AFTER uninstrumented confirmation: control/
A/B/C on modes0 and7,seed9103,100m items,100000 entries16-byte members,3 warmups.
Eight captures,requested1000us;two known-function400m-iteration calibrations. Profile
acceptance controls:>=15 samples,no overflow,all symbols resolved,exact fixture checks;
calibrations>=30 samples and>=90%known_arithmetic samples. Failures retained/no retry.
Capture codegen and explain added guard/helper dispatch without exact-cycle attribution.
Sampler cadence/aliasing/overhead/frequency remain unknown;not unbiased percentages.

All source/referee frozen,root baseline untouched. Local M1/arm64/macOS26.3,Clang17,
C11,-O3,-g,-fno-omit-frame-pointer,libc/assertions equal. Sequential coordinator fresh
confirmation,not an independent agent;backend/model/cost unknown. No threshold changes.
