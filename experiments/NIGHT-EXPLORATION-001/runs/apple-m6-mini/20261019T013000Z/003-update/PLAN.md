# UPDATE-001 — M6 distinct public update paths

Preregistered before timing in round 2, 19 October 2026. Baseline source unchanged.
Host provenance: ../launch-manifest.json, launcher verified Apple M6 / arm64 / 12
cores / macOS 27 / Apple Clang 21; worker sysctl denied and not retried. Frequency,
DVFS, performance-core residency, migration and PMU observations unavailable.

Reuse the published M1 score patterns, with exact origin commit/source hash recorded
in harness-origin.json. The M6 referee adds one explicit warmup protocol: run the
operation on a duplicate, free it, then read every member of the timed original.
The original preserves its initial scores/layout. No tree construction, clone,
warmup, final verification, profiling or instrumentation inside measurement windows.
Timing includes public FindForAdd + UpdateScore, target computation and checksum.
One process/one batch; no subtraction. Independent build/query permutations and hash
seeds use separate streams. Exact 16-byte binary keys; long-member semantic guards.

Cases at 100 / 1K / 10K / 100K / 1M, discovery seeds 1/2/3:
- same: score unchanged;
- preserve: 4*id+1 <-> 4*id+2 strictly between neighbors;
- nearby: each even member moves across its odd neighbor, +2/-2;
- distant: first quarter moves between original scores and scores above the full set;
- plus-n: original monotonically increasing score+N retained separately (not reversible).

Validate all five patterns/five sizes native and ASan/UBSan before timing. Additional
8/319/320/321/1024-byte pattern checks at 1K, plus finite/signed-zero/tie oracles with
binary variable lengths and clones. Never change existing upstream checks. Untimed
instrumentation counts successful in-place, preceding/following order failures and
exact pack failures. Public scoped self-profiles at 10K/100K/1M for preserve/distant;
release assembly and two sampler-probe controls. External profiler attachment already
failed round 1; no retry/permission change. Self-samples are diagnostic PCs, not exact
runtime shares, cycles or a PMU profile.

Calibrate all 25 baseline cells: three 200K-op observations each; choose fixed counts
from fastest observation for >=50 ms, cap100M. Save every row. A/A six ABBA blocks,
seeds1/2/3 each twice, position preserving at100K and1M. Strict ±1% every block, >=10ms
all windows. Fixed same-session serial timing; no other builds/tests/profiles/analysis.
Inventory: seed1 calibration rows plus new fixed-count observations seeds1/2/3 only
if useful and within300s phase budget. No repeated failed schedule; at most one causal
noise diagnostic, only with a specific question.

Default potential optimization primary preserve100K/16, second1M. All patterns/sizes,
long members, lookup/rank/iteration and memory are required before adoption. No
hypothesis is selected yet. Only after profile: three sequential proposal passes/chair
(or independent agents if explicitly permitted), then three isolated implementations
of one hypothesis. Preserve patches. No primary relabeling. NONE is a useful result.
Exact serving model/token cost unknown; visible Codex/GPT-6 family. No agents so far.

Coordinator owns Git writes. Freeze evidence first, request publication, remain idle
until matching ack (5s polls/120s maximum). Pin acknowledged commit and hashes before
comparison. If no ack, record pending provenance and continue bounded local diagnosis.
Never write baseline src/, upstream integrations or another host's evidence.
