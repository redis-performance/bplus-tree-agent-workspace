# Independent matched Intel profile review

The immutable e49b21fe6 profiles provide directional evidence consistent with the intended exact-vector mechanism, strongest at1M. They do not quantitatively establish cycles saved or explain a precise elapsed percentage. Overall source remains NONE/PARK with the original guard gaps unchanged.

The independently authored audit reconstructs all120 captures in exact frozen order, including ten repetitions and alternating base/B order for seeds301–303. It checks all serial command records, the600-second CPU2 job, raw CSV identity, exact callbacks/checksum/tree bytes, disabled/native/sanitizer parity, original and diagnostic source hashes, matching relative build commands, and final24 diagnostic plus22 original artifacts. The known-work control independently reconstructs67 enabled samples entirely inside known_work, zero disabled samples and equal checksum. No worker profile audit script was imported or relied upon.

Every raw histogram is joined to its own source's LLVM18 inline map. Counts are included once for a helper frame, even where caller frames overlap. Both sources have identical actual callback totals within each size, so the normalization denominator is matched:

| Size | Source | In-range samples | Helper samples | Helper per million actual callbacks | Helper share |
|---|---|---:|---:|---:|---:|
|100K|base|1305|337|2.1896|25.82%|
|100K|B|1258|316|2.0531|25.12%|
|1M|base|1740|419|2.7884|24.08%|
|1M|B|1712|316|2.1030|18.46%|

At100K the difference is only21 helper samples across30 captures per source; the nominal6.23% normalized reduction is coarse and cannot carry a precise causal claim. At1M the103-sample difference and24.58% normalized reduction are more directionally persuasive. Neither is an elapsed-time speedup or exact cycle estimate. Sampling regularity, potential missed signals, source/bucket mapping and shared machine conditions limit inference; no formal confidence interval is justified by these aggregate counts alone.

The scope patch starts after construction/warmup and stops before scan postvalidation, retaining small timer/control edges. The sampler observes10ms intervals,2-byte buckets and scale65536. Every maximum bin is below65535, and conservative process-CPU-duration bounds rule out16-bit overflow. The denominator is captured executable-text samples; library/out-of-range/lost/missed events are not fully measured. Inline shares overlap and are not additive. Diagnostic executables also differ from original timing executable layouts, so their sample magnitudes cannot be directly substituted for original elapsed measurements.

Disassembly corroborates bounded16-byte movdqu loads, exact pcmpeqb/pmovmskb masks and nonzero position enumeration in B, with original scalar/SWAR residual handling still present. This establishes that the intended mechanism is compiled, not that all branches or dense/folded/reversed states benefit. It also does not resolve AMD's separate instructions-versus-cycles discrepancy or transfer Intel timing qualification to AMD.

The ten-repeat schedule was revised and frozen before the first candidate capture, based on previously known low baseline sample counts. No interim selection, retry or extension appears in the preserved fixed schedule. Independent elapsed confirmation remains valid as separate evidence. The mixed original iteration guard and23 unqualified original cells still prevent adoption; focused/length/resize/broad-reversal coverage remains separate. No new measurement is requested by this review.

One actual AMD native agent independently authored this review and audit. Exact inherited model and measured token/USD costs are unknown. No Intel runner access or new profiling occurred. Detailed reconstruction: independent-audit.json and audit.py.
