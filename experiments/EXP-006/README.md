# EXP-006 — bounded inline leaf tag search

Date2026-10-18. Status complete; decision C/PARK, source adoption NONE. Main baseline preserved.

## Frozen context

Basea2ff0c5ddc00ffc11ff7d73e202d6384df77c84c plus explicitly uncommitted SHA256
snapshots in freeze.json. Source PRa7ecd959374d66847c095250bf2d373edf7316c5.
HARNESS-007attempt002, unchanged libc allocator/SipHash/assertions, Apple Clang17
C11O3-g-Wall-Wextra-Werror-fno-omit-frame-pointer-DREDIS_DEBUG; O1ASan/UBSan correctness.
Local M1arm64, one unpinned thread; frequency/effective QoS/migration unknown.

[PLAN](PLAN.md) freezes primary mixed16/batch16, qualified hit320/batch16 guard,
three additional unqualified diagnostic guards, seeds/counts/blocks/thresholds/fresh
confirmation/profile scope. [AA-012](../OVERNIGHT-2026-10-17/AA-012/README.md)
qualifies both chosen cells on bothseeds. [PROFILE-004](../OVERNIGHT-2026-10-17/PROFILE-004/README.md)
shows memchr leading mixed captures. No independent agent ran; exact backend/model/
token cost unknown, supervisor records usage separately.

## Population step1

Three sequential proposal passes, not independent agents: Ainline tag scan;
Bfuture-query prefetch; Clength prefilter. [Chair](selection.md) ranksA/B/C and selects
only bounded inline tag scan. Profiles do not establish memory stalls forB, and current
fixtures lack unequal lengths forC. All proposal records preserved.

## Population step2

Three isolated implementation passes share exact source and referee. Abyte scan,
B8-byte memcpy/SWAR scan, C16-byte unrolling with8-byte/scalar tail. Word paths require
little endian; other hosts use bounded scalar fallback. Patches and risks in variants/.
No assertion/hash/allocator change. Losers stay retained. Correctness complete; measured selection C/PARK; no claim of an independent population.

## Correctness and validation

[Driver](validate.py) freezes original43tests, raw guard pages, exact first-match
oracle and batch fixturegrid in native and ASan/UBSan. [Measurement](measure.py)
and [analysis](analyse.py) run fixed serial ABBA and held-out seeds after validation.
All stdout/stderr, command windows, hashes and failed outcomes retained.

## Decision and review

[Implementation selection](implementation-selection.md),96fresh confirmation rows,
matched profiles and [sequential review](review/adversarial.md) complete.
Cpasses the fresh primary bound, but one long-key guard is inconclusive and the
unqualified single-lane guard shows concerning screening regressions. No ACCEPT possible until missing original/additional guard
qualification, independent review and committed provenance are resolved. No upstream
action, publishing or git metadata retry. Source baseline stays for morning review.
