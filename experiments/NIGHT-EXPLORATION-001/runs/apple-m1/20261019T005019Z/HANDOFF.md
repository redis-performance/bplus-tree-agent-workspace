# Round 3 early-stop handoff — 2026-10-19

The injected round ends 02:02:30 UTC; this handoff was prepared about
01:45 UTC, more than 90 seconds before cutoff. Runtime started 00:50:42
UTC; injected campaign deadline remains 20:00 UTC. The first-pass queue is
complete and no eligible candidate remains. [Early final report](MORNING-REPORT.md),
[blocked note](BLOCKED.md), [host status](STATUS.md), and
[DECODE-001 result](005-decode/RESULT.md) are the current documents. Do not
restart the expired October 17 campaign.

**First next action if external state changes:** check published
`exploration/apple-m6-mini-*` branches and main, read the exact M6 status,
decision, patch and harness hashes, then compare only matching source/patch
locally. The last remote check at 01:43:12 UTC failed DNS resolution for
`github.com`; M6 branch, commit and outcome are UNKNOWN. An explicit M6
discard of a matching candidate vetoes M1 timing. No M6 numbers were pooled.

DECODE-001 built isolated scratch snapshots from the launch source and frozen
EXP-008 referee. Eight release/sanitizer self-tests, 1,040 focused cells and
the four serial phases pass. `005-decode/AUDIT.json` reconstructs all 6,720
processes / 866,880 rows. A/A qualifies 0/70 cells; all three variants have
large repeated guard losses despite width-60 count-one gains. Decision
PARK/source NONE; no fresh confirmation or public iterator work. Three
proposal and implementation passes were sequential by one GPT-6 worker,
not independent agents. Exact backend variant and round-3 measured token
usage remain unknown. Prior EXP-008 whole-process samples and current
assembly are the only decoder mechanism evidence; fresh macOS sampling was
denied once and not retried. All three losing patches are retained.

Optimization totals are now 0 accepted / 3 rejected / 6 parked across
9 populations. The tree and header SHA256 remain
`d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`
and `496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83`.
Frozen `bench/microbench.c` remains
`b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde`.
Current host branch HEAD at reporting is
`4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9`, published through round 2;
round-3 evidence is uncommitted after the recorded index-lock denial. Do
not retry denied Git writes or change permissions. The coordinator can
verify publication when a writable Git context exists. No timing children
remain. No source candidate was adopted.

Do not repeat failed rank, update or decoder A/A schedules unchanged. A
separate, committed and qualified precision-referee revision or a newly
published M6 patch is needed before another useful comparison. The bounded
extension applies only when such evidence arrives; the early stop follows
PLAN.md's stop-early rule. No upstream PR/issue/merge action is authorized.

## Prior round 2 handoff

Campaign runtime started 2026-10-19 00:50:42 UTC and ends at the injected
2026-10-19 20:00:00 UTC deadline. Round 2 ends 01:42:43 UTC; use the
runtime status and next injected round deadline, not archived calendar dates.
This handoff was prepared before the round cutoff. Do not restart the
expired October 17 campaign.

**First next action:** recheck published M6 branches/main and the latest
same-hypothesis decision. Last attempts through 2026-10-19 01:26:29 UTC
failed DNS resolution for github.com; branch, commit, patch and outcome are
UNKNOWN. An explicit matching discard vetoes the M1 trial. No M6
performance numbers have been used.

RANK-001 completed three isolated source snapshots from launch commit
77d32df82cd5da02b95c6afb6193fcf83f67223f. Native, ASan/UBSan and
targeted rank oracles pass. A/B/C shorter-side patches are retained.
The frozen 144-process public-rank discovery screen did not find a
consistent dual-primary improvement. Bounded trial REJECT, source NONE;
strict 100K/1M A/A remains failed. See 002-rank/RESULT.md. Three
implementation passes were sequential by one GPT-6 worker, not
independent agents.

UPDATE-001 completed a new independent-permutation five-path referee:
75-process inventory, untimed path/reason census, six scoped profiles,
release/sanitizer validation and a 48-process same-binary A/A. At 1M,
11,058 of 20,000 position-preserving updates reinsert solely because
the exact score does not fit the current packed leaf representation.
Both primary A/A cells fail; candidate NONE and no implementation
population. See 003-update/RESULT.md. Do not repeat this A/A schedule
unchanged or use this new uncommitted referee for candidate comparison.

LOOKUP-001's independent-query referee passes release/sanitizer hit/miss
through 1M. Longer hit profiles locate platform memchr; untimed
counts show about 1.14–1.16 full member comparisons per hit.
Three sequential proposal passes led the chair to NONE; EXP-006
already tried the supported inline scanner family and saw
single-lane concerns. See 004-lookup/RESULT.md.

The optional slot now points to a **DECODE-001 count-one diagnostic**,
with ITERATE-001 skipped this pass. 005-decode/SELECTION.md records
why. Next bounded loop: inspect exact frozen EXP-007 B and original
scalar count-one paths, profile the current count-one contract,
then freeze a new hypothesis/population/guard plan or select NONE.
Do not describe seed-invariant count-one values as new input diversity.
Do not integrate a private decoder result into the public iterator
without a separate design and guards.

Round 2 audit PASS: 144 rank process CSVs, 75 update inventory CSVs,
48 update A/A CSVs, 25 update path cells, 10 reason cells, 12 lookup
validation cells, 12 lookup counter cells and 12 lookup profile logs.
ROUND-002-FILE-HASHES.sha256 lists 620 round 2 evidence files; all
entries were checked after generation.
Root tree and frozen bench/microbench.c retain launch SHA256 hashes
d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2
and b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde.
Raw profile logs and original path-bearing transcripts remain in
ignored scratch; public evidence uses relative paths. All tool
children exited. No final report is due until campaign elapsed 7h15
or a final_round signal.

The local host branch HEAD is c53b1d91ab8103f7e923791f5380c434db5da0c7,
published externally after round 1, with the same tree blob as launch.
Round 2 evidence and documentation remain uncommitted. The round 1
index-lock denial was recorded once; this worker did not retry git
writes or a push. Commit/push provenance remains pending when an
authorized writable git context is available. Exact backend variant
and measured round 2 token usage are unavailable until supervisor
accounting completes; model family GPT-6 is known. Current totals:
0 accepted / 3 rejected / 5 parked across 8 populations.

# Round 1 handoff — 2026-10-19

Round 1 has a complete five-size baseline and a profile-supported rank exploration target; no candidate or source change. Read `STATUS.md`, `HOST-MANIFEST.json`, `001-baseline/matrix/SUMMARY.md`, `002-rank/README.md`, `002-rank/selection.md`, and `002-rank/DISCOVERY-PLAN.md`. The full campaign deadline is 20:00 UTC; use `scratch/night-apple-m1-20261019T005019Z/status.json` for elapsed time and the next injected round deadline. Do not follow the expired October 17 campaign.

**First next action:** check the remote for published M6 host branches/main and record exact UTC, branch, commit and decision, or UNKNOWN if unavailable. If the same hypothesis is explicitly discarded there, skip the M1 trial and advance to UPDATE-001. Otherwise create three isolated source snapshots/builds from launch HEAD with unchanged referee, implement and validate the chair's shorter-side rank hypothesis in three distinct ways. Git writes were denied once at the worktree index lock; do not retry a denied commit in this round. Preserve exact patches/hashes, and use source snapshots if worktree creation remains unavailable. No baseline `src/` edit.

Then run only the fixed exploratory primary screen in `002-rank/DISCOVERY-PLAN.md`, serially, if validation and deadline permit. Rank controls failed precision, so no variant can be accepted from this screen. Preserve raw rows and negative results. Move to UPDATE-001 when the bounded screen concludes or is vetoed. Do not repeat the failed A/A schedule unchanged.

Baseline runner edit: metadata-only fallback for denied macOS `sysctl`, patch SHA256 `e0975200db490c1bed12aee8099da4aaff9bfa85bcc396a9e649785c3d5a1d3c`. Tree hash `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`; referee hash `b84d81d0e39b4c7405da0bc12e4f1a14b7fd1f83a38fec595fea87ad3d9effde`. Profile binary and diagnostic hashes are in `002-rank/` output or should be recomputed from retained scratch if needed. No detached children. Model family GPT-6 per session instructions; exact backend variant and measured token cost unavailable. Sequential proposals are not independent agents.
