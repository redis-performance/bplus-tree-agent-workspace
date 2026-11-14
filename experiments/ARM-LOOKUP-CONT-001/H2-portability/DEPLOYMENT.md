# Portability deployment inputs

Preparation only. Root owns any future image construction, fleet admission and cleanup. This document is not execution approval. The named-container cleanup and both replacement timers must be independently reviewed and live before installation or driver work; retired timers must be inactive.

Canonical image procedure, separately reviewed and bounded by root:

1. Verify `files.json`, exact original/B sources, full base image ID and new lease generation. Stage exact B C bytes as `H2-B-source/zset_btree.c`; all other original inputs retain their paths.
2. Create the exact `RUN_ROOT_BASENAME-portability-image` container from base `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`, read-only task root at `/work`. Its command is `sh /work/experiments/ARM-LOOKUP-CONT-001/H2-portability/prepare-image.sh`. Supply all three labels below, a bounded resource policy and the reviewed600-second preparation cap. Network is allowed only for this installation stage. Save exact create/start output and return codes; no unattended retry.
3. After successful installation, commit only that exact inspected owned container ID to a new task-owned image. Set image labels `h2.portability.base` to the full base ID and `h2.portability.prepare` to the frozen prepare-image.sh hash. Preserve inspect/config/creation evidence and exact full derived image ID. Do not modify the base tag/image or host packages. Remove only the exact owned preparation container after proof capture.
4. Review the derived image/operational record and run only `driver.py --mode image-receipt` with exact pins. The named check container has no network. Fetch/review receipt plus exported apt/package/tool/library evidence. No guest C workload is run by this mode.
5. A separate independent correctness review binds the exact receipt bytes, input manifest and derived image ID. Only then may root invoke correctness mode. No retry on a consumed phase. Fetch private ELFs and evidence before optional removal of the exact derived image. No image/volume/container pruning.

The three exact container labels for both preparation and check containers are:

- `org.redis-performance.cleanup.owner`: `bplus ARM-LOOKUP-CONT-001`.
- `org.redis-performance.cleanup.root`: exact absolute reviewed run root.
- `org.redis-performance.cleanup.generation`: exact32-hex reviewed lease generation.

Container names are exactly root basename plus `-portability-image` and `-portability-check`. Cleanup must validate names, all labels and immutable container ID before reaping; any mismatch blocks coordinator resume. The driver does not force-remove containers after a failed client; independently reviewed cleanup retains that responsibility.

`driver.py` requires `--root`, `--mode` (`image-receipt` or `correctness`), `--image-id` (full sha256 content ID), `--manifest-sha256` (files.json), `--isolation-record`, `--isolation-sha256`, `--review`, `--review-sha256`. Correctness additionally requires `--image-receipt` and `--image-receipt-sha256`. No candidate/seed/mode selector can alter the correctness grid.

The operational record inherits the reviewed Q4 operational fields/schema (owner, run_root, deadline, lease_sha256, coordinator PID/start_ticks, saved Parca state, two cleanup timer schedules, target-service ExecStart hashes, cleanup artifact hashes and restoration/reaping obligations). Its Intel extensions are:

```json
{
  "base_image_id": "sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460",
  "lease_generation": "<reviewed32hex>",
  "task_started_epoch": 1000,
  "task_deadline_epoch": 2800,
  "containers": {"image":"<root-basename>-portability-image", "check":"<root-basename>-portability-check"},
  "container_labels": {
    "org.redis-performance.cleanup.owner":"bplus ARM-LOOKUP-CONT-001",
    "org.redis-performance.cleanup.root":"<absolute-run-root>",
    "org.redis-performance.cleanup.generation":"<same32hex>"
  },
  "cleanup_contract": {
    "containers":{"image":"<root-basename>-portability-image", "check":"<root-basename>-portability-check"},
    "reap_containers_before_resume":true,"restore_sibling50":true,"ownership_required":true
  },
  "cleanup_service_properties": {
    "Type":"exec","TimeoutStartUSec":"3min","RuntimeMaxUSec":"3min",
    "TimeoutStopUSec":"15s","KillMode":"control-group","SendSIGKILL":"yes"
  },
  "timer_properties":{"AccuracyUSec":"1us","RandomizedDelayUSec":"0"},
  "retired_timers":["<old-primary.timer>","<old-backup.timer>"]
}
```

Durations match canonical `systemctl show` strings:3min=180000000µs,15s=15000000µs,1us=1µs. Exact strings and all schedules are live-checked. Record cleanup artifact pins include the exact implementation and its generation-bound invocation; these fields do not replace independent code review.

Each independent review JSON requires schema_version1, decisionAPPROVED, nonempty reviewer_role, isolation_sha256, manifest_sha256, phase exactly matching the invocation, and image_id. The correctness review additionally requires image_receipt_sha256. The driver checks exact review-byte hashes throughout. A valid image review cannot admit correctness and a review for another generation/image/manifest fails.

Outputs use atomic single-use directories `H2-portability-image-receipt-001` and `H2-portability-correctness-001`. Repeated invocation rejects existing directories, including failed/partial phases. Result status is IMAGE_PREPARED, CORRECTNESS_COMPLETE or INCOMPLETE_OR_UNSUPPORTED. None is a performance qualification or source adoption; H2 remains PARK.

The task timestamps above are illustrative schema values, not an approved window. Root fixes actual task_started_epoch/task_deadline_epoch once before image preparation. The interval must be at most1800seconds, ending at least300seconds before lease expiry. Every driver invocation shares that absolute deadline, so image preparation/review time cannot silently reset the budget. All subprocess timeouts clamp to the remaining task/lease/timer margin.

Every compile, image-metadata and guest command now executes through `bounded-command.sh` inside the named container. The driver freezes an absolute ceiling equal to the earliest per-command cap, shared task deadline, lease margin or timer margin. After Docker startup, the shell recomputes remaining seconds using `/usr/bin/date`, reserves15seconds for KILL escalation plus2seconds exit margin, and invokes GNU `/usr/bin/timeout --signal=TERM --kill-after=15s` with positional arguments unchanged. Thus the2/5-minute total caps include startup and termination grace; a delayed launch cannot renew its allowance. Missing tools or nonpositive remaining budget fail without fallback. Host client wait includes the reserved grace; external cleanup still handles daemon/client failures. The image receipt records timeout/date hashes and GNU timeout version. No local wrapper or guest workload was executed. Prior client-only timeout freeze remains in revisions/implementation1.
