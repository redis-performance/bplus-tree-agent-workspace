# Standalone assertion contract review — private check passes

The standalone adapter omits a truthful nonreturning function contract.
`compat/server.h` declares ordinary `void standalone_panic(...)`, while the separate
implementation prints the diagnostic and unconditionally calls `abort()`. The tree
translation unit therefore conservatively permits panic to return when compiled
without LTO. Adding C11 `_Noreturn` consistently to the declaration and definition
is a supported **standalone adapter correction**, not a B+ tree optimization.

No root adapter, tree, referee or test file changed. All work used private copies
under `scratch/m6-assertion-contract/{base,noreturn}`. `adapter.patch` contains only
the two private annotations; root decides whether to publish a separate harness
fix and requalify the baseline. Source selection remains NONE.

Reviewer `/root/followup_proposal_c`, an actual independent reviewer. Visible family
GPT-6/Codex; exact serving model, token usage and monetary cost unknown. No other
pending proposal was read. No comparative timing, sampled profile, optimization
candidate claim, Git write or shared-memory change occurred.

## What changes and why

The implementation already never returns. The old declaration is legal and no
functional production defect is demonstrated here; it withholds useful information
from callers. Even if compilation of `standalone.c` infers that its definition never
returns, that inference is unavailable to the separately compiled tree without LTO.
The annotation communicates the existing behavior through the adapter header.

Assertion conditions, error messages, abort call, hash, allocator, tree source,
packed decoder, APIs and layouts are unchanged. The compiler can remove continuation
paths after failed assertions and avoid preserving live tree state across a call
that cannot return. It may also prove redundant checks unreachable from surrounding
control flow. This changes compiler knowledge rather than weakening source checks.

The private baseline iterator assembly reproduces the frozen009 iterator instruction
stream exactly after normalizing addresses and literal relocation. Both binaries
compile the same original tree and frozen iterator frontend with C11/O3, debug
symbols, frame pointers, identical assertion/hash/allocator policy and no LTO.
Only adapter declaration/definition annotations differ.

| Static `zbtreeIteratorNext` observation | Original adapter | Private `_Noreturn` adapter |
|---|---:|---:|
| Whole-function instructions |155|114|
| Stack frame on ordinary paths |96 bytes|0 bytes|
| Register-pair stack saves on ordinary paths |6|0|
| Largest emitted frame, including cold panic path |96 bytes|16 bytes|
| Emitted panic call sites |2|1|

The original six-pair prologue executes before the first iterator leaf read. In the
corrected build, ordinary returns execute without a stack prologue; the sole pair
save and 16-byte frame occur only after an invalid external-record NULL pointer is
detected, immediately before panic. Normal paths have no call in either version.
The corrected function still emits a panic call and checks the external pointer.
This is static code evidence, not a speedup, measured stack peak or profile claim.

## Correctness and fault evidence

All 23 bounded commands and their raw stdout/stderr hashes are recorded in
`review.json`. Every command has the expected result; no failed build or unexpected
test outcome occurred. Expected aborts are explicitly distinguished from failures.

- The private corrected adapter passes all 43 original tests natively and all43
  under ASan/UBSan, with the original `REDIS_TEST`/`REDIS_DEBUG` settings.
- Both original and corrected adapters, native and sanitized, receive deliberate
  `serverAssert(0)` and `serverPanic("contract probe panic")` calls. All eight probes
  terminate through SIGABRT, print their intended diagnostic and never print the
  post-panic marker. These are independent adapter-fault probes; no tree test or
  assertion was changed. Core files are disabled only in these bounded child
  processes to avoid creating crash artifacts.
- The declaration passes local Clang's strict C11 syntax check with
  `-pedantic-errors -Wall -Wextra -Werror`.
- Original source/header/adapter/test/hash hashes match before and after. All11
  source/referee files and all three binaries in the original009 freeze retain
  their frozen hashes.
  Private tree source remains exact baseline SHA256
  `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.

Raw outputs remain local under the ignored scratch directory. The report, private
patch, reproduction script, fault source, test summaries and assembly excerpts are
retained here with generic relative paths. The iterator binaries were built for
static inspection and were never executed for timing or profiling.

## Portability and campaign implications

`_Noreturn` is the C11 function specifier, matching this workspace's C11 build mode;
it requires no architecture intrinsic or compiler-specific attribute. Local Apple
Clang21 accepts it. `/usr/bin/gcc` reports the same Apple Clang21, so this host does
not supply independent GNU GCC coverage. No GNU GCC, other architecture, C++ or
older C language-mode execution is claimed. A future replacement panic function
must continue not to return; returning from an annotated function would violate
the contract and introduce undefined behavior.

Adopting this adapter fix would change generated code across the tree, including
assertion-heavy functions. It must be a separate harness commit followed by new
baseline qualification and profiles before another source optimization comparison.
Baseline and candidates in each new comparison must share the exact corrected
adapter. Existing results remain valid for their frozen original adapter and must
retain that provenance; neither their timings nor control qualification carries
over to the new build. In particular, comparing an old-adapter baseline against a
corrected-adapter candidate would confound the source change with compiler knowledge.
No existing rejected/parked decision is revised by this review.

The review supports preparing that separate adapter correction. It does not itself
authorize a source merge, acceptance decision or new timing campaign. Root owns
those decisions and subsequent baseline requalification.
