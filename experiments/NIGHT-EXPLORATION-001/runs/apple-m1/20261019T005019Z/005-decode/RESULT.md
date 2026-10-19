# DECODE-001 — count-one private decoder trial

**Decision: PARK; source selection NONE.** All three sequential, isolated
count-one policies passed correctness. Each had exploratory width-60 count-one
gains, but the frozen A/A qualified **0/70 cells**: every timed batch window was
under 10 ms. Each policy also had large, repeated guard losses. None is eligible
for fresh confirmation or integration with the public iterator. The count-one
idea remains a lead only if a distinct, qualified referee and guarded policy are
designed; do not repeat this schedule unchanged.

| Variant | Width 60 forward count 1 | Width 60 reversed count 1 | Example losing guard, paired block range |
|---|---:|---:|---|
| A: scalar for all count-one ranges | −18.00% [−18.69, −17.30] | −9.80% [−10.40, −8.71] | width 63 forward count 2: +17.14%..+19.76% |
| B: scalar for noncrossing count one | −35.29% [−35.89, −34.80] | −26.87% [−27.40, −26.36] | width 59 forward count 1: +13.53%..+15.29% |
| C: scalar for width-60 count one | −43.68% [−43.70, −43.19] | −25.16% [−25.34, −24.14] | width 0 forward count 16: +19.41%..+23.14%; width 60 forward count 2: +6.47%..+6.60% |

Entries are medians of six ABBA block effects, with observed block ranges;
negative means less elapsed time. They are unqualified exploratory observations,
not confidence intervals or portable speedups. The count-one fixtures have
invariant deltas across seeds. No outlier was removed. At the primary A/A cells,
the forward blocks span −0.05%..+1.88% with minimum windows 0.176–0.180 ms;
the reverse blocks span 0.00%..+1.84% with 0.161–0.164 ms windows. The global
minimum window was about 0.011 ms. Zero of 70 A/A cells passed both fixed gates.
There is no measured frequency, DVFS state or within-window core residency.

The frozen EXP-008 count-one whole-process samples locate decoder policy and
caller PCs but include setup and warmup. A fresh `sample` attempt on both current
release binaries returned 255 (`sample cannot examine process`); it was not
retried or used as evidence. Current generated Apple Clang assembly shows the
count-one branch and output store in A. Base and A retain an outlined policy
call; B/C inline policy code into the batch caller. Thus the large guard losses
on unchanged bulk paths may involve caller layout/codegen, and the trial does
not isolate a pure decoder-operation cost. The same double-array store,
materialization barrier and checksum are in the frozen kernel for every variant.
Tree-owned leaf bytes and fixture/checksum fields match across variants.

The campaign used an Apple M1, Apple Clang 17 `-std=c11 -O3 -g -Wall -Wextra
-Werror -fno-omit-frame-pointer -fno-lto`, one unpinned process at a time.
All eight release/sanitizer self-tests passed 1,820 fixtures each; 1,040 focused
width/direction/count/shift validation cells passed. A/A and three candidate
phases each ran 1,680 serial processes, 216,720 timed sample rows and six blocks
per cell; total 6,720 processes, 866,880 rows and 108.88 seconds of process
timing. The independent archive audit reconstructed every row, process median,
fixture/checksum, paired block and hash. Four compressed raw archives and
manifests are in `aa/` and `discovery-{A,B,C}/`; [audit](AUDIT.json) has all
70 cell effects and observed ranges. All three losing [patches](candidate-A.patch)
are retained alongside `candidate-B.patch` and `candidate-C.patch`.

Source pin: launch HEAD `77d32df82cd5da02b95c6afb6193fcf83f67223f`,
tree source SHA256 `d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2`;
frozen bulk helper `6da7d81bfd0dfa9828922cd17508403b7ea9a86ea3ac64159dedacf6a02ab4ad`;
kernel `e8c43850860c7018a82f99d94f872ce049ff8835c7dae69cd30458560e5046c8`;
driver `f5e61ec7ed88b01a11d928285f891c8b88ae5efd90b76081976341d4953d4aa5`.
Build flags, all input, binary and assembly hashes are in the
[public build summary](BUILD-SUMMARY.json); full command logs remain in scratch.
Git writes were previously denied at the worktree index lock, so commit-based
provenance remains pending. No root tree source changed.

Reproduce from the repository root, using a new output path for each phase:

```sh
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/005-decode/build-local.py --out scratch/night-apple-m1-20261019T005019Z/round-003/decode-build
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/005-decode/build-local.py --out scratch/night-apple-m1-20261019T005019Z/round-003/decode-build-sanitize --sanitize
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/005-decode/run-local.py --build scratch/night-apple-m1-20261019T005019Z/round-003/decode-build --out NEW-PHASE-OUTPUT --phase aa --budget-seconds 300
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m1/20261019T005019Z/005-decode/analyse-local.py
```

`--phase A`, `B`, or `C` runs each frozen candidate comparison. Use the actual
run directory when reproducing; no original raw rows should be overwritten.
M6 branch/main checks at 01:32:51, 01:36:15, 01:38:02, 01:38:46 and 01:39:28
UTC failed DNS resolution for `github.com`. Branch, commit and matching decision
are UNKNOWN; no M6 timing was pooled. The CPU Performance Engineering MCP was
consulted for method, but the conclusion rests on local raw rows and assembly.
No independent agent or reviewer ran; this was one GPT-6 worker making three
sequential proposal and implementation passes. Exact backend variant and
measured token cost are unknown.
