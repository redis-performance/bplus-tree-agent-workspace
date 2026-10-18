# COUNTERS-011 — scoped lookup path counts across batch sizes

Preregister before capture. Diagnostic hypothesis: changing batch1 to16 changes API
call frequency but not the leaf/index path census for an identical query stream and
tree. If counts differ, preserve and inspect the discrepancy; never normalize timings
with these counts. DIAG-019 failed precision and prefetch-attenuation gates; no retry.
Its caller assembly matches control/C except five panic-line immediates per mode,
but that does not establish identical dynamic work or machine layout.

Use four DIAG-019attempt002 snapshots(control/C ×prefetchon/off), exact frozen referee
plus only LLVM public counter reset/dump hooks. Installed Clang17 header
profile/instr_prof_interface.h was read: reset clears counters; dump prevents exit
redump. Include the real header, require __LLVM_INSTR_PROFILE_GENERATE, freeze header
hash and relevant interface text. No private API or hand-declared guessed signatures.
Compile O3 with existing flags plus fprofile-instr-generate/fcoverage-mapping.
These instrumented builds are never timed candidates. Fixed seeds83103/query83119
and83111/query83123,n8192,16-byte hits,32768members,3warmups,batch1/16:16captures.
Reset immediately before the measured-region work; dump after wall/thread/CPU/QoS
endpoints but before postvalidation. Full existing checksum/memory checks remain.
Every child<=120s, no new child after06:02UTC. Build all before capture; serial only.

One calibration binary first calls known_before10times, resets, calls known_scope20
times, dumps, calls known_after30times. Export must show0/20/0 calls. Stop capture if
this scope control fails. Capture expected zbtreeScores count=ceil(32768/batch),
dictGenHashFunction=32768, zbtreeInsertNew/zbtreeFree=0, work=1. Check exact operation,
checksum and memory output. Compare zbtIndexFind and zbtScoreLeafFindMember function
and branch counts across batch sizes per source/seed, and acrosscontrol/C/prefetch
modes per seed when source snippets align. All branch mapping resolves LLVM file IDs.
C helper counts retained descriptively. No minimum speed or branch-efficiency claim.

Normal output agrees with uninstrumented recipe semantics; no A/A or profiling-rate
qualification follows. Counts show logical reachability, not cycles/stalls/hotness,
frequency, unbiased sampling or performance explanation. SourceNONE and existingPARK
remain. Exact backend/model/token cost unknown; coordinator sequential review only.
