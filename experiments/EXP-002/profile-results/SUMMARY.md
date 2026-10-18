# Matched iterator profiles

Descriptive interrupted-PC counts, not unbiased time shares. All samples resolved.
- control-4507: 85 samples; {'main': 11, 'zbtreeIteratorNext': 74}
- C-4507: 68 samples; {'zbtreeIteratorNext': 60, 'main': 8}
- control-4801: 92 samples; {'zbtreeIteratorNext': 82, 'main': 10}
- C-4801: 78 samples; {'zbtreeIteratorNext': 71, 'main': 7}

Codegen: baseline generic function saves six register pairs on entry. C public fast-path
dispatch is separate from noinline generic fallback. Inspect saved assembly for exact
instructions; this supports dispatch/register isolation, not a cycle attribution.
Sampler cadence/perturbation/frequency unknown; no accepted or portable performance claim.
