# DIAG-013 — compact traversal warmup intervention

Preregistered before new measurements. AA-011 compact fixtures had three warmup
traversals (285items), far less work than three traversals of the previous n100000
fixtures. Its no-output integer and mixed-output zero cells showed positive A/A bias
in both seeds. Hypothesis: this very short operation-matched warmup contributes to
that bias; increasing fixed warmup work reduces it. Frequency remains unknown; no
claim that longer warmup must cure noise, and no repetition of unchanged AA-011.

Same frozen HARNESS-006 binary and source. Two cells:n95/bytes16/trimmed/forward,
integer mask0 and alternating-zero mask6. Fresh seeds41101/41113. Two interventions:
short3warmuptraversals vs long100000warmuptraversals (9.5mitems). Measured requested
items stay20m,effective20000065. Six blocks, each a separate identical-binary ABBA
within each cell/seed/intervention. Rotatecell/seed and alternate intervention order
by block. Fixed192rows;oneprospective1mitembinarywarmup using short policy,retained.
No additional warmup beyond this schedule, no excludedrows,optionalstopping or changes.
Children<=120s,total300s. Alltimingsserial;no builds/tests/agents duringmeasurement.

Wall ns/effectiveitem primary. Compute six-block effects100*(B/A-1),95%t df5
interval for eachcell/seed/intervention, plus means/dispersion of wall and threadtime,
CPU boundaryIDs,observedQoS,warmupduration and memory/checksum/fingerprint invariants.
Threadtime/IDs cannot establish frequency,coretype or lack of within-window migration.

Support requires: allinvariants and >=10ms windows; ALLfourlong-policy intervals
entirely[-1,+1]%; absolute A/A mean bias at most half short-policy bias in at least
threeoffourcell/seedpairs. Ifshortpolicy alreadyqualifiesallfour, causalremedy is not
established and result is inconclusive. Otherwise unsupported ifcriteriafail. Preserve
allrawrows. This is diagnostic, not sourcequalification; no retroactive AA-011 repair,
pooling, optimization selection or new baseline count. Any referee policy adoption
would need separate freezing/requalification. Independent reviewer unavailable;
sequentialreview,backend/model/costunknown.
