# M6 lookup geometry — baseline census complete

No optimization is proposed or selected by this diagnostic. Source remains NONE.
The observations identify physical storage relationships; they do not establish
cache misses, dependency latency, hardware cache-line size or a speed opportunity.
Every emitted frontend timing field is explicitly unused. No timing comparison,
new time profile, calibration or optimization population was run.

Participant `/root/followup_proposal_a`, actual independent agent; inherited
GPT-6/Codex family, exact serving identifier/token/monetary cost unknown. The frozen
baseline is e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf, source SHA256 d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2.
Instrumented source exists only under scratch/m6-geometry. `instrumentation.patch`,
`freeze.json`, `frontend.patch` and `lookup-geometry.c` preserve the exact changes.
The original score decoder is byte-for-byte unchanged, hash b86b7e89cb3cc765d345d7f09a00753133b03c7f2a371d18728623b040614c0f.

## Data

24 native cells cover hit/miss/mixed queries at10K/100K/1M members with16-byte binary
keys and100K with321-byte binary keys, seeds1/2,20,003queries each. Six representative
ASan/UBSan cells cover all three modes at10K/16 seed1 and100K/321 seed2. All original
frontend checks pass. Four additional37-query controls compare warmup1/3 for hit and
miss; public request/path counters agree despite different warmup work. Two source-
included private-helper sanity runs (native/sanitized) verify inactive-before/after,
reset-after-setup, public query counting and width0/nonzero helper return values,
positions, counts and geometry denominators. All41 commands pass without warnings.
All children have finished.

Native hit observations, two seeds shown as ranges; these are logical counts and
virtual-address geometry, with no elapsed-cost interpretation:

| Members / bytes | Leaf visits/query | Tag candidates/query | Mean score-word to matched-record distance, 64-byte blocks |
|---|---:|---:|---:|
|10K /16|1.00850–1.01090|1.15058–1.15543|15.403–15.610|
|100K /16|1.01440–1.01475|1.15043–1.15383|15.005–15.139|
|1M /16|1.00770–1.00815|1.13828–1.13953|14.859–14.896|
|100K /321|1.01395–1.01535|1.15263–1.15603|18.041–18.198|

Every observed candidate and match with a nonzero score width has score-word and
in-leaf member-record starts in different diagnostic64-byte blocks, including the
representative sanitizer cells. Tag/score starts are also always in different
blocks in the requested native hit cells; offset-entry/score starts differ in
99.495–99.640% of those matches. A distinct starting block is a geometric fact,
not evidence that either load misses a hardware cache.

The observed random-construction leaves are all normal orientation: reversed-leaf
fraction0 both in the full snapshot and visited population. Snapshot leaf counts:
144/144 at10K;1493/1502 at100K;15088/15042 at1M. The100K/321 fixtures have the same
1493/1502 score-leaf topology as100K/16, with external member records in the long-key
case. Matched scores overwhelmingly use widths6/7, with rare8/16/17; exact0..64
histograms remain in `census.json`. No reversed or broad-width throughput claim is
supported by these ordinary fixtures.

At16bytes every tag candidate reaches an equal-length full member comparison.
At321bytes the retained external full-hash filter rejects most false tag candidates:
20,003/20,004 full comparisons for20,003 successful queries, versus23,056/23,124 tag
candidates in the two seeds. All321-byte matches use external member payloads;
no16-byte match does. Record-header and member-payload geometry are distinct fields.

Misses reach leaf search only0.01550–0.02705 times/query across requested native
fixtures and have zero full member matches. Mixed mode has exactly10,002matches out
of20,003queries. These path observations agree in direction with004's prior census;
no rows or timings are pooled with the old100K-query observations.

## Counter definitions and scope

`queries` counts public zbtreeScoreRaw calls while the diagnostic is active. The
frontend activates/resets counters after construction, warmup and expected-checksum
preparation, immediately before starting the original timer. It deactivates/dumps
immediately after the original loop's closing clock read, before post-loop checks.
The setup snapshot iterates all score leaves before activation; all path counters
then describe only loop queries. `leaf_calls` counts helper entries;
`index_candidates` counts eligible index candidates immediately before those calls,
and agrees exactly with leaf_calls. `unique_leaves` uses a private ID-indexed seen
array prepared outside timing; no raw pointer or leaf-ID trace is emitted.

`tag_candidates` counts successful memchr positions, including candidates later
rejected by external hash or length. `full_compares` counts actual equal-length
memcmp evaluations after the external hash check. `matches` counts exact member
matches. Width/orientation arrays are weighted separately by leaf visit, tag
candidate and exact match. Snapshot width/orientation counts enumerate the entire
tree once. They must not be confused with sampled request-weighted counts.

A diagnostic block is floor(virtual_address/64). Only bounded absolute block-distance
histograms are emitted, never addresses; bin64 means>=64blocks. The pair order is:
tag-byte↔offset-entry, tag-byte↔record-header, offset-entry↔record-header,
tag-byte↔score-word, offset-entry↔score-word, score-word↔record-header. Score word
means the first byte of the original decoder's8-byte load for the physical slot.
Width0 has no such load and is excluded from score-word denominators. Header pairs
still count width0 candidates. The candidate's score-word geometry is prospective:
false candidates do not execute the original score decoder. Matched payload distance
uses zbtPackedData's returned member pointer, which can lie outside the score leaf.
The extra cross-block field describes only the8-byte word, not an optional ninth byte.

Every requested public query uses a non-null score output. Full matches, histogram
sums and all geometry denominators are checked against independently known query
hit counts. Private-helper sanity deliberately calls the helper directly, so its
leaf matches have no public-query/index-candidate count; that distinction is tested.
Warmup controls compare logical paths only, since allocator placement can change
address geometry between processes. Native/sanitizer address histograms are separate;
neither is treated as a performance control or hardware measurement.

## Evidence, limits and next handoff

`census.json` retains per-process data and exact commands; `commands.jsonl` duplicates
the command journal for inspection. `summary.json` derives all fractions/pair means,
and `summary.csv` is the compact per-run view. Logs retain the original CSV output
including unused times, and stderr geometry JSON. Raw logs remain in private scratch;
public logs substitute a generic workspace marker. `audit.json` and `artifacts-sha256.json`
seal source/referee/support and output checks. No failed command or excluded row exists.

Prior004 profiles still show memchr/leaf regions, with insufficient10K/100K miss
captures and no unbiased time attribution. This census adds no PMU, frequency,
residency, cache-miss or dependency-stall information. Instrumentation changes code
shape and touches metadata, so its emitted times cannot be interpreted as baseline
speed. Geometry depends on fixture history/allocator placement, and the ordinary
fixtures provide no reverse-leaf coverage. Existing decoder/leaf/index source and
all earlier candidate decisions remain unchanged. Root must review these observations
before authorizing any new hypothesis or implementation population.
