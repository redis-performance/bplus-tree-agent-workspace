# EXP-004 — compact-history guard extension

Preregistered after corrected AA-011, before candidate builds/profiles/timings.
Retain existing EXP-004 population/hypothesis and exact source A/B/C patches. No fifth
population, new hypothesis, primary substitution or source adoption. Main baseline stays.

Isolate copies of frozen HARNESS-006 with only src/zset_btree.c replaced by each exact
retained candidate. Copy qualified control binary byte-identically. Identical compiler,
flags/assertions, hashing and libc allocator. Diagnostic capacity adapters never used.
Each A/B/C must pass release and ASan/UBSan original43tests, packed decoder/zero mutation
suites and288compact fixturecells/build:192trimmed cells n31/95,bytes16/320,
integer/wide/alternating-zero,bothdirections,all8masks;96clone/cycle cells n95,samebytes/
encodings/directions,masks0/4/6/7. Existing tests not weakened.

Only qualified guard: n95 bytes16 alternating-zero trimmed forward mask4. AA-011
corrected analysis qualifies bothseeds41031/41043; original analysis erratum retained.
All other compact guards remain PARK and are excluded by baseline rule, before candidate
timing. The original integer mixed-output guard remains unresolved.

Profile control/A/B/C on compact integer forward4,zero forward6,wide forward7(bytes320),
100mrequesteditems rounded to traversals,seed41031,3warmups,1000us self-sampler;
12captures plus2known-arithmetic calibrations. Fixed profile controls inherited from
HARNESS-006/PROFILE-PLAN. Instrumented timings excluded. No cycles/cache claim.

Screen allthreevariants against control:3ABBAblocks x2seeds41031/41043 x1cell =72rows.
Fresh confirmation for ALLthree regardless of screening:seeds41051/41063,same3blocks,
72rows.20mrequesteditems,95members,210527traversals/20000065items,3warmuptraversals.
Prospective1mitemwarmup perbinary before screening,retained. Rotatevariant/seed order.
Wall ns/effectiveitem primary;thread time descriptive. Eachchild<=120s,eachphase<=240s.
No builds/tests/agent work overlap measurement. No exclusions/optional stopping/pooling.

Each variant/seed:95%t df2 interval for paired100*(B/A-1). Guardpass requires upper<=+1%
and exactchecksum/fingerprint/count/memory equality. Confirmed regression requires
lower>+1% on BOTHfreshseeds. Such failure rejects thatvariant. Ifall3fail,REJECT/NONE;
ifA failsbutothersdon't,NONE/PARK pending complete re-evaluation. Otherwise A/PARK remains.
No selection by this guardonlysubset and no acceptance; broader guard qualification,
independentconfirmation/review and committedprovenance stillpending. Sequential review,
backend/model/costunknown. Allpatches/failedruns retained.
