# DIAG-011 — caller-mask context interaction

Preregistered after AA-008 fails joint precision;EXP-004 stays PARK. New falsifiable
hypothesis:removing per-item dynamic output tests in the CALLER reduces EXP-004A's
mask6 penalty by at least half in both new fixtures. This diagnoses caller context,
NOT a replacement referee or an acceptance workaround. Even support leaves the old
mixed-output guard unresolved;never replace the referee to make a candidate pass.
No assumed predictor/cache/branch-miss mechanism without counters.

Isolated snapshots of exact EXP-004 control/A trees. Diagnostic copies of HARNESS-004
add --caller dynamic/fixed;fixed4/6/7 traverse functions use literal output masks and
consume identical returned values/counts. Both callers still invoke unchanged public
iterator with the same requested outputs. Select a function pointer OUTSIDE timing;
retain original full independent byte/score/order/state and memory oracle. Only caller
code differs. No source optimization added;original root/referee/variants unchanged.

Before measurement:release and ASan/UBSan,control/A,2caller modes,3masks,2directions,
4encodings,16/320bytes,n129,ops1000;192fixture processes per source/build,768total.
Exact expected checksums/counts and original oracle must pass. Save diagnostic patch,
source/binary hashes. No benchmark from sanitizer. No warmup-only data exclusion.

Fixed timings:2fresh seeds14107/14143,2callers,3masks4/6/7,control/A ABBA,3blocks;
144rows,size100000,100mitems,3warmups,forward/integer16. Rotate mode cells per block;
all serial,child<=120s,total300s,no local builds/tests/profiles/agent computation.
All rows/failures preserved. Wall primary;thread/CPU IDs/QoS recorded,frequency unknown.

For each seed/mask/caller calculate paired3block A/control effects with95%t df2.
For mask6 calculate blockwise dynamic-minus-fixed effect D and95%t interval. Support
only if dynamic penalty lower>+1% and D lower>max(1%,half dynamic mean) for BOTH seeds.
Other cases describe context specificity;do not promote to acceptance or requalify A/A.
No optional stopping/exclusions/threshold change. Failure/uncertainty=>unsupported/PARK.
Save all data and codegen differences. New-trial cutoff01:22:36UTC;retain incomplete work.
Sequential coordinator,reviewer startup failed;backend/model/cost unknown.
