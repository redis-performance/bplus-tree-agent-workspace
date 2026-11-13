# Variant C: map only within requested output branches

Independent implementation C starts at `4876d21ce62fdf9306572b690c891d2d5ed0e04d`, with current unstable source `ee8e7f70152404649ac947157fd662d11b4a00d5`. Only the successful-match block of `zbtScoreLeafFindMember()` changes. No A/B implementation was read.

The score branch supplies `zbtScoreLeafPhysicalPos(leaf, physical)` directly to `zbtScoreLeafScore()`. The position branch independently supplies the mapping to its output. When both outputs are null, neither expression is evaluated in the C abstract machine. When both are requested, the compiler may reuse the pure mapping; the implementation does not depend on that optimization for correctness.

[Patch](change.patch) and [source/referee identity](identity.json) preserve the exact change. Candidate source SHA256: `80341637d93aad9f41a6c23b163681d53e317179fae06ce6f786d8dbbc2934ea`. All 11 other files in the frozen referee manifest match their baseline hashes. No header, fixture, adapter, hash implementation, compiler flags or build script changed.

## Semantics and risks

Equality, length validation, external hash rejection and collision continuation execute exactly as before. No scanner, packed decoder, helper attribute or data layout changes. Both optional outputs retain the same logical position for normal and reversed leaves; score extraction is unchanged. Callers requesting a position without a score still receive it.

The compiler may still hoist side-effect-free position arithmetic above the output conditions. Exact fleet assembly must establish whether the intended no-score work removal occurred. Conversely, separate expressions may increase work or affect register pressure/code layout when both outputs are present. Neither source form nor static reasoning proves a timing gain; all registered guards remain mandatory.

## Validation

`sh experiments/ARM-LOOKUP-GAP-001/qualify.sh` runs the unchanged native and ASan/UBSan correctness suites, then verification-only fixture checks for hit/score/miss/long at seeds 17/29/43. These local checks do not read a performance clock. Final exit status and results are recorded in validation.json with copied logs in correctness/.

No local or fleet measurement was performed by this implementer. The chair owns serialized fleet comparison and instruction/profile validation. No source adoption, commit or publication was performed here.

## Provenance and consultation

Backend: Codex with inherited session model; exact model identifier and token/currency costs unknown. An own-session cpu-perf tool discovery again found no directly exposed cpu-perf/library_status tools. This implementation consumes the controller's shared consultation documented in the root experiment CONSULTATION.md and the already-recorded independent proposal C, rather than claiming another session's calls as its own. It follows the chair's single selected hypothesis without adding another mechanism.

## TMA classification

| Category | Qualified baseline | Variant C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Baseline topdown output remains exploratory CPU-wide evidence because continuous CPU exclusion was not proven. Variant C has no capture. No timing, sample or instruction percentage substitutes for TMA.
