# Natural widening and relocation reachability — validated

Four fixed whole-oracle captures pass all existing checks: baseline live widening,
active clone, all-move and selective-decline relocation. Actual narrow and wide ID
reads, dual-table SCAN and resize completion occur in every capture. Active duplication
occurs in clone mode; active header/index relocation and leaf repair occur in both
move modes, and the NULL callback branch occurs in selective mode.

Every capture observes2047mixed-width SCAN calls. Counts include fixture setup and
all verification; they are reachability evidence, not timed-loop samples, hotness,
cycles, frequency or speed gains. The original numeric cursor spans actual mixed and
completed width states; no private ID injection is used.

[Preregistered plan](PLAN.md), [manifest](manifest.json), [summary](summary.json),
[fixed analysis mappings](analyse.py). Raw profiles/exports stay in ignored scratch,
with committed-size branch summaries and hashes here.29additional diagnostics;
source NONE and all existing PARK decisions unchanged. Sequential review only.

[Two additive captures](extensions/README.md) confirm external-buffer move/decline and
dense renumber/rebuild paths. Total six captures; diagnostic count remains29.
