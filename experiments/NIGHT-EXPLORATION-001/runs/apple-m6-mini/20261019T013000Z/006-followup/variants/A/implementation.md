# Variant A — forced inlining of the original generic leaf lookup

Hypothesis: M6-LOOKUP-CALLER-001. Participant `/root/followup_proposal_a`, actual
independent implementation agent. Backend/model family GPT-6/Codex inherited from
root; exact serving model, token usage and monetary cost unknown. No B/C
implementation was read. The earlier proposal A/NONE remains unchanged.

The complete change is one declaration: `zbtScoreLeafFindMember` becomes
`static inline __attribute__((always_inline))`, following the existing compiler
attribute style of `zbtIndexTableFind` and `zbtIndexFind`. Its function body is
byte-for-byte unchanged. This exposes the original generic body to existing
constant optional-output call sites. There is no new physical decoder, source
specialization, scanner, wrapper, threshold or layout change. All call sites retain
their original argument expressions. Compiler inlining can simplify generated code;
any resulting score-decode simplification is a compiler consequence of that one
annotation, not reuse of the prior physical-decoder patches.

The source starts from exact baseline e52c26c4b52c167b5ed3948eb9440f3fc2ffabaf.
`source-freeze.json` records baseline/candidate/patch/header/referee/test/support
hashes. `candidate.patch` is the complete production change. Isolated source/build:
`worktrees/m6-caller-A`. Only that directory and this variant's artifacts were written.
No source changes were made after validation began.

## Correctness and commands

Validation PASS: 43 original tests in native and ASan/UBSan builds; all 20 frozen
lookup size/length cells per build; and the frozen physical-score oracle's 4,160
cells / 515,840 exact-score/position/optional-output checks per build. Both
orientations, widths 0..64, shifts 0/3, signed zero, tag collisions and misses pass.
The source-included physical oracle links no second tree source. No checks were
weakened. There were no failed build/test commands. All 53 commands, UTC boundaries,
return codes, binary hashes and log hashes are in `validation.json`.

Release flags match frozen lookup validation: Clang, C11, -g, -Wall, -Wextra,
-fno-omit-frame-pointer, -O3, no LTO; original hash/allocator/assertion settings.
Sanitizer flags use -O1 -fsanitize=address,undefined -fno-sanitize-recover=all.
Original tests additionally use -DREDIS_TEST -DREDIS_DEBUG. The oracle compiler
command includes `referee/physical-oracle.c` and support sources, without a second
`src/zset_btree.c`. Exact compiler version is in logs/compiler.stdout.

Frozen `lookup-bench.c` was run solely as the existing bounded 2,003-operation
semantic smoke matrix, with seed1, sizes100/1K/10K/100K/1M and lengths8/319/320/321/
1024 at1K. Its emitted timing columns are retained in the unmodified outputs but
were neither analyzed nor treated as benchmark/performance evidence. No new profile,
calibration, A/A, candidate timing comparison or agent launch was performed.

Raw command output is retained privately at `worktrees/m6-caller-A/.validation/raw`.
Published logs substitute `<workspace>` for the absolute workspace path; a final
scan found no absolute user-home path. Referee copies are exact hash matches to 004-lookup.
Shared src/header and original support/test/referee files remain unchanged.

## Generated-code mechanism and risk

`codegen.json` and the extracted release assembly document the static mechanism.
The generic leaf helper symbol is absent and both direct generic leaf calls inside
`zbtreeScoreRaw` disappear. memchr and memcmp remain in the inlined caller, with two
static call sites each. The original score decoder source remains unchanged.

The 176-byte ScoreRaw frame grows to240bytes, while the separate144-byte leaf frame
disappears. ScoreRaw grows from345 to601static instructions, with stack load/store
sites growing37 to89. Those are static sites across the entire function, not dynamic
per-query counts. This trade-off could reduce call layering or increase register/code
pressure; no performance direction is inferred. The small zbtreeScore wrapper remains
25instructions. The source uses an established GCC/Clang attribute already required
elsewhere in the baseline; no new architecture-specific instruction is introduced.

Status: implementation and bounded correctness complete; source frozen for the root's
common frontend freeze, baseline requalification, serial comparisons, full guards,
fresh confirmation, matched profiles and independent review. No selection or adoption
is claimed. No commit, push, shared source edit or permission change was attempted.
