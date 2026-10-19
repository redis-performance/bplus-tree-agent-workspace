# Common evidence packet: possible distinct ARM fold-predicate hypothesis

No hypothesis is selected and no candidate is implemented by this packet. The exact
prior NEON population017 is **REJECT, source NONE** and stays rejected. This packet
supports independent proposals, including NONE, only if root assigns that process
after reviewing fresh020 controls. Nothing here authorizes another experiment.

## Fixed source and prior failure

Target remains standalone src/zset_btree.c/.h, corrected adapter baseline
13e459ff8800be3f02b6b45c87dd7b0c39453fa9, baseline timing binary869425ed06643058e561df05177d1b85c42c9f662c5a80654c25caca02349055.
Tree source d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2,
header496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83.
Compiler Clang18.1.3, native timing-O3, assertions/hashing/allocator unchanged, CPU2.
Original8fab failed controls and earlier populations remain separate final decisions.

017's independently authored16-byte NEON implementations were all correct under the
frozen145-command validation but much slower in all36 discovery blocks (144 rows):

| Implementation | 100K paired effect range | 1M paired effect range |
|---|---:|---:|
| A | +96.89% to +102.01% | +68.98% to +72.40% |
| B | +76.65% to +78.59% | +54.84% to +55.83% |
| C | +98.89% to +101.80% | +68.35% to +69.84% |

See immutable144ee7e0d, ../017-corrected-neon/RESULT.md, raw rows and seals. No primary
survivor exists and its held-out confirmation contract was never triggered. Maintenance
preference did not make B a winner. It is used for diagnosis because its simpler mask
loop exposes the shared generated fold overhead, not because a failed source is eligible.

## Static and sampled evidence

Read-only018 report3e085fdcf reconstructs exact generated assembly. Each complete16-byte
chunk rebuilds the tag==1 predicate using35 instructions:2 stack byte stores,1 halfword
reload,16 scalar bit extractions and16 vector transfers. Both physical directions have
this sequence. B forward zero-mask continuation is51 instructions/16bytes versus the
baseline's19/8bytes. A/C additionally generate forward population counting. Counts are
static, not cycle costs. Function layout, residual processing and decode registers also
changed, so the exact cause of the complete slowdown is unresolved.

019 matched profilecb708e4ec uses unchanged exact baseline/B timing binaries. Full-process
PMU capture with fail-closed timed-call-site post-filter (not physical timed-only PMU)
finds B's exact70 predicate addresses account for17.67%/16.87% of timed sampled period
at100K/1M,400/421 sampled events. Every seed exceeds15%; frozen material-support gates
pass. All17482 raw sample classifications retained:7629 timed,2129 verification,7654
other,70 incomplete. All slot samples are assignable;12 reports state lost0. All28
executions/52 command records and exact semantic/source/referee/binary checks pass.
Root independently reconstructed samples, raw-IP→ELF mapping, controls and all124seals.
Independent AMD audit45ecc704e reconstructs all classifications, exact addresses, controls and thresholds and agrees; consult the latest root review.

The ~17% sampled share **does not establish enough recoverable work to beat baseline**.
B must overcome a55–79% slowdown before satisfying a2% improvement gate. Removing a
sampled region is not equivalent to recovering that fraction of elapsed time; dependencies,
normalization, transfer cost, register pressure and other changed code remain. There is
no measured replacement and no full causal attribution. NONE is a valid outcome if no
falsifiable hypothesis explains why it could pass against the unchanged baseline.

Detailed evidence: ../018-neon-codegen-diagnosis/{README.md,analysis.json,analyze.py};
../019-neon-matched-profile/{PLAN.md,plan-freeze.json,RESULT.md,profiles/,analysis/}.
The exact source-linked assembly, predicate IP list and per-capture counts are retained.
No timings are pooled across hosts/sources or carried from another adapter identity.

## Fresh precision and subsequent requirements

020 fresh baseline-only controls are preregistered at7cdb019e1:48 serialCPU2 processes,
100K/1M,16bytes,5M requestedops,seeds701/702/703 twice,sixsamebinaryABBA,300s cap,all6
within±1% and every window≥10ms. No retry, discardedblock or count/duration changes.
Fresh020 results are now complete: both sizes qualify allsix blocks.100K effects +0.752294%, +0.189216%, -0.589458%, -0.223440%, +0.299663%, +0.178333%; minimum417.860ms.1M effects -0.662373%, -0.145239%, +0.715132%, -0.118031%, -0.013566%, +0.254002%; minimum531.751ms. See ../020-fold-predicate-aa/{RESULT.md,aa-audit.json,aa.json,evidence-sha256.json}. No retry or partial-block exclusion occurred; root independent audit is pending.

Any root-selected new hypothesis requires actual three independent proposals and chair,
then three isolated implementations, preserved losses, exact source/referee/fixture/
compiler/allocator identity and serial frozen discovery. It must beat unchanged8694,
not merely improve rejectedB. Correctness includes folded0+1 tags, all physical matches
in ascending order, reversal mapping, partial chunks and bounded loads, binary members,
exact finite score/signedzero, resize/generation/leaf-ID semantics and all existing tests.
Architecture guard/portable fallback, qualified performance guards, independent fresh
confirmation, matched profile and adversarial review remain mandatory for acceptance.
No new experiment after07:15UTC; fleet release08:00UTC. Unknown model/cost stays unknown.
