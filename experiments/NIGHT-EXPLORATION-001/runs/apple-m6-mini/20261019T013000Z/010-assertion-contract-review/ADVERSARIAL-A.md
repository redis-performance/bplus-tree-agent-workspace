# Independent adapter-contract review — approve separate harness correction

Reviewer `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving
model/token/monetary cost unknown. I did not author C's patch or run its driver.
This review only read original sources/options, frozen009assembly, C's patch,
code-generation records, probe/upstream logs and hashes. It ran no build, test,
profile or timing and contacted no other agent. Only this report and its JSON
companion were written. Source optimization selection remains NONE.

**Approve the two `_Noreturn` declarations as a truthful standalone-adapter contract
correction, in a separate harness commit with new baseline qualification.** They
must not be counted as an accepted B+tree optimization or mixed into an existing
candidate comparison. No speed effect is established by this review.

## Existing behavior and assertion evaluation

The complete original standalone_panic body calls fprintf for file/line/message
and then unconditionally calls the standard abort function. There is no return
statement, conditional recovery branch or alternate normal-return path. A diagnostic
write failure does not introduce a return: if fprintf returns, abort follows. If the
process terminates or control leaves nonlocally before that, it still does not return
normally to the panic caller. `_Noreturn` states that existing property; it is not
an instruction to remove assertion evaluation or replace abort with undefined behavior.

C's exact patch adds the C11 function specifier to both the public adapter prototype
and matching definition, changing no body or macro. `serverAssert(x)` still evaluates
x once in `if (!(x))`; stringification does not evaluate x again. False predicates
still call standalone_panic with the same file/line/expression. `serverPanic(msg)`
still evaluates/passes its message and uses the same diagnostic/abort implementation.
Successful assertions still preserve any necessary expression side effects under
normal C semantics. There is no assume-only assertion or replacement with an
unreachable primitive. A compiler may eliminate a check already proved true on
returning paths, which does not remove the failure of a genuinely false reachable
assertion.

The adapter's serverAssert does not follow NDEBUG and remains active in release.
debugServerAssert still follows REDIS_DEBUG: the unchanged Makefile builds original
tests with REDIS_TEST/REDIS_DEBUG and leaves debug assertions off in ordinary
benchmark builds. C's change alters neither policy, sanitizer settings, hashing,
allocator implementation nor target C/header source.

A future test/interposition replacement that logs and returns would make this
annotation false and could cause undefined behavior. That replacement is not the
current adapter. Nonlocal escape is not a normal return; `_Noreturn` must not be
misread as a promise of no signals, no nonlocal transfer or no diagnostic effects.

## ABI and portability

The function keeps C linkage, its symbol name, void result and identical three
argument types. The specifier is a compiler control-flow contract, not a new calling
convention, extra parameter or struct-layout change. Ordinary Clang/GCC C ABI calls
remain compatible with an implementation that actually aborts. Generated caller
instructions can change substantially, which is the intended reason to requalify
measurement binaries; unchanged ABI does not mean unchanged machine code.

The Makefile and campaign compile with `-std=c11`, so the standard `_Noreturn`
keyword is appropriate and needs no stdnoreturn macro/header. C's strict C11 syntax
check passed. Current target is C, not C++; pre-C11/C++ modes require their own
portability treatment and were not tested. C23/deprecation behavior is outside the
current C11 build. Compiler/platform scope remains explicit: both local clang and
the command named gcc identify Apple Clang21, so there is no independent GNU GCC
or Linux execution evidence. The annotation itself introduces no architecture
intrinsic; the existing allocator adapter already separately limits supported hosts.

## Generated code and evidence audit

009's original Next assembly saves six register pairs in a96-byte frame before
loading/checking the iterator leaf; even its ordinary/end paths pass through that
frame. Its only calls are two cold panic branches. The old declaration gives the
caller translation unit no promise those calls cannot return, so the compiler must
preserve a possible post-panic continuation and live state. Passing multiple.c
files in one Clang command does not create LTO; the recorded flags contain no LTO.

C's retained corrected assembly has no stack frame on ordinary return paths. Its
sole16-byte prologue/panic call is reached only after the external member pointer
fails the non-null assertion. I inspected those branches, including the successful
external-member path back to ordinary output/advance and the early null-leaf return.
The code still implements the original offset arithmetic, member decoding, score
reconstruction and iterator advancement. The declaration makes redundant impossible
post-panic continuation code unnecessary; it does not supply an iterator cache.

I independently counted155original and114corrected instruction lines, matching the
saved assembly hashes. These are static instruction/frame observations, not elapsed
time, cycle counts or a claim that saved instructions explain a measured speed gain.
009's PC observations remain a profile of its exact original binary; their stack
sample counts do not measure the isolated cost of those stack instructions.

Read-only audit of C's evidence verifies23command records and all46raw-log hashes.
Eight assertion/panic probes (base/corrected × native/sanitizer × assert/panic)
terminate with recorded SIGABRT6, retain their diagnostic and omit AFTER_PANIC.
Both corrected original-test logs show43passed/0failed. The strict C11 declaration
check succeeds. I also verified the patch hash, current review-script hash, exact
private-copy two-declaration edits and root-before/root-after source/support hashes.
No command has an unexpected failure. These are independent evidence checks of
C's execution, not another execution or hardware confirmation by this reviewer.

The probes demonstrate failure termination; they do not independently exercise a
successful assertion with a side effect. Preservation of that case is established
by the unchanged macro/body and ordinary C evaluation semantics, not by overstating
the probe coverage. No mock returning panic implementation was tested or supported.

## Campaign treatment and required next step

The AGENTS.md rule applies directly: compat is the frozen referee during candidate
comparison, and harness fixes are separate commits followed by baseline requalification.
Treat this as correcting an incomplete adapter contract; keep src/zset_btree.c/.h
and optimization-population decisions unchanged. Publish exact old/new adapter,
compiler/flags/referee/binary hashes and the code-generation/evaluation evidence in
the harness record before starting dependent measurements.

Historical comparisons remain internally valid where control and every candidate
used the same original adapter/flags. The missing declaration can interact with
candidate code shape, but that discovery does not retroactively change their raw
rows, qualify failed controls, or turn rejected/parked variants into wins. Preserve
all those decisions/evidence and their adapter provenance.

The corrected header is visible throughout target, allocator and harness translation
units, so code beyond IteratorNext may change. Rebuild every control/candidate/referee
with the same corrected adapter; do not splice corrected baseline rows or009profiles
into the old comparison. A new baseline needs matching correctness, calibration,
A/A and scoped profiles for its declared workload/guard matrix. Fresh candidate
comparison/confirmation remains separate if subsequently selected. An Intel cache
patch rebuilt with this adapter is a new binary/method identity, not a replication
of Intel's old-adapter timing binary. No cache replication is selected by this review.

No blocking semantic/ABI issue was found for the exact current C11 adapter and patch.
Approval is for a separately recorded correction with renewed measurement provenance,
not for using altered referee settings inside any frozen candidate trial.
