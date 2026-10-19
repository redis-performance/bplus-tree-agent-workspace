# Independent review of AMD corrected iterator baseline plan

**Plan review: no blocker found. Execution review remains pending.** Reviewed immutable
af2131b80, AMD029-corrected-iterator-plan. This is a baseline diagnosis, not a selected
optimization or permission to run. No runner access, source edits or measurements were
performed for this review. Parent/root retains execution authority.

## Verified semantics and identity

Independently verified all8 plan-freeze file hashes and10 source/referee hashes against
exact13e459ff8800be3f02b6b45c87dd7b0c39453fa9. The protected A/A binary1ecbe6a426bd3a593a9fce6b8e8c6796c8c2287706fdd7eafdba595df9bad9ed matches both before/after identities in the
actual015-adapter-requalification/results/manifest.json; it is not inferred from a
fresh archive. That is manifest provenance, not a new live-host check by this reviewer.
The plan correctly requires live before/after hashes and protects other existing builds.

Original iterate passes ele=NULL,len=NULL,score=&score. Source zbtreeIteratorNext guards
member decoding with `if(ele || len)`, so this scope primarily exercises score decoding,
position advance, leaf crossing and harness consumption. It does not automatically
support Intel's earlier full-output member-offset-cache hypothesis. No full-output,
reverse, tied/fractional/signedzero or mutation coverage is claimed.

50M requested operations yield exactly500 traversals at100K and50 at1M, and50M visited
members in either case. Exact checksums are2499975000000 and24999975000000. The sanitizer
1K/2001 smoke rounds to3 traversals/3000 members/checksum1498500. Scores are exact small
integers representable in double; checksum arithmetic stays within uint64. Original
per-traversal visited assertions and final checksum remain unchanged. Source byte/hash
fixtures and allocator must match within each original/diagnostic build mode.

## Known-work oracle and scope

Reviewed unsigned64-bit volatile recurrences and noinline inside/outside functions.
The C recurrence wraps modulo2^64 as intended. Independently computed100M-step outputs
using2×2 modular matrix exponentiation, distinct from the supplied affine-pair oracle,
and crosschecked against21 small direct-loop cases. Exact expected before/inside/after
values are576d9c942c494901,dcbca4dc3edf4303,6557d69def72a107. Machine-readable checks are
in plan-independent-checks.json. No100M local workload was executed.

The reused tree profile frontend differs from the original only by FIFO support and
enable/disable hooks around the original clocked body. Construction/lookup warmup and
postvalidation are outside; acknowledged control and clock edges remain inside and
must remain in attribution totals. The known-work control places distinct outside_work
before enable and after acknowledged disable, giving a useful negative scoping check.
The fixed disabled no-perf/stat controls, enabled positive stat counters and enabled
sample attribution (>80% period,>=20 known events,zero outside events) are appropriate
fail-closed tests. They establish this transport/scoping diagnostic, not general PMU
accuracy or a tree performance gain. Unknown/control/system samples must stay counted.

## Requirements for the execution-freeze review

Verify actual code matches both fixed schedules and hard caps; clear inherited
PROFILE_DISABLE for enabled jobs; use-D-1 and acknowledged FIFOs; retain exit codes,
partial output/timeouts, raw samples and losses. Positive counters must be measured,
not inferred from a missing/not-counted field. All semantic row fields and fixture
memory identities must be checked, with exact expected checksums and actual operations.
Keep original43 tests and sanitizer options intact. No A/A before the independent
profile completeness/control audit, and no count/seed/time-limit retries after failure.

Actual015 timing binary, isolated newly built original and diagnostic require separate
identity and source-linked instruction mapping. Same source does not guarantee identical
layout/opcodes; report relocation differences and unmappable regions. Charge only the
sampled physical instruction, with same-IP inline labels distinguished, not cumulative
ancestor shares. A large aggregate iterator share cannot justify a candidate by itself.
The fresh A/A must use the actual protected015 binary and not the rebuilt diagnostic
original. All six±1%/10ms blocks at both sizes are required before candidate work can
be considered. No old8fab/Intel/ARM timing pooling or rescue of prior failed controls.

Actual reviewer /root/aws_arm, native Codex agent; exact model/tokens/cost unknown.
No authorship of AMD plan/control source and no runner actions. Review covers plan,
source semantics and arithmetic now; a separate additive review will pin the execution
freeze before any conclusion about its implementation.
