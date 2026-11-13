# Extraction audit

The new `current/src` files are byte-exact from Redis `51e28c2a724a2632c0c75f376c352cd8aee37e0e`. Their hashes are in source-manifest.json. Historical `src`, `compat`, `bench` and sealed reports remain unchanged.

Compared with the recorded `a7ecd959374d66847c095250bf2d373edf7316c5` extraction, the merged source adds fallible reserve and shrink APIs, prehashed lookup entry points, index-resize headroom, range-deletion migration progress, same-tag scan deduplication, external-allocation leak annotations and additional correctness tests. Naming/comment changes are also present. The original raw lookup, table probe and leaf tag/member matching bodies are unchanged. Build layout and index construction can nevertheless change, so old standalone measurements do not qualify this source.

The merged two-input intersection calls raw lookup without a score; `reuse_hash` is enabled only for more than two inputs (`t_zset.c:3401`). Listpack conversion reserves the upcoming 129 members, checks/inserts the 128 existing members using raw APIs, then inserts the incoming member. The new fixture mirrors those data-structure calls, without linking server code. Two independently allocated trees keep query bytes separate from target bytes.

The new libc adapter retains prior allocator and SDS semantics and adds `ztrycalloc_usable`/`zcalloc_usable`. It rejects requests at `SIZE_MAX/2` and reports actual usable allocation size. This is an explicit extraction compatibility change, not a performance candidate. Original merged tests pass 57/57 in the initial native check; full qualification logs accompany the frozen fixture. Historical inline-tag EXP-006 remains PARK, and ARM mask follow-up remains REJECT due to iterator guards. Neither is reused as an accepted optimization.
