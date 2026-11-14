# H2 supplemental public-API guard preparation

Ready for controller review and freeze; no guard performance result exists. [PROTOCOL.md](PROTOCOL.md) specifies cases, fixed counts, A/A controls, timing/memory gates, scope and consultation. [guards.c](guards.c) is independent of the frozen lookup referee and accesses only public tree APIs.

Local correctness completed216 cells: baseline/H2-B/H2-C × native/ASan-UBSan × seeds17/29/43 × iterator/rank/churn ×1/2/5/8 sweeps. All passed, with exact same-mode candidate/baseline output equality including memory. No local timer or measurement mode was executed. Compiler/source/referee/binary identities are in [correctness-manifest.json](correctness-manifest.json); process stdout, stderr and return codes are in [correctness/](correctness/). Local binaries stay ignored under `local/`.

The supplied driver `python3 experiments/ARM-LOOKUP-CONT-001/guards/verify.py` only builds and runs correctness mode against the existing isolated sources. It fails on the first unsuccessful process, retaining that process record. It does not perform fleet operations or performance collection.

Build from the repository root with `sh experiments/ARM-LOOKUP-CONT-001/guards/build.sh SOURCE OUTPUT native` (or `lto`, with the intended compiler environment). This command builds only. The executable interface is `OUTPUT verify|measure iterator|rank|churn SEED SWEEPS`. Only `verify` is authorized locally; it rejects counts above8 and emits no elapsed field. Measurement mode requires an even sweep count and executes the fixed1,000-sweep warmup. The fleet controller must enforce the protocol's exact case counts and cohort qualification; the executable itself does not manage fleet reservations.

JSON output includes verified/mode/case/seed/sweeps/ops, successful items, rank_sum, score_sum, weighted_sum, mutation_api_calls, and owned_bytes_before/after. Measurement mode adds elapsed_ns. An iterator operation is one returned element; a rank operation is one query; a churn operation is one delete/reinsert pair, also reported as two mutation API calls. Both memory endpoints must be retained. Churn checksum scores describe inserted values; independent final-state checks validate stored results.

This preparation author was previously the independent H1 reviewer and is now the guard implementer. An independent reviewer must assess this new referee before acceptance; H1 review independence does not transfer to the new harness. No original source, referee, fleet state, commit or remote repository was changed.
