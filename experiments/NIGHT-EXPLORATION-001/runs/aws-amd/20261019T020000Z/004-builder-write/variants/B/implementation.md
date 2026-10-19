# Variant B

The same forward write is explicitly inlined in the member construction loop using existing local encoding values.

Sequential implementation, isolated snapshot/build, exact baseline 8fab511e. No allocation/layout, hash, assertion, index-registration or external ownership changes. Score encoding remains unchanged, including signed-zero distinction. Zero width skips score data; little-endian conversion and the cross-byte predicate are preserved. C changes only local score-write ordering before leaf publication. A/B may compile identically; no independent algorithm claim.
