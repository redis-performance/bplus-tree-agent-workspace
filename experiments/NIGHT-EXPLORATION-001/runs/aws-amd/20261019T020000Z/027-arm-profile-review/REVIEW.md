# Independent rejected ARM B profile review

**The preregistered material-support criterion is satisfied at both sizes.**
Independent reconstruction of immutablecb708e4ec matches every one of17,482 raw
sample classifications and every per-capture/pooled numerator and denominator.
The rejected population remainsREJECT/NONE; no implementation is proposed here.

|B fixture|Timed events|Timed period sum|Predicate events|Predicate period sum|Share|
|---|---:|---:|---:|---:|---:|
|100K|2,264|6,334,992,444|400|1,119,382,245|17.669828%|
|1M|2,496|6,977,567,180|421|1,176,861,266|16.866355%|

At100K the per-seed shares are17.7273%,18.1631%,17.1105%; at1M they are17.2510%,17.9442%,15.3982% (full precision in audit.json). Each seed clears1%, each pooled
size clears5% and100 events. All sampled physical zbtIndexScanSlot events in every
capture are assigned to timed or verification main returns, exceeding90%.
Baseline predicate values are not applicable; machine-readable zero placeholders
must not imply an equivalent baseline region was measured.

The audit parses unfiltered callchains independently without reading/importing the
worker analyzer. Exact physical main+0xe04 identifies the timed call; main+0xf90
identifies verification. Inlined main labels alone do not qualify. Missing or
multiple physical main frames fail closed. Only a physical zbtIndexScanSlot label
at the sampled top IP can be charged to its region: an ancestor at another address
does not contribute. All70 exact candidate addresses join the separately reviewed
35-instruction forward/reverse reconstruction regions; no enclosing-range gaps or
baseline offsets are charged. Frozen source-linked main assembly has entry0xf18,
bl zbtreeScan at0x1d18/0x1ea4 and return0x1d1c/0x1ea8 respectively. No return-PC
adjustment was made after observing samples.

Eight independently authored synthetic parser checks pass: timed, verify, missing,
conflicting, inlined-only, other, ancestor-only and duplicate physical main. These
are local text tests only, not additional measurements. All raw classifications
agree exactly with the published per-sample file.

Full accounting retains7,629 timed samples (period21,333,343,958),2,129 verification
(5,950,500,415),7,654 other (20,723,337,786),70 incomplete (6,295,118),zero ambiguous.
The categories sum to every sample and every period. Each perf report's approximate
event total exactly matches its raw period sum; exact integer sample headers match
where available.1M report sample headers are abbreviated2K, so exact counts come
from raw callchains, not invented precision from that label. All12 reports state
zero lost samples. This does not establish zero sampling bias or perfect stacks.

All52 commands complete successfully and serially in42.8s under the600s cap. The
fixed12-capture order and all argv match: both exact binaries,100K/1M,16bytes,5Mops,
seeds1–3,997Hz cycles:u/frame-pointer callchains. All28 plain/sampled/disabled CSV
rows preserve actual operations, checksum, owned memory, traversals and warmup
counts, including cross-source fixture joins and CPU2 start/end. Four disabled
perf-stat controls report not-counted cycles and only expected Events disabled
stderr. No instrumented elapsed-time comparison is used.

All124 evidence hashes and preregistered inputs verify. The frozen baseline869425...
and B1e584193... identities join017; before/after source/referee/binary records agree.
Raw perf.data files stay runner-local with recorded hashes and sizes; this reviewer
did not independently rehash or read those binaries. Full unfiltered text is public.
No runner access, builds, source edits, timings or new captures occurred here.

The PMU sampled the entire process. This is exact-callsite post-filtered analysis,
not physically gated timed-only PMU capture. Whole zbtIndexScanSlot includes index-ID,
resize and decode work, and is not synonymous with the all-match helper. Period
shares describe sampled-IP attribution; skid, dependency overlap, unequal instruction
cost, changed layout and profiler perturbation prevent assigning17% causal cost or
predicting recovered speed. The observed samples support a materially executed
region, not proof that removing it explains or reverses the55–79% slowdown.

Reviewer AMD authored C and previously performed the static025 review; those facts
are disclosed. This review examines exact B and independently reconstructs evidence,
not independent C authorship. Exact inherited model/cost unknown. No multi-reviewer
skill workflow is claimed. Source adoption remainsNONE, pending root's separate review.
