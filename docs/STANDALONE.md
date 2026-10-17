# Standalone extraction contract

Source: [PR #15635](https://github.com/redis/redis/pull/15635), pinned head
`a7ecd959374d66847c095250bf2d373edf7316c5`. The PR was open when inspected on 2026-10-17.
The current base and merge base in `source-manifest.json` are provenance, not benchmark
competitors. Optimisations compare against the extracted standalone baseline.

The two tree files are initially unmodified. Their private `server.h` dependency resolves
to `compat/server.h`, which declares only the helpers needed by the tree. No Redis checkout,
server executable, Redis process or submodule is required.

| Dependency | Standalone treatment |
|---|---|
| malloc/realloc/free, usable sizes | libc, native `malloc_size` on macOS / `malloc_usable_size` on Linux |
| Hashing | Original SipHash implementation; explicit 16-byte seed per benchmark process |
| SDS | Original header and three adapter functions: `sdsnewlen`, `sdsnew`, `sdsfree` |
| Fixture string allocation | SDS64 layout for all sizes; fixture allocation excluded from timings |
| Assertions | Always-on `serverAssert`; debug checks enabled in correctness executable only |
| Prefetch/endian helpers | Compiler builtins and compile-time byte order |
| Lexical infinity sentinels | Distinct identity-only pointers exposed as `shared.minstring/maxstring` |
| Page dismissal after fork | No-op; excluded from validation/performance claims |
| Defragmentation callbacks | Tree API retained; not yet covered by the microbenchmark harness |

The public tree API keeps its upstream preconditions: insert-new requires absence,
update uses a position from a successful lookup with no intervening mutation, ordered
append requires increasing `(score, member)` order, iterators/member pointers expire on
mutation, and lexical ranges require equal scores. NaN rejection belongs to the original
caller layer; this workspace does not promise a new low-level NaN contract.

`zbtreeAllocSize` measures tree-owned usable allocation bytes, not RSS, allocator metadata,
fragmentation outside the tree, fixture strings, or process memory. Allocator changes affect
leaf capacity and must be treated as a separate experiment with a new baseline.

The existing embedded tree tests are compiled with `REDIS_TEST` and `REDIS_DEBUG` and run
directly. No Redis test runner is involved. This validates the extraction's exercised
paths, not complete equivalence of all Redis integrations. Additional adapter/lexical,
boundary and model-based tests should precede changes touching those areas.

For a source refresh: record the new immutable PR head, review the diff and dependency
surface, update source and support files together, retain notices, refresh the manifest,
rerun correctness/sanitizers, and requalify benchmarks. Never silently follow a branch tip.
