# Intel supplemental SCAN guards

Supplemental correctness preparation passes: 756 validator commands, 90 fixture models per source, native/sanitizer public-census parity, 43 original tests per build and 32 total negative controls. Exact reviewed model manifests match, baseline/B outputs agree within build modes, and 38 post-preparation hashes remain unchanged. Completed in 69.55 seconds under the 600-second cap. Frozen baseline calibration is next; no supplemental candidate timing yet.

Imported referee ec21ce601 and frozen protocol 7dbfe8259. Original 8fab baseline and exact SSE2 B are distinct from the corrected-adapter source. This covers 30 cells with lengths 8/319/320/321/1024, three score encodings including signed zero, small fully reversed leaves and active paused resize. All original guard gaps remain unresolved. Source adoption NONE.
