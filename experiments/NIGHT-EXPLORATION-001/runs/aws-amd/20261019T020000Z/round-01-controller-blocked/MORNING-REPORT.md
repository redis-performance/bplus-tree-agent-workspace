# AWS AMD early blocker report

This is an early report for round 1, not a claim about the completed overnight campaign. Only the assigned aws-amd host is in scope; no other host was accessed.

Outcome: NONE. Controller shell initialization failed with `bwrap: setting up uid map: Permission denied`. The runner configuration and existing baseline could not be inspected. The baseline was already launched at 8fab511e according to the supplied instructions; its actual result remains unknown. No additional remote workloads ran and no source was adopted.

Rejected or parked directions: none evaluated in this round. The user-supplied rejection of shorter-side rank accumulation remains a constraint, not a newly measured result.

Missing gates: baseline evidence retrieval and hash validation, native/sanitizer verification, profile and duration calibration, A/A, candidate population, ABBA primary/guard/memory measurements, fresh confirmation, profile validation, and adversarial review. No benchmark or chart counts can be updated from new measured data.

Next action: restore the configured controller execution capability, then follow [HANDOFF.md](HANDOFF.md) to inspect and harvest the existing baseline without duplicating it. See [BLOCKED.md](BLOCKED.md) for the precise failure and [STATUS.md](STATUS.md) and [ACTIVITY.md](ACTIVITY.md) for the round record. Publisher integration is pending; no Git write was attempted. Do not alter runner release controls or extend the 08:00 UTC deadline.
