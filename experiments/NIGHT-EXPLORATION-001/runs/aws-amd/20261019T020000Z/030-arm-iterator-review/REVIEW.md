# ARM024 preparation review — no execution blocker found

Reviewed immutable d5105925e, execution-freeze SHA256
52169964c692b8accb350efaeebfa95d7ca87832db306722114254ca40a6ffe4.
This review used local source/artifacts and synthetic parser checks only; no runner
access, compiler, workload or timing. Root must still confirm ambient observation has
ended and grant idle handoff. A/A requires completed profile audit, mapping review
and its separate root phase grant. No candidate is authorized.

I authored the imported AMD029 harness. This is an independently authored review of
ARM's adaptation and bindings, not a claim that the base harness was authored or
reviewed by an unrelated third party. Exact inherited model/token/USD cost unknown.

`checks.json` and reproducible `check-freeze.py` verify all24 frozen files, all10
source/referee hashes against13e459ff8, all16 original import pins, and the actual013
baseline manifest binary330b39a9. The protected set includes that binary, prior corrected
scan869425 and all three NEON candidates; no candidate is invoked by this workload.
The source-only diagnostic archive is separate. Actual013 is hashed/read/disassembled
and then used unchanged for A/A; it is never replaced by a new diagnostic build.

All51 command manifest records equal the reviewed AMD manifest after only the declared
ARM path substitutions. Native/sanitizer build flags and relative frontend arguments
are unchanged; ARM additionally requires Clang18.1.3 with an aarch64 target. Fixed
six-capture and48-process schedules, known-work source/oracle, scope frontend and
sample parser are byte-identical to their frozen imports. Scope bytes also match ARM014.
The public score-only call contract remains forward `Next(...,0,NULL,NULL,&score)`.
Literal pre-capture assertions now check size/seed/member bytes/requested and actual
operations/traversals/checksum/warmup, in addition to original-versus-disabled parity.
50M visits imply500/50 traversals and checksums2499975000000/24999975000000. Sanitizer
1K/2001 rounds to3000 visits and checksum1498500 under the original referee.

The wrappers clear inherited scope variables and use `set -eu`. Enabled perf removes
PROFILE_DISABLE, starts disabled with fresh FIFO control/ack endpoints, and enables
around the original timing region. Known-work controls run before scientific captures:
disabled counters zero/not-counted, enabled counters positive, exact arithmetic outputs,
>=20 physical known events, >80% all-period share and zero outside-work events. Failure
stops before captures without tuning or retry. Unknown/control samples remain visible;
reported losses are not silently corrected. On ARM these controls must pass anew;
AMD's successful scope control is not transferred as an ARM observation.

The profile enforces600s total/120s child bounds and serialCPU2, retains failure output,
and runs six fixed50M captures only after controls. The separate A/A enforces300s/30s,
checks the passed profile audit/mapping, validates exact source/binary pre/post identities,
and retains48 rows with seeds701–703 twice in alternating size order. All six blocks
at both sizes require absolute effect<=1% and>=10ms windows. The adapted A/A audit
binds actual profile evidence hashes and requires positive elapsed values. No retry,
seed/count substitution or automatic candidate follows failed controls.

The new parser requires GNU `elf64-littleaarch64`, one8-hex encoded word per instruction,
aligned addresses, unique nonnegative offsets and unique function names. Independent
synthetic checks accept exact native words/source offsets and reject wrong architecture,
short words, x86 split bytes, unaligned/duplicate/negative addresses and duplicate
functions. Words are retained verbatim; no relocation normalization occurs. The map
compares each sampled physical function offset across diagnostic/original/actual013,
keeps different and missing rows in denominators, and separately emits the union of
full iterator-body offsets with differences. Source labels alone never imply equality.
The parsed body can include padding words: its difference count is descriptive, not an
executed-instruction count. `status=mapped` means mapping completed, not that differences
are acceptable or that causal/performance equivalence is established; root's separate
raw-evidence review before A/A preserves that distinction.

Known-work sampling may fail its frozen threshold on ARM; that would be an inconclusive
control, not permission to tune. Main/caller layout may differ and sampled periods may
skid. No elapsed benefit, removable-cycle budget or future implementation is inferred.
AMD029's100K failure, older full-member iterator work and all old8fab outcomes remain
unchanged. Review recommendation: eligible for root's bounded baseline-only profile
grant after confirmed idle handoff, with the frozen stop conditions intact.
