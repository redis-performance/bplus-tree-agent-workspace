# DIAG-017 — child completion transport

Preregistered before measurement. Local Python source inspection establishes that
Popen.wait(timeout) with file output uses WNOHANG polling and exponential sleeps up
to50ms; Popen.communicate(timeout) with stdout/stderr pipes uses a selector. Neither
statement measures actual child exit latency. Both retain120s timeout/kill/reap.
Inspect benchmark source: CSV and stderr are produced after the timed interval.

Hypothesis: switching the complete file/poll wait path to pipe/selector completion
attenuates the predecessor-workload contrast without breaking same-workload placebo
precision. This tests transport/buffering/scheduler/parent wakeup together. It does
not isolate polling delay, frequency, cache or CPU placement, and is not a referee
or source optimization. No data transport occurs inside the benchmark timed loop.

Same frozen HARNESS-006 binary, target95/bytes16/trimmed/forward/alternating-zero/mask6,
20m requested items/20000065 effective,3warmups. OTHER predecessor integer/mask0;
SAME identical target. Freshseeds49109/49121. Fourcells file-contrast,pipe-contrast,
file-placebo,pipe-placebo,rotate order eachblock,alternate seeds. A=SAME,B=OTHER in
contrast,bothSAME in placebo. SixABBAblocks/seed/cell:192target+192predecessor rows,
oneprospective1m targetwarmup. Allcommands and paths precomputed. File handles opened
before eachpair forbothpaths. Pipe bytes held in memory until targetreturns,then
written to same rawfiles. Journaling/hash/manifests after each quartet forbothpaths;
minimal identical pair journal before next pair. Record parentCPU/monotonic intervals
and launchgaps. RawCSV may be lost for an interrupted pair in pipe mode; completed
pairs are written immediately. No analysis during measurement, allserial, no agents,
builds/tests/profiles. Individualchild120s,total400s,no rowremoval or optionalstopping.

Wallns/item primary. Sixeffects100*(meanB/meanA-1),df5Student-t95%interval; thread
secondary. Supportrequires all functional/count/fingerprint/memory controls,targets
>=10ms,bothfilecontrast upperbounds<-1%,allpipecontrast andpipeplacebo intervals
inside[-1,+1]%,bothpipecontrast magnitudes<=halffilecontrast,andbothpaired
interaction(pipe-file)lowerbounds>1%. Fileplacebo precisionreported. Otherwise
unsupported;controls failinvalid/PARK. No acceptance or timingpolicyadoption;
separatefreshconfirmation/qualification needed evenif supported. Actual exitgap,
frequency,effectiveQoS andwithinwindowmigration unknown. Backend/model/costunknown;
independentreviewerfailed,sequentialreview. OriginalsourceguardremainsPARK.
