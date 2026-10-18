# Proposal B — prefetch future query strings before hashing

Sequential coordinator pass B, not an independent agent; backend/model/cost unknown.
Same baseline, harness, AA-012 and PROFILE-004 input as passA. Long-hit320 qualifies;
SipHash leads all its profiles. Hypothesis: prefetching future batch members before
hashing hides their initial data latency, improving long-hit320 by>=2%.
Target zbtreeScores first hash loop only, bounded by count; hash implementation stays
unchanged. Guards include qualified mixed16 and unqualified short hit/miss subsets.

Profiles identify SipHash instructions, not data misses or first-line latency.
The working set can fit in shared cache; arithmetic may dominate. Prefetch can add
work/cache pressure without benefit. Requires before/after profile plus codegen and
fresh confirmation; falsify by absent benefit, changed scope or >1%guard/memory loss.
Evidence quality lower than direct removal of a sampled library boundary. Do not
assume speculative reads beyond count or transferable architecture numbers.
