# Focused system samples

These `/usr/bin/sample` captures target the frozen control at count 1, cutoff-A at
count 1, and cutoff-A at count 4 (all width 60 forward). Each includes process setup,
fixture generation, warmup and measurement; none is a timed-only profile. They show
samples in `decoder_batch` and `zbtScoreLeafDecodePolicy`, as expected from the call
structure, but do not establish why scalar count 1 is faster or assign a cycle cost.
Use only as mechanism pointers for a separately frozen count-one experiment.
