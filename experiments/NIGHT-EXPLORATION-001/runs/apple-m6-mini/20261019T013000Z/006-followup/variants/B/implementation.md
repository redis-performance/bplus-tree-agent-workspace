# Variant B — shared inline body and generic wrapper

Participant `/root/followup_proposal_b`, actual independent implementation agent.
Backend visible: inherited Codex/GPT-6 family. Exact serving model, measured token
usage and monetary cost unknown. No A/C implementation was inspected.

Source starts from e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf, SHA256
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`.
Only `src/zset_btree.c` in `worktrees/m6-caller-B` changes. Candidate SHA256:
`0375470bbbcbf5e88bc1c307b3270dd35f3ea94b38fd0d073543635b83c953a8`.
`candidate.patch` contains the complete change; its hash is in `validation.json`.

The unchanged scanner body becomes `zbtScoreLeafFindMemberBody`, marked always
inline. `zbtScoreLeafFindMember` remains a generic, explicitly noinline wrapper
calling that body. The already-inline `zbtIndexTableFind` selects the wrapper
when `score_pos` is non-NULL and exposes the body directly with a constant NULL
position otherwise. Constant propagation removes that dispatch on public read-only
call paths; generic rank/mutation callers retain the original function boundary.

The original score decoder and leaf-search body are textually identical, apart
from the latter's function declaration/name. The original logical-to-physical
score expression remains in the source; this does not reuse physical-decoder B.
Memchr/memcmp, hashes, record/tag checks, layouts, allocator, assertions, public
signatures, index traversal and resize logic are unchanged. The implementation
uses the compiler attributes already used by this source, with no architecture
intrinsic or instruction-set dependency.

Validation passed with Apple Clang21.0.0, arm64 target, exact commands and hashes in
`validation.json` and reproducible driver `validate.py`. Release uses C11/O3/debug
symbols/frame pointers/Wall/Wextra, matching the frozen lookup comparison.
ASan/UBSan uses O1 and no sanitizer recovery. The original tests use REDIS_TEST
and REDIS_DEBUG, exactly as in the frozen comparison.

- Native and ASan/UBSan: all 43 original tests pass in each build.
- Native and ASan/UBSan: all 20 public size/length lookup correctness smoke cells
  pass in each build. These are bounded 2,003-operation correctness runs, not
  comparative timing evidence; their incidental timer fields support no claim.
- Native and ASan/UBSan: the frozen source-included physical oracle passes 4,160
  cells / 515,840 exact-score, position and nullable-output checks in each build.
  It includes widths0..64, shifts0/3, both orientations, signed zeros, colliding
  tags and misses. It links no second tree source.
- Original header/referee/test/allocator/hash source files match the shared frozen
  copies. The two copied oracle/referee files have unchanged recorded hashes.
  No failure occurred in these 51 build/run/code-inspection commands.

Release `otool` evidence confirms exposure, with a concrete code-size trade-off:

| Static observation | Frozen baseline | B |
|---|---:|---:|
| zbtreeScoreRaw instruction lines |345|601|
| zbtreeScoreRaw explicit frame bytes |176|240|
| zbtreeScoreRaw calls to generic leaf helper |2|0|
| zbtreeScoreRaw memchr/memcmp call sites |0/0|2/2|
| Generic leaf helper instruction lines |161|159|
| Generic leaf helper explicit frame bytes |144|144|

The two leaf bodies correspond to the old/new index-table paths already present
in the caller. The separate leaf frame disappears from read-only calls, while
the caller frame grows64bytes and its instruction count grows substantially.
This confirms compiler exposure and exposes instruction-footprint/spill risk; it
does not establish a speed win, stack peak measurement or causal attribution.
Full retained function assembly and `codegen-summary.json` document the counts.
The public sds wrapper remains25instruction lines. The generic helper retains
memchr/memcmp and its original144-byte frame.

Semantic risk centers on the compile-time output dispatch: any caller requesting
a position must still use the generic wrapper and receive the exact logical
position. The frozen four-output-combination oracle passes. There is only one
source body, reducing divergence risk. No new ownership or layout operation is
introduced. Generic helper instruction differences may reflect optimizer context;
all caller paths still need the full campaign guards, fresh confirmation, profile
validation and independent review. The new shared frontend and qualification are
owned by root and were not changed here.

Public logs use generic relative paths; raw command outputs remain in the owned
worktree's scratch directory. No comparative benchmark, profile, commit/push,
shared source/referee change, environment permission change or agent spawn was
performed. All implementation work is complete; no speed or adoption recommendation
is made before root's serial comparison.
