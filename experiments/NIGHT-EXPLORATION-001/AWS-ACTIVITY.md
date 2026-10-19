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

- 2026-10-19T02:11:34.914310+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:12:11.009958+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.

- 2026-10-19T02:13:50.819937+00:00: aws-intel running, 2 rounds, publication native worker commits; aws-amd running, 2 rounds, publication native worker commits; aws-arm running, 1 rounds, publication native worker commits.
- AMD LOWERBOUND-001 rejected: three candidates, 144 serial processes, 36 paired
  effects independently reconstructed by root. AWS measured populations 1;
  accepted/rejected/parked 0/1/0. ARM profile attribution corrected before timing;
  unmeasured exact-mask proposal withdrawn. Intel screen continues.

- 2026-10-19T02:15:14.416994+00:00: aws-intel running at `46a052e8`: SSE2 lookup population build; A/A partial qualification; aws-amd running at `865beadd`: LOWERBOUND-001 REJECT/NONE; one scoped diagnostic pending; aws-arm running at `f41ae0ba`: exact-mask-selection-superseded-none; miss-profile-next.

- 2026-10-19T02:15:50.935137+00:00: aws-intel running at `b8945b4d`: lookup REJECT/NONE; preparing update-path profile; aws-amd running at `865beadd`: LOWERBOUND-001 REJECT/NONE; one scoped diagnostic pending; aws-arm running at `f41ae0ba`: exact-mask-selection-superseded-none; miss-profile-next.

- 2026-10-19T02:19:37.691308+00:00: aws-intel running at `b8945b4d`: lookup REJECT/NONE; preparing update-path profile; aws-amd running at `a97f04c0`: LOWERBOUND-001 complete; packed-score move census next; aws-arm running at `f41ae0ba`: exact-mask-selection-superseded-none; miss-profile-next.

## 19 October 02:20 UTC — two independently audited AWS rejections

AMD lazy lower-bound metadata decoding and Intel bounded SSE2 lookup scanners both
failed the preregistered speed gate. Root independently audited all 144 AMD and 432
Intel raw processes. AWS count: 2 measured populations, 0 accepted / 2 rejected /
0 parked; ARM's corrected-profile withdrawal was unmeasured and is excluded. No
source adoption. Host workers continue distinct profile-led directions until the
08:00 UTC deadline. See the central AWS-DECISIONS.md ledger and retained host patches.

- 2026-10-19T02:20:45.851012+00:00: aws-intel running at `bc4de81c`: five-pattern update referee validated; scoped gprof running; aws-amd running at `a97f04c0`: LOWERBOUND-001 complete; packed-score move census next; aws-arm running at `f41ae0ba`: exact-mask-selection-superseded-none; miss-profile-next.

- 2026-10-19T02:21:22.221902+00:00: aws-intel running at `bc4de81c`: five-pattern update referee validated; scoped gprof running; aws-amd running at `0eb34bbf`: packed move census complete; scoped insert/delete profiles running; aws-arm running at `f41ae0ba`: exact-mask-selection-superseded-none; miss-profile-next.

- 2026-10-19T02:22:30.367113+00:00: aws-intel running at `bc4de81c`: five-pattern update referee validated; scoped gprof running; aws-amd running at `0eb34bbf`: packed move census complete; scoped insert/delete profiles running; aws-arm running at `0ce43c0e`: count-one-decoder-candidate-validation.

- 2026-10-19T02:25:45.580985+00:00: aws-intel running at `bc4de81c`: five-pattern update referee validated; scoped gprof running; aws-amd running at `0eb34bbf`: packed move census complete; scoped insert/delete profiles running; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:27:25.424632+00:00: aws-intel running at `bc4de81c`: five-pattern update referee validated; scoped gprof running; aws-amd running at `1fa63027`: builder score-write metadata profile complete; full-pass A/A running; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:29:05.398993+00:00: aws-intel running at `bfeb1e51`: update diagnosis complete NONE; evaluating remaining profile-supported queue; aws-amd running at `1fa63027`: builder score-write metadata profile complete; full-pass A/A running; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:30:13.586799+00:00: aws-intel running at `bfeb1e51`: update diagnosis complete NONE; evaluating remaining profile-supported queue; aws-amd running at `8da42f7e`: builder score-write metadata profile complete; full-pass A/A running; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:32:57.366351+00:00: aws-intel running at `bfeb1e51`: update diagnosis complete NONE; evaluating remaining profile-supported queue; aws-amd running at `6d3790c4`: builder-write qualified AA, all59validation commands pass; fixed screen next; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:34:05.455964+00:00: aws-intel running at `41fbb315`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `6d3790c4`: builder-write qualified AA, all59validation commands pass; fixed screen next; aws-arm running at `00271fef`: count-one-decoder-candidate-validation.

- 2026-10-19T02:34:41.699502+00:00: aws-intel running at `41fbb315`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `6d3790c4`: builder-write qualified AA, all59validation commands pass; fixed screen next; aws-arm running at `5f2f9e57`: duration-AA-failed; fixed-screen-ready.

- 2026-10-19T02:40:04.224630+00:00: aws-intel running at `41fbb315`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `f3fcad10`: BUILDER-WRITE-001 rejected; full-chunk move assembly/census investigation; aws-arm running at `5f2f9e57`: duration-AA-failed; fixed-screen-ready.

- 2026-10-19T02:42:16.063974+00:00: aws-intel running at `543e0af1`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `f3fcad10`: BUILDER-WRITE-001 rejected; full-chunk move assembly/census investigation; aws-arm running at `5f2f9e57`: duration-AA-failed; fixed-screen-ready.

- 2026-10-19T02:42:52.441837+00:00: aws-intel running at `543e0af1`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `0f69ae28`: FULL-CHUNKS-001 census/profile/proposal frozen; fresh AA next; aws-arm running at `5f2f9e57`: duration-AA-failed; fixed-screen-ready.

- 2026-10-19T02:44:33.322000+00:00: aws-intel running at `543e0af1`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `90aa9a0e`: FULL-CHUNKS-001 AA qualified; isolated correctness build running; aws-arm running at `23433379`: decoder-B-screen-running; A-and-root-complete.

- 2026-10-19T02:47:48.575554+00:00: aws-intel running at `543e0af1`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `f8eb45f6`: FULL-CHUNKS-001 correctness and independent review pass; fixed144process screen next; aws-arm running at `23433379`: decoder-B-screen-running; A-and-root-complete.

- 2026-10-19T02:51:36.054983+00:00: aws-intel running at `543e0af1`: iterator referee1920checks pass; sampling controls66/66 known-work,0disabled;24scoped captures running; aws-amd running at `b02b79b3`: FULL-CHUNKS-001 rejected; baseline query-length codegen investigation next; aws-arm running at `f2549243`: decoder-PARK; unchanged-update-validation.

- 2026-10-19T02:52:44.829707+00:00: aws-intel running at `58ee8315`: iterator cache all validation gates pass; fixed exploratory screen frozen; aws-amd running at `b02b79b3`: FULL-CHUNKS-001 rejected; baseline query-length codegen investigation next; aws-arm running at `e4c5398b`: update-profile-analysis.
