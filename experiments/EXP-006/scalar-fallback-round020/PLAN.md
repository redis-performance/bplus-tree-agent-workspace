# Scalar fallback branch validation — preregistration

The B/C candidates guard word search with compiler byte-order macros. Prior tests
ran their little-endian word paths on this M1; the scalar fallback was reviewed but
not deliberately selected. Test that omitted-macro branch without claiming execution
on a big-endian CPU or accepting portability/performance. No new candidate or population.

After the cross-boundary normal/fault children finish, copy exact EXP-006 tag-guard
snapshots control/A/B/C into separate scratch/experiment006-scalar-fallback-round020.
Keep all candidate/oracle/adapter files byte-identical. A new wrapper preincludes the
original system/adapter headers under the real host macros, pushes __BYTE_ORDER__,
undefines it only while including the frozen source-including oracle, then restores
it. Separate adapter and SipHash translation units retain real host configuration.
Do not globally spoof big endian: that would change the storage adapter incorrectly.

Before builds, preprocess native/forced wrappers and require whole preprocessed text
identical except the single zbtInlineTagSearch function in B/C. Control/A must be
identical. Extract and record B/C forced helper; require no memcpy, matches or ctz,
and the scalar loop present. If other macro effects appear, STOP and preserve them.
Do not silently loosen equality. Preprocessing output lives in scratch with hashes.

Run all four sources, nativeO3 and O1ASan/UBSan, both exact first-match and protected-
page oracles:16 semantic cells/16 builds, same commonC11-g-Wall-Wextra-Werror
-fno-omit-frame-pointer-DREDIS_DEBUG flags. Expect1,585,152 tagchecks and198,144
protected-page checks respectively, exact digests equal for all sources/builds.
All checks remain; no timing. No new named boundary or diagnostic count: this is
additional EXP-006 regression validation. Original43tests are not represented here.

One fixed sensitivity control on an isolated C snapshot changes only the scalar
fallback to inspect p[0] when n==0, then runs the guard oracle underASan/UBSan.
Require nonzero non-timeout failure and inspect its exact cause; a survivor is recorded,
not repaired. Save its patch. This repeats the out-of-span-read family, no newfault count.

Each child120s limit; no children start after06:27UTC. Commands serial, timestamps,
stdout/stderr/source/binary hashes retained. Raw sanitizer paths under scratch;
public logs redact only workspace path. Main source and all prior evidence preserved.
Even complete success establishes the forced scalar branch only; real architecture,
ABI/compiler portability, performance guards and independent review remain unresolved.
