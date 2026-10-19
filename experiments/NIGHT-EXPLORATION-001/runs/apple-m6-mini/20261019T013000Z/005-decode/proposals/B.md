# Proposal B — inline the existing all-bulk policy

The release caller has a per-leaf policy branch-and-link. Force the existing policy
inline to remove call overhead at every count, without scalar decoding. Predict
count1 gain and unchanged bulk stores. Hypothesis is distinct from a scalar policy.
Risks: duplicates large bulk dispatch into callers, changes counts2+ code paths and
can increase instruction footprint. It is less bounded than the shared count1 lead.
Falsify on count1 miss or larger guard regressions; sample PCs do not prove call cost.


Provenance: same Codex worker, sequential pass; not an independent agent.
Visible model family GPT-6; exact serving backend/model/token cost unknown.
Evidence seen: referee publication80177d1e; PROFILE.md, primary28PCs, actual
release policy call; prior EXP-007/008 losses and all176-cell plan. Other proposals
were authored sequentially; no independence is claimed.
