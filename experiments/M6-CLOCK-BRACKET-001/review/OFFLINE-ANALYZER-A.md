# Offline controls analyzer A — ready

This helper is prepared before native data exists. It executes no controls, benchmarks, builds or native binaries. Participant `/root/followup_proposal_a`, inherited Codex/GPT-6 family; exact serving model, token count and currency cost unknown. This is harness validation, not a source population or performance result.

CLI from the canonical worktree:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/M6-CLOCK-BRACKET-001/review/analyze-controls-a.py --input <rawCSV> --output <newJSON>
```

The output must not exist; creation uses exclusive mode. Any validation failure returns 1 after retaining all parsed rows/cells, input hash, row errors and available derived observations in the new JSON. CLI/IO errors do not overwrite an existing result. No driver or peer analyzer is imported. The script handles exactly 72 rows in 24 repetitions of empty/CPU/block, validates unsigned integer ranges and exact fields/checksums, both within-clock orders and successive same-process order, positive nominal resolutions, and blocking sleep wall ≥20ms with residual ≥18ms. Different clock epochs are never numerically ordered against each other.

The CPU checksum is computed independently by affine-map exponentiation modulo 2^64, giving **3294929107973101697** after 2,000,000 iterations from seed 1. Six direct small recurrence checks exercise composition and modular wrapping separately.

With I=w2−w1, T=t1−t0 and M=(w1−w0)+(w3−w2), the conditional zero-error CPU interval is [max(0,T−M), min(T,I)], with off-CPU complement [I−upper, I−lower]. Every raw timestamp, nominal resolution and interruption count remains. Empty intervals are preserved as model inconsistencies, **not fatal sensitivity errors** under the revised preregistration. The result separates `sensitivity_status`, `zero_error_model_status`, `model_inconsistency_count`, and `physical_attribution` (always `UNVALIDATED`). No guessed accuracy allowance, zero-clamping repair, empirical worst-case error bound, alternative acceptance clock or physical attribution is introduced.

Eleven synthetic parser/model controls passed: valid distinct clock epochs; wrong checksum; short sleep; insufficient blocking residual; nonmonotonic wall; empty interval preserved as a nonfatal model inconsistency; malformed integer; wrong schedule; missing row; extra row; wrong header. The final-source synthetic report retains full fixtures/results in ANALYZER-SYNTHETIC-A-FINAL.json (SHA256 `4bb2c027a0306e10c5a9b76f2644d55a98e14ac3644bf5f3c647881f99d1f496`). The initial synthetic report remains unchanged; a subsequent metadata-only default-field refinement was retested offline against the final helper. No real control or future raw data was read.

Reviewed contract hashes: PLAN.json `b50d0fe0d7c553f872075815b70f4c7e066a30efb33c77ab4f3e4c1d6aea2c5e`; clock-bracket.h `74f83a8ccdecba0b03a4089ecdc92ddacf8225e26c04d67562c9f44112f34581`; controls.c `c6e76f69b3c025d938243e5e48dc6cdac8a5a06ce39950d69b23c464698472bd`. These are preparation identities, not a substitute for the controller's eventual freeze.

Own required MCP discovery at 14:57:46 UTC found no exposed cpu-perf/library_status/ask tool in this participant's callable catalog. I explicitly consumed the controller's **shared** actual stdio consultation at 14:55:32 UTC rather than claiming an own ask. Shared journal SHA256 `a471566c9dc8aacb2f88c392720e236264e97aaa841f4a8bfa79960e5ac85e9b` pins exact requests/responses privately. Server cpu-perf 0.1.1, bundled library commit deb5a0bac467, keyword-only 0/287 indexed. The actual ask covers this six-timestamp bracket, deterministic CPU and blocking controls, conditional margins and unknown accounting error. No matching passages supported a physical accuracy bound. The fetched [LLVM benchmarking guidance](https://llvm.org/docs/Benchmarking.html) distinguishes reduced noise from bias; it does not establish macOS accounting accuracy or transferable numerical precision. Unread suggested sources and other-machine example numbers are unused. Canonical sorted-JSON response hashes are library_status `879c1e0ff8eab46fce19273839b836828183796f40321e0efb4d87610b01c10d`, ask `d991982ea5154230f9aca50b5fd24742a08678b32cbb1e07a2fd0c72c23b18ad`, read_source `3b22bb5c2e644cb4b419c4ddd5dd72b9e0f9ac167a6f8768584ef0a32cc00294`.

Ready for controller review/invocation after freeze; no timing or qualification result is claimed. All native execution remains the controller's separate exclusive phase.
