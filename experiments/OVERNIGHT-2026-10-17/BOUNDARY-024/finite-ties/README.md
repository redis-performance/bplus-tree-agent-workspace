# Finite extremes and equal-score groups

All16source/build/seed cells pass with12fixed exact finite patterns: ±largest finite,
±smallest subnormal, ±smallest normal, ±zero, ±1 and ±2^53. Each cell completes260score
updates,6full sorted models,288inclusive/exclusive equal-score range checks and all
live SCAN/continuous-anchor/memory checks. No NaN/infinity or tolerance is introduced.

The planned equal-neighbor-order fault **SURVIVED**. Its sanitizer binary completes
normally; this is not a detection. Repeated scores validate ordering after reinsertion,
but these moves come from middle scores far outside their original numeric neighbors.
They do not force the in-place equal-neighbor rejection branch. No production failure
or test weakening occurred. Raw survivor output and patch are preserved in faults/.

A distinct follow-up fixture must force score equality with a current adjacent key
whose binary order requires movement. Do not rerun this unchanged recipe expecting
fault sensitivity. No additional fault type is counted here. SourceNONE; performance
PARK unchanged. See PLAN.md/run.py/manifests/patch for exact isolated provenance.
