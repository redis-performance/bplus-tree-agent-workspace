# Generated code before timing

The `*-decoder_batch.s` files show the common caller. Each calls the shared policy once per requested range; this policy call is outlined in all four builds. The `*-zbtScoreLeafDecodePolicy.s` files show the dispatch itself: A compares the range count to 4, B to 8, and C to 16. The scalar loop and frozen bulk decoder are both inside that policy body, outside the caller's per-score result-check loop. The frozen bulk range helper is inlined into the policy body by this compiler.

These are generated assembly snapshots, not timing evidence. `codegen.json` hashes the caller snapshots. Whole-process sampler outputs are separate files and must remain outside timing comparisons.
