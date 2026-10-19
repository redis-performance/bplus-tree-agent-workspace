# Independent final AA review

**Raw audit PASS; AA qualification FAIL; replication PARK / source NONE.** The fixed schedule completed all 48 baseline-only processes and 12 ABBA blocks. All six 100K blocks qualify. Two 1M blocks fail the unchanged ±1% gate, so discovery is not eligible. This is not a measured rejection of the NEON candidates: none was timed.

I inspected the [independent audit](aa/independent-audit.json), its seal, phase status and journal; directly rehashed all 96 raw stdout/stderr streams; inspected the eight original CSV rows and cleanup metadata for the two failing controls; and independently recomputed all 12 integer gates from all 48 raw elapsed values. I also rehashed all 588 frozen inputs, which match. The exact previously prepared independent auditor was invoked by root, not by this reviewer; its recorded script SHA-256 remains `17bfe2bd692a6f08fda3b40e5857632b5581a98848fde13372c8d87354ed4315`. The sealed report SHA-256 is `c07ec8ddffedc106a380c64a080304789890c1b38bd44bb4a4965cba0c6926d9`.

| Zero-based block | Size | Seed | Outer elapsed sum (ns) | Inner elapsed sum (ns) | Exact-derived effect | Qualification |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1M | 402 | 516,125,000 | 508,556,000 | −1.466505207% | FAIL |
| 4 | 1M | 402 | 507,313,000 | 515,640,000 | +1.641392986% | FAIL |

The gate is `abs(inner−outer)*100 <= outer`, applied independently to every block. Opposite signs do not cancel these failures. The remaining four 1M blocks and all six 100K blocks pass. Every retained window exceeds the 10ms floor: the observed range is 223.938–259.910ms. There is no short-window explanation for this failed precision gate, and the data do not establish another causal explanation.

All rows use the same baseline binary, fixed 5M requested SCAN operations, 16-byte members, one warmup pass and seeds 401–403 twice. The complete raw audit independently reconstructs schedule/argument/environment identities, exact CSV semantics, original duplicate-aware SCAN operations/checksums/traversals/owned bytes and all block statistics. Actual emitted operations total 243,244,400; duplicates are preserved. The eight inspected failing-control rows agree on 5,008,545 actual callbacks, checksum 2,506,001,602,335, five traversals and 32,907,120 tree-owned bytes. No output/memory mismatch rescues or explains the failed precision controls.

The complete 27.621759-second phase ended at 06:36:04.114406 UTC, within the 300-second and absolute UTC limits. All 48 journals record exit zero, no timeout, direct child reaping, owned-group disappearance and safe release; recorded intervals are serial. Public status `COMPLETE` correctly describes execution while `qualified: false` describes precision. The auditor's `PASS` describes raw reconstruction and identity validity. Neither means performance qualification.

Both public and private discovery directories are absent at review time. No retry, count change, row drop, candidate comparison, held-out confirmation or candidate profile follows. Full guards, fresh confirmation, profile validation and independent adversarial acceptance remain unfulfilled. CPU endpoint changes are retained metadata; they cannot establish residency, effective frequency or a cause for variance on this unpinned native macOS runner. No timing effect is carried from ARM, another adapter or another M6 session.

Only this new review file was written. Frozen inputs, original outputs and the auditor were not changed. No build, native execution or benchmark rerun was performed. Participant `/root/followup_proposal_a`; inherited Codex/GPT-6 family, exact serving model/token/currency costs unknown. Ready for root's PARK publication; idle.
