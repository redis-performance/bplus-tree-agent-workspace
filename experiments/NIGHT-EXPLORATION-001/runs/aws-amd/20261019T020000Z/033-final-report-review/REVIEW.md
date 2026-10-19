# Final draft and release evidence review

No material population-count or outcome contradiction was found in the morning draft reviewed after main `a51d1a0ac`. Eight measured AWS populations remain zero accepted, five rejected and three parked; source and architecture replications are separate. The corrected baseline table, retained patch inventory, AMD outcomes and ARM historical-mask primary PARK agree with the published evidence inspected.

Scope: read-only review of the private morning draft, public release auditor and tests, published release-action preflight, existing 06:26 release inspection, corrected baseline audits/chart validation, reporting audit/resolution and ARM mask-screen audit. No draft or main edits, new tests, measurements, builds, runner access or remote mutations were performed. This is a reporting/evidence review, not a fresh revalidation of every raw campaign row. I authored AMD campaign work and earlier cross-host reviews; exact inherited native model, token usage and monetary costs are unknown.

Two wording corrections were reported to root:

- Corrected Intel has two failing A/A blocks in one known-guard fixture, not two distinct guard fixtures. The recorded effects are −1.4174698% and −1.0467306%.
- ARM026 ran 570 validation commands: 536 correctness/fault executions (4 original suites, 512 mode executions, 12 oracle executions, 8 expected negative controls) and 34 preparation/build/inspection commands. Describing all 570 as correctness commands is imprecise.

The release auditor retains the reviewed nested systemd cgroup lookup, recursive descendant process checks and fail-closed query/enumeration errors. The proposed final proof still requires all three live coordinator PIDs, inactive owned slices, zero owned units/processes and no inspection errors. No further test execution was warranted by this read-only review.

The release action writes LEASE-RELEASED before stopping the slice and restarting OSS. Its timestamp therefore identifies release-attempt start, not restoration completion. The auditor checks marker/saved status are nonempty, without validating freshness or parsing the saved RUNNING status. Root should manually inspect a fresh marker and saved RUNNING status alongside live PIDs, and report the live verification time or interval rather than deriving an exact completion time from the marker. The retained 06:26 preflight has neither file on all three hosts, supporting that later files are new. The default one-minute timer accuracy can put the scheduled 08:00:20 read-only audit before actual timer firing; an early failed audit is not a restoration proof.

At review/publication, the campaign lease remains **ACTIVE until 08:00UTC**, with actual restoration pending. Root owns post-deadline verification, private fleet release and final publication. This report is not release proof.
