# Sequential proposal pass C — cached packed-score iterator state

Participant: coordinator pass C, not an independent agent. Backend/model/cost unknown.
Shared context same source/profile/A/A/history. Iterator profile contains packed-score
extraction and state-advance sites. Hypothesis: caching leaf score bits/base/physical
position in iterator state avoids per-entry decoding setup enough to gain>=2%.
Target iterator struct and seek/next initialization; must preserve every seek mode,
reverse physical encoding, exact bits/signed zero and mutation invalidation.
Prediction most gain in narrow scores; byte/accounting unchanged for tree but iterator
stack footprint increases. Portability and ABI/maintainability risk greater than A;
no specific instruction-cycle evidence separates decode cost from dispatch cost.
Falsification: no gain or any state/score discrepancy. Recommend no implementation now:
new state and all initialization paths need broader fixture/profile evidence first.
