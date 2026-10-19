# Corrected baseline profile audit — PASS

All16 planned captures agree with retained commands, raw PC data, public bins and
fixture metadata. Each contains35–75 captured PCs and meets the preregistered25-PC
minimum. All18 frozen input hashes and three binary hashes match. **This establishes
sufficient baseline captures under the declared sampling scope; it establishes no
speedup, cache behavior, cycles or unbiased cost share.** Source selection remains
NONE.

Reviewer `/root/followup_proposal_c`, GPT-6/Codex family; exact serving model, token
usage and monetary cost unknown. This independently audits A's profile driver and
root's captures. A's separate region analysis was neither read nor changed. No new
profile, benchmark, build, source edit, agent launch or Git write occurred.

## Schedule, launcher and identity

The independent script verifies the exact16-entry inventory:100K/1M members,
integer/full/forward, integer/full/reverse, integer/score-only/forward and
fraction/full/forward, each on seeds1/2. Actual command names, full argument lists,
output masks,100million requested items,16-byte members, three warmup passes,
120-second child bounds and order exactly match the frozen plan and planned-command
document. Three build commands also match their declared flags and inputs.

Each capture records the explicit `PROFILE_USEC=1000` override. Static launcher
inspection confirms that the corrected driver supplies that environment to `Popen`;
every raw PROFILE header independently reports1000us. The launcher fix was resealed
before authorization, with no binary rebuild, semantic-check rerun or early capture.
There are exactly16 profiler invocations in the complete30-command journal, all
after authorization. No capture retry or hidden extra invocation is recorded.
1000us is the requested/applied interval, not a measured delivery-rate guarantee.

Current source/header, corrected adapter, referee, unchanged sampler, plan, driver,
correctness records and all three binaries match their18+3 frozen identities.
The ACK hashes match the final freeze/driver/plan. Local commit
`7c8f5c0bdcbfdc32ce779ea2e6c36cb1b0378529` contains the exact acknowledged freeze,
driver, plan and command inventory. Authorization precedes launch and the first
capture. This verifies retained ACK/local commit provenance; no live remote
publication check was performed.

## Private PCs to public evidence

All60 stdout/stderr log pairs from the30 commands match both public and private
hashes. Each raw capture has one PROFILE header, the matching PC count and no
recorded sample-buffer overflow. The audit independently reconstructs every
module/symbol count and symbol-relative offset bin from the private PC rows and
compares it with both the per-capture JSON and final summary. All sums and bins
agree. No process addresses are published by this audit.

The public stderr transformation is verified exactly: raw PC rows are removed,
the PROFILE header is retained, and the private-row-count marker matches the
removed count. Private raw PC file identities remain recorded by checksum.

| Contract |100K PCs, seeds1/2|1M PCs, seeds1/2|
|---|---:|---:|
|Integer, full output, forward|55 /56|63 /73|
|Integer, full output, reverse|61 /75|68 /69|
|Integer, score only, forward|48 /42|35 /48|
|Fraction, full output, forward|51 /67|63 /63|

These are per-capture counts, not performance comparisons. The original009 sample
counts were not read or pooled. Only its frozen referee/bridge bytes were checked
for exact identity. The historical002 known-work sampler controls retain their
hashes and expected sampler-probe attribution; they are reused controls for the
unchanged sampler, not a fresh corrected-adapter calibration.

## Scope, correctness and cleanup

Source inspection verifies the existing sample hooks enclose traversal plus its
QoS/CPU/thread-clock observations. Construction, initial semantic verification,
warmup, post-traversal verification, output and teardown remain outside those hooks.
The sampler is stopped and blocked before raw-PC reporting. Symbol/offset evidence
does not turn that scope into exact timed-loop attribution or unbiased time shares.

Independent Python fixture reconstruction reproduces all five construction
fingerprints and nine checksum contracts, including the small semantic fixture.
Requested/actual counts, traversals, seed, member length, encoding, direction, mask,
warmup and exact-bit checksum metadata agree. Owned bytes match the same corrected
fixture identities in012; no012 timing or PC data is combined with these profiles.
All eight sealed native/sanitizer semantic checks and exact-identity reused43-test
logs retain matching hashes. No tests were rerun.

Every recorded command exits successfully without timeout and is marked reaped.
All16 capture UTC intervals agree with their command records, are serial and fall
inside the completed capture phase. The capture lock is absent. Recorded capture
phase wall time is8.198410291seconds, within its900-second budget and absolute stop.
That is orchestration wall time, not profile cost or an operation speed measurement.
Recorded intervals establish seriality among these children, not proof that every
other host process was idle; exclusive-runner/other-work-idle remain operator ACKs.

All emitted operation elapsed fields remain unused by this audit. No CPU endpoint,
PC count or symbol bin supports a frequency, residency, cache, cycle or causal
speed claim here. Region interpretation remains a separate review, and sufficient
capture counts do not select an optimization hypothesis or satisfy adoption gates.

Reproduce the read-only audit from the repository root:

```sh
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/013-corrected-iterator-profile/independent-audit.py
```

`INDEPENDENT-AUDIT.json` preserves reconstructed bins, capture metadata, private file
identities, publication provenance and audit limits.
