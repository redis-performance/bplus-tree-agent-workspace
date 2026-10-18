# EXP-008 proposal A — retain scalar work for short ranges

Proposer: `/root/hybrid_proposal_a`. Exact backend/model identity and token cost are unavailable to this worker; both remain unknown.

## Evidence and target

EXP-007's B bulk decoder is about 33% faster at 96 forward width-60 scores and about 43% faster at aligned widths 8 and 64, but is 20.79% slower at one width-60 score, 10.60% slower at one width-63 score, and 6.49% slower at seven width-63 scores. The losses recur across fresh confirmation blocks. The saved assembly inspection reports that B is an outlined helper called once per leaf while the control decode loop is inlined into `decoder_batch`; B's aligned and noncrossing score loops omit per-score crossing checks. This makes call/dispatch cost a plausible contributor to short-range losses, though the inspection does not establish the cause.

Target a private hybrid wrapper in the isolated EXP-007 snapshot. Make the wrapper inline into its caller where the compiler permits; for short ranges it should execute the original scalar loop directly in the caller, bypassing B's outlined call, and for large ranges it should call the unchanged B helper. Preserve the original scalar decoder and B implementation as fixed controls. This proposal does not modify the public scalar iterator or production source.

## Falsifiable hypothesis

For a requested range of fewer than eight scores, executing the original scalar decode loop directly in the caller will avoid enough outlined-helper overhead to beat B; at eight or more scores, B's width-specialized loop will amortize its one helper call and retain its bulk advantage. Implement a count threshold of 8, with short ranges taking the original scalar path and ranges of 8 or more taking B. The threshold is selected once per range, outside the per-score loop.

This predicts that the hybrid will remove the demonstrated short-range losses at counts 1 and 7, while matching B at count 96. It predicts the crossover lies between counts 7 and 8. The hypothesis is falsified if either short guard still regresses by more than 1% against the original control, if count 8 fails to beat the control by at least 2%, or if B's count-96 primary gain is not retained. A crossover elsewhere is evidence against this proposal's fixed threshold; it must not be repaired after observing results.

## Fixtures and threshold candidates

Measure counts 1, 2, 4, 7, 8, 16, 32 and 96. Counts 1 and 7 reproduce EXP-007 losses; 2 and 4 cover shorter ranges; 8 tests the proposed boundary; 16 and 32 check amortization; 96 checks the established full-leaf gain. Keep each count within one leaf, with identical output materialization and checksum work across control, B and hybrid.

Use widths 8 and 64 as aligned guards, width 60 as the primary/crossing-safe geometry, and width 63 as the crossing-capable short-range guard. Exercise forward and reversed orientation in correctness checks; timing should retain the EXP-007 preregistered orientations and guards. Keep seeds, score shift, compiler, allocator, leaf bytes, and referee fixed across variants. Test native and ASan/UBSan correctness over widths 0–64, both orientations, shifts, empty/partial ranges, exact score bits, and zero-count behavior before timing.

Primary implementation threshold: 8. To locate whether a crossover exists without post-hoc tuning, implementation variants may use only predeclared thresholds 4, 8, 16, or 32, selected before their measurements. Report each threshold on the complete fixed count matrix. Do not retune after discovery; hold out fresh seeds for confirmation of the selected variant. Preserve all losing patches and rows.

## Predicted mechanism and risks

The scalar branch should keep tiny requests in the caller's existing loop, avoiding B's outlined call and range-loop setup costs; the bulk branch should preserve B's once-per-range geometry dispatch and per-score gains. Generated code must confirm that the wrapper inlines, that short cases do not call B, and which work remains in each score loop. If that code shape does not materialize, the mechanism prediction fails even if timing moves. A timing result alone cannot establish this mechanism.

Risks include an extra threshold branch, retained helper-call overhead, compiler inlining changes, code-size growth, and a crossover that varies with width, orientation, compiler, or architecture. Correctness must preserve logical order, reversed-leaf mapping, exact finite score bits including signed zero, width-64 masking without shift-by-64, padding/read bounds, and zero-count no-access behavior. A bulk-helper win still does not establish an iterator win; iterator integration requires a separate matching workload and guard campaign.

## Decision conditions

Use the workspace gates: qualified same-cell A/A, at least three serial ABBA blocks, at least 2% improvement in the preregistered primary case, and no demonstrated regression above 1% on any qualified guard. Compare every hybrid to the unchanged original control and retain B as a diagnostic reference. If A/A precision cannot resolve the 1% guard, or the profile does not support the proposed mechanism, park the result. Do not claim production adoption from this bulk harness.

No builds or timings were run for this proposal. It uses EXP-007's reported evidence only. Exact backend/model and token cost are unknown.
