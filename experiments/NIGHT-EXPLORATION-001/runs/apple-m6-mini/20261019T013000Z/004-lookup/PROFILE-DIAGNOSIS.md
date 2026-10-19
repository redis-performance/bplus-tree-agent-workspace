# M6 public single-query lookup diagnosis

Round3 completed 40 size/build/seed hit-miss checks,24 length checks,4 invalid checks,
and two deliberate public-result fault controls. All passed. Original43 tests/build
are reused from launcher with matching hashes; no repeated inventory.

Round4 resumed the fixed six-profile plan without rerunning children. Controls pass.
10K/100K/1M hits collect56/139/266 PCs; platform memchr appears21/57/148 times.
Miss captures13/19/101 PCs: first two fail minimum25 and remain insufficient. No
cutoff reduction, longer retry, unbiased time-share or hardware counter claim.
Release assembly retains memchr/memcmp calls and bounded packed-record decoding.
Raw PCs and complete assembly remain ignored scratch with SHA256 in profile summaries.

Twelve untimed seed/size/mode cells count actual paths. Hit full compares/query
are1.14–1.16, leaf scans about1.15–1.17; mean bytes consumed up to first found tag or
end are about31–32 per scan. Miss leaf calls/query are0.016–0.028. These are logical
counts, not PMU, cache miss or elapsed-cost observations. Size histograms retained.
EXP-006 C previously removed memchr yet showed concerning single-lane regressions
on M1. An unchanged inline scanner is a control, not a new hypothesis. Profiles here
identify a region but do not yet explain how a new scanner avoids those losses.

Exact referee/source/binary hashes: freeze.json; origin: harness-origin.json.
Host Apple M6 comes from launcher metadata; direct sysctl unavailable, no retry.
Round3 ended exit1 after its sample-minimum assertion; all partial work retained.
Round4 resume driver records that limitation; original run.py and referee unchanged.
Next: published freeze then once-only baseline calibration/A/A and proposal chair.
