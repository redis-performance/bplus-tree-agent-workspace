# DIAG-006 — bounded sampler perturbation supported locally

All48 planned serial off/on rows complete; both fixed descriptive intervals meet the
preregistered diagnostic bound. All operations/checksums/memory/fingerprints and sample
count controls pass. No rows removed, counts extended or thresholds changed. The result
supports use of coarse profiles with explicit limits; it does not validate sub-percent
precision, unbiased sample fractions or a source speedup. AA-003 stays PARK.

[Plan](PLAN.md), [diagnostic-only patch](diagnostic.patch), [freeze](freeze.json),
[release/sanitizer validation](validation.json), [commands/raw hashes](manifest.json),
[wall-time analysis](SUMMARY.md), [all block effects/sample counts](summary.json).
Same exact executable A/B; PROFILE_USEC=0/1000. CSV rows public; full per-PC stderr
retained in ignored scratch with checksums. Two held-out-seed lookup cases, six ABBA
blocks each. No comparison to another machine or inferred stable clock/residency.

This isolated diagnostic splits profile stopping from dumping, so post-loop output no
longer contaminates the thread-clock endpoint. Boundary syscalls still affect the thread
interval. The off route installs the same inactive handler; no timer is armed. Small
release and ASan/UBSan all-case smoke passes both off/on. Parent known-function
calibration remains PROFILE-002's evidence; inherited calibrate.c is archival and not
built here (its old stop signature would need updating for this header). Do not claim
new calibration or merge this prototype without consolidating its diagnostic interface.

Evidence checker consulted before conclusion. Frequency/effective QoS/within-window
residency, aliasing, timer quantization and sample bias remain unknown. Review sequential,
not independent; backend/model/token cost unknown. No source candidate, population or
acceptance. Root source/referee preserved; uncommitted snapshots await morning review.
Next: round evidence audit and handoff; no further measurement planned this round.
