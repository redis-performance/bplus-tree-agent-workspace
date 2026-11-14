# Probe census fleet artifact review

**FLEET ARTIFACT ADMISSION: PASS for all four saved artifacts, limited to the frozen structural census.** Exact emitted-code gates pass, and the supplemental dependency receipts match the original referee manifest, with the capture chronology disclosed below. This review admits no timings, candidate optimization, or performance conclusion. No diagnostic executable was run, and the reviewer performed no fleet action or compilation.

Reviewer role: independent artifact reviewer, prior source reviewer, and proposer of one diagnostic lead; not the census implementation author. This supplement retains the original history and limits in [the source review](PROBE-CENSUS-CODE.md), SHA-256 `22599324b179bb576b3a78f5a45780ee1182e3bd2825d4024ce8cac62ef5a193`.

## Identity and emitted bytes

Both build receipts name directory freeze `82e7ca06eaf451d26b4bc3b40e6386bf689d34fab418af3862e82d586ac3ef48` and the reviewed generation manifest `f14cc62377359f1d53f6f7cd85c05ee7ec8891b01ea0c36e20af08d7773ed0e7`. I independently rehashed all 48 recorded input pins per receipt, each build manifest, the four actual ELFs, and full saved assembly. Receipt compiler text matches the saved compiler output. Both native builds use GCC 13.3.0; both target builds use GCC 15.2.0 with LTO and pinned image digest `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`.

The recorded commands select the unchanged `build.sh`: native `-O3`, target `-O3 -flto=auto`, C11, debug information, warnings as errors, frame pointers, assertions enabled, frozen include paths, and the 13 wrap/retention linker arguments. Build command return codes are zero and explicitly marked build-only. The driver invokes generation verification, compiler, symbol tools, disassembler, and Python static checks; it does not invoke the census ELF.

| Artifact | Actual ELF SHA-256 | Assembly SHA-256 | Emitted bytes joined |
|---|---|---|---:|
| ARM native | `5c2bcf4418b445ea99a97416f08fa58e84c65e3676d67674eb888cbbbb0069d9` | `e78f91120b2d875cd4a3bc25aa17c4cee8ea12f99f4db1240feae8f9e3f52cec` | 96976 |
| ARM target LTO | `2d2e90ecaa2bfc951b4f01561fabb6e186e348008b80a2188443d17e8cb17540` | `bec95b3f6b453b32c8ea831ad6fc2101faf106d3457587b35a2a6d9e72246287` | 56468 |
| Intel native | `bfdfc3e77c2d05940c7d785b0e72c391e30c85e8ea92481dc6625df92edf5f24` | `483f1b91ec092110bc7a643873ac3f80d32b5ae0d9bc6ff3e15baf5f37d05988` | 103859 |
| Intel target LTO | `47116266f5f76474714376aacdbffcc571707314a8baf4bcb571df9743608bac` | `0c1064c6f240adb39798dc5fe2e7253222bdc26071106c497ea2858484bde9e2` | 61250 |

All 318553 emitted bytes match their actual ELF load segments, including Intel continuation lines. ELF machine types match the named architectures. Original-leaf call targets and wrapper addresses were also joined directly to ELF symbol tables; undefined-symbol checks were repeated against those tables. These are static integrity checks, not retired-instruction measurements.

## Original leaf calls

Line references below address the complete `assembly.txt` belonging to the exact artifact identified above.

| Artifact | Original helper | Counted call PCs and assembly lines | Inactive forwarding |
|---|---|---|---|
| ARM native | `0x3c64` | `0x3ee4` line 3427; `0x403c` line 3513 | Original calls remain in callers when the census record is absent |
| ARM target LTO | `0x404fe0` | `0x405648` line 5052; `0x4057f0` line 5158; `0x405834` line 5175 | Tail branch `0x4057b8`, line 5144 |
| Intel native | `0x4a80` | `0x4cdc` line 3918; `0x4e03` line 3999 | Original calls remain in callers when the census record is absent |
| Intel target LTO | `0x405960` | `0x405e4d` line 5180; `0x405f9a` line 5274 | Tail jump `0x405f81`, line 5268 |

The first counted site in each row serves the repeated-identity path as well as ordinary history-bearing calls. Matching a previous failure snapshots requested output bytes, then reaches the original helper with the original arguments. Only after that call does code test the repeat flag, reject an unexpected successful return, and compare requested output bytes. ARM native `0x3ee8`–`0x3f14`, ARM target `0x405650`–`0x405674`, Intel native `0x4ce1`–`0x4d15`, and Intel target `0x405e52`–`0x405e89` retain those checks. Empty-history and unmatched-history paths also call the original helper. No repeat result substitutes for the search.

GCC 15.2 auto-vectorizes part of the ARM diagnostic history scan, visible at `0x40556c`–`0x4055a4`. This is compiler output for diagnostic bookkeeping, not a source SIMD optimization or a baseline lookup change. It reinforces the restriction to logical structural counts: the diagnostic cannot represent original instruction cost or latency.

## Clock denial

All 13 wrappers exist in all four actual ELF symbol tables. Each inspected body calls only `write@plt`, then `_exit@plt` with status 125. No wrapper returns or reads time. No denied API remains undefined, and complete emitted assembly contains no direct timer-counter read or direct syscall instruction. Native compatibility timing entry points that remain linked route to the denial wrapper; they do not provide a timing fallback.

| Wrapper suffix after `__wrap_` | ARM native line | ARM target line | Intel native line | Intel target line |
|---|---:|---:|---:|---:|
| clock_gettime | 23758 | 14153 | 25356 | 15088 |
| clock_getres | 23769 | 14167 | 25369 | 15101 |
| clock | 23782 | 14179 | 25382 | 15114 |
| time | 23796 | 14191 | 25395 | 15127 |
| gettimeofday | 23810 | 14205 | 25408 | 15140 |
| times | 23824 | 14217 | 25421 | 15153 |
| getrusage | 23838 | 14229 | 25434 | 15166 |
| timespec_get | 23852 | 14243 | 25447 | 15179 |
| timespec_getres | 23866 | 14255 | 25460 | 15192 |
| __clock_gettime | 23880 | 14267 | 25473 | 15205 |
| __clock_gettime64 | 23894 | 14281 | 25486 | 15218 |
| __gettimeofday | 23908 | 14293 | 25499 | 15231 |
| syscall | 23922 | 14305 | 25512 | 15244 |

The contract remains limited to owned linked calls and inspected emitted code. It does not intercept arbitrary injected libraries or private dependency internals. This review performed no runtime tripwire test.

## Source generation and fixed work

I reran the read-only source/patch validator against all four saved builds; all checks pass. Generated tree and harness hashes remain `c975a36f61d9780c8450f78336e8b509cbae75b23c87abb0de6f6acc4855dff5` and `9b54905269b64205b98267c1522883fad8e833fc202622b9d0fb5dcdc8be99af`. Exact original fixture/setup, seed 17, six cases, 500 members, independent query buffers, and assertions retain their source-review identities. No argument selects a seed, work count, or timing mode.

All four main functions retain a warmup call with 1000 sweeps and a distinct counted call after reset/enable. ARM native calls are at `0x1444`/`0x150c` (lines 639/689); ARM target at `0x401048`/`0x401108` (494/542); Intel native at `0x1e07`/`0x1f05` (903/960); Intel target at `0x401f1c`/`0x402008` (912/964). The counted argument retains the fixed one-sweep read/two-sweep update selection. Counter disable and immediate memory/resize capture precede validating lookups and output; ordinary compiler movement of side-effect-free field loads around the enable flag does not move validation into the counted interval.

The existing parser and memory gates remain mandatory: all six cases, exact operations/hits/score sum, immediate before/after owned bytes fixed to 14272 for hit/score/miss, 146656 for long, 217600 for external, and 14432 for update. The revised parser and its 12 passing Python tests remain unchanged. A printed `verified` flag alone is insufficient. No runtime result is claimed in this supplement.

## Dependency provenance and execution scope

The build receipts pin the census directory and original tree source. The reviewed build script also consumes the existing compatibility implementation, SipHash, and headers. Initial census metadata did not independently list those dependencies. At the reviewer's request, the controller captured separate read-only dependency receipts after compilation and before any census execution, on both idle reserved hosts. I independently joined all eight actual hashes in each receipt to `referee-manifest.json` and the local canonical bytes. All match: the seven current source/header/compatibility/vendor files and original lookup harness.

The ARM dependency receipt SHA-256 is `b4ba73078f238de280b12c4803c6e631f1726746e64e6365316bb489d70cedd4`; Intel is `85d774d353d1c1bd9710f464b9b5642063e61ba6a4b0dd42ad2f5a5d8a405428`. These are explicitly **post-build, pre-execution** captures. They must not be described as a complete contemporaneous pre-build dependency manifest. The reviewed upload driver transfers only the census directory; the controller reports earlier original-source/referee checks and no intervening dependency edits. The current matching receipts plus that bounded transfer history are sufficient for this structural diagnostic admission; they do not independently reconstruct arbitrary historical filesystem changes. The controller will rehash these eight files and census inputs before and after every case.

These artifacts are eligible only for the frozen six-case structural census on the admitted fleet. The controller must retain live reservation/isolation checks, exact ELF identities, complete outputs/stderr, exit statuses, and parser results. Do not run a local executable, collect timings, add repeats, calibrate work counts, or treat compiler-generated bookkeeping as evidence of optimization gain.

No new MCP consultation, TMA, profile, instruction measurement, or fleet action was performed by this reviewer. The prior shared-consultation limits remain intact. H2/Q4 PARK decisions and original candidate acceptance gates are unchanged.
