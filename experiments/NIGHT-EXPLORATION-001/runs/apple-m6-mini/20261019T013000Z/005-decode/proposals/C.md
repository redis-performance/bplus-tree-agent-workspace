# Proposal C — custom one-score bit reader

Use an explicit count1 delta read, bounds/crossing predicates and ordered-to-double
conversion instead of the scalar helper, retaining B for other counts. Expected
gain comes from fewer generic range operations. Risk: duplicates mature score
logic, including bits0/64, reversed mapping, high shifts and binary signed zero.
Count1 fixtures happen to use delta0; specializing that value would be invalid.
Must preserve arbitrary partial count1 requests; branch-count reduction alone is
not evidence. Falsify on exact-bit oracle or primary/guard gate failure.


Provenance: same Codex worker, sequential pass; not an independent agent.
Visible model family GPT-6; exact serving backend/model/token cost unknown.
Evidence seen: referee publication80177d1e; PROFILE.md, primary28PCs, actual
release policy call; prior EXP-007/008 losses and all176-cell plan. Other proposals
were authored sequentially; no independence is claimed.
