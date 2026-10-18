# EXP-008 checks before timing

`python3 experiments/EXP-008/build.py` and `--sanitize` built control/A/B/C from
isolated detached worktrees at the same source commit. Warnings-as-errors; release
O3/no-LTO; ASan/UBSan O1 separate objects. Build commands, compiler, source/policy,
object and binary hashes are captured in the two build manifests.

The existing decoder suite (`tests/test_decoder.py`) passed all four Python groups
for all eight release/sanitizer binaries. The exhaustive self-test checks1820 widths,
directions, counts and score shifts with exact score bits, subrange canaries and
checksummed batches. Semantic oracle calls the selected hybrid policy for empty,
single, partial and full ranges. The timing matrix itself also checks output bit
validity, same-fixture identities and checksums before and after every batch.

The source-specific extension freezes the EXP-007 B bulk helper byte-for-byte.
Every variant preserves that helper and adds only its count policy. Main src files,
benchmark driver, allocator and adapter are shared. Generated code inspection is
saved in profile-results; baseline whole-process sample is saved separately from
experimental timing. Successful timing profiles are excluded from the comparison.

Root `src/zset_btree.c` is compared with frozen baseline commit4fd3a3f before each
build. No Redis server or overnight supervisor is used.
