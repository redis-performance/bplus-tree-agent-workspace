# H2-B portability preparation review

**Preparation is suitable to continue; execution is not yet admitted.** The proposed paired i686 little-endian and s390x big-endian checks address specific missing correctness coverage. H2 remains PARK. This is not a performance population, source-adoption decision, or native code-generation qualification.

Reviewer role: independent protocol reviewer; not this portability harness author. No fleet action, build, emulator, or workload execution was performed in this review. All 15 listed input files were independently rehashed. Reviewed protocol SHA-256: `349f075da99b9f2c6777e3efa59b4994455243541083fc778372e9005f3400e2`; inputs manifest: `9309b9d2ab1f1cac8fd7b84ba8466d2aa9427add53081352773060e762aea67d`. Later preparation revisions require a new freeze and code review.

The protocol correctly preserves exact baseline/H2-B sources, compiler/tool pairing within each ABI, explicit user-mode emulation, a separate task-owned image, unchanged original unit/fixture/output tests, and no host-package or binfmt changes. It distinguishes emulator correctness from native performance and sanitizer coverage. Baseline-first execution and stopping on any failed proof/build/test avoids calling a baseline limitation a candidate pass. Neither source nor test counts may be repaired or reduced within this phase.

The ABI reporter must establish the actual guest properties through three agreeing sources: ELF class/machine/data encoding, compiler target/macros, and runtime integer byte order and type/layout observations. Compiler names or an emulator invocation alone are insufficient. Baseline/B layout equality is checked within an ABI; the predicted i686 sizes are not evidence before execution. External pointer widths and allocator rounding prohibit importing 64-bit owned-byte expectations or comparing absolute memory across ABIs. The frozen compatibility/SipHash/header inputs must accompany both sources.

One concrete coverage gap remains in the proposed focused tests. The existing 7693-validation schedule checks cache consistency after varied mutations but does not prove that all four refresh sites execute under both ABIs' potentially different packing. The author was asked to add separate harness-only cases that successfully invoke leaf build, re-encoding in-place insertion, fast insertion, and in-place deletion, then verify the count/width/displacement transition and actual record/score contents. Preserve the existing schedule/count, report added direct cases separately, and do not instrument or modify candidate source. Successful public API mutations alone do not prove which insertion branch ran.

Final code admission also requires:

- Exact patch reconstruction/source hashes, read-only selected trees, frozen harness/wrapper/parser/Dockerfile inputs, and before/after drift checks.
- A paired oracle with baseline field adapters only; baseline recomputes displacement and has no synthetic cache. B checks its actual uint16 cache against the independent formula. Flag/shift tests preserve moved-out/index-resize values and B cache bytes.
- Strict parsing of 57 unit tests, the 18 exact verify invocations per source/ABI, 90000/45000 supplied checks, focused counts, and ABI outputs. Missing or malformed output fails. Original verify output does not contain a sweep field, so count 1 must also be enforced by the recorded command.
- Correct translation-unit selection for include-source oracles, no duplicate source linkage, and no assertion suppression.
- A retained clock-denial link check for the actual lookup ELF; all accepted invocations must use verify mode. Any unresolved alternate clock entry or unexpected timing output blocks execution/admission.
- Immutable image/tool/library identities, observed interpreter/sysroot paths, fixed emulator CPU selection, serial baseline/B order, single-use output claim, finite resource/deadline caps, and preserved failures with no silent retry or target substitution.

The four refresh-site additions and the pending implementation still need independent review. Package availability and actual image/guest behavior remain preparation claims until controller evidence exists; this reviewer made no new portability-specific MCP or package-source consultation. No TMA category or performance estimate is inferred.
