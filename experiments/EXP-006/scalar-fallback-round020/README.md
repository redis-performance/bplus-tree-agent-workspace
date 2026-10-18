# EXP-006 scalar fallback validation

**PASS: 16 semantic cells, 16 builds and 16 preprocessing commands.** All four exact
sources pass native and ASan/UBSan first-match and protected-page oracles with the
scalar fallback deliberately selected. B/C each pass1,585,152 first-match checks and
198,144 page-boundary checks per relevant build. All source/build digests agree.

The [plan](PLAN.md) preincludes host/system/adapter headers normally, then undefines
__BYTE_ORDER__ only while including the frozen oracle/implementation. Separate adapter
and SipHash translation units retain the actual host configuration. Native-versus-forced
preprocessed output is identical for control/A and differs only in the single tag
helper for B/C. The emitted forced helper contains the scalar loop and no word-mask,
memcpy or ctz path. All source/oracle/adapter files retain their parent hashes.

A deliberate isolated C fault performs a volatile read when the input span is empty.
The protected-page oracle detects it with an ASan BUS failure. Its patch and raw/public
stderr are retained. This repeats the out-of-span-read fault family; no new count or
production bug is claimed.

```sh
python3 experiments/EXP-006/scalar-fallback-round020/run.py
```

[Manifest](manifest.json) records all commands, outputs, timestamps, binary/source
hashes and preprocessing hashes. Raw preprocessing and sanitizer stderr stay under
ignored scratch; public diagnostics redact only the workspace path. Driver refuses
existing snapshots and retains its historical cutoff; use a fresh plan/directory for
new work. [Round audit](../../OVERNIGHT-2026-10-17/ROUND-020-VERIFY.json) recomputes
preprocessor equality, outputs and the fault patch.

This validates a forced scalar branch on the M1. It does **not** validate actual
big-endian execution, another ABI/CPU/compiler, or performance. C/PARK and source NONE
remain; counts of named suites/diagnostics/optimizations are unchanged.
