# Intel update-path diagnosis: NONE

Tree source remains8fab511e.360native/sanitizer validation cells pass.15timed-region gprof captures plus disabled control (no accumulated samples/calls) isolate update work; instrumentation and shared-library visibility still bias profile shares.25untimed census cells separate branches.75calibration observations freeze counts, then600serial release rows/150same-binary ABBA blocks complete in220.07s. Raw audit passes. No candidate selected.

The new position-preserving fixture intentionally uses alternating odd integer gaps and fits current packed precision: all sampled same/position updates stay in place, all distant/original updates reinsert, nearby updates are about50%order-failure plus0.46–0.48%packing failure at larger sizes. This differs from Apple fixtures with many exact-pack failures; those results are not pooled or superseded.

| Cell | Median ns/op | A/A min% | A/A max% | Qualified |
|---|---:|---:|---:|---|
| distant-100 | 418.274 | -3.454 | 3.151 | False |
| distant-1000 | 558.380 | -3.086 | 2.822 | False |
| distant-10000 | 590.255 | -5.659 | 2.855 | False |
| distant-100000 | 781.570 | -1.262 | 2.328 | False |
| distant-1000000 | 989.793 | -1.095 | 0.233 | False |
| nearby-100 | 172.227 | -3.233 | 3.351 | False |
| nearby-1000 | 260.951 | -2.727 | 3.087 | False |
| nearby-10000 | 325.702 | -5.300 | 3.099 | False |
| nearby-100000 | 477.473 | -2.329 | 4.366 | False |
| nearby-1000000 | 428.259 | -0.600 | 1.069 | False |
| original-100 | 356.280 | -3.517 | 2.652 | False |
| original-1000 | 524.829 | -3.872 | 2.872 | False |
| original-10000 | 578.649 | -2.763 | 2.868 | False |
| original-100000 | 763.612 | -2.243 | 2.243 | False |
| original-1000000 | 979.055 | -1.096 | 0.588 | False |
| position-100 | 53.502 | -5.364 | 0.180 | False |
| position-1000 | 71.096 | -2.857 | 1.360 | False |
| position-10000 | 93.019 | -2.977 | 3.049 | False |
| position-100000 | 214.446 | -2.075 | 0.890 | False |
| position-1000000 | 373.041 | -0.562 | 0.440 | True |
| same-100 | 47.684 | -2.651 | 0.512 | False |
| same-1000 | 66.079 | -3.311 | 2.857 | False |
| same-10000 | 89.076 | -3.006 | 3.120 | False |
| same-100000 | 196.791 | -2.370 | 2.633 | False |
| same-1000000 | 344.037 | -0.242 | 0.714 | True |

Only same/position at1M qualify all six±1%blocks;23other cells fail. Tree-owned memory matches within every block. These are batch-average timings, not individual latency percentiles.

Noise provenance: no recorded steal ticks on the host/CPU2/CPU50; SMT sibling50 has zero busy ticks; CPU2 is99.807%busy across measured process windows. Timed wall-minus-thread maximum0.844%, median slightly negative from clock boundary overhead. This does not explain the several-percent A/A spread; frequency/DVFS remain unknown. /proc/stat covers setup/run/teardown and has jiffy quantization; hostwide context switches do not prove loop preemption.

Scoped position-preserving profile: zbtScoreUpdateInPlace self share6.94% at100K,2.00% at1M. FindForAdd/leaf lookup dominate. Three sequential proposals/chair choose[ NONE](selection.md); no weak implementation population. Independent root referee inspection found exact-bit/model logic consistent, but generated scores are nonnegative integers and do not constitute signed-zero/tie-layout candidate coverage.

[Raw baseline audit](baseline-audit.json),[noise provenance](noise-provenance.json),[profile/census plan](PLAN.md).
