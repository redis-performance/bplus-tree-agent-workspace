# Predecessor diagnostic: mirrored treatment and placebo confirmation

Preregistered after discovery completed, before fresh confirmation. The zero-trim-f6
target met both discovery seed bounds, while int-trim-f0 did not. Confirm only the
supported target; preserve all discovery rows and label this selection explicitly.

Same frozen HARNESS-006 binary, target95/bytes16/trimmed/forward/alternating-zero/mask6,
20m requested (20000065 effective), three warmup traversals. Fresh seeds43133/43141.
Six ABBA blocks per seed per protocol; alternate seed/protocol order each block.
Protocol contrast reverses discovery labels: A predecessor integer/mask0 (other),
B predecessor alternating-zero/mask6 (same). Protocol placebo gives BOTH A and B
the same alternating-zero/mask6 predecessor. Target is always unchanged. This tests
the selected predecessor contrast against fresh seeds and a same-session A/A control;
it does not by itself establish general scheduler causality.

96 target +96 predecessor rows, one prospective1m binary warmup; no more rows,
exclusions, optional stopping or threshold changes. Serial children<=120s, full<=300s.
Use the identical deferred-bookkeeping pair launcher from discovery. No local agents,
builds/tests/profile computation while timed children execute.

For contrast compute six effects100*(mean A/mean B -1), preserving OTHER/SAME sign
despite reversed labels. Require both fresh95%t df5 intervals entirely below -1%.
For placebo compute100*(mean B/mean A -1); require both95% intervals entirely within
[-1,+1]%. All invariants, fixed counts and >=10ms target windows must pass. Only then
mark the selected diagnostic effect confirmed. Otherwise PARK the robustness claim,
report exactly which criterion failed and retain discovery as discovery. No precision
policy adoption, prior guard substitution, source acceptance or new diagnostic count.
Frequency, effective placement, within-window migration and independent review remain
unknown/pending. No interpretation of thread time as a stable-frequency certificate.
