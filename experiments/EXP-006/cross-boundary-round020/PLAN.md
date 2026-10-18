# EXP-006 cross-boundary compatibility — round20 preregistration

Frozen before children, 2026-10-18. Hypothesis: all three retained inline leaf-tag
implementations preserve the existing partial-promotion, narrowing/renumbering,
and mixed-width external clone/relocation oracle contracts on fresh streams.
This extends existing BOUNDARY-023/025 coverage; no new oracle, optimization,
harness revision, baseline qualification, or measurement diagnostic is counted.

Exact source base a2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus EXP-006/freeze.json
uncommitted SHA256 snapshots. Exact oracles from ROUND-019-NEXT-PREFLIGHT.json;
verify their source and parent manifest hashes. Copy all source/referee inputs into
new isolated scratch/experiment006-cross-boundary-round020/{control,A,B,C}.
No edits to target, oracle, allocator, assertions or existing evidence. Each oracle
includes the implementation itself: compile no second src/zset_btree.c object.

Fixed schedule: discovery seed 92503 with REDIS_DEBUG, confirmation seed 92521
without REDIS_DEBUG. Each seed uses control/A/B/C × native O3 and O1 ASan/UBSan
× partial-promotion, narrowing, external-relocation modes 0/1/2: 40 semantic
cells per seed, 80 total, 48 builds. Common C11 -g -Wall -Wextra -Werror
-fno-omit-frame-pointer, system cc (Apple Clang17), unmodified libc adapter and
SipHash; sanitizer uses -fsanitize=address,undefined -fno-sanitize-recover=all.
No NDEBUG: every unconditional check survives debug-off confirmation. The fresh
seed is held out until discovery completes, not selected from observed outcomes.

All children serial, each capped at120s, no measured benchmark/profile. Driver
budget1050s, absolute no-new-child cutoff06:27:00UTC; budget exhaustion is incomplete,
not PASS. Expected under10minutes from prior runs, not a timing or speed claim.
Stop at first unexpected compile/run/assertion failure; preserve stdout/stderr,
commands, timestamps, hashes and snapshot. Do not fix an oracle in place.

Require every existing exact-bit, sorted model, length, mask, outside-count canary,
interval completeness, anchor continuity, ownership/disjointness, leaf-ID, natural
widen/narrow/promotion, allocation accounting and bounded-termination check.
Require terminal PASS and equal logical digest across sources/builds per seed/oracle/
mode. Physical counters and allocation sizes are not presumed equal across builds.
No per-run wall duration is a performance observation. Any failure disqualifies the
affected correctness claim; pass only extends compatibility and leaves C/PARK,
source adoption NONE. Original43tests already passed exact sources in round18/19;
this matrix does not represent their rerun or full fault immunity.

After a successful matrix, a separately preregistered bounded sensitivity transfer
may test existing faults on C. No new fault taxonomy count without review.
Independent reviewer startup failed (thread-store rollout missing); use explicitly
sequential review. Exact backend/model/token cost unknown. Supervisor records CLI
usage separately. Main baseline stays for morning review. No git metadata retry,
publishing, permission change or supervisor/runtime/STOP edits.
