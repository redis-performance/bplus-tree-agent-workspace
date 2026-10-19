# Fresh follow-up preparation FAILED; timing blocked

The one executed600s preparation phase ran08:27:44.840542–08:30:57.813780UTC
(192.984seconds), issuing2118/2124 frozen commands. Command2118 was the retained
HARNESS-005 signed-zero negative-control run in the native build. It exited−6 at:

`bench/iterator_modes_v5.c:62: score_bits(nextscore)==score_bits(model_score(nexti,n,encoding))`

The unchanged oracle caught the deliberately erased zero sign during its copied-next
iterator check. The frozen driver instead required the current-item assertion text
`score_bits(score) == score_bits(model_score(i,n,encoding))`, so its exact-diagnostic
check failed. This is a negative-control registration mismatch, not an undetected
fault, and not evidence of normal-source correctness failure. It nevertheless FAILS
the preregistered preparation contract. No success certificate, timing, retry, repair
or continuation has been issued. The remaining six commands were not executed.

Completed checked commands include four original43-test runs,512 unchanged HARNESS-004
cells,1536 unchanged HARNESS-005 cells,12 packed/mutation/signed-zero oracle runs and
10 registered fault detections. One additional fault process aborted at the actual
copy assertion above but does not count as a passed registered check. Do not claim
all14 planned detections or complete preparation.

The driver exited before its final aggregate hash checks. A SEPARATE read-only SSH
inspection independently confirms all28 frozen inputs, six protected timing binaries,
four complete actual/newsource-referee sets unchanged. Raw text dump hashes independently
confirm rebuiltcontrol matchesactual013 and rebuiltA matchesoldA exactly. Four newguard
binary hashes were retained, but this does not authorize their use after the failed gate.
No owned units or cgroup PIDs remain. Fresh follow-up lease is still ACTIVE until10:15UTC;
this idle proof is not coordinator restoration. The oldnightrelease remains verified.

All4241 generated validation artifacts have raw/public publication hashes; four raw
.text files remain locally/onrunner with their exact hashes. Every reached command,
output, timeout policy, finalerror and unexecuted suffix is recoverable from the frozen
manifest and partialresult. Original026 PARK/sourceNONE and all oldresults remain final.
The prepared timingfreeze8d11db31a is unexecuted and blocked by this preparation result.
Only an explicitly reviewed new correctness plan could address the remaining gap;
no automatic retry or acceptance follows this diagnosis. Backend nativeCodex; exact
model/token/cost unknown.
