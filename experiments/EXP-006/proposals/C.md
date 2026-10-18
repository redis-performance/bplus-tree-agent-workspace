# Proposal C — packed member length prefilter

Sequential coordinator pass C, not an independent agent; backend/model/cost unknown.
Same baseline/harness/qualification/profile set. Hypothesis: reject length mismatches
before fully materializing packed data in leaf matching. Target zbtPackedData and
zbtScoreLeafFindMember. Mixed batches have many absent members; length rejection could
reduce decode/memcmp after tag collisions while preserving byte equality semantics.

Current fixtures use equal-length keys, so this mechanism has little demonstrated
coverage. Packed lengths already feed a length equality check before memcmp. External
records also check full hashes first. Profile attribution cannot prove wasted decode.
Need a different varied-length fixture and qualification before this hypothesis is
measurable. Risks duplicate decoding/branch overhead, external ownership assumptions,
and binary length errors. Falsify if source inspection/codegen already does the work.
