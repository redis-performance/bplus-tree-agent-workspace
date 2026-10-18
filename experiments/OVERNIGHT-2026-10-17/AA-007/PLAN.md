# AA-007 — current-round baseline check for EXP-004

Preregistered before measurement. Same HARNESS-004 referee and unmodified EXP-004
control source,now exact local executable from EXP-004 validation. Requalify ONLY the
10 cells qualified by AA-006;do not retry its four failed mixed-output cells unchanged.
This is a current-round prerequisite for new equivalent score-predicate candidates,
not a proposed remedy for prior noise. No performance claims from structural counts.

Fixed10cells:forward integer16 masks0,1,4,7;reverse integer16 masks4,7;
forward fraction320 masks4,7;reverse wide320 mask7;forward wide320 mask4.
Size100000,20m emitted operations,seed7103,3mode warmups. Six serial ABBA blocks,
240rows;rotate cells per block. One retained prospective warmup f-int16-m4,1m ops.
Child<=120s,total600s;all validation/builds finished first,all agents idle. No overlap
with local computation. No optional stopping,outlier removal,threshold changes.

Same AA-006 gate:24rows/cell,all checks/invariants and>=10ms each,95%t(df5,2.5705818366147395)
interval across six block effects wholly within[-1,+1]%. Wall time primary. Record
thread time/opaque boundary CPU IDs/reported QoS;frequency/effective QoS/within-window
migration unknown. Source/referee/binary hashes frozen before run. Only freshly qualified
cells may pass EXP-004 comparison gates;newly unqualified cells remain diagnostic and
block acceptance. If primary fails,do not run source timings;PARK and finish other work.
M1/arm64/macOS26.3/Clang17,one unpinned thread,C11,-O3,-g,-fno-omit-frame-pointer,libc.
