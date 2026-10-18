# Compact-history baseline profiles

After HARNESS-006 validation/freeze, build a separate instrumented copy of unchanged
baseline using the previously validated public self-sampler from PROFILE-003. No timing
rows from instrumented binaries enter speed comparisons. Two known-arithmetic controls
of 400m iterations and six captures: n95, 100m requested items, three warmup traversals,
construction trimmed; integer forward mask4 bytes16, alternating-zero forward mask6
bytes16, wide forward mask7 bytes320, seeds41031/41043. Record exact rounded counts.
PROFILE_USEC=1000, serial children <=120s. Build everything before capture.

Controls: exact checksum, all semantic/count/memory checks, no dropped samples,
resolved symbols, >=15 captured PCs per traversal; calibrations >=30 PCs and >=90%
known_arithmetic samples, checksum3200000000. No profiling cadence/frequency claim.
If controls fail, retain failure/PARK profile. This is descriptive fixture evidence,
not evidence that a previously selected candidate must win or a new optimization vote.
