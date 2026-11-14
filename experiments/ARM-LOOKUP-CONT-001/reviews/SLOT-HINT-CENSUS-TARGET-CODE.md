# Slot-hint census: independent target ELF review

**PASS for the static code and identity gates of the two exact fleet-built ELFs below.** No emitted-code blocker remains. This is not operational execution admission, runtime correctness, performance qualification or source adoption. The separate operational review and all eventual strict six-case output checks remain required.

| Artifact | SHA256 |
|---|---|
| Frozen source directory manifest | `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` |
| Native fleet ELF | `8facf50e3c68a07ecc738aed446a0f0f9290e85e5d69c26e82d727e98031687c` |
| LTO fleet ELF | `0a9c7f0dca40d181bd8770dcd0c46c7eb9030ca584749dfc2e0db6514cedaf39` |
| Native 21-entry build receipt | `e9a9f0b3e76b70a9df981b3807caa2c0a0feb155091f5d56ca99fb1f511addd6` |
| LTO 21-entry build receipt | `9ae224257f7945c561f3b704d9cec5375cfb27b4c71992eafdc9d5dc1cf50b8e` |
| Overall build receipt | `3e1cc2e88d5ae7eb14e113182da1823c00d46e3161d446b3458b6f2dd4f1fc13` |
| Independent offline inspection evidence | `8d7bc9d4d604f4af563b7a3b4f64cf28e4ecc4daefae8eb7f0c7da59158d4d31` |

This reviewer authored proposal B, reviewed the design and issued the earlier [source-stage review](SLOT-HINT-CENSUS-CODE.md). The diagnostic implementation and fleet build driver have separate authors. This review used only completed fetched artifacts, Python source checks and local binary-inspection tools. Neither ELF was executed; no fleet action or measurement was performed. The earlier controller-build PASS was not carried over to these ELFs.

All **105 input pins** in the overall build receipt independently match the approved local bytes, including the source freeze, generated source/harness, checker, seven frozen source/header/compat/vendor dependencies, original lookup and operational dependencies. Every entry in both 21-entry build receipts matches its actual source or fetched artifact. I reran source reconstruction and patch/body checks: the original leaf-search body, fixture/setup and completion-fence constraints remain intact. Receipt paths beginning with `slot-hint-build/` were resolved against the fetched fleet archive root; experiment paths against the unchanged checkout. No receipt or raw artifact was edited to accommodate local paths.

The native command uses the host compiler, recorded as **Ubuntu GCC 13.3.0**, with `-O3`. The LTO command uses **GCC 15.2.0**, with `-O3 -flto=auto`, in the image pinned as `sha256:9ca91b05c7b07d2979f16413e8b2cd6ec8a7c80ffca4121ccab0aeba33f90460`. Saved image inspection reports that exact ID and repository digest, Linux/amd64; the recorded Docker command selects that ID. Both commands invoke the frozen build script, which supplies the common language, warning, frame-pointer and clock-wrap options. Compiler version records and image identity establish the retained build provenance; they are not a hermetic compiler reproducibility proof or a runtime environment test. The two builds are not being compared for speed.

I independently ran `nm`, `nm -u` and `objdump -d` on both actual ELF files using GNU Binutils 2.42. Both symbol outputs and both undefined-symbol outputs are byte-identical to the saved records. Disassembly text is **not** byte-identical. Native differs only in the ELF filename banner. LTO differs in that banner and eleven `sar`/`shr` operands: local objdump explicitly prints `$1,`, whereas the saved output leaves the implicit one-bit count unstated. Equality was checked after replacing only the filename banner and removing only this explicit `$1,` for `sar`/`shr`. No addresses, instruction bytes, branch targets, symbols or other operands were normalized. The full resulting texts match. The fleet objdump version is not recorded by the frozen build script; no exact version is inferred from this formatting difference.

Fresh CFG analysis ran on the independently produced disassembly, then matched the saved fleet validator result. Native `shLeaf` calls the retained original helper at `0xb672` or tail-calls it at `0xb79e`; its normal exit sites are `0xb6c0`, `0xb77f` and `0xb79e`. LTO calls at `0x407255` or tail-calls at `0x40738a`; its normal exit sites are `0x4072aa` and `0x40738a`. Every normal path has exactly one original call. Both have eleven separately terminating assertion sites. Outlined assertion helpers were checked for their straight-line panic call rather than treated as fatal merely from their names.

Manual inspection of the target helper and wrapper agrees with that proof. The original leaf body retains tag search, external cached-hash rejection before member pointer decoding, length checks and full `memcmp`, followed by original logical-position and optional score/position writes. In LTO the successful hinted path still reaches the original call; afterwards it checks original success, requested position and score object bytes. The returned result is the original result. The noncounted path tail-calls the same original helper with the original arguments. The diagnostic-only `noinline,noipa` declaration retains the original helper in both actual builds; it does not turn the shadow hint into a lookup implementation.

All **13 denied clock/syscall wrappers** are present in each actual ELF. Each inspected wrapper has a straight-line `write` followed by `_exit(125)`, with no normal return or branch around termination; no denied original symbol remains undefined. This is fresh inspection of the fleet ELFs. The separate explicit-clock link probe from source preparation remains compile-only controller evidence; it was not rebuilt or executed during this fleet phase. The claim covers owned linked calls, not hypothetical injected libraries or private timer implementations.

The saved build command records have five successful return codes and finish with `COMPLETE_BUILD_ONLY`; their actions are image inspection, native compilation, owned-container-name check, LTO compilation and static validation. Detailed reservation, inactivity, fetch timing and cleanup admission belong to the separate operational audit. A completion record alone does not authorize workload execution.

No hint count, lifecycle runtime coverage or performance conclusion follows from emitted-code review. The strict raw loader, exact schemas, fixed fixtures/bounds, final post-free fence and original source/memory models remain binding. All source-review limitations concerning C-asserted seed bytes, bounded initial snapshots and unexercised mutation histories still apply. H2/Q4 remain PARK, ARM remains released, and selected source remains NONE.

The shared consultation produced no supporting passage. No profiling was collected.

| TMA category | Baseline | Candidate |
|---|---|---|
| Frontend_Bound | unavailable | unavailable |
| Bad_Speculation | unavailable | unavailable |
| Backend_Bound | unavailable | unavailable |
| Retiring | unavailable | unavailable |

Child categories are unavailable too; there is no candidate or measured TMA classification.
