# M6 round 2 — update repacking rejected

Saved 2026-10-19T02:20:22.306941+00:00; round deadline 02:31:47 UTC, campaign deadline 08:00 UTC.
No experimental children remain. Final handoff is more than 90 seconds early.

UPDATE-001 completes the five-pattern/five-size public referee, native/sanitizer
checks, untimed path census, scoped profiles, release assembly, baseline calibration,
fixed A/A, both sequential population steps and three isolated implementation patches.
Baseline and rank evidence were resumed without rerunning completed schedules.

The existing in-place path is used by all same-value calls. Position-preserving
updates sometimes require a new exact packed representation: 1,517 of 20K calls at
100K, 11,058 at 1M. We tested re-encoding within the existing allocation, retaining
member records, leaf ID and index. [Results](003-update/RESULTS.md) reject the declared
dual-primary objective: no 100K implementation improves 2%. A/B/C 100K medians are
+0.084/+1.694/+1.992%; 1M medians −7.705/−8.765/−9.270%. The 1M observations remain a
separate exploratory transient-packing lead, not a selected contender or relabeled
primary. Both A/A cells fail strict ±1%, maxima 1.1722/1.5527%.

All 43 original tests per source/build and targeted native/ASan-UBSan checks pass.
Each candidate's private oracle exercises 74 successful repacks, including six
reversed leaves, unchanged records/IDs/ownership/memory and failure-atomic headroom
checks. Two deliberate faults detected. Initial baseline-only private-oracle UAF
was detected by ASan; corrected test pointer lifetime, existing public tests unchanged.
Other metadata/classifier/audit finalization errors are disclosed without rerunning
experimental schedules. Isolated control's instruction text matches calibrated control.
Git worktree creation denied once; four isolated copied source/build trees used.

Audit PASS: 75 calibration +48 A/A +144 discovery rows, 36 reconstructed block effects,
three exact patch reconstructions, frozen source/referee/binary hashes and 878 serial
command windows without overlap. Candidate timing 6.913444s; shortest window 43.577ms.
[Separate operator audit](OPERATOR-UPDATE-DISCOVERY-AUDIT.json) independently agrees
on the raw discovery arithmetic/checksums; scope excludes new timings/semantic review.
No full candidate guards, fresh confirmation, adoption profile or independent
adversarial review, because no dual-primary contender qualified. Source selection NONE.
No main source, header, historical referee, allocator, hashing or upstream-test changes.

Published milestones: profile/referee 33bf7899, chair f8d2badf, candidates a9e16781.
Earlier timeout evidence remains; publication resumed. Decision/handoff ack is next.
Coordinator alone commits and pushes. No worker Git writes or settings/permission edits.

Launcher metadata: Apple M6 / arm64 / 12 cores / macOS 27 / Apple Clang 21. Worker
sysctl denied and not retried. Frequency, DVFS, actual core residency/migration and
hardware counters remain unknown. Profile PCs are diagnostic, not exact time shares.
Cached M1 context 4c48fa7e has matching fixture branch counts but different warmup;
exact candidate/harness replication NOT RUN and no host timings pooled.

Branch totals: 9 populations (7 sequential fallback +2 multi-agent), 0 accepted /
4 rejected /5 parked, all 27 patches retained, 12 validated harnesses. Concurrent
M1 night counts remain separate pending reconciliation. Both current population steps
used one worker's sequential passes; exact serving model and token cost unknown.

Next: resume [HANDOFF.md](HANDOFF.md), create 004-lookup, inspect EXP-006 and profile
public independent hit/miss queries before proposing. A chair NONE is appropriate
without a new mechanism. Never restart failed update/rank schedules or wait for this
host remotely. Reporting begins 07:15 UTC; keep baseline source unchanged overnight.
