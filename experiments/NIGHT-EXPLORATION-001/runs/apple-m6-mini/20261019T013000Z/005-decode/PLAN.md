# M6 DECODE-001 — single-score scalar policy

Frozen hypothesis M6-DECODE-COUNT1-001: replacing only count==1 in the all-bulk
private policy with the original scalar decoder reduces width60/forward/count1
materialized-output time by at least2%, while preserving every larger-range helper
and all guards. This is a private helper experiment; public tree source stays frozen.
Control is root source plus byte-identical EXP-007 B helper from EXP-008 referee and
its all-bulk policy. Three candidate policies start from exactly that source.
ITERATE-001 is skipped. Cutoffs4/8/16 are excluded.

Primary: width60, forward, count1. Required guards: widths0/8/31/57..64, both
orientations, counts1/2/4/7/8/16/32/96, 8 leaves:176 cells including the primary.
Correctness additionally covers widths0..64, zero/max shifts, partial and empty
ranges, finite extremes, exact signed-zero bits and output canaries. Materialized
double arrays, compiler barriers and four checksum chains are identical. All eight
leaf objects have equal bytes for matched fixtures; no tree-owned metadata changes.
Count1 fixture deltas are zero and seeds are input-invariant: fresh seeds cannot
be described as fresh input diversity. Larger ranges use matched generated seeds.

Driver revision copies the existing referee, raises maximum rounds to100million,
uses one measured sample/process and warmup min(rounds,1024). It preserves original
--self-test and unchanged tests/test_decoder.py. --extended-test adds all eight
required counts in one process, with2080 geometries/build and existing bit-packer,
partial/empty/canary oracle. Timed loops have no sampler in release builds.

Calibrate base only: three observations/cell at10000 rounds; freeze rounds to
ceil(50ms / fastest observed ns/round), capped at100million decoded scores.
Then baseline A/A and each A/B comparison cover all176 cells in six process-level
ABBA blocks, seeds1/2/3/1/2/3, rotated and reversed cell order on odd blocks.
Every phase has4224 serial processes,300s wall budget,120s child cap,03:06:30UTC
cleanup cutoff. No tests/builds/profiles overlap timing. Partial phases are retained,
never restarted. Fine qualification requires every control block within±1% and
every window >=10ms. Unresolved noise means PARK; one fixed exploratory comparison
is allowed without qualified controls. No diagnostic retry is planned.

Selection requires primary <=−2% in every block and no guard block above+1%,
plus all qualified controls and equal leaf-owned memory. Otherwise NONE/PARK or
REJECT if primary fails. No best noisy sample ranking. If multiple clear discovery,
choose smaller generated code then smaller source policy. A provisional exploratory
lead may be retained with exact missing evidence. Eligible discovery needs separately
preregistered fresh A/A+confirmation seeds101/102/103, profile validation, independent
confirmation and adversarial review before adoption. Missing gates cannot be waived.

Both population steps will be three sequential passes by the same Codex worker,
not independent agents. Exact serving model/backend and cost are unknown; visible
identity is GPT-6 family. Session rules permit sequential fallback; no agents spawned.
Source/referee pins are acknowledged coordinator commit plus exact frozen hashes.
No Git worktree retry after earlier denial; isolated copied source/build directories
record exact hashes. Publication coordinator alone writes Git.
