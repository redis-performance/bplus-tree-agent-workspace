# BOUNDARY-024 — score moves during live mixed-width SCAN

All16source/build/seed cells pass: unchanged control and EXP-004A/B/C, nativeO3/debug
and O1ASan/UBSan/debug, seeds70501/70507. Source adoption NONE; prior PARK unchanged.
This is correctness coverage, not a timing result or an optimization population.

The same live cursor spans natural widening,258cross-leaf score moves and two exact
signed-zero updates. Six independent sorted-model checks per cell pass, with full
current binary bytes/length/score checks, sampled rank/seek, full postmigration lookup,
parent/subtree/registry invariants and exact tree-owned usable bytes. SCAN interval
and continuous-anchor checks pass. Every member remains present. The independent
score vector changes only after each successful public UpdateScore; callbacks check
current score bits. Initial anchor count392809 and final393209 are local observations.

Observed movement classes per cell:235uncopied-source/copied-target,1copied-source/
uncopied-target and22copied/copied; zero uncopied/uncopied. Target class describes the
successor destination leaf immediately before the update; splitting can create a
new destination ID. This does not imply a direct relabel in the old narrow table.
There are2158active mixed-width SCAN calls before completed-wide state. Append stops
before score mutation, preserving its ordered-input precondition. The same cursor
terminates within16384groups and every initial anchor appears.

Both isolated deliberate faults are detected by successful sanitizer binaries:
omitted destination insertion in zbtIndexMove and stale packed in-place score bits.
The latter is caught by exact signed-zero checking. No existing check was weakened.
See [plan](PLAN.md), run.py, manifest.json, summary.json, oracle.patch and faults/ for
exact commands, UTC endpoints, stdout/stderr, hashes and patch provenance. Snapshots
remain uncommitted under scratch/; main source/referee unchanged. Reviewer startup
failed; review and confirmation are sequential, not independent agents. Exact model,
backend and token cost unknown. Performance guards and committed provenance remain open.
