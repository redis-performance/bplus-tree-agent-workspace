# ARM024 raw profile review — pass, source NONE

Independent reconstruction of immutable4e43c9f59 finds no evidence-integrity, scope,
semantic or timing-binary mapping blocker to root's separately gated A/A phase.
No A/A was run for this review. No runner access or new measurement occurred.
`audit-raw-profile.py` independently parses commands, CSVs, counters, sample text and
AArch64 disassembly; it imports no worker analyzer or mapper. Worker output JSON was
compared only after reconstruction. I authored the imported AMD029 base harness;
this review independently audits the native ARM adaptation/evidence, with root as an
additional reviewer. Exact model/token/cost unknown.

All24 execution inputs remain sealed to52169964… . All51 exact commands completed
serially with exit0, matching frozen argv/cwd/scope environments and child limits;
complete phase elapsed29.623s is inside600s. Ten source/referee hashes, six diagnostic/
test binaries and five protected binaries join before/after. Actual A/A baseline remains
013 binary330b39a9, not the separately rebuilt original or869425 scan binary. The
original43-test suite passes. All21 tree semantic outputs reconstruct exact case,
size/seed/16-byte members, rounded operation/traversal/checksum contracts, warmup,
CPU2 and paired tree-owned bytes. Scientific fixtures each visit50M members.

Independent affine exponentiation verifies the three100M-step known-work outputs,
with14 small iterative crosschecks. Four known-work modes agree exactly. Disabled tree
and known-work counters are zero/not-counted; enabled cycles/instructions/branches are
positive and branch misses nonnegative. The known sample has238 events,672220048 total
period,234 known_work events and672219994 known period (99.9999919669%), zero outside_work
events and zero reported loss. This passes the fixed>=20,>80%,outside0 gates without
retries. Ancestor-only known/outside frames are not charged; a synthetic inline/ancestor
check verifies that behavior. Known-control samples stay out of scientific totals.

| Size | Scientific events | Total sampled period | Physical tree events / exact matched period share | Exclusive score decode | Exclusive iterator body |
|---|---:|---:|---:|---:|---:|
|100K|454|1304601196|217 /49.529374%|29.347994%|17.218172%|
|1M|516|1481655031|284 /56.011086%|38.921372%|15.572673%|

The six captures have151/174/152/172/151/170 events in frozen seed/size order. All970
scientific events and per-capture report period sums are reconstructed exactly; all
reported loss counts are zero. Exclusive symbol totals agree with the worker audit.
These are coarse sampled-period shares, not elapsed fractions or removable cycle costs.
Unknown/control samples remain in all denominators.

All501 sampled physical tree events have exact encoded words across diagnostic,
rebuilt original and actual013. The full IteratorNext body has114 word offsets,112
identical across all three. Differences+0x1b4/+0x1bc are ADD immediates constructing
assertion string addresses on the source599 external-pointer assertion path; neither
was sampled, and original/actual013 agree there. They are retained, not normalized.
Inspection also confirms that the public score-only call skips member decoding.
No claim of whole-function byte identity is made.

Caller main is explicitly different at the same relative offsets:225/220 events,
50.470615%/43.988906% total period. Twelve additional events per size are missing from
three-way mapping (137/128 period). Equal source or relative offset is not used to
claim equivalent caller instructions. All location counts, words, effects of gaps and
body differences match the worker's output. Equal tree code does not establish equal
layout/cache context, unbiased sampling or a causal speed opportunity.

Verified110 published profile artifact hashes and112 total evidence-seal entries.
Seven raw perf.data hashes join complete/PUBLICATION manifests, but the files are kept
private/local and were not independently rehashed by this reviewer. Public full sample
exports/disassembly are verified after disclosed operational-path redaction and
whitespace normalization; original raw hashes remain available. This limitation is
explicit and does not turn private raw files into independently verified evidence.

Recommendation: root may grant the unchanged48-row A/A phase after its own review.
A/A must still satisfy every-block±1% and>=10ms at both sizes; this valid profile does
not qualify those measurements in advance. No candidate or adoption follows from this
review alone. AMD029's failed100K controls and all older iterator decisions remain final.
