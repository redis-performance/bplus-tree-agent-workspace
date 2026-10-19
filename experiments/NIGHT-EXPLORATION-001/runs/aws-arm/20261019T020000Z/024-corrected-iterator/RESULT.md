# Corrected ARM score-only iterator baseline result

**Both fixed A/A cases qualify; source NONE.** Baseline diagnosis only, with no
candidate, proposal round, implementation or new measured optimization population.
All prior decoder/iterator/NEON decisions remain final. This separate corrected13e
score-only workload does not retry old8fab full-output replication or transfer AMD029
measurements/qualification. Root and AMD independently reviewed the profile before
root explicitly granted the separate A/A phase.

[Profile result](PROFILE-RESULT.md):51 commands, six fixed captures,970 scientific
samples, all original/disabled/native/sanitizer/known-work controls pass. Independent
AMD raw reviewd42ca4ef2 reconstructs the controls and exact actual013 code mapping;
root separately verifies it. Caller mapping differences remain explicit.

A/A owned-helper interval2026-10-19T06:33:07.488086Z to06:33:47.200851Z, return0,
serialCPU2,300s hard cap. All48 processes/12 complete blocks, exact50M operations,
16-byte members, sizes100K/1M, seeds701–703 twice, same-binary ABBA. Every actual
operation/checksum/traversal/warmup/owned-memory invariant and source/referee/binary
identity check passes. No retry, discarded block, operation adjustment or seed change.

| Case | Max absolute paired A/A effect | Minimum window | All six gates |
| --- | ---: | ---: | --- |
| 100K |0.05391125%|166.240475ms|PASS|
| 1M |0.37152408%|186.780319ms|PASS|

All individual effects, raw CSV/stderr and command windows are preserved in aa/;
aa/audit.json reconstructs the complete schedule. Actual timing binary remains
330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc, exact corrected
source13e459ff8800be3f02b6b45c87dd7b0c39453fa9. New diagnostic binaries never replaced
it. Both phases use the same allocator, assertions, hashing and fixed native flags.

The original corrected0131M-op iterator windows were short; this fixed50M contract
was selected before new measurements, without duration calibration or priming. Longer
windows are not claimed to guarantee qualification in general. These observations
are not an old/new adapter speed comparison or a comparison with another host.

Runner workload has ended. Raw A/A review and root decision remain pending. Source
selection staysNONE, and no candidate/proposal is authorized by timer qualification
alone. Any next hypothesis needs source-linked profile evidence, independent proposals
and chair decision, isolated implementations, frozen comparison and all acceptance
gates. No new phase follows automatically. Fleet lease remainsACTIVE until08UTC;
actual release/OSS restoration remain pending.
