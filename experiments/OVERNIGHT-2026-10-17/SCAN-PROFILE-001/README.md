# SCAN-PROFILE-001 — sampling unavailable in worker sandbox

One frozen baseline child: scan, size 100000, member length 16, seed 1, 100000000
requested ops, ten lookup warm-up passes. One-second delay, five-second sample at
one-millisecond intervals. Child bounded to 120 seconds in total, no overlapping work.

Benchmark completed with all internal checks (exit 0). `sample` exited 255: it could
not examine the child despite the process existing. No sudo, permission changes or
retry. The tool suggestion to escalate is not followed. Raw error is saved as
scan.sample.txt; manifest records exact arguments, binary and raw checksum. Timings
with attempted sampling are excluded from A/A. No baseline scan profile was obtained.

Decision: profile evidence absent, scan population selection remains NONE/not run.
The prior EXP-001 lookup profiles remain useful leads, but their corresponding new
A/A cells fail qualification. Next useful work: a separately preregistered measurement
diagnostic or additional semantic boundary validation, without inventing a hot path.
