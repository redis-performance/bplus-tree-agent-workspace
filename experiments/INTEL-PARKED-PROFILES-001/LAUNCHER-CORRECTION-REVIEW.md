# Independent launcher correction review

**GO for the separate V2 collection attempt on unchanged prepared binaries.** No completed measurement is being repeated, and no timing acceptance is authorized.

[Archived failure audit](attempt1/INDEPENDENT-AUDIT.json) independently verifies all36 launches exited1 before readiness with numactl's CPU2 out-of-range error. There are zero TMA, counter or sampling captures. Preparation remains valid:177 successful commands,36 semantic configurations, eight43-test suites,12 cache oracles and221 source/driver hashes verified. Failure artifacts remain unchanged.

Reviewed diff: `collect-v2.py` changes only the protocol filename and adds `numactl --all` before absolute CPU2 selection. The controller remains pinned CPU0; workload affinity must still be exactlyCPU2. The bounded [affinity probe](attempt1/RELEASE-AND-LAUNCHER-PROBE.txt) reports `[2]`; coordinator restored and old job/timer inactive. No permission, cgroup, source, workload, threshold or binary change is part of this correction.

`resume.py` verifies all recorded build/source hashes before reuse, confirms36 empty-capture failed launches, and copies exact completed preparation evidence into the new results directory. It runs a fresh CPU2 affinity assertion under the controller's inherited affinity before collection. `run-v2.sh` retains the reviewed coordinator reservation/recovery/owned-process-group cleanup and substitutes resume for build/validation work. The recovery timer is separately named `bplus-intel-parked-recovery-v2`; old attempt identity remains intact. Existing L2 quality gates and no-retry policy are unchanged.

Actual collection can still fail quality; every failed/partial capture must remain unavailable. Original preparation copies are provenance reuse, not fresh validation runs. Coordinator restoration and final raw review remain required. Reviewer `/root/intel_b_review`, Codex; model/token costs unknown. Own MCP availability and concrete inventory consultation remain recorded in reviewer-consultation.json for this continuous session.

## Reviewed hashes

- `protocol-v2.json`: `11a8369d144710ad5ca724e202665168ad338ed7bf05129818169c380d74d112`
- `collect-v2.py`: `0a74ba56b227d42c35929e2c3984f55469e5f10206105a869af9eede5fdab0e7`
- `resume.py`: `9cbc8d29a5b08f159986ccbcdb2dcaeabfc084c6cb0ac5b0573338dae36824d5`
- `run-v2.sh`: `a79028b3579396101891ae57163fbf0dd97bba3aeb84a2faa974f4d7bcae28ba`

Reviewed UTC: 2026-10-20T14:22:46.419345+00:00
