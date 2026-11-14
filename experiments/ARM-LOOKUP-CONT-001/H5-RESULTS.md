# H5 resize-boundary population: REJECT

No candidate meets all gates; source selection is NONE. A passes the original native ARM and Intel comparisons but improves the principal ARM GCC15/LTO hit case by only0.519–0.531% across the three blocks, below the frozen2% requirement. Its target guard blocks and owned-memory endpoints pass. The native gains do not compensate for that target failure.

B fails the static mechanism gate: per-candidate rehash checks remain in both ARM compiler cohorts. C fails the native ARM primary gate, with gains of0.133–0.703%. Neither advances. All sources, losing patches, unused builds and admitted rows remain preserved; there are no unchanged retries or later H5 confirmations/profiles.

| Measured cohort | Candidate | Primary elapsed-time change, three blocks | Result |
|---|---|---|---|
| ARM native | A | -2.336%, -2.117%, -2.129% | Original six cases pass |
| ARM native | C | -0.465%, -0.703%, -0.133% | Primary fails |
| Intel native | A | -3.411%, -3.463%, -3.400% | Portability guards pass |
| ARM GCC15/LTO | A | -0.530%, -0.519%, -0.531% | Target primary fails |

The288 comparison rows use216 distinct relevant A/A control rows. Original source/referee and exact ELF joins, three-block ABBA structure, checksums, operation counts, minimum windows and unchanged memory are independently checked in [final review](reviews/H5-FINAL.md). The raw target cohort is in [H5/lto](H5/lto/analysis.json); the native cohorts and static build artifacts remain alongside it and under `intel/`.

## TMA classification

Qualified ARM baseline/candidate Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable. No H5 candidate TMA was collected after the failed target gate. Native/target compiler differences establish a scoped performance result, not a pipeline cause. Separate Intel baseline categories cannot explain this candidate's ARM result.
