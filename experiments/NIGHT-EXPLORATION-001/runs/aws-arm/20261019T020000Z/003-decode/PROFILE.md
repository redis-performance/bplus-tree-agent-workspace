# Count-one baseline profiles

Controls use width60, forward, count1, 64 leaves, rounds65536 and64 samples. Every run materializes identical outputs and consumes the same checksums. Whole-process perf includes fixture construction and validation; the long repeated kernel dominates these tiny fixtures.

The unadopted EXP-007 B bulk control has 59.96% of cycle samples in decoder_batch and40.03% in the outlined zbtScoreLeafDecodePolicy. Its inlined bulk geometry contributes35.72% of whole-process samples. The root scalar range adapter places99.99% in decoder_batch: compiler inlining differs. Assembly confirms a policy call per leaf for B and no corresponding call in the scalar root control. These are sampled proportions, not isolated instruction latency.

Unpaired profile runs report median3.3498ns/decode for B and2.9715ns for the root adapter; this is contextual calibration, not an ABBA gain. Minimum samples are14.03ms/12.43ms. The capped65536rounds prevent reaching the50ms calibration target for count1, but these samples exceed10ms. Root remains unchanged; B remains experimental. A scalar count1 policy is a supported hypothesis for a controlled comparison, not an accepted optimization.

A read-only summary initially parsed elapsed_ns as integer, but the CSV stores decimal values. That summary failed before printing; parsing was corrected to float without rerunning any profile or calibration. Raw rows are unchanged.
