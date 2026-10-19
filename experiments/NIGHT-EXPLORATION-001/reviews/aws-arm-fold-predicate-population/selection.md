# ARM fold-predicate proposal chair — NONE

Decision at 2026-10-19T05:49:38.040682+00:00: **NONE before implementation**. Three actual independent
proposal passes used common packetc3323969a and qualified fresh020 controls. The chair
is a fourth participant, not a fourth proposer. No implementation population or candidate
timing is authorized. This does not add a measured population;017 remains REJECT.

| Proposal | Evidence and useful-gain assessment | Scope, risk and portability | Chair disposition |
|---|---|---|---|
| ARM | Verified repeated predicate lowering and material samples; proposes ≤20-instruction ordinary path before timing. Useful gain against baseline remains unmeasured. | Explicit loop dispatch; duplicated code and register/layout risk; bounded NEON path with portable tail/fallback. | Retain as dissent/deferred hypothesis; do not implement now. |
| Intel | Identifies missing baseline-relative recovery evidence; warns static subtraction omits match/residual/decode costs. | NONE adds no code or portability risk; preserves precise future falsification conditions. | Supports selected NONE. |
| AMD | Quantifies required recovery from rejected B and distinguishes sampled materiality from removable elapsed time. | NONE adds no code; separately deferred bitwise-mask mechanism is not combined with ARM dispatch. | Supports selected NONE. |

Ranked choices: (1) NONE, (2) deferred ARM invariant dispatch subject to new evidence,
(3) deferred explicit fold-mask alternative. Ranking is a chair judgment, not a measured
performance ordering or an assertion that one author's source is better. Exact proposals
are copied verbatim with hashes and provenance in participants.json. All authors disclose
prior017 participation; separate authorship is real, blinding is not claimed. Serving
models and measured token/currency costs are unknown.

## Why the material profile does not select an implementation

Baseline controls qualify both primary sizes, and root/AMD independently reconstruct
all17,482 profile samples. The70 predicate addresses receive17.670%/16.866% of B's
filtered timed sampled period. This establishes a concrete diagnosis, not its removable
cost. Rejected B is+78.161%/+55.342% slower by primary median. A replacement needs roughly
44.99%/36.91% reduction from B's elapsed to meet−2% against unchanged baseline8694.
Illustrative proportional subtraction of the predicate share leaves losses; this is
neither a causal bound nor a performance prediction. Compiler dependencies can make
interactions nonlinear, but the current evidence does not quantify a favorable recovery.

ARM's dissent is substantive: source-level invariant dispatch might avoid both the35
reconstruction instructions and normalization, and it proposes a strict static stop gate.
The chair retains that argument. However, the static zero-mask path omits matching chunks,
tails and downstream decoding; instruction count does not establish end-to-end gain.
ARM's additional samples at branch successors likewise do not prove branch cost or
attribute it to the fold predicate. We do not assume that unexplained time disappears.
This is an evidence-quality decision, not a claim that such a rewrite cannot work.

No branches, assertions, allocator rules, compiler flags or fixtures are changed. No
retry of017, no performance comparison against rejected B alone, and no guard relaxation.
Fresh020 controls and all losing patches remain useful retained evidence. A distinct
baseline-focused diagnosis can proceed separately without reopening this decision.

## Evidence

- Common packetc3323969a, original rejection144ee7e0d, static diagnosis3e085fdcf.
- Matched profilecb708e4ec; independent AMD45ecc704e and root
  [raw profile audit](../aws-arm-neon-profile-independent-audit.json).
- Fresh020 controls and [root48-row reconstruction](../aws-arm-fold-predicate-aa-audit.json).
- [ARM proposal](proposal-arm.md), [Intel proposal](proposal-intel.md),
  [AMD proposal](proposal-amd.md), [actual participants](participants.json).

AWS measured counts remain8:0 accepted /5 rejected /3 parked. Source adoption NONE.
