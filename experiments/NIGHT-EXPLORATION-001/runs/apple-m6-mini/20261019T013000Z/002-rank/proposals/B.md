# Pass B — member lookup path

Provenance: one Codex/GPT-6-family worker, exact serving model and measured token
cost unknown. Three sequential passes, NOT independent agents. Each pass uses the
same M6 profile, release assembly, A/A and shared target/guard definitions. M1
shorter-side proposal is prior context, not independent confirmation.

Public rank samples frequently resolve to memchr:48/107 at100K and205/389 at1M.
Hypothesis: reduce leaf-tag scanner call overhead for short scans. This targets
zbtScoreLeafFindMember, not ancestor accumulation. EXP-006 already has batch versus
single-query disagreements; this evidence does not explain them. A bounded scanner
change needs lengths/collision census and explicit single-query profiling before
implementation. Risks are bounded reads, first match, length decoding and code size.
Defer to LOOKUP-001; do not combine with rank arithmetic or reuse the old patch as a
new hypothesis. No predicted rank speedup from these sample ratios.
