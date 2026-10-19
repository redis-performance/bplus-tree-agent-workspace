# AWS activity log — 19 October 2026

- 01:52 UTC: fetched latest public main and Apple host branches; local checkout
  clean. Read live OSS fleet inventory and historical release records. Verified
  SSH and actual CPU/compiler on Intel secondary, AMD profiler and ARM secondary.
  No active benchmark containers on Intel/ARM; existing idle AMD processes retained.
- 01:54 UTC: published Linux affinity metadata correction as `8fab511e`, keeping
  measured source/referee behavior unchanged. Set08:00UTC release timers, stopped
  and verified all three OSS coordinators, launched independent CPU2 five-size
  baseline services. All three services active; no candidate timing yet.
- 01:57 UTC: published the reservation in the private OSS fleet inventory. Added
  deadline-bound serial remote job helper and AWS worker/publication instructions.
  Initial supervisor test run:5/6passed; found completed-worker versus STOP race.
  Fixed by rechecking process completion after process-tree discovery. Full
  process-control tests rerun before optimization launch; result recorded below.

This is operational preparation, not an optimization decision. Counts unchanged.
- 01:58 UTC: all six process-control tests pass after the supervisor race fix
  (32.34seconds), including hard deadline cleanup, STOP, continuation/usage,
  duplicate-supervisor exclusion and campaign isolation. Remote helper compiles
  on all three hosts. No permission settings changed.

- 02:03 UTC: all three baseline services succeeded. Reconstructed960rows/host and
  verified all raw CSV/stderr hashes, source commit, CPU2 affinity and seven
  validation stages. Evidence committed4e8edf65. Generated and visually inspected
  the five-host chart (200cells). Native workers independently verified SSH and
  published initial status; failed detached CLI evidence retained separately.

- 2026-10-19T02:04:17.844635+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:05:57.934567+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:09:13.643796+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:09:50.185352+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:10:58.503737+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.
