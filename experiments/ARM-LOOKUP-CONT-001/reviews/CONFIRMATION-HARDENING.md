# H2-B six-case confirmation hardening

Ready for independent review; no confirmation process or new A/A observation was collected by this worker. The controller states no previous confirmation ran. All fresh-seed A/A must use the independently reviewed revised collector. Source/ELFs and the active `fleet_compare.py` collector are unchanged.

Revised `fleet_confirmation.py` SHA256:
`1491e9dd9fede0f5c62ce5e04169a62b48626f04f56b799e6e47e3c1f7e2237b`.

The prior script is preserved byte-for-byte in existing Git commit `7152ecc9d0170c4f588d25ae5c096d04b726c0b7`, at `experiments/ARM-LOOKUP-CONT-001/fleet_confirmation.py`, blob `922a505d35f57b0b6434d29246f1ece959a20bd6`, SHA256 `20406fad12215890d512f24cca157f1a0d0ceae6bdcc7a260ffd3d499765bfd8`. No commit or push was made for this hardening.

## Concrete changes

- Only `--origin-phase H2-native|H2-lto` and seed29 or43 are accepted. Cohort, platform, scale, candidate source and both ELF paths/hashes are derived from four explicitly pinned completed origins: ARM native, ARM GCC15/LTO long-window, Intel native and Intel GCC15/LTO. Arbitrary phase/source/variant/binary labels are removed.
- Output is deterministically `<origin>-confirmation-<seed>`. An existing directory rejects the attempt, and atomic directory creation claims it before any fresh-seed process. Partial, failed and parked outputs remain consumed. There is no resume/retry flag or alternate phase-name argument.
- H2-B source is whitelisted as `63b18cd5aa70d455fb2639e826386045841052b8f2cea85e5b97f9018d829f29`. Eight baseline/referee/dependency hashes, the exact baseline/candidate ELF identities, and original metadata/analysis/raw-row/command-file hashes are pinned in the collector. The candidate's actual source file is hashed too. The original lookup harness remains `1e6dc19c9b0f49abafb75c67e3434a87cc6d7d5222049c90a68368755c2a5827`.
- Before fresh work, the collector reconstructs the original72 B comparison rows and their own72 cohort A/A rows. It verifies complete ABBA grids, process stdout/stderr and command joins, pinned ELF selection, seed17, exact per-case counts, fixture-model checksums, duration and per-block gates, plus reproducible memory endpoints. Origin metadata must identify the pinned upstream source and a passing B comparison; the correct cohort qualification must pass. The old failed LTO qualification is never substituted for its separately qualified long-window cohort.
- Comparison is self-contained. No invocation or mutation of `fleet_compare.py` remains. The caller supplies the independently reviewed SHA256 of this collector through `--collector-sha256`; it is checked before work and before/after every child process.
- Every child process is preceded and followed by identity checks, current exclusion-file checks, and live lease/isolation checks: exact owner and RESERVED state, cleanup margin, original coordinator PID/start ticks and stopped state, unchanged lease identity/deadline, active release timer, controller affinityCPU0, expected architecture, measurement CPU2 online without an active SMT sibling, and no Docker containers. Intel additionally requires recorded sibling-state provenance, CPU50 offline, and Parca explicitly inactive. A zero-work child verifies effective affinityCPU2 without relying on Python assertions.
- Each seed first runs fixture verification and all72 A/A observations, then compares only if all18 blocks qualify. Comparisons retain all72 rows/18 blocks. Counts, warmup within the immutable ELF, ABBA order,250ms minimum,±1% A/A and1% guard/memory limits are unchanged. ARM hit confirmation retains2% improvement per block; Intel portability follows its preregistered≤1% hit-regression requirement. No cross-platform timing comparison occurs.
- Model checks reject changed case/seed/ops/hits/score sums, invalid duration/memory fields and inconsistent repeated memory. Fresh comparison baseline memory must match its own fresh A/A. Processes record command/return code/stdout/stderr, preflight success and separate postflight success. Exceptions and timeouts preserve available raw process evidence and the consumed phase; PARK/FAIL/ERROR never implies source adoption.

## Offline validation

Imported the collector without side effects and reconstructed all four actual saved origin cohorts: four sets of72 qualification rows plus72 B comparison rows,576 observations in total. Each pinned provenance file matched the current retained copy. No measurement executable was invoked.

Twenty-nine focused negative checks rejected arbitrary/renamed/path-traversing phases, unauthorized seeds, bad row fields, duplicate slots, A/A noise, short windows, guard/memory regressions, excluded B, changed lease owner/state/deadline/coordinator identity, wrong controller affinity, Docker work, inactive release timer, active Parca, online Intel SMT, wrong architecture and a consumed output phase. Isolation tests mocked file/subprocess responses; they did not query fleet or local service state.

Twenty-two further isolated corruption checks rejected each reviewed collector, source/referee, provenance and ELF identity in the ARM-native configuration. Positive arithmetic checks distinguish ARM primary and Intel portability gates. Python compilation and whitespace checks passed. These are unit/offline checks, not performance qualification; the independent reviewer must assess the final exact bytes before fleet use.

## Invocation and remaining boundaries

On an authorized, isolated fleet host only, from its owned run root:

```sh
python3 experiments/ARM-LOOKUP-CONT-001/fleet_confirmation.py \
  --root "$RUN_ROOT" --origin-phase H2-lto --seed 29 \
  --collector-sha256 1491e9dd9fede0f5c62ce5e04169a62b48626f04f56b799e6e47e3c1f7e2237b
```

Use the actual owned root; the example does not provide runner identity or access. Native uses the original `H2-native` origin; the other seed is43. There is intentionally no caller-selected cohort, scale, variant or binary. The controller must admit sufficient lease time and serialize this work with every other collector. Checks at process boundaries do not prove continuous CPU-wide exclusion or independently validate clock accuracy. Deliberately deleting or modifying pinned evidence/output protections is outside the authorized workflow and must not be used to retry a failed seed. A changed-condition experiment requires new preregistration and review, not relaxed pins.

The pins intentionally fail if original evidence files are edited after review. Add subsequent reports separately; do not rewrite the frozen origin to make the collector proceed. Fresh-seed supplemental guards have their own collector/review and are not replaced by these six cases. Source selection remains NONE pending all required confirmation, matched-profile and acceptance gates.

## Provenance and TMA

This worker changed only the confirmation collector and this report for the task. No benchmark, timing, fleet query, source/referee/ELF edit, commit or push occurred. Backend is execution; exact model, tokens and cost are unreported. The worker's available-tool catalog has no cpu-perf/library_status tool. The controller's recorded consultation in `../CONSULTATION.md` is shared evidence, not this worker's calls; no retrieved passage establishes a workload mechanism. This is collector/control-flow hardening, not a new performance hypothesis.

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring remain unavailable as qualified categories for these unexecuted fresh-seed confirmations; qualified children are unavailable. No pipeline-slot or causal performance claim is made.
