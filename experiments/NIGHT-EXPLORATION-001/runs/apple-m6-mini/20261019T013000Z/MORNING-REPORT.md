# M6 morning report — interim operator checkpoint

Updated 2026-10-19T04:15:02.401889+00:00. Active through08:00UTC/09:00Lisbon; experiments end07:15UTC.
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

The [baseline geometry census](007-profile/RESULTS.md) is sealed. The three
independent [follow-up proposals](008-review/selection.md) choose NONE: geometry
and assembly do not establish a paid score-load stall.

The [iterator profile](009-iterator-profile/RESULTS.md) has 16 sufficient local
captures, 1054 sampled PCs. Frame regions account for 303 PCs, a descriptive count
rather than cycle cost. This exposed an incomplete compiler contract in the
standalone adapter: `standalone_panic` always aborts but lacked `_Noreturn`.
[Two independent reviews](010-assertion-contract-review/README.md) verified the
exact two-line adapter correction, 43 native and 43 sanitizer tests, and eight
abort probes. Tree C/header stay unchanged. Static iterator code shrinks from
155 to 114 instructions and its normal stack frame disappears; this is not a
measured speed claim. The separately committed correction is now on main at
13e459ff8 and on this exploration branch at 7f299a5f5.

The [corrected baseline](011-contract-baseline/RESULTS.md) completes 120 processes,
960 rows and seven validations; independent raw audit PASS. Five of 40 cells
qualify, 35 are noisy, and 14 include short windows. Operation timers sum to
71.958584 seconds; subprocess-loop wall time is 160.052971 seconds. Historical
old-adapter rows remain separate and cannot be subtracted to infer improvement.
The five-host README chart retains its original-adapter identity.

The [matched adapter diagnostic](012-contract-diagnostic/RESULTS.md) completes
384A/A and192old/newABBA processes. All checks pass, all windows exceed10ms, and
owned memory is identical. Only3/16adapter/workload controls qualify; zero ofeight
workloads qualify onbothadapters. Thus all effects remainconditional. Fullinteger
forward/reverse medians are−6.081%/−8.122% at100K and−4.674%/−7.058% at1M,
all observed blocks negative. Failed controls prevent a qualified speed claim.
This is harness-only; no candidate population/adoption. Independent audit PASS576rows/144exact effects; chart complete. Corrected-adapter baseline-only profile013 is preparing; no capture yet.
No cache replication or new source optimization is selected.

Totals12completedpopulations(9sequential+3multi-agent),0accepted/7rejected/5parked,
36retainedpatches/15validatedharnesses. M1 night and concurrent AWS populations
are separate. [Shared live scoreboard](STATUS.md). [Measured supervisor usage](USAGE.json)
excludes unknown interactive-root/collaboration-agent accounting.

The prior worker checkpoint is preserved in
[REPORTING-WORKER-ROUND010-MORNING.md](REPORTING-WORKER-ROUND010-MORNING.md).
An ownership barrier ended its empty reporting loop at round10; the interactive
root continues the campaign and invokes the same single-writer publisher.
