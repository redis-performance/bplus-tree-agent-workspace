# Portability cleanup staging review

Decision: **PASS for retiring the superseded timers only**. This is not harness, image, workload, performance, or adoption admission. H2 remains PARK.

The reviewer independently queried the staged service properties and Docker identities at 2026-11-14 04:53:08 UTC. The deployed cleanup SHA-256 is `115b44d09b7d64ec59c005b4f9c54b0acd8584188594cd182f5d933efb691f1c`; the deployed lease SHA-256 is `5b3a145241fcc9c1e6678cacbe95357689bb385194ab697bbc67fc669898abd0`, exactly matching the prior code review and proposed lease. Both new cleanup services invoke that script with the same immutable lease generation.

Both replacement timers are active, scheduled for 07:12:00 and 07:15:30 UTC on November 14. Their accuracy is one microsecond and randomized delay zero. Both services are inactive with MainPID zero and have Type=exec, TimeoutStart=180 seconds, RuntimeMax=180 seconds, TimeoutStop=15 seconds, KillMode=control-group and SendSIGKILL=yes. Both superseded timers were still active during this review. Retiring them is a separate controller operation that must be verified afterward.

The seven unrelated stopped containers have exactly the same immutable IDs, names, state, labels and mounts as the retained pre-stage snapshot. No running or task-owned containers or task-owned processes were found. The work service has MainPID zero; the original coordinator identity is stopped; the sibling CPU remains offline; and the profiler remains inactive with empty CPU-affinity policy. These are point-in-time observations, not a guarantee against subsequent changes. The correctness driver must revalidate replacement timer schedules, command/generation, service caps, timer precision, and both retired timers' inactive state before and after its phases.

The original staging attempt stopped before mutation because it rejected any historical Docker container. Its failure artifacts are retained. The revised staging preflight permits unrelated stopped containers while still rejecting running or ambiguously owned containers; no pruning was performed.

The independent probe invoked no cleanup entrypoint, workload, container launch, or service mutation. It imported the reviewed deployed module to use its read-only identity checks. That import did not disable Python bytecode caching, so it may have created a bytecode cache file; this narrow filesystem caveat is retained in the private provenance. Subsequent probes must disable bytecode writes. Raw receipts and identity details remain private.

## Retirement follow-up

At 04:54:36 UTC a second independent read-only probe confirmed both superseded timers inactive and both replacement timers still active. The fetched operational record matches the controller's local bytes, SHA-256 `56d34f068a4af2e4dbab92fa63f55c79dccba6f751f761bf7bdaf032b671701f`. It binds the reviewed cleanup/lease, generation, container labels, timer schedules, command hash, caps, precision and retired names. The actual profiler unit named by that record is loaded, inactive, MainPID zero, with empty affinity policy. This second probe disabled Python bytecode writes. The first probe used a generic profiler unit alias, so the second observation is the authoritative unit identity check. The controller retirement receipt is retained alongside this independent observation.

