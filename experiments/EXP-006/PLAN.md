# EXP-006 fixed implementation comparison

Primary: HARNESS-007attempt002 mixed16/batch16,n8192,2millionrequested members,
3warmup passes. Qualified guard:hit320/b16. Additional diagnostic guards:hit16/b16,
hit16/b1,miss16/b16 (failedAA-012); cannot clear acceptance. Seeds80703/q80719 and
80711/q80723. Control+A/B/C from exact frozen baseline with unchanged allocator,
O3-DREDIS_DEBUG compiler flags; ASan buildsO1. Baseline/profile refs in selection.md.

Three isolated implementations of bounded inline leaf-tag search. Keep candidates
under scratch/experiment006/{control,A,B,C}; patches in variants/. No main source edit.
Before timing eachsource:43originaltests/native+ASan, raw guard-page oracle/native+ASan,
new tag-search exact-first-match oracle/native+ASan, and batch fixture grid native+ASan
(n17/257,bytes16/320,batches1/3/16,hit/miss/mixed,opsn+3;36cells/build/source).
New tag oracle exhaustively compares all256tags across span0..128 with deterministic
random/adversarial values at16alignments, including borrow masks and repeated matches.
Baseline uses libc memchr through a diagnostic wrapper, candidates their helper.
Referee unchanged per source; no production private state mutated.

Screen all passingA/B/C against control serialABBA,3blocks percase/seed/variant,
rotating case/variant order perblock:360rows. Wall ns/member primary, perseed3block
95%t(df2) interval for100*(candidate/control-1). Provisional eligibility: upperprimary
<=-2%and qualifiedguardupper<=1%bothseeds, exactmemory equality; unqualified guards
remain diagnostic and cannot yield ACCEPT. Select eligible smallest patch; otherwise
select smallest patch with largest mean primary gain for fresh falsification only,
explicitly not a winner. If all primary means nonnegative selectNONE and confirm all
three only on primary/qualifiedguard. Preserve every row, no exclusions/threshold edits.

Fresh confirmation predeclared seeds80803/q80819,80811/q80823,6ABBA blocks primary+
qualifiedguard. If provisional choice exists run that one (96rows); ifNONE run all3
(288rows). Require primaryupper<=-2%and guardupper<=1%bothseeds (df5); otherwise
PARK or REJECT for demonstrated regression. Independent confirmation/review unavailable.
No ACCEPT while original or new guardqualification unresolved. Allchildren<=120s;
screen360s,confirmation360s; stop starting experiment children by05:33UTC to curate.

Profile selected provisional/falsification variant or fastestprimary ifNONE, matching
PROFILE-004 instrumented capture scope for bothseeds,requests1000/3001us,primary50m/
guard20m. Existing same-round baseline/calibrations retained; allsource and sampler
hashes checked. No instrumentedtiming comparison. Inspect assembly of all variants.
If schedule cannot complete preservepartial andPARK. Commit provenance pending morning.
