# H7 affected-index guard preparation

**UNUSED AFTER H7 STATIC REJECTION.** All three variants fail the controller's frozen target raw-frame gate. These artifacts never received timing admission. The original six cases and five supplemental guards remain unchanged.

The [provisional protocol](PROTOCOL.md), [referee](guards.c) and [counts](proposed-counts.json) describe collision hits/misses, growth/shrink reference-repair churn and complete member-returning scans. The optional measure branch was never executed. No fleet collector was created.

Correctness uses frozen baseline/H7-A/B/C sources, public native/sanitizer builds and separate read-only native diagnostics. [run-correctness.py](run-correctness.py) links a clock-denying wrapper for every local binary. [check_oracle.py](check_oracle.py) independently derives byte/count/sum expectations and compares every output and memory endpoint. Final completion and joins are in [verification.stdout](verification.stdout) and [oracle.stdout](oracle.stdout); exact binary/source identities are in [correctness/build-manifest.json](correctness/build-manifest.json).

Useful path observations, identical across the saved native implementations for seed17:

- The256-member fixture resolves30 hits from home and226 after displacement, reaching30 bucket steps. All32 collision misses require continuation past a full home bucket.
- Two churn sweeps observe60 active-before and61 active-after states,110 growth/11 shrink samples,5 completion transitions and1,203 surviving-member leaf-ID changes. Of those changes,57 are observed while a resize remains active. These are state witnesses, not exact reference-finder call counts.
- A full scan uses9 cursor calls,482 callbacks and256 unique members. Duplicate callbacks are retained and checked. The corrected oracle requires every member separately in **each** completed walk.
- Two-sweep churn records22,600 owned bytes before,26,896 immediately after and22,736 after validation. Validation lookups can finish maintenance; the immediate endpoint cannot be replaced by the smaller validation endpoint.

The [retained oracle defect](failed-attempts/cumulative-scan-coverage/README.md) explains why cumulative callback coverage was insufficient. No candidate failure or performance result is inferred from it. The first passing matrix and prior referee are preserved; corrected sources were rebuilt and rerun.

These small correctness cells do not validate the proposed large measurement counts, sustained duration, physical peak allocation, active-resize read/scan traffic, wide IDs or every mutation branch. See the protocol for complete limits. For baseline and H7-A/B/C, Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and all child shares are unavailable: no TMA/profile collection ran. Public role: guard implementer and H7-C author, not an independent reviewer of C or this harness. Shared MCP provenance and unavailable own tools are recorded in the protocol.
