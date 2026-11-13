# H1-B: selective membership specialization

Status: implemented and local correctness PASS; performance selection NONE. Independent implementer: Codex worker `cont_tags`, implementing option B from the selected helper-boundary proposal. Other implementation worktrees were not read. Model, token accounting and monetary cost are unknown. No commit, push, fleet access or local performance measurement was performed.

Base commit: `73914990698c106c62a1ea09394b7a9147ea1077`. The sole changed source is `current/src/zset_btree.c`, SHA256 `4b84d68656ea0dc7ceeabc61ec0768fc47708cc3c2b9fa783378a959321cae6e`. [candidate.patch](candidate.patch) has SHA256 `505709c3d13c0d0fec89e8c2ff63f166d7b3c6fbcd3ff7a6d8267211b25296e7`. Source, referee and local correctness-binary hashes are in [manifest.json](manifest.json).

The original leaf body is moved byte-for-byte into `zbtScoreLeafFindMemberImpl`, marked always-inline. A generic `zbtScoreLeafFindMember` wrapper is explicitly noinline so output-producing and mutation callers preserve that boundary. A separate always-inline `zbtScoreLeafContainsMember` passes literal NULL score and position outputs into the same body. There is one source copy of the scanner, packed decoder, comparison and result-materialization logic.

The already-inlined table lookup selects membership specialization only when all score, score-leaf, score-position, found-bucket, found-position and insertion outputs are absent. Both raw and prehashed raw entrypoints explicitly dispatch a NULL score through an index call with literal NULL outputs. Mutation requests for leaf/cursor/insertion outputs retain the generic wrapper even when no score value is requested. No hand-written logical-position shortcut is included; compiler elimination after inlining is part of this selected hypothesis. The earlier equality proposal is not implemented.

## Correctness

Controller compiler: GCC 13.3.0, Ubuntu `13.3.0-6ubuntu2~24.04.1`. The unchanged `qualify.sh` completed successfully:

- Native: 57/57 upstream tests and 18/18 correctness-only fixture cells.
- ASan/UBSan: 57/57 upstream tests and 18/18 correctness-only fixture cells.
- Supplied output oracle under ASan/UBSan: 90,000 checks passed.
- Supplied external-record output oracle under ASan/UBSan: 45,000 checks passed.

The fixture cells cover seeds 17/29/43 and hit, score, miss, 256-byte long inline, 384-byte external and update cases. The supplied oracles exercise output masks, reversed leaves and exact signed-zero score outputs. All build/run stderr files are empty. Native and sanitizer allocator accounting differ, so their owned-byte fields are not compared across builds or reported as a memory performance result. No referee files were edited.

Qualification command: `sh experiments/ARM-LOOKUP-CONT-001/qualify.sh`, run at the isolated worktree root. Its generated upstream and fixture logs are copied into this variant directory. Each supplied oracle was built using `cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O1 -fsanitize=address,undefined -fno-sanitize-recover=all -DREDIS_DEBUG`, the current src/compat/vendor include directories, the oracle source (which includes the target C file), current `compat/standalone.c`, current `vendor/siphash.c`, and `-lm`, then executed once. Captured logs preserve both builds and runs.

## Static code-generation check and limits

The original-body text comparison passed; [body-preservation.txt](body-preservation.txt) records this. The local O2 correctness binary retains the generic `zbtScoreLeafFindMember` symbol; the shared core and membership wrapper have no out-of-line symbols. In [local raw assembly](local-raw-assembly.txt), the score-pointer test branches to membership at `0x9a43`; scored paths retain generic leaf calls at `0x967b`/`0x9917`, while membership contains direct memchr/memcmp calls at `0x9c7c`/`0x9cc9` and `0x9fe8`/`0xa031`. [Mutation assembly](local-mutation-assembly.txt) retains generic calls at `0xc04c`/`0xc48b`. This verifies the intended boundary distinction for the local correctness build only. The raw function expands, so code footprint and displaced spills remain real risks.

This is controller x86 GCC13/O2 static inspection, not ARM performance evidence or an instruction-count measurement. Exact fleet native O3 code generation must be assessed before interpreting any measured result. The chair's qualified native cohort alone is eligible for the current diagnostic; GCC15/LTO remains PARK after failed A/A. The frozen ≥2% primary and ≤1% guard thresholds are unchanged. No performance winner is implied by these correctness passes.

## Consultation provenance and TMA

Own fresh tool-catalog discovery found no `cpu-perf` or `library_status` tools. The coordinator's actual stdio consultation and reconsultation are shared evidence, not this worker's calls. The shared server reports version 0.1.1, bundled revision `deb5a0bac467`, 3/287 sources and 158 passages; no supporting passage matched the selected mechanism. The coordinator also supplied fresh native whole-process sample shares (leaf 41.38%, raw 21.77%, SipHash 7.65%, memcmp 2.82%) as shared context. They are not local measurements or qualified resource classifications. No library-backed causal claim is made.

| Pipeline-slot category | Baseline | H1-B |
|---|---|---|
| Frontend_Bound | Unavailable: no qualified isolated funnel supplied to this worker | Unavailable: uncollected |
| Bad_Speculation | Unavailable: same blocker | Unavailable: uncollected |
| Backend_Bound | Unavailable: same blocker | Unavailable: uncollected |
| Retiring | Unavailable: same blocker | Unavailable: uncollected |

Qualified child categories are also unavailable. Samples, static assembly and test execution are not substituted for TMA slot shares. Fleet comparison, matched profiles, guard validation, independent confirmation and review remain the chair's next gates.
