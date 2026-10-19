# Exact historical EXP-005 A ARM replication — preparation only

Root chair4d36b2d0e selects conditional replication after three actual proposals;
Intel/AMD NONE dissent remains preserved. This is EXACT historical EXP-005 A,
patchca14579cbf4325816d5511697cb0bec5ab0e618ef661830acbc4bfe72a5cc88f,
not a new algorithm/implementation population. Original authorship was the recorded
sequential coordinator, exact model/cost unknown. No B/C or source alternative.
Target13e459ff8800be3f02b6b45c87dd7b0c39453fa9 yields candidate source
 aa834a771284bed367400a8f54538cd366b2791666d9711a8e160aaa93f62fc4.
The source changes only the nonzero-width mask expression. Width0 bypass remains;
width1..64 maps to shifts63..0. Cross-word read/predicate, endian conversion, physical
reversal, base/shift, finite score bits and all state/layout remain unchanged.

No launch follows preparation. Root and independent AMD review must approve immutable
inputs and grant validation explicitly. Screen requires a separate successful
code-generation review and explicit root grant. No phase may start at/after07:15UTC;
lease release08UTC. No main adoption. Broad guards/fresh confirmation/matched profile
cannot all fit in the remaining window, so primary success can only mean diagnostic
PARK. No follow-up phase or acceptance is implied; every prior decision stays final.

## Exact sources, referee and control

New isolated root scratch/arm-exp005A-replication-13e459ff8 holds control/A/fault
snapshots reconstructed from an exact13e archive. Existing actual013 baseline at
scratch/adapter-worktree-13e459ff8 remains unchanged, binary
330b39a991573985c421194cfe83f21b44797e1a83372f623120672eb910b3bc.
Control/A timing binaries use identical relative frontend/output paths and exact
Makefile native flags: Clang18.1.3, C11,-g,-Wall,-Wextra,-fno-omit-frame-pointer,-O3,
unchanged includes/allocator/assertions/hash. Both build/adapter-requalification/
btree-bench paths are separate snapshot outputs. No REDIS_DEBUG/TEST/NDEBUG timing
flag. Test-only debug/sanitizer flags are identical per source/mode.

Rebuilt control .text MUST be byte-identical to actual013 .text, without relocations
or normalization. Mismatch stopsNONE; do not rebuild or replace actual013 to make it
match. Protected existing binaries and actual source/referee hashes are checked before
and after validation; actual/control/A timing identities precede any screen. Original
024 fixed48-row A/A applies only to unchanged actual013 and its exact public50M fixture.
No new timing referee is used. HARNESS-004 iterator_modes.c is imported unchanged for
small correctness fixtures only; its included microbench.c is the exact corrected13e
file, with the original helper interfaces inspected. No correctness elapsed output
counts toward performance or control qualification.

## Validation: one owned serialCPU2 job,600s hard cap

validation-commands.json fixes570 ordered commands, allargv/cwd before data. Driver
executes that manifest directly, records every start/end/exit/stdout/stderr and retains
partial timeout streams. Each child<=120s and remaining whole-phase budget. No retry,
repair, narrowing or extension. Any process/semantic failure stops this attemptNONE.
No scientific timing occurs in this phase.

- Two source snapshots × native/ASan+UBSan: original43 tests unchanged, four runs.
- Identical128 iterator-mode cells/source/build,512 total: n129,ops259=>387visits,
 16/320-byte binary members, integer/fraction/wide/zero encoding, both directions,
  all8 output masks, seed7103. All original pre/post full member/order/score/sentinel/
  iterator-copy/checksum/owned-memory assertions remain. Exact output contract checked.
- Unchanged iterator_mutation_oracle.c, packed_decode_oracle.c and
  zero_physical_oracle.c in all four source/build cells,12 complete runs. Bitstream
  oracle covers widths0..64, valid width+shift combinations, ten leaf counts1..96,
  two seeds, both physical directions and poisoned padding; independent scalar writer/
  reader and exact finite bits. Mutation preserves varied outputs, iterator copies,
  reverse flags and reinit-after-edit semantics. Signed-zero oracle retains real
  reverse/update/query and settled-rehash memory checks. No live iterator after edit
  or active-resize timing coverage is claimed.
- Four exact historical BOUNDARY-013/014 fault patches applied to separate baseline
  snapshots: missing ninth byte, width64 mask, last-zero-base and equal-zero-update.
  Each native and sanitizer build must fail with the retained oracle diagnostic,
  eight detections. Timeout/nonzero without expected diagnostic is not detection.
  Faults never modify control/A or any oracle. Provenance/hashes are in expected.json.
- Full source-linked disassembly and raw .text dumps from actual013, rebuiltcontrol
  and candidateA, after correctness. Before/after immutable snapshot/binary checks.

No new fault or oracle strength is invented; these are repetitions of retained
negative controls on the current native build. Four patch applications and all oracle
hashes were checked locally without compilation or executing a workload.

## Static gate: explicit independent review before screen

Validation completion records `correctness_complete_static_gate_pending`, not PASS
for performance. Root/AMD inspect full actual/control/A disassembly and publish a
separate codegen-gate.json bound to freeze, validation result, all three assembly hashes
and exact timing binaries. Gate requires a complete source/operand dependency account.

Baseline ordinary nonzero-width mask construction is FOUR instructions at actual
IteratorNext+0x100/+0x104/+0x108/+0x10c: MOV-all-ones, CMP-width64, variableLSL, CSINV.
MOV constant materialization IS counted. FinalAND+0x114 is excluded on BOTH sides
only because its necessary work remains identical; interleaved independent score_shift
load+0x110 is excluded. Candidate must use<=3 mask construction instructions, counting
ALL feeding constants, negations, moves and setup even if hoisted outside the nearby
source range. No added conditional branch. The equivalent whole ordinary nonzero
path, including entry/exit/setup, must also lose>=1 instruction; do not move work out
of the counted range or outsource it to an added call. Width0/64 and cross-word paths
must retain defined behavior and existing conditional access.

Full source-linked code for zbtreeIteratorNext and shared decoder callers
zbtreeScore, zbtreeRank, zbtreeFindForAdd and zbtIndexScanSlot must be inspected; the
full binary assembly additionally retains every inlined/update path. Record exact
function/range/words, additions/removals, unchanged load/guard semantics and any
compiler layout/caller changes. No normalization of assertion-address differences.
Any unexpected widening/extra memory read/new branch or unclear equivalence is a
blocker or requires explicit PARK, not silent ignored code. Static counts are not
cycles/speed proof. If the gate fails, selectNONE and never start the screen.

## Conditional primary screen: separate ownedCPU2 job,300s

Only root's explicit post-validation/gate grant can start run-screen.py. Frozen
screen-schedule.json has48 processes: sixABBA blocks per100K/1M, fixed50M operations,
16-byte members, seeds401–403 twice, size order reversed on odd blocks. LabelA invokes
unchanged actual013 baseline; labelB invokes exact historical candidateA. No random
variant choice. Every child<=30s and remaining budget; no retries, substitutions or
count changes. Original numeric checksum/consumer and one warmup remain unchanged.

Require exact50M actual visits,500/50 traversals, expected integer checksum,
CPU2 endpoints, within-block exact tree-owned memory and source/referee/binary identity
before/after. Effect100*((candidate middle elapsed sum)/(control outer sum)-1).
Every one of12 blocks must be<=-2% with all windows>=10ms to survive. Any failed
primary yieldsREJECT/NONE for this native replication; no fresh-seed rescue. If a
semantic/identity/resource failure prevents a full schedule, preserve partial evidence
and selectNONE/inconclusive, not a measured full-gate result.

If all primary blocks pass, outcome is diagnosticPARK/sourceNONE. Missing mixed-output,
no-output, reverse, fraction/wide/zero, binary/long-length and all-original-operation
guards remain missing. Historical adverse length+score observations stay explicit.
Independent fresh confirmation, qualified performance/memory guards, matched profile
and adversarial acceptance review are not authorized and cannot be implied. Existing
historical timings or another host cannot fill those gates. Stop after this fixed
screen and publish every row/losing patch for independent raw review.

Actual preparation author/root/aws_arm; native Codex, exact model/tokens/cost unknown.
Imported algorithm/oracles keep original authorship. All source/evidence/permissions
and original coordinator state remain unchanged; only the owned bounded helper may
run authorized phases.
