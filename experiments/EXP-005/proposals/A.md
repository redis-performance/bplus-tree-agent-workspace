# Nonzero score-mask arithmetic

Sequential coordinator pass, not an independent agent. Same frozen HARNESS-004 source, EXP-004 baseline profiles/codegen, prior experiment history. Backend/model/cost unknown.

Existing baseline score-only profiles concentrate interrupted PCs in iterator score work. Assembly has mov/lsl/cmp/csinv/and for width mask. Inside bits!=0, use UINT64_MAX>>(64-bits), removing compare/select if Clang cooperates. Hypothesis: >=2% primary improvement without >1% qualified guard/memory regression. Exact target zbtScoreLeafScore mask only. Preserve cross-word predicate. Width64 shift0 is valid; width0 remains guarded. Exhaustive decoder and real signed-zero mutation tests required. Reject absent compiled instruction change or fresh primary/guard failure; PARK noise. Portability relies on unsigned64 C semantics, not arm-only code.
