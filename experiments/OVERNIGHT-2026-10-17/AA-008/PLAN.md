# AA-008 — long score-plus-length guard diagnostic

Preregistered after EXP-004 screening/fresh0,4,7/profile results,BEFORE this new trial.
EXP-004 mask6 diagnostic shows a slowdown but old20m precision failed. PARK that guard.
New hypothesis:100m returned items(5x prior count) resolves +/-1% A/A precision for
score-plus-length on two fresh fixtures. This is a duration/fixture diagnostic,not an
assumed cure or unchanged retry. Include score-only duration control. Same frozen
HARNESS-004/EXP-004 control executable;no source,referee,allocator or QoS intervention.

Four cells:forward integer16 masks4,6 crossed seeds13103,13109;size100000,100mitems,
1000traversals,3warmups. Six ABBA blocks/cell,96rows,cell rotation;one separately retained
prospective warmup mask4seed13103,1m items. Child<=120s,total300s. No local build/test/
agent computation overlap. All rows/failures retained;no optional stopping/exclusion.

Same precision gate:24rows/cell,each>=10ms,all independent score/member/state/count/
checksum/owned-memory/fingerprint checks;95%t df5 interval wholly within[-1,+1]%.
Wall primary,thread/CPU IDs/QoS diagnostic only. Frequency/effective residency unknown.
Hypothesis supported only if BOTH mask6 seeds qualify; otherwise PARK,do not repeat.
Comparison at this duration needs this qualification;cannot carry it to20m or other modes.
M1/arm64/macOS26.3,Clang17,C11,-O3,-g,-fno-omit-frame-pointer,libc,one unpinned thread.
Unknown model/backend/cost;uncommitted exact snapshots retained;root baseline preserved.
