# Natural-wrap and colliding-SCAN census — PASS

Three serial whole-oracle baseline captures pass every model check. The real zero-skip
branch is taken twice in the singleton fixture and four times in the multi-member
fixture. Active batch flushes occur two/six times respectively. The SCAN fixture records
256active-table scan calls,68250displaced-slot paths,712995multiple-tag match paths,
and62728probe-reachability rejections. These counts include entire oracle processes;
they do not measure CPU time, hotness, speedup or timed-loop cost.

PLAN.md freezes the scope. run.py builds all three before captures; analyse.py checks
mapped source-file/line/column branch records and writes summary.json. manifest.json
preserves commands, source/binary/raw/export checksums and timestamps. Curated *-counts.json
resolve actual coverage file IDs, including macro expansions. Raw profiles/exports remain
in ignored scratch. No frequency, placement or performance inference. Source NONE and
previous PARK unchanged. This is the28th additional diagnostic; suites22/faulttypes44
unchanged. Independent review unavailable; backend/model/cost unknown.
