# M6 exact decoder replications — source NONE

The three original decoder experiments completed 19,200 serial processes and
2,476,800 measured batches on M6. Native/sanitizer checks pass, canonical runners
returned zero, and all owned process groups are empty. All 207 frozen identities
match after measurement. Original source/variants and the legacy adapter match the
M1 experiment definitions; the current corrected-adapter baseline stays separate.
No population, unique patch or harness count changes: these are new-host
replications of existing experiments.

Every campaign contains sub-10ms individual timer windows in every cell. Relative
A/A below means only the original all-six-block ±1% rule, not full precision
qualification. All effects are descriptive and conditional. No source acceptance,
cycle estimate, cross-host timing pool or whole-tree speedup follows.

| Experiment | Discovery processes / batches | Relative A/A | Observation | Decision |
|---|---:|---:|---|---|
| EXP-004 focused loop | 960 / 123,840 | 3/20 | Width60 forward A +3.350821%; reverse +4.473779% | Diagnostic only; no advancement |
| EXP-007 private bulk | 2,880 / 371,520 | 14/30 | Primary medians A −34.272446%, B −20.477069%, C −24.790811%; primary A/A fails | Original diagnostic shortlist A; fixed fresh confirmation complete; audit PASS |
| EXP-008 scalar/bulk cutoff | 15,360 / 1,981,440 | 38/160 | Count16 medians A −0.042088%, B +5.728661%, C +71.145130%; none reaches −2% | NONE; confirmation skipped by original rule |

EXP-007 A's six primary effects are −34.120572, −34.303406, −34.365325,
−34.241486, −34.034654 and −35.110294%. Its primary A/A spans −3.662% to
+1.856%. All guard median losses above 1% number A6/B8/C7; restricting only to
relative-A/A-passing controls gives A1/B4/C2. The latter still have short timer
windows. A's width62/reverse/count96 median is +1.179487%; this is retained as a
conditional guard loss, not a precision-qualified source regression.

The unchanged EXP-007 plan explicitly requires one diagnostic fresh confirmation
when the shortlist rule selects a semantically valid candidate with primary
median improvement ≥2%. A has the fewest guard median losses, then the strongest
primary. This follow-up uses the original 30 cells, six blocks, 129 samples,
seeds82037/82051, fresh A/A and 180-second budget: 1,440 processes and 185,760
batches. Shortlisting does not permit source adoption. The separate wrapper and
plan passed root and independent static review, were published in5289562af and
launched only with all analysis workers idle. The fixed confirmation and A profile
completed with exit0 and empty owned groups; no retry. EXP-008 has no eligible candidate.

The three canonical whole-process profiles pass capture audits and reach the
intended decoder regions: EXP-007 base777 observations in decoder_batch;
EXP-007 B651 in its helper plus126 in caller/checksum; EXP-008 base148 in policy,
23 in caller/checksum and1 in printing. These are captured locations, not cycles
or exact source-line costs; profiled timing CSVs are excluded. The selected A
now has its own fixed profile:776 exclusive observations in decoder_batch,
where A is inlined, matching binary/fixture/checksum metadata. Raw path-bearing profiles
remain local; generic reports and checksums are public in profile-analysis/.

The independent EXP-004 audit reconstructs all960 processes,123840 rows,1920 raw
hashes,40 finite-score fixture/checksum contracts and serial UTC intervals.
All1926 discovery files are byte-identical copies after a clean privacy scan.
EXP-007/008 independent audits also pass exact schedules, raw statistics, histograms, all fixture/checksum contracts and serial UTC. All5,768 EXP-007 and30,728 EXP-008 discovery files are byte-identical public copies after clean privacy scans. Across all210 cells, full precision qualification is0/210: all2,476,800 individual windows are below10ms.

Canonical process-loop wall times were6.311158s,23.059993s and136.567421s;
outer owner wall times were6.415474s,23.213820s and136.810234s respectively.
These budget fields include subprocess/validation work, not only operation timers.
Original M1 and new M6 rows are never averaged; compiler differences (M1 Clang17,
M6 Clang21), host conditions and failed controls limit direct interpretation.

Fresh A confirmation completed1,440 processes/185,760 batches in11.427547s internal
campaign-loop wall (11.606582s outer-owner wall). Canonical analysis and independent reconstruction/copy pass all raw statistics,
fixed fresh schedules, checksums, source identities and serial UTC. All2,888
confirmation files are byte-identical public copies after a clean privacy scan. The primary median is
−34.344992%, six effects−34.365325/−34.283943/−34.262701/−34.324659/−34.489164/
−34.648582%. Fresh primary A/A fails at−1.103617..+0.682806%;14/30 relative
controls pass. Six guard median losses remain, including width62 reverse/count96
+1.232033% and width63 forward/count7 +1.477532% with relative-A/A-passing controls.
Both lose above1% in every block, but individual timing windows remain short.
These cannot support source-level regression or acceptance claims. All185,760 fresh timer windows are below10ms (maximum0.156542ms). Final
replication total:20,640 processes/2,662,560 measured batches.

Root remains the driver through08:00UTC/09:00Lisbon, experimental cutoff07:15UTC.
Actual A/B/C agents prepared isolated checkouts and independently reviewed evidence;
exact serving models, token usage and currency costs remain unknown.

Post-discovery correctness supplement: the unchanged original EXP-008 validator
passes16,512/16,512 cells (8,256 native and8,256 ASan/UBSan). It covers all widths,
directions, shifts and declared counts, including4/16/32 omitted by the runbook's
1820-fixture self-test. This explicitly ran after timing, from a fresh scratch cwd
with unchanged binaries/script and preserved historical paths, under a predeclared
300s owner bound. Actual wall72.005689s; every child exited and all53 frozen inputs
and8 binaries match before/after. Exact arguments, return codes, matrix and audit
are public in EXP-008/post-discovery-validation/. No timing CSV was used and no
performance conclusion changes.
