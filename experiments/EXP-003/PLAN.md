# EXP-003 preregistered screening

Same exact HARNESS-004 source/referee and AA-006 qualification. Base commit
 a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus frozen uncommitted harness;root untouched.
Hypothesis solely outline member decoding under EXISTING ele||len test in IteratorNext.
Three isolated variants:A noinline pointer-return helper with length-out;B noinline
void helper writes optional outputs;C noinline struct-return helper(pointer,length).
No new top-level fast-path guard,score decoder/state/API changes. Patches all preserved.

Each control/A/B/C release+ASan/UBSan original43 tests,128 fixture cells (n129,16/320
bytes,4encodings,2directions,8masks) and BOUNDARY-012 mixed mutation oracle must pass.
Referee/support/assertions/allocator/compiler flags identical across timed binaries.

Reuse fixed EXP-002 guard-extension schedule:14 cells,100000 members,20m ops,seed7103,
3 mode warmups,3 ABBA blocks/variant/cell,504 serial rows,variant rotation ABC/BCA/CAB,
cell rotation per block. All4 unqualified AA-006 masks diagnostic only;others qualified.
No omitted rows/outlier removal,child<=120s,total600s;no local build/test/profile overlap.
Wall time primary;95%t df2,t4.302652729911275. Primary f-int16-m4 entire interval<=-2%;
all qualified guards upper<=1%;exact matched count/checksum/bytes/fingerprint;>=10ms.
Any qualified guard lower>1% disqualifies. Eligibility requires ALL qualified guard
upper bounds<=1% and primary passes;unqualified guards still block ACCEPT. Rank eligible
by primary mean,overlap prefer smaller patch. No eligible=>NONE/PARK or REJECT if a
confirmed guard failure;do not relabel noisy primary failure as acceptance.

Fresh confirmation/profile of a preferred variant requires separate preregistration.
If none eligible,record all failure mechanisms and save fresh confirmation as next
step where needed. Round cutoff00:54:32UTC takes precedence;no new trials then.
Local M1/arm64/macOS26.3,one thread,Clang17/C11,-O3,-g,-fno-omit-frame-pointer,libc,
assertions unchanged. Frequency,effective QoS,residency unknown. Backend/model/cost
unknown;sequential fallback explicit. No new profile fractions/cycles/hardware headline.
