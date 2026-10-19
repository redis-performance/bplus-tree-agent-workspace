# Inner-child investigation, no candidate

Matched census of1M updates at100K/1M:3M/3.967M child selections, average fanout17.257/18.226 and scan steps10.672/11.098; zero score ties in these unique-score fixtures. Disabled control zero, semantics equal. Insert100K/1M average steps9.668/10.862. Counts are not time fractions.

Fresh previous scoped sample31/92 FindLeaf events puts about60% local period in child pointer/header transition and30–36% in linear scan. Function total6.30%/8.28%, so nominal removable scan share only2–3% overall. Binary search may introduce worse branching/locality; census alone is insufficient. No implementation selected.

One bounded matched attribution check preregistered:12 scoped records, six per size100K/1M, exactly1M updates and16-byte members, seeds1/2/3 eachtwice, original frozen8fab511e source and existing controlled FIFO diagnostic harness, cycles:u F997, CPU2,60-second total unit limit. Parse all sample periods using symbol offsets. No performance claims from profiled elapsed times. Classify FindLeaf offset0x60..0x7e as original scalar scan loop and0x37..0x48 as selected-child pointer/header transition; retain allother offsets. Aggregate per-size, preserve per-capture counts and period fractions, report sampling limits. If loop headroom remains weak, chair NONE; no noise-driven repeated profiling.

Checked published Apple branches M1 4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9 and M6 87c3305f8af8c78b622cc3146f5e0745488a3bd3 for inner-child/binary-search mentions, none found. Unpublished work unknown. Root independently reviews direction.
