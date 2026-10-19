# Round 1 handoff

Work stopped early after controller sandbox startup failed on the initial commands. No active job was started by this worker, detached or otherwise. The previously launched baseline may still be running; no claim is made about its state.

1. Restore controller command execution without changing campaign permissions or bypassing restrictions.
2. Read AGENTS.md, shared memory, population rules, campaign PLAN.md and MEASUREMENT.md, AWS-STATUS.md, prior reports, and ignored private worker configuration.
3. Verify only the assigned host through the prescribed read-only SSH query using its configured identity and BatchMode.
4. Poll the existing frozen 8fab511e baseline service and manifest; do not relaunch it. Coordinate harvesting through file existence and hashes. Preserve divergent files, failures, attempts, and raw rows. Sanitize logs before public copying.
5. Profile baseline and calibrate before any proposal or candidate work. All remote workloads after the baseline must use the configured bounded-job helper, with separate serial phases and CPU2 affinity. Check owned services before timing and monitor Intel sibling CPU50.
6. Preserve population, correctness, A/A, ABBA, confirmation, profiling, memory and adversarial gates. Missing evidence means NONE; unresolved noise means PARK. Do not adopt candidate source overnight.
7. Stop starting experiments at 07:15 UTC and preserve the 08:00 UTC release deadline. Leave lease, slice, supervisor and timers unchanged.

Publisher: integrate these blocked reports into canonical status and activity files after reading their current state. This worker could not inspect or update shared logs, README counts, charts or Git. No Git write was attempted or denied. No evidence was collected that would justify changing measured counts or charts.
