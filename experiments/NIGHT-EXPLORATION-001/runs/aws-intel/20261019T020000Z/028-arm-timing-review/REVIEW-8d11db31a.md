# Independent ARM timing review — initial revision

Reviewed immutable `8d11db31a`, ARM027-mask-followup. **No launch clearance:** the separately reviewed composite preparation closure and auditor corrections remain pending. No ARM files were changed and no runner/build/benchmark work occurred.

## Concrete blockers

1. `run-phase.py:9` correctly requires the original preparation result to say `correctness_complete`. The actual failed preparation must remain failed. A separately pinned composite closure must bind the original evidence, accepted already-observed fault diagnostic and bounded never-started continuation, plus final source/referee/protected/public/guard binary identities. Removing the failure check or relabelling its original result would lose evidence. Root/ARM already identified this transition.
2. `audit-phase.py:11–18` trusts `run.checked` and independently checks only raw/record equality, CPU endpoints and positive elapsed time. A consistently wrong size/seed/operation count/warmup or iterator mask/direction/encoding/checksum can pass that audit. Reconstruct fixture semantics independently against each frozen contract, including exact original operation order and same-fixture baseline A/A references for comparison. Preserve the distinction between audit integrity and qualification/guard gate outcomes.
3. `audit-phase.py:12–14` checks timestamp ordering but not the 60-second child limit, whole phase budget or 10:15 UTC deadline. Validate all three independently. The outer lease helper remains the actual hard process-group bound; this is a missing evidence audit, not a request to change timing budgets.

## Verified scope and schedules

`check-schedules.py` independently reconstructs all six schedules from the written matrices, without importing producer code. All 25 freeze identities and all 4,272 planned commands match:48 primary A/A,48 primary comparison,120 original A/A,120 original comparison,1,968 iterator A/A and1,968 iterator comparison. Labels, exact binary selection, block-major/reversed cell order, six blocks, seeds1101–1103 or1301–1303, counts and full argv match. Confirmation1201–1203 is unused.

The independently generated matrix matches82 required iterator cells and40 original cells, of which29 are required and11 predeclared diagnostics. The auditor’s lines34–45 correctly implement every-block±1%/10ms qualification, primary every-block≤−2%, guard all≤+1% pass, all>+1% reject and mixed PARK. Qualified adverse diagnostics contribute to the overall REJECT/PARK flags and cannot be erased merely because they are coverage-only. A full diagnostic comparison after noisy guard controls is explicitly allowed by the plan; it cannot establish a qualified pass.

The original1M-op lookup-hit/rank sum formula is valid for all five declared sizes because1M is divisible by each size. Mode checksum reconstruction agrees statically with HARNESS-004 raw score bits and HARNESS-005 folded bits, signed zero, first-member-byte and length contributions, unsigned64 wrapping and traversal rounding. The alternating-zero fixture’s4096 size is even; the negative-zero half-count is valid for this frozen inventory.

## SCAN semantics and build provenance

Frozen `13e459ff8:bench/microbench.c:214–224` permits legitimate SCAN duplicates, then independently checks full member coverage, exact bytes/score identity and per-traversal callback count/checksum outside the timed loop. Consequently `operations == size*traversals` or a unique-score closed-form checksum is not valid. The auditor should check the lower count bound, count/checksum divisibility by traversals, exact same-fixture baseline A/A output and ABBA equality, while explicitly relying on that unchanged assertion-checked referee for duplicate-aware semantic coverage. No new reference workload or referee change is justified.

Preparation commands use identical relative source/output paths and flags for control/A modes and modes5, separately for native and sanitizer builds. These are separate-TU guard programs. The preparation’s public reconstructed control/A `.text` checks establish parity with their respective actual public binaries; they do **not** assert that different guard executables have the public benchmark’s `.text`. The composite closure must separately retain the new guard binary hashes, copied oracle/source snapshot hashes and matching source-specific validation. Timing pre/post guard hashes must bind that reviewed closure.

## Provenance

Participant `/root/aws_intel`; exact native backend/model, token usage and costs unknown. Prior ARM026 raw/chart review and Intel027 confirmation-driver authorship are disclosed; this reviewer did not author ARM027 timing orchestration. This is static and local metadata review, not live identity verification, completed experimental evidence or an acceptance recommendation. Original outcomes remain unchanged.
