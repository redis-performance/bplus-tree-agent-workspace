# HARNESS-005 — new ordered and signed-zero iterator fixtures

Locally validated separate referee revision. Release and ASan/UBSan each pass 1,408
fixture cells (640 original +768 new), original43tests and five invalid-input checks.
Three intentional length/sign/state faults detected. The first fault driver failed
because its expected assertion text did not match the adapter; the actual length fault
was caught. Original failure retained; continuation ran only the remaining two faults.

Exact score bits/full bytes/order/state-copy/sentinels remain checked before/after timing.
Big-endian IDs only for alternating-zero numeric ties. Construction orders and high-bit
checksum folding described in [plan](PLAN.md); no timing pooled with HARNESS-004.
All snapshots/hashes/commands/logs retained; main source/referee unchanged.
Independent reviewer startup failed; sequential review only. Backend/model/cost unknown.

Decision: fifth locally validated harness, commit review pending. AA-010 preregistered.
New fixtures never replace old guards. CPU MCP05/14 consulted for observability/result
consumption; unrelated ask passages not cited. No M4 numbers transferred.
