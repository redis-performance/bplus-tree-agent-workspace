# EXP-008 implementation A — scalar fallback through four scores

Author: `/root/hybrid_proposal_a`. Exact backend/model identity and token cost are unavailable to this worker; both remain unknown. No other implementation proposal was read.

## Choice and touched code

Adds only `policy.inc`, intended to be appended after the unchanged EXP-007 B decoder helper. It defines `zbtScoreLeafDecodePolicy(leaf, start, count, out)`. Count zero returns without reading the leaf or writing output. Counts 1–4 use the original `zbtScoreLeafScore` once per logical position. Counts above 4 call the existing `zbtScoreLeafDecodeRange` exactly once. The exact cutoff is **4** (`count <= 4` selects scalar; `count >= 5` selects B). It adds no width, orientation, or other geometry policy and changes no source, referee, or build files.

## Semantic assumptions and risks

For nonzero count, the caller must provide a valid logical range (`start` and `count` within the leaf) and an output buffer with at least `count` doubles that does not overlap the leaf. The B helper has the same range/output contract. The scalar path passes `start + i` in increasing logical order to `zbtScoreLeafScore`, which owns the leaf's reversed-position mapping and exact score conversion. No score arithmetic or bit decoding is duplicated here.

The main semantic risk is a mismatch between caller range guarantees and either decoder path; unsigned addition in `start + i` relies on the valid-range precondition. Zero count deliberately returns before touching `leaf` or `out`. Exact finite score bits, including signed zero, width-64 mask handling, packed padding reads, and reversed leaves depend on the unchanged underlying decoder implementations. A future change that gives the scalar and B paths different preconditions could make this dispatch unsafe.

The policy is a diagnostic private helper, not a scalar iterator or public API change. This source has not been built, tested, profiled, or timed. No correctness or performance claim is made.
