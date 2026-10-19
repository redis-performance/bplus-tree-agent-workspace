# Corrected baseline rank/update survey: diagnosis complete, source NONE

Exact13e459ff8 baseline-only survey completed74serialcommands in130.03seconds within600s CPU2 owned cap. All12 original/disabled native pairs,2 sanitizer pairs,2 four-counter disabled-zero controls and original43 tests pass. Exactly12 fixed cycles:u997Hz captures cover rank/update×100K/1M×seeds1–3,5M requestedops,16-byte keys; every capture matches its original semantic/owned-memory fields and all12 raw perf hashes verify. All5 newly built diagnostic/test binaries and4 protected existing binaries remain hash-identical before/after. No candidate was measured or proposed.

The table shows exclusive innermost sampled cycle-period shares. Unknown/control samples remain in each denominator. Same-IP inclusive counts are retained separately in profile/audit.json and overlap; do not sum them. Every fixture performs5M actual operations. Update therefore revisits shuffled keys50times at100K and5times at1M; this is a distinct mutation history from first-pass profiles.

| Case/members | Events | Four largest exclusive symbols | Exact-byte-mapped tree period / all period |
|---|---:|---|---:|
|rank/100000|1578|[unknown] 15.38%, sdsType 15.20%, main 13.95%, zbtIndexTableFind 13.87%|67.47%|
|update/100000|7299|zbtScoreLeafWriteScore 8.88%, [unknown] 7.70%, zbtScoreLeafScore 7.24%, zbtScoreEncoding 6.01%|87.53%|
|rank/1000000|5499|zbtIndexTagMask 23.34%, zbtIndexTableFind 21.94%, zbtScoreLeafFindMember 15.15%, sdsType 14.81%|85.53%|
|update/1000000|16613|zbtIndexTableFind 8.84%, sdsType 8.57%, zbtIndexSetId 7.92%, zbtWriteBits 6.92%|90.19%|

Rank1M additionally attributes15.15% to zbtScoreLeafFindMember and14.81% to sdsType; update1M attributes7.92% to zbtIndexSetId and6.92% to zbtWriteBits. These identify locations, not proof that their arithmetic is removable or that a cache miss caused a sample. Code fetch/load/store stalls and sampling skid remain possible. Unknown symbols include unresolvable library/control frames and are not assigned to tree work.

Actual timing-binary mapping uses015 binary1ecbe6a4…, not merely a separately built control. Full source-linked original/diagnostic/timing disassemblies and1395 sampled instruction mappings are retained. All sampled tree instructions in rank match encoded bytes across allthree. Update has only7 tree sample events at three differing call displacements: zbtScoreLeafBuild+0x591,zbtScoreDeleteInPlace+0x405,zbtScoreInsertAt+0x18c7; each resolves to memcpy@plt in allthree (different PLT addresses). They remain classified differing rather than normalized away. Driver main body and unknown/library locations are not claimed equivalent. Full binary hashes/layout differ; equal helper code does not imply equal runtime context or elapsed benefit.

Review against earlier decisions: lower-bound lazy decode002, builder-write004 and full-chunk packed moves005 already failed fixed gates;006query-length showed mandatory first-header access rather than useful repeated decode headroom;007inner-child was insufficiently supported. This new profile does not rescind those outcomes. Rank also reuses the previously investigated member-search path, and exact shorter-side rank was rejected on Apple. The new corrected identity supplies separate observations, not permission to retune or repeat failed candidate families. Index-reference movement/tag handling remain possible diagnostic topics, but this survey alone does not establish a distinct safe optimization or its required precision. Current selectionNONE; no proposal population started.

Root independent review is pending. Source-linked audit/map scripts reconstruct raw records; public text copies have operational paths removed and trailing whitespace normalized, with original local raw hashes retained. Raw perf stays local/owned runner. AMD is idle at05:13:03UTC; no retry or extra capture. Actual native AMD author, exact serving model and measured token/USD costs unknown.
