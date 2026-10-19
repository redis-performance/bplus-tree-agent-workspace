# M6 morning report — interim operator checkpoint

Updated 2026-10-19T03:39:22.056759+00:00. Active through08:00UTC/09:00Lisbon; experiments end07:15UTC.
Source selection **NONE**. All five M6 candidate trials reject their declared gates.

| Trial | Finding | Decision |
|---|---|---|
| Rank |100K regressions in everyblock|REJECT|
| Update repacking |1M lead,100K gate fails|REJECT dualprimary|
| Physical-score lookup | B100K−4.80%,1M gate fails|REJECT dualprimary|
| Count-one decoder |~30%privatecount-one lead; qualified guard losses|REJECT universal policy|
| [Caller specialization](006-followup/RESULTS.md) | A100K−2.712%everyblock;1M2/6blocks reach2%|REJECT dualprimary|

Latest trial has three actual independent proposal agents and three isolated
implementations. All original native/sanitizer tests and exact-bit oracles pass.
The independent audit verifies2871rows/66frozen artifacts. Baseline101-cellAA:
39qualify,62noisy,0short;100Kprimary qualifies,1Mfails. No eligible fullcandidate
guards, fresh confirmation or adoption profile. [Chart](006-followup/candidate-screens.png).

The [baseline geometry census](007-profile/) is a new baseline-only diagnosis.
It does not select a new optimization or establish cache misses. Detailed sealed
report is pending. Baseline src/header/referees remain unchanged.

007geometry diagnosis is sealed;008proposal-only review endedNONE with three
independent proposals. No score-load bottleneck is established.009nowprepares
a local baseline iterator profile to assess published Intel/ARM cache leads.
No architecture replication or new candidate is selected yet.

Totals12completedpopulations(9sequential+3multi-agent),0accepted/7rejected/5parked,
36retainedpatches/15validatedharnesses. M1 night and concurrent AWS populations
are separate. [Shared live scoreboard](STATUS.md). [Measured supervisor usage](USAGE.json)
excludes unknown interactive-root/collaboration-agent accounting.

The prior worker checkpoint is preserved in
[REPORTING-WORKER-ROUND010-MORNING.md](REPORTING-WORKER-ROUND010-MORNING.md).
An ownership barrier ended its empty reporting loop at round10; the interactive
root continues the campaign and invokes the same single-writer publisher.
