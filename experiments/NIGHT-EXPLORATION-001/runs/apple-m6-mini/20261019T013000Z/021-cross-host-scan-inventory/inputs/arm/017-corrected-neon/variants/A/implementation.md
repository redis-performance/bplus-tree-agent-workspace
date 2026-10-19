# Implementation A — exact nibble-position mask

Author `/root/aws_arm`, native Codex; exact model and measured token/USD cost unknown.
Implemented independently from exact baseline13e459ff8 in an isolated detached Git
worktree. No peer implementation or proposal was read before sealing this patch.

Only src/zset_btree.c changes. A little-endian AArch64+NEON compile guard selects
16-byte comparisons. Tag1 ORs equality against zero. Narrowing each pair of 0xff/0x00
comparison bytes by four bits produces two exact nibbles; a0x1111111111111111 mask
keeps one bit per physical lane. A guarded ctz divided by four identifies the next
physical position. Clearing that single bit emits exactly once in ascending physical
order; reversed mapping retains count-1-position. The original eight-byte word path
handles an odd remaining word, followed by the unchanged original scalar tail.
Unsupported architectures and ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE use original words
and tails. No new state, allocation, hash, assertion, adapter or timing flags.

Every vector load consumes two complete words, bounded by count/8. Exact lane mapping
is restricted to little endian. No zero-mask bit scan or shift by64. Original count0
behavior is retained. Query0 remains exact zero matching; only query1 folds0+1.
Only positions[0..found) are written. Narrow/extract overhead and dense emission remain
performance risks; there is no measured performance claim.

Local x86 native correctness checks exercise the portable fallback only. Original43
passed before the final comment-only clarification; source code semantics unchanged.
V2 oracle result is retained separately. Native ARM NEON compilation/assembly and full
native+ASan/UBSan original/V2/semantic suites await the serial combined600s validation
job and root review; absence of local NEON execution is not presented as native proof.
No candidate timing has run. The designated portable validation macro is
ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE; it must never be set for timing.

A local preparation command initially used parent-relative paths from inside the
isolated child worktree, yielding FileNotFoundError and a missing oracle source before
compilation. It changed no source or checks. The corrected working-directory commands
then copied and built the unchanged V2 oracle. This operational failure is retained
here; no failed native implementation was repaired or discarded.
