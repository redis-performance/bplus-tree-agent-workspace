# Pass A — tree accumulation

Provenance: one Codex/GPT-6-family worker, exact serving model and measured token
cost unknown. Three sequential passes, NOT independent agents. Each pass uses the
same M6 profile, release assembly, A/A and shared target/guard definitions. M1
shorter-side proposal is prior context, not independent confirmation.

Evidence:35/107 and98/389 diagnostic PCs are in rank accumulation at100K/1M;
coarse observations only. Mean preceding siblings27.823/37.418 across3ancestors.
Clang already vectorizes groups of8. Hypothesis: select the smaller of preceding
and following siblings, obtaining a prefix from existing parent/node subtree totals
when using the suffix. Fewer count visits can reduce public successful rank time at
100K and1M without changing layout, mutation code or owned memory. Extra side-choice
branch and metadata loads may erase the benefit; explicit SIMD is not proposed.
Target zbtScoreRank only. Preserve forward/reverse ranks, optional scores, finite
score bits, ties and unsigned count arithmetic. Existing subtree invariants must
hold across all mutations. Falsification: no public primary benefit beyond A/A,
repeatable primary regression, failed exact rank oracle or memory change. Public
full guards and independent confirmation/review remain mandatory for adoption.
