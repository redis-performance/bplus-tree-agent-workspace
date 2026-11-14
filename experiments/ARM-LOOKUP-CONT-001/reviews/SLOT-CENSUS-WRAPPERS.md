# Slot census staging and launch wrapper review

**PASS for the reviewed wrapper code and operations-stage admission.** Staging is permitted only within its fixed window after the separate source-stage approval. Actual successful staging, build-phase approval, emitted-code review and census-phase approval remain required. This review runs no SSH, systemd, Docker, C executable or fleet workload.

The initial wrappers and findings are preserved. The final staging wrapper uses structured positive source-stage and operations-stage decisions with strict integer schema versions, exact source-freeze/driver/wrapper hashes and complete input mappings. It no longer treats a hash appearing in prose as approval. Source approval `9006af641be4a0f942b66f122884f4faf19ca88d3cef20cde2463bc76d14b47b` joins the independently reviewed source freeze `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` and [source review](SLOT-HINT-CENSUS-CODE.md), whose hash is `2fdf6f493648a950abf0167e99b6ac34651075eeedb3066d1ba50150a430cb91`.

Remote staging enforces 05:45–06:30 UTC at entry and again after post-staging isolation immediately before issuing STAGED. The distinct execution deadline remains 06:45 UTC. It checks the exact existing lease and cleanup implementation, rejects owned containers/processes and nonempty work cgroups, and performs the pinned full infrastructure audit before and after upload. Existing input files must match their approved hashes; new files use exclusive creation. Dangling target symlinks and symlink parents are rejected. Duplicate paths, unsafe archive members, existing driver/source destinations and reused staging claims fail closed. Failed staging preserves its partial artifacts and ERROR record; it cannot generate a successful receipt.

The launcher checks the exact complete successful staging receipt locally and remotely before reset/start. Config, review, source, driver and staging hashes must join. It rejects occupied phase/review/launch paths before service mutations, checks owned process/container/cgroup absence, invokes the reviewed driver admission and full pinned infrastructure audit, and recomputes sufficient remaining budget after that audit. Only then may it reset the exact idle failed work unit and create its exclusive review/launch receipts.

The service entry uses the unchanged bounded-command wrapper with the absolute 06:45 ceiling. Relative service limits remain at most 900 seconds for build or 240 seconds for census, with 15 seconds stop allowance. Type=exec, TimeoutStart=30 seconds, SendSIGKILL=yes and KillMode=control-group are explicit. Selected actual service properties are captured for later operational evidence review. A delayed activation cannot renew the absolute command budget. No new image or expanded cleanup ownership is introduced; unrelated containers are not removed. The closed portability window and original lease are not rewritten.

All **17 synthetic wrapper tests pass**. Local tests reject negative or malformed source/operations decisions, Boolean schemas, wrong script/driver/source joins, incomplete mappings, out-of-window staging, reused config files, failed/partial/extra-field staging receipts and incorrect phase-review hashes. Embedded remote-code tests cover successful exact uploads without rewriting matching existing inputs, entry/post-audit cutoff checks, owned work and cgroup rejection, dangling symlinks, mismatched existing inputs, failed isolation before source upload, duplicate reviews, absent/failed receipts, late preflight, absolute service ceilings and both mode-specific service caps.

The tests use temporary filesystem trees and relocate only the embedded root/cgroup paths. SSH, subprocesses, systemd, Docker and live isolation/admission boundaries are mocked. Original source bytes are copied and hashed as data; no C is compiled or run. These tests establish guard and orchestration behavior, not actual source semantics, live reservation state, target code generation or structural count validity. The separate 21-test driver review remains applicable.

| Artifact | SHA-256 |
| --- | --- |
| Staging wrapper | `9e9a20dd04d2918502ea4b97be5aee0e85052e8d0a73669ba3e147149010aa16` |
| Launch wrapper | `29a7393886a0321babbc0355d8d0d97ae1feea37a53fe6992f4665c98a75e88c` |
| Operational driver | `7bd5dbb22a00363232a5b914628d6ecf96f4f9be0c52e02f09c685ce74a359a8` |
| Independent wrapper tests | `cc67d53949db9cfa5698eb9b39214b1988f516c12dfed3ce43f8e7bf1928d1bb` |
| Test log | `26c50c7449e552f65235d044a4e22e933dbe7155eced12c7dedf9e444f52298c` |

A phase-specific operations-stage JSON binds these exact bytes, full required inputs, the source admission and fixed deadline. It cannot authorize build or census execution because those phases require their own actual-staging-bound approvals. No speed, qualification, adoption or new performance-population conclusion follows; H2 remains PARK.
