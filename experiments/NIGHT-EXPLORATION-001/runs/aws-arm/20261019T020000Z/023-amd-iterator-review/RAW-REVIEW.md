# Independent AMD029 raw profile and A/A review

**PASS for evidence integrity; 100K remains unqualified and source selection NONE.**
Reviewed immutable profile9230fb3d4 and final6d19f4df4, using independently authored
parsers and arithmetic rather than running the operator audit. All original profile
files are byte-identical in the final revision. Earlier plan/execution reviews remain
sealed and unchanged. No runner access, compilation, sampling or timing occurred here.

## Profile reconstruction

Verified110 public file hashes,21 frozen execution files,10 source/referee hashes
against13e459ff8,51 exact serial command/environment records, all43 original tests,
original/disabled/sampled fixture semantics and exact tree-owned memory. All six cells
visit50M scores with the independent arithmetic checksum and one warmup pass. The
sanitizer1K/2001-ops fixture performs3000 visits using frozen seed101. All four known
control outputs match the independently checked100M-step arithmetic oracle.

Disabled tree and known-work counters are not counted; enabled known cycles,
instructions and branches are positive. Independent parsing finds86 known-control
samples,81 physically in known_work,398895607/398895769 sampled period
(99.9999594%), and zero sampled outside_work events. Unknown/control edge samples
remain in the denominator. Seven reports record zero lost samples; this does not
prove absence of sampling error or perfect scope boundaries.

Reconstructed1218 scientific samples and every sampled period:594 events at100K,
624 at1M. Physical zbtreeIteratorNext accounts for55.77049% and59.43114% of period.
Exclusive score-decoder labels account for25.8190% and29.3498%; physical-position
and ordered-to-score labels are separate, not added twice through inline ancestry.
These are diagnostic observations, not removable work or a speed claim.

All682 physically sampled tree instructions match exact encoded bytes and source
lines in diagnostic, isolated original, and actual015 timing assembly. The full
iterator function has151 offset entries (including continuation/padding entries):
149 are byte-identical. The remaining two unsampled entries,+0x1ef/+0x1f6, are RIP-
relative string-address loads on the source599 assertion path. This body check
supports the sampled tree mapping but does not claim whole-binary equivalence.
Caller different/missing mappings are retained: at100K,14.80639%/29.42313% period;
at1M,16.27949%/24.28937%. No caller cost is silently assigned to a tree helper.

Public hashes were checked directly. Seven raw perf binary hashes reconcile across
the completion/publication manifests; their binary bytes and live runner binaries
were not read by this reviewer. Protected015/017/019 identities and new build/source
identities match before/after manifests. This is manifest verification, not an
independent live identity measurement. Public path redaction and whitespace
normalization are disclosed in the operator PUBLICATION.json.

## A/A reconstruction

Verified98 public hashes and all48 CSV rows against the independently constructed
six-block ABBA schedule, seeds701–703 twice,50M operations,16-byte members andCPU2.
Every command, serial window, checksum, traversal count, warmup, actual-operation
count, reported rate and exact fixture-owned bytes passes. All12 effects reproduce
the operator results within1e-12 percentage points; no first-block exclusion.

| Case | Maximum absolute A/A effect | Minimum window | Qualification |
| --- | ---: | ---: | --- |
| 100K | 2.4309127% | 212.570ms | FAIL: block0 |
| 1M | 0.1648464% | 221.156ms | PASS: all6 blocks |

The first100K block is retained despite the remaining five passing. No retry,
operation-count change, candidate measurement or source adoption follows.1M timer
qualification is scoped to that fixture and session; it cannot qualify100K or
rescue any earlier failed controls. Baseline timing identity remains1ecbe6a4...,
source13e459ff8; profile instrumented elapsed values are not used as speed evidence.

Independent reviewer/root/aws_arm, with no AMD profile/referee authorship. Native
Codex backend; exact model, tokens and cost unknown. Reproduction scripts and full
independent reconstructions accompany this review; supply the immutable029 directory
and an output JSON path when invoking either script from a checkout with13e objects.
