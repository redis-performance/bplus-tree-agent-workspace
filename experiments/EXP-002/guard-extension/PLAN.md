# EXP-002 expanded implementation guard comparison

Preregistered after AA-006, before any expanded candidate timings. Same hypothesis,
retained A/B/C patches and original population membership; not a new population round.
HARNESS-004 independent referee change is frozen and validated; AA-006336 rows qualify
10/14 modes, including primary f-int16-m4. Four modes remain unqualified (m2,3,5,6).
Do not hide them or call whole guard suite qualified. No source may ACCEPT this round.

Freeze new isolated control/A/B/C copies from HARNESS-004 plus exact EXP-002 candidate
source hashes. Referee/support byte-identical across copies. Validate each candidate
release and ASan/UBSan on original tests and640 mode cells/build as HARNESS-004.
Correctness failure disqualifies. Existing code/patches and root baseline preserved.

Reuse all14 AA-006 cells,100000 entries,20m operations,seed7103,3 mode warmups. Three
serial ABBA blocks/cell/variant;baseline label A,candidate B.504 fresh processes.
Variant order ABC/BCA/CAB,cell rotation by block. No exclusions or optional stopping;
no binary warmups (validation already exercised each executable),child<=120s,total600s.
No other builds/tests/profiles/agent activity during measurement. Save all failures.

Wall ns/item primary. Effect100*(mean(candidate)/mean(control)-1) each ABBA block.
95% descriptive t interval df2,t4.302652729911275. Unchanged primary gate entire interval
<=-2%;guard upper bound<=+1%;same exact tree bytes/count/checksum/fingerprints;all
windows>=10ms. A qualified guard with lower interval>+1% demonstrates regression.
Unqualified modes diagnostic only;no acceptance if any mandatory mode unresolved.

Decision: remove a candidate from preference if any qualified guard demonstrates>1%
regression;otherwise PARK any unresolved intervals/qualification/independence/provenance.
No expanded eligible variant=>NONE, retain original C discovery selection as historical.
If several have no demonstrated regressions rank qualified primary,overlap prefer
smaller patch,provisional only. Confirmation next must use separately preregistered
fresh seeds/cases. No trade-off relaxing guard gate declared. All three retained,
including losses. Profile any demonstrated guard regression with separate matched
instrumented snapshots/codegen; sampling never substitutes for timing precision.

Local M1/arm64/macOS26.3,Clang17,C11,-O3,-g,-fno-omit-frame-pointer,assertions/libc;
one unpinned thread. Frequency,effective QoS,within-window placement unknown. Exact
backend/model/cost unknown. Independent reviewer failed startup;sequential fallback.
