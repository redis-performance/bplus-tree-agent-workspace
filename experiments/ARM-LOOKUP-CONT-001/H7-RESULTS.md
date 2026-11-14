# H7 exact-mask population: static rejection / NONE

All three variants are ineligible before timing. Their exact ARM GCC15/LTO general `zbtreeScoreRaw` frames grow from176 to192 bytes; the no-score clones remain176. The frozen [selection](H7-selection.md) explicitly rejects any raw-frame growth. A grows at405f20; B and C at405f00. No post-hoc source rescue or timing trial follows.

Correctness and independent source reviews pass. The intended mechanism is emitted: exact masks remove four candidate-byte recheck instructions. Mask arithmetic adds one instruction on narrow paths and two on wide paths, with two additional dependency stages; that cost alone does not violate the registered four-extra-stage threshold. The independent frame gate is decisive. [B/C ARM byte/code audit](reviews/H7-BC-ARM-CODEGEN.md) and [A ARM byte/frame audit](reviews/H7-A-ARM-CODEGEN.md) preserve exact identities and limitations.

Native frames remain176. C additionally changes reference/scan callers; its native scan emits compiler-generated population-count work, while that scan is absent from the lookup-only LTO ELF. No scan performance or complete target scan certification is claimed. The prepared affected-index guards are explicitly UNUSED AFTER STATIC REJECTION; their corrected correctness/path diagnostics and retained harness defect remain available.

No performance cohort ran for H7. It is tracked as an unmeasured static screen and adds no timing attempt or measured population to the completed ledger. All three patches, six ARM builds and unused Intel builds remain preserved. Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children are unavailable for these candidates; no candidate profile was collected.
