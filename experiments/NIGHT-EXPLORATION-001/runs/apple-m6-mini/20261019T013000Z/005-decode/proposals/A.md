# Proposal A — scalar only for count1

The bulk policy is active in18/28 primary PCs and is called from decoder_batch.
Hypothesis: using original zbtScoreLeafScore for count1 avoids bulk dispatch/loop
setup and improves materialized width60 forward count1 by>=2%, with frozen B
retained for all larger/empty ranges. Exact target is private policy, no leaf layout.
Predict largest gains for non-byte widths/count1; counts2+ should retain algorithm.
Risk: compiler may outline the whole policy or grow code, harming unchanged guards;
logical reverse/start handling must remain delegated to original scalar decoder.
Falsify if any primary block misses−2% or any qualified guard exceeds+1%.


Provenance: same Codex worker, sequential pass; not an independent agent.
Visible model family GPT-6; exact serving backend/model/token cost unknown.
Evidence seen: referee publication80177d1e; PROFILE.md, primary28PCs, actual
release policy call; prior EXP-007/008 losses and all176-cell plan. Other proposals
were authored sequentially; no independence is claimed.
