# EXP-009 — guarded physical-slot lookup on Apple M6

Status: PREPARING; source selection NONE. Root owns this follow-up, newly authorized after the overnight campaign closed. All checkpoints, raw timing rows, patches and decisions publish to main. Other sessions: do not run M6 timing or change these frozen inputs while the measurement lease is active; retain separate host data and publish your own ownership/status before work.

The historical 004-lookup B reduced successful-score-lookup elapsed time by 4.80% median at 100K (six blocks, qualified same-cell controls), but failed its dual-size acceptance gates. It used the legacy panic adapter. This is a hypothesis lead, not proof of a safe or M6-exclusive optimization. Historical results remain unchanged.

## Scope and prerequisite gates

Use current main's corrected panic adapter and unchanged tree as baseline. Inspect the actual source/codegen and collect fresh baseline profiles before the three independent proposals and chair. Qualify new same-session A/A controls before selecting a source hypothesis. Work is confined to src/zset_btree.c and .h; referee additions are a separate committed/frozen harness revision. No Redis server/integration or upstream actions.

Investigate a semantic dispatch condition, such as whether the caller requests a logical position. No tree-size threshold inferred from the old 100K result and no assumption that arm64 identifies Apple M6. An unchanged source fallback can still compile differently; check its generated code and measure affected paths.

## Preregistered performance contract

Primary cases: public successful score lookup, 16-byte members, 100K AND 1M members. Require at least 2% less elapsed time in every one of six paired ABBA blocks at both sizes. Same-binary A/A must be within ±1% in every block and every measured window at least 10 ms. Use fixed baseline-calibrated operation counts targeting 600 ms, with calibration cap 100 million queries. Discovery seeds 1/2/3 repeated; held-out confirmation seeds 501/502/503 repeated. No retry, post-result count adjustment, row exclusion or primary change after a completed schedule. Any failed primary control means PARK before source implementation or candidate timing.

Before acceptance: retain all original 40 standard cases, 30 key-length/hit/miss/mixed lookup cases, six public batch cases and 25 update cases from the 006 frontend inventory; explicitly add correctness coverage of all four score/position output combinations, reversal, widths 0..64, finite/signed-zero scores and binary members. A missing or unqualified guard cannot be called a pass. No demonstrated >1% regression in guard time or tree-owned memory. Guard calibration/replication limits are frozen separately before execution, never copied from historical runs. Candidate validation includes unchanged native and ASan/UBSan tests, exact-bit private oracle and deliberate-fault sensitivity.

Three actual independent proposals plus chair; only if prerequisites pass, three isolated implementations from the exact same source commit plus measured selection. Keep every patch, including losers. Fresh confirmation, matched candidate profile, independent raw audit and adversarial review are mandatory for acceptance. Hardware counters remain unavailable unless supported without permission changes; sampled locations are not cycle shares. If evidence is absent choose NONE/PARK.

## Execution and publishing

Serial native work on the user-authorized local M6. Root owns launches and main publication. Preparatory agents may inspect/read only; all agents idle before measured work. Each phase has a fixed immutable input/binary manifest, write-once output paths, command timestamps and a bounded child/process-group cleanup. Baseline qualification phase maximum 10 minutes wall; overall follow-up maximum 90 minutes after the published launch, with no extension or rerun to chase a pass. A blocked prerequisite ends the experiment with a concrete result and revisit condition.

Historical counts remain 12 M6 candidate populations, 0 accepted / 7 rejected / 5 parked, 36 patches, 15 harnesses. This preparation is not a completed population or accepted optimization. Backend visible as Codex/GPT-6 family; exact serving model, token and currency costs unknown. Record actual participants and outcomes, never invented independence.

## Shared status

See [STATUS.md](STATUS.md) and [status.json](status.json). Current source and referee identities are in [baseline-identity.json](baseline-identity.json). Historical findings: [lookup B](https://github.com/redis-performance/bplus-tree-agent-workspace/blob/85afa6c7b798130452ca9dbd63082337e8bd78b7/experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/004-lookup/RESULTS.md).
