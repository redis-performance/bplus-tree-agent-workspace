# DIAG-018 — observed completion delay

Preregistered instrumentation diagnostic, not a repeat of DIAG-017's failed precision
criterion. Hypothesis: file-output Python timeout polling adds a measurable delay
between a blocked waitpid observer noticing benchmark completion and Python returning;
pipe/selector transport reduces that observed delay by at least5ms on both freshseeds.
No claim about exact kernel exit, actual frequency, causality of benchmark throughput,
or suitability of either policy for source acceptance.

Build a small POSIX wrapper: fork/exec unchanged HARNESS-006 benchmark; block waitpid;
record CLOCK_MONOTONIC timestamp immediately after return, then write metadata and
exit with child's status. Parent uses the identical CLOCK_MONOTONIC API for its return
stamp. Wrapper teardown/metadata and parent scheduling are included. Wrapper has an
independent110s alarm that kills/reaps its child; parent120s bound remains. No detached
processes. Validate normal binary stdout/stderr, return-code propagation and timeout
kill/reap in both transports before freezing. Source review must establish no observer
computation during the benchmark except blocked wait and signal support.

Target95/bytes16/trimmed/forward/alternating-zero/mask6,20mrequested/20000065effective,
threewarmuptraversals. Two freshseeds53101/53113, sixABBAblocks/seed;A=filetimeoutpoll,
B=pipe/selector.48targetrows plusoneprospective1m wrapper/binarywarmup. Commands/paths
precomputed; rotate seedorder perblock; rawCSV/stderr/completionmetadata retained.
Metadata parsing/hashing only after each child completes; no rowremoval/optionalstop.
Child110s,wrapper120s,total180s; allserial/noagents/builds/tests/profilesoverlap.

Primary diagnostic is wall delayms=(parentreturn-clock - wrapperwaitpid-clock).
For eachblock effect=mean(delayA)-mean(delayB), sixpaired effects,95%t df5interval.
Supportrequires bothlowerbounds>5ms, nonnegativeallobserveddelays, validnormalchild
statuses, allbenchchecks/fingerprints/memory/effectivecounts andtargetduration>=10ms.
Otherwiseunsupported; invalidcontrols=PARK. Report benchmarkwallns/item andthread
A/Aeffects descriptively, without sourcequalification or policyadoption. No exclusion
on CPU-ID change. Everyrequestedblockrun evenif partialresultlooksconclusive.

This wrapper is diagnostic instrumentation and changes the launch environment;
its observations cannot replace original guard measurements. Mainreferee/source
unchanged. Backend/model/tokenunknown; reviewerstartupfailed,sequentialreview.
