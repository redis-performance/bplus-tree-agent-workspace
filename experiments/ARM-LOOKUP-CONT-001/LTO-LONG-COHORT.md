# ARM LTO long-window metrology cohort — preregistered change

The original GCC15/LTO qualification2 failure remains PARK: update block2−1.318389% exceeded±1%. No unchanged retry. Under the six-hour charter, test a distinct measurement condition: all six work counts increased5×, with controller pinnedCPU0 and child explicitlyCPU2. Keep source, exact existing GCC15/LTO ELF, libc, seed17 and acceptance gates unchanged. This tests whether longer samples plus controller separation qualify stable observations; it does not establish the cause of the old failure.

Fixed sweeps: hit250000,score250000,miss500000,long100000,external100000,update100000. Three ABBA A/A blocks percase,72rows. Everyblock±1%; everyrow≥250ms; exactchecksums/finalstate/ownedmemory. Failure parks this newcohort without further unchangedretry. No candidate comparison precedes full pass. Successful comparisons use the same workscale/controllerisolation, threeblocks/case,≥2% hit improvement everyblock and≤1% guard/memory regression.

Record child user/systemtime, contextswitches and faults around each process as diagnostic telemetry; these include setup/warmup and are not timed-loop counters. No PMU instrumentation enters A/A. The two changed conditions are not factorially separated, so no isolated attribution to duration or controllerpinning is permitted. Original failures remain published. Newcohort evidence cannot retrospectively qualify oldLTO rows.

TMA classification: Frontend_Bound,Bad_Speculation,Backend_Bound,Retiring and children unavailable for this timingqualification; no profile collected here. Matched profiles/topdown assessment follow only in a separate profile phase.
