# H1-C: inline physical-slot match kernel

Implemented by independent Codex worker `cont_metadata`, completed 2026-11-13 23:19 UTC. Exact model, token and monetary costs unknown. Base commit `73914990698c106c62a1ea09394b7a9147ea1077`. No other implementation tree was read. Only the continuation's `current/src/zset_btree.c` changed; the referee is unchanged. Source SHA256: `6a4f58085a85179d6bfe91b5873353df8c59c54f36d0d3c4eeb90e01b6495c89`. [Patch](change.patch).

One shared `static inline __attribute__((always_inline))` kernel, `zbtScoreLeafMatchMember`, retains the original memchr tag scan, full-hash rejection for external records, packed decoder and exact length/byte comparison. It returns the matching physical slot or `UINT_MAX`. The existing generic `zbtScoreLeafFindMember` wrapper rejects that sentinel before mapping the physical slot to logical order and writing optional outputs. Its successful output path retains the original mapping and score behavior.

`zbtIndexTableFind` uses the inline kernel when neither score nor score position is requested; otherwise it uses the generic wrapper. The match kernel has no score/position output arguments or score decode state. This removes the matching function boundary from membership rather than merely deferring logical-position arithmetic. No metadata cache, layout change, new scanner, hash change, batching, prefetch or explicit SIMD is included.

Correctness risks are confusing physical and logical positions for reversed leaves, dereferencing the no-match sentinel, writing absent outputs, and changing the external-hash rejection path. The kernel preserves the original filtering and comparison statements; only its successful return contract changes. Failed matches leave outputs untouched. Existing index bookkeeping executes at exactly the original success point. No persistent size or allocation behavior changes are intended.

## Local correctness and static code generation

All execution here was correctness-only. No local timing, instruction measurement or profiling was performed; the worker made no fleet calls.

| Check | Result | Evidence |
|---|---|---|
| Existing native suite | 57 passed, 0 failed | [Native log](qualification/upstream-native.log) |
| Existing ASan/UBSan suite | 57 passed, 0 failed | [Sanitizer log](qualification/upstream-sanitizer.log) |
| Native fixture verification | All18 cells passed: 3 seeds × hit/score/miss/long/external/update | [Rows](qualification/fixture-native.jsonl) |
| ASan/UBSan fixture verification | All18 cells passed | [Rows](qualification/fixture-sanitizer.jsonl) |
| Optional-output oracle, ASan/UBSan | 90,000 checks passed | [Result](output_oracle.json) |
| External-record oracle, ASan/UBSan | 45,000 checks passed | [Result](output_external_oracle.json) |
| O3 build with `-Werror` | Passed | Binary hash in [manifest](local-binary-sha256.txt) |
| Diff whitespace check | Passed | `git diff --check` |

The unchanged `qualify.sh` commands were executed with only its `LOG=` assignment redirected into this variant's `qualification/` directory, preserving the frozen qualification evidence elsewhere. [Stdout](qualify.stdout), [stderr](qualify.stderr). Both oracle builds used C11, GCC13.3, `-O1 -g -Wall -Wextra -fno-omit-frame-pointer -fsanitize=address,undefined -fno-sanitize-recover=all`, the continuation's src/compat/vendor include paths, standalone compatibility source, SipHash and `-lm`. The oracles include the candidate C file directly as supplied. `build.sh build/arm-cont-private/codegen` built the separate O3 correctness/code-generation binary; it was not benchmarked. All binaries have [recorded hashes](local-binary-sha256.txt).

Static inspection of that local x86-64/GCC13.3 binary confirms actual inlining: there is no `zbtScoreLeafMatchMember` symbol. In [raw-lookup disassembly](local-raw-disassembly.txt), the NULL-score checks at `d6c6` and `d97a` branch to integrated matching; the direct memchr calls are at `dd8d` and `db8d`. Non-NULL output paths retain calls to `zbtScoreLeafFindMember.constprop.0` at `d6ef` and `d9a3`. This is compiler-output evidence only, not ARM performance evidence. The parent must inspect exact ARM candidate assembly before measurement; disappearance of the boundary alone does not establish a speedup. Larger caller code and moved spills remain material risks.

## Validation scope and consultation

The controller reports GCC15/LTO A/A parked for noise and a separately qualified native diagnostic cohort. The unchanged diagnostic gates are ≥2% primary benefit and no demonstrated >1% guard/memory regression. No timing result or source acceptance is claimed here. Fresh ARM assembly, fleet comparisons, selected-profile explanation, confirmation and Intel guards remain the controller's responsibility. Metadata work remains a separate hypothesis.

This worker repeated its own exposed-tool discovery for `cpu.perf` / `library_status` and found no matching tools. It consumed the controller's actual shared stdio selected-H1 consultation, including its `library_status` and `ask` responses, and does not claim those as its own calls. Server0.1.1, bundled library `deb5a0bac467`,3/287 sources,158 passages,0 vectors; no supporting passage matched. The selected-H1 question challenged the three boundary implementations and duration correction using the fresh GCC15/LTO profile and leaf frame. Those profile numbers belong to that separate cohort, not this local implementation. Unread source leads are not used as evidence. The shared consultation did not establish a causal claim; source semantics and exact compiled code decide whether this is a distinct implementation, and controlled fleet results decide performance.

The isolated worktree lacked the ignored `.workspace-memory` directory. The worker read the shared root's MEMORY, LIVE-STATUS and handoff instead; the sealed prior rejection remains unchanged.

## TMA classification

| Category | Qualified baseline | H1-C |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

No slot collector ran in this worker session. The prior CPU-wide funnel is not qualified process evidence; candidate measurements and any supported child categories remain pending. Static disassembly and correctness checks cannot substitute for TMA.
