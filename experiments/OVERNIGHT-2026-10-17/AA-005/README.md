# Fresh traversal A/A — iterator cells qualify, scans PARK

[Plan](PLAN.md), [all rows](manifest.json), [results](SUMMARY.md).
All96 fixed rows pass correctness/memory controls. Forward iteration16/320 qualify
unchanged whole-interval precision gate; scan16/320 do not. Suite/lookup/scan PARK.
No source speedup claim. Sixth baseline exploration, with new long-member traversal
coverage and fresh seeds; instrumented PROFILE-003 timings are not reused here.

Commands: run.py,analyse.py via repository paths. Frozen uninstrumented HARNESS-003,
source and binary hashes checked before/after, raw stdout/stderr retained. Scans use
actual emitted counts and the retained whole-scan oracle; duplicates are legal.
Exactly one prospectively excluded binary warmup. Unknown frequency/effective QoS/
within-window residency, serial local M1 only, no independent confirmation.
Qualified iterator subset permits EXP-002 sequential population exploration. Reverse
and other optional-output performance guards remain unqualified; no broad acceptance.
