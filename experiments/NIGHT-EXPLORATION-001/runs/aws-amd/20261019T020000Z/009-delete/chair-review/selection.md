# Chair decision: NONE; park deletion offset adjustment

Actual chair `/root`, native agent, independent of the three proposal authors.
Exact serving models and measured token/USD costs remain unknown. The common baseline
packet is AMD `a04b9f69d`; exact source8fab511e and unchanged compiler/referee. Three
separately authored proposals are copied byte-for-byte here with hashes and revisions.
Participants did not read one another's proposals. AMD submitted while A/A was running;
Intel and ARM received the same subsequently completed control update before submission.
This is independent authorship, not a blind study; all knew the identified loop.

| Chair rank | Proposal | Evidence and useful gain | Risk/scope/portability | Current decision |
|---|---|---|---|---|
| 1 equal | Intel | Distinct loop and census support a falsifiable mechanism; noisy1M blocks preclude qualification | Narrow portable selected-value assignment; bounded-tail, unsigned and extra-store risks explicit | NONE |
| 1 equal | ARM | Same supported mechanism, no precise sample-derived headroom claim | Narrow portable zero-or-delta assignment; aliases/ownership/extra stores covered | NONE |
| 1 equal | AMD | Same mechanism; conditional recommendation explicitly requires qualified controls | Narrow portable selected-value assignment; unchanged-value stores may erase gain | Conditional requirement failed; NONE |

The common hypothesis is an unconditional value-preserving offset assignment enabling
packed stores, replacing the current vector compares plus scalar conditional stores.
It is distinct from prior rejected packed moves/builders. The1M loop attribution is
101/1844 samples (5.496%);100K has only7 loop samples. This is coarse attribution, not
a rigorous speed ceiling or proof of branch misprediction. No proposal has evidence
justifying a different primary, metric, retry or immediate implementation after failure.

Root independently reconstructed48 A/A rows /12 blocks from raw files.100K qualifies;
1M does not: effects+0.527,+0.520,+0.499,+4.682,+3.035,+1.087%. Windows exceed10ms,
serial boundaries and CPU2 match, and operation counts/checksums/owned memory agree.
The precision failure is therefore retained rather than hidden by a short-window label.
See [raw audit](../aws-amd-delete-aa-audit.json) and AMD controls revision9893c18a2.

**Select NONE.** Do not start the implementation population or candidate timing.
Preserve all proposals, profile/census and control evidence. The revisit condition is
a separately justified campaign with qualified controls, not a same-night retry or
operation-count adjustment. Three implementations are required after a winning
hypothesis is selected; selecting NONE intentionally stops before that step.
This is an unmeasured diagnosis/proposal decision, not an eighth measured population.
No source changes, adoption, performance claim or upstream action. AMD can independently
review the existing Intel scan follow-up while its own host remains idle.
