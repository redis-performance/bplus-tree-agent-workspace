# Sequential review before results

The public Dup API copies active resize metadata and both tables; no private writable
snapshot trick is needed. The resize code copies at most one uncopied leaf per lookup;
completion is a separate step after the final leaf. count-1uncopied leaves therefore
predicts promotion on the last batch lane. Entry/exit assertions alone do not independently
observe its precise internal lane. A separate scoped instrumentation diagnostic could
confirm that stronger statement. This suite directly observes promotion inside the call.

Missing output lanes are not required to keep their guards. Only the prefix and
outside-count suffix are compared to the initial sentinel. Zero count uses null members
and null output as the implementation's no-op. Full clone lookup verification happens
only after the transition. Clone allocation bytes are independently recomputed, not
compared to source usable bytes, avoiding allocator-size assumptions.

External buffers must be unique in each tree and disjoint between clone and source.
Their addresses are sorted as uintptr_t values; no relational comparison between
unrelated C pointers is used. No SCAN of the clone overwrites the source's global
continuous-anchor tracking. Read-only logical checks leave migration active. The source
still finishes the original live cursor after clones are freed. Main source is untouched.

This is coverage, not a performance result or independent-agent review. It does not
clear unresolved A/A precision, original performance guards, or committed provenance.
