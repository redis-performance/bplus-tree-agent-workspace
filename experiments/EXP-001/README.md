# EXP-001 — standalone baseline qualification

Date: 2026-10-17. Status: LOCAL EXPLORATION COMPLETE. Decision: QUALIFICATION PARKED.

The user explicitly authorised local microbenchmarks. The [M1 run](local-m1-2026-10-17/README.md)
completed 144 processes / 984 rows and four sampled profiles with unchanged source.
All result checks passed; only 1/41 cells met the preregistered precision/duration gates.
Raw results, MCP methodology, codegen, allocator evidence and next controls are recorded.
The original qualification plan follows; its remaining gates are still open.

Objective: establish a reproducible control for direct B+ tree API microbenchmarks before
proposing optimisations. No candidate, population winner or accepted speedup exists.

1. Select a dedicated native runner and record compiler, CPU, allocator and affinity.
2. Pin the workspace commit and hash release binaries; run correctness and sanitizers.
3. Select a bounded matrix from docs/MICROBENCHMARKS.md, including 319/320/321-byte members.
4. Calibrate operation counts/durations. Run the same binary as A and B for at least
   three ABBA blocks per chosen cell. Check whether precision resolves the 1% guard.
5. Capture baseline profiles of the chosen hot path; separate setup from hot-loop evidence.
6. Freeze primary/guard cases and fresh confirmation seeds. If noise remains unresolved,
   PARK baseline qualification with a concrete next action.
7. Only after qualification, open EXP-002 for three proposals and chair selection.

Population steps are not applicable to this control-only qualification; both become
mandatory for candidate experiments. Record measurements here without retroactive wins.
