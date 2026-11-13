# Investigation status

STARTED 2026-11-13T22:19:24.579974+00:00

Controller: Codex; model and token costs unavailable. Branch investigate/arm-lookup-gap-20261113, prepared commit b0775e790. Reading source qualification and mandatory consultation protocols. No fleet reservation or measurement yet. No candidate selected.

Baseline corrected to upstream unstable `ee8e7f70152404649ac947157fd662d11b4a00d5`, fetched and verified 2026-11-13T22:25:57.664440+00:00. No performance workload had started. See unstable-manifest.json; correctness and fixture requalification now runs on the refreshed extraction.

2026-11-13T22:27:28.177211+00:00: unstable refresh qualification PASS: 57 native + 57 sanitizer upstream tests, 12 native + 12 sanitizer fixture cells. Bounded ARM fleet lease acquired; no timing launched before this gate. Next: frozen 48-row A/A and baseline profiles.

2026-11-13T22:27:45Z: current-unstable campaign launched on reserved ARM fleet host, source/referee commit 4876d21ce62fdf9306572b690c891d2d5ed0e04d. Fixed A/A and separate baseline profiles executing serially in a 20-minute bounded unit; independent 90-minute release timer armed.

2026-11-13T22:31Z: qualified baseline complete (48/48 rows;12/12 blocks). Three actual independent proposal agents A/B/C started after baseline profile and cpu-perf reconsultation. Baseline report and raw summaries preserved. No candidate selected.

2026-11-13T22:36Z: all three implementations pass native/sanitizer upstream and fixture checks, unchanged-referee hashes, and90,000 optional-output sanitizer oracle checks each. Fixed144-row ARM discovery comparison executing serially; no results selected. Independent adversarial reviewer is auditing source, fixture and baseline evidence.

2026-11-13T22:46:41.957002+00:00: COMPLETE — REJECT/source selection NONE.144/144 discovery rows complete; no variant meets primary gate. Final upstream unchanged. ARM released and fresh heartbeat/queue checks pass. No queued work. Independent final review COMPLETE: no unresolved blocker for reporting this bounded rejection.
