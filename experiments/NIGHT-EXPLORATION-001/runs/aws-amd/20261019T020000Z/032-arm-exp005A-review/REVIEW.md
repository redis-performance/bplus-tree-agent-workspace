# Exact historical EXP005 A replication preparation review

No static execution blocker found in immutable a9b09cadc, execution freeze
328c21556bc285df97fedca7a212148be107c0c827793bb16a05b0505ce806b2.
This reviews the chair's bounded diagnostic replication, not its expected benefit.
My independent031 NONE recommendation remains unchanged and public. Root must grant
validation separately; no screen follows until complete correctness plus independent
codegen review and root's second grant. No runner access, compilation or measurement
was used in this review.

Verified all20 frozen inputs and ten exact13e source/referee hashes. A zero-fuzz patch
application in a temporary local directory independently reconstructs aa834a77… from
historical patchca14579… . Patch bytes match original EXP005 A exactly. The only source
change is the mask expression within the unchanged nonzero-width block; no additional
algorithm, implementation population, ownership/layout or iterator-state change occurs.

For every valid width1..64, right shift count64-width is63..0 and produces exactly
that many low set bits. Width64 therefore shifts by0. Width0 still bypasses the entire
expression; moving it outside that guard would be invalid, but the exact patch does
not do so. Unsigned arithmetic and UINT64_MAX preserve defined behavior. Cross-word
predicate/conditional ninth byte, little-endian conversion, physical reversal, base/
shift and exact finite score representation remain unchanged. Existing valid-input
assumptions do not extend to NaN or arbitrary corrupted width fields.

The four imported oracle hashes equal retained historical files. The570-command
manifest includes512 complete mode cells (control/A × native/sanitizer ×128 each),
12 full mutation/packed/signed-zero oracle runs, four original43-test runs and eight
negative fault runs. Independently reconstructed128-cell Cartesian products cover
16/320-byte members, four encodings, both directions and all eight masks, at129 members,
259 requested operations and seed7103. Full oracles cover independent bitstream width0..64,
valid shift combinations, exact signed zero/reversal, mutation/copies/seeks/exhaustion
and varied outputs. Four historical fault patch hashes match; each negative must exit
nonzero without timeout and emit its retained diagnostic, after successful compilation.
No test is weakened or replaced with implementation-mirroring checks.

Imported iterator_modes includes corrected13e microbench helpers but is used only for
small correctness fixtures. These runs do not qualify performance guards. Both timing
binaries build from isolated snapshots with identical relative paths, flags/assertions/
allocator/hash. The original actual013 binary330b39a9 and its source are read/hash-checked
only. Rebuilt control .text must equal actual013 bytes without normalization before
correctness can finish; mismatch stops rather than rebuilding actual013. Source/oracle/
protected-binary hashes are checked before/after. Separate native/sanitizer flags are
identical per source/mode. The positive test outputs are checked, not just exit codes.

Validation uses serialCPU2,600s whole cap/120s child cap and retains failures/partials.
The separate screen uses300s/30s and refuses phase start at/after07:15UTC. Root's existing
lease bounds still apply. Do not launch a late phase by treating preparation approval
as a standing grant. Partial/resource/semantic failure is inconclusive/NONE, not a full
measured primary rejection. No retries, source alternatives or repaired schedules.

The static gate correctly defines FOUR mask-generation instructions including the
MOV all-ones: MOV/CMP/LSL/CSINV. The necessary final AND is excluded symmetrically only
if unchanged, as is the independent score_shift load. Candidate feeding constants,
negations/moves and hoisted work must all count. It must have<=3 generation operations,
no added conditional branch and>=1 fewer instruction on the equivalent whole ordinary
nonzero path, including entry/exit/setup. Full actual/control/A and shared-caller
assembly must be reviewed; moved work, extra memory reads, branch/call substitutions,
width0/64/cross-word changes or unclear equivalence block the gate. This is currently
unexecuted, not a promise that the candidate compiler output satisfies it.

run-screen requires a PASS gate bound to execution freeze, validation result, all
three assembly hashes and actual/candidate binary hashes. It preserves unchanged
actual013 as outer A and exact candidate as middle B, sixABBA blocks per100K/1M,
seeds401–403 twice,50M visits and16 bytes. Independently reconstructed all48 schedule
entries, including reversed size order on odd blocks. Exact checksums, traversal and
warmup counts, CPU endpoints, per-block owned bytes and source/binary pre/post identities
are enforced. Every one of12 blocks needs<=−2% and>=10ms. Any failed primary ends the
replicationREJECT/NONE; a full pass can only be diagnosticPARK because qualified guards,
independent held-out confirmation, matched candidate profile and final adversarial
acceptance remain absent. Prior adverse length+score evidence remains explicit.

Recommendation: eligible for root's validation-only grant under this frozen plan.
No acceptance or source adoption. Actual reviewer/root/aws_amd, native inherited Codex;
exact serving model/tokens/cost unknown. See checks.json and check-freeze.py for local
hash/application/domain/schedule checks. No peer source variant was authored.
