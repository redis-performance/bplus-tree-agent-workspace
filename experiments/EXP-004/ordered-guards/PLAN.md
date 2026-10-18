# EXP-004 ordered/signed-zero guard extension

Preregistered after AA-010, before candidate builds, profiles or timings. Existing EXP-004
three sequential proposals/chair and three implementations remain the same population;
this is additional guard evidence, not a new source hypothesis or population.

Freeze isolated copies of HARNESS-005 for control/A/B/C, replacing ONLY src/zset_btree.c
with exact retained EXP-004 variant source hashes. No change to root/old snapshots.
Qualified control binary is copied byte-for-byte from HARNESS-005. New candidate binaries
use identical compiler/flags/assertions/allocator. Preserve all patches. Both-build
validation for A/B/C: original43tests,192newfixtures (n97/513,bytes16/320,twoencodings,
threeorders,bothdirections,masks0/4/6/7), packed bitstream and exact-zero mutation suites.

AA-010 qualifies six cells on both seeds: integer descending reverse mask4;
alternating-zero ascending forward4,descending forward4,reverse4,forward6,forward7.
Two integer forward cells excluded by fixed both-seed precision rule, not candidate data.
No substitution for original failed integer mask6 guard. All8 cells remain in AA ledger.

All six eligible cells are GUARDS against regressions, not replacement primaries.
Control/A/B/C descriptive scoped profiles before timing: three cases integer-desc-r4,
zero-desc-f4,zero-desc-f6;100mitems,seed31031,1000us timer,two400madd calibrations.
Conservation/nooverflow/symbolresolution/cadence controls; profiles excluded from speed
measurements. No causal attribution or exact-cycle claim from sampled-PC counts.

Screening: each candidate vs control,three serial ABBA blocks on eachcell,seeds31031/31043;
432rows. Fresh confirmation precommitted for ALLthree candidates regardless of screening:
samecells,seeds31051/31063,threeABBAblocks=432rows. 20mitems,n100000,bytes16,3warmups;
rotatedvariant/cell/seed order per block. Wall ns/item primary,threadtime descriptive.
Prospective wholebinary warmup1mitems for eachcontrol/candidate before screening,retained.

Eachchild120s; screen and fresh budgets480s each. No builds/tests/agents during timings.
Allrows retained; no optional stopping, exclusions, pooling seeds or adjusted thresholds.
For eachvariant/cell/seed, paired ABBA mean percent and95%t df2 interval. Guard passes
when upperCI<=+1%,sameexactchecksum/fingerprint/count/memory; confirmed guardfailure
requires lowerCI>+1% on BOTHfreshseeds for the samecell. Such a failure REJECTs variant.
Otherwise any uncertainty remains PARK. Rejection of all3 updates EXP-004 to REJECT/NONE;
if A rejected but others not, selectionNONE/PARK until originalprimary/guards re-evaluated.
No new selection by ranking this guard-only subset; ACCEPT impossible this round.

Sequential adversarial review required; independent reviewer failed startup. Frequency,
effectiveQoS,withinwindowmigration,samplingbias,independentconfirmation and committed
provenance remain unknown/pending. Main baseline kept for separate morning review.
