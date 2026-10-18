# Proposal A — one test for the ninth score byte

Sequential proposal pass A,not independent agent. Backend/model/token cost unknown.
Inputs:HARNESS-004 frozen source,AA-006 qualification,PROFILE-003/EXP-003 control profiles,
COUNTERS-003 structural census,EXP-002/003 rejection history. No speed result invented.

Evidence:control iterator sampled PCs include score decoding;codegen has separate branch
on shift==0 followed by bits>64-shift. All score widths are0..64;inside bits!=0, the
ninth byte is required exactly when bits+shift>64. The first test is logically redundant.
COUNTERS-003 shows common6/7bit paths and rare64/63bit paths;all must remain supported.

Hypothesis:one equivalent cross-word predicate in zbtScoreLeafScore reduces conditional
instruction work enough for >=2% forward integer16 score-only wall improvement,with no
>1% guard/memory regression. Only this predicate changes;no fast-path dispatch,mask,
loads,layout,hashing or allocator changes. Every branch still reads the same bytes.

Risk:invalid shift64 if predicate implemented incorrectly;overflowed unsigned arithmetic
if source invariants misunderstood;codegen changes elsewhere may regress non-score paths.
BOUNDARY-013 plus existing API/mutation/sanitizer suites required. Prediction:score modes
benefit or unchanged;no-output modes should not regress but are mandatory guards.
Falsify if primary gate misses,guard regresses,or codegen does not remove redundant test.
Profile attribution remains descriptive,not a cycle model. Unqualified broader guards
and independent review prevent final acceptance until resolved.
