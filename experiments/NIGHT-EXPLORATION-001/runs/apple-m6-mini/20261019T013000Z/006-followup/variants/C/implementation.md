# Implementation C — read-only leaf body exposed to the caller

Participant `/root/followup_proposal_c`; actual independent implementation agent.
Visible family GPT-6/Codex; exact serving variant, per-agent token usage and monetary
cost unknown. The prior proposal C/NONE remains unchanged. The chair selected
M6-LOOKUP-CALLER-001; this implements that selected hypothesis rather than changing
the proposal's original recommendation. No A/B implementation was read.

Baseline: `e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf`;
source SHA256 `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
Owned isolation: `worktrees/m6-caller-C`. Only `src/zset_btree.c` changes in the
production patch. Header, allocator, hashing, referee and public API are unchanged.

## Source change and scope

Retain `zbtScoreLeafFindMember` byte-for-byte. Add a separate
`zbtScoreLeafFindMemberReadOnly` body with the same scanner and comparisons, remove
its position-output parameter/store, and force that body inline. The successful
match still computes the original logical position with
`zbtScoreLeafPhysicalPos(leaf, physical)` and calls the unchanged
`zbtScoreLeafScore(leaf, logical)` expression. No physical decoder is introduced.
The existing always-inline `zbtIndexTableFind` selects the read-only body when
`score_pos == NULL`; callers requesting a position retain the original helper.
There is no tree-size threshold, tag-scanner change, decoder change, layout change
or second optimization hypothesis.

This exposes the scanner/optional-output branch to the already-specialized caller.
It can eliminate a separate leaf frame, but may increase caller spills and code
size. Runtime improvement is unmeasured. Code duplication is a maintenance cost:
future semantic edits would need to keep both bodies equivalent. Eligibility is
based only on whether position output is requested; score output remains optional.

Candidate source SHA256:
`53b5891f65ecf589cdf3fd74043d4ce965ba9088dc0550d2aa11dbdf6e8ae7b0`.
Patch SHA256:
`8d179f9342ec0dfbfa1af9435bed612f1bb9cfad5f2c9ab047a16b2fbdb97383`.

## Validation completed

`validation.json` retains all 55 exact commands, return codes, UTC bounds and
stdout/stderr hashes. The driver is `validate.py`, invoked from the repository
root. Raw logs remain under the owned worktree's ignored
`scratch/caller-C-validation/`; public evidence uses relative generic paths.
No failed command occurred and no source revision was needed after validation.

Both native and ASan/UBSan builds pass the original 43 tests. The frozen
`004-lookup/lookup-bench.c` passes 20 bounded public correctness cells per build:
hits/misses at all five sizes plus five additional binary-member lengths. These
executions use 2,003 operations for correctness only; their timer output is not a
performance comparison or result.

The frozen source-included physical oracle passes 4,160 cells and 515,840 exact
score/position/output checks per build. Its direct calls target the original generic
helper. Therefore the separate `readonly-oracle.c` also passes that complete original
matrix while adding a read-only-helper result check at every original query and an
additional read-only miss check per cell. All original assertions remain; the frozen
oracle is unchanged. This covers widths 0..64, shifts 0/3, both orientations, signed
zero, exact finite scores, colliding tags, missing keys and optional score output.
Source-included oracles link **no second tree source**.

Release options match the frozen comparison: Apple Clang, C11 `-O3`, debug symbols,
frame pointers, identical assertion/hash/allocator policy, no LTO. Sanitizer builds
use the frozen `-O1 -fsanitize=address,undefined -fno-sanitize-recover=all` settings
and are used only for correctness. Exact compiler command arguments and source,
referee, allocator and binary hashes are in `validation.json`.

## Static mechanism observation

Retained `otool -tvV build/lookup` output confirms the read-only body is inlined:
there is no standalone read-only symbol, and `zbtreeScoreRaw` has no call to the
generic leaf helper. The public score caller contains two memchr and two memcmp
call sites, retaining the original two-table search paths. Its frame is 240 bytes
(`sub sp, sp, #0xf0`), versus the frozen baseline's 176-byte caller frame plus a
separate 144-byte leaf frame. This describes code structure, not total runtime
stack use or measured speed. The original generic helper remains emitted with a
144-byte frame and memchr/memcmp calls for other callers. Candidate excerpts and
their hashes are retained alongside this report.

No benchmark campaign, timing comparison, profile, source adoption, commit or push
was performed by this agent. Full guard-front-end validation/requalification,
serial discovery, fresh confirmation, candidate profiles and independent review
remain root-owned gates. Stop source changes here and preserve the patch even if
the subsequent campaign rejects it.
