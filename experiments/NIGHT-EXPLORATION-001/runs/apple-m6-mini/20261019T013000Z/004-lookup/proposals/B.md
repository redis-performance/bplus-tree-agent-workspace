# B — Replace leaf memchr with inline tag scanner

Memchr PCs appear frequently on hits and scans consume about31bytes to first match.
A scalar/SWAR/unrolled replacement could remove library boundaries, but EXP-006
already explored this and showed single-lane losses. Current profiles do not expose
a new scanner mechanism that avoids that issue. Reusing unchanged C is a control.
Risks: endian handling, first match, bounded reads and extra register pressure.
Falsification requires public single-query dual primaries and all lookup guards.
Recommendation: do not repeat unchanged scanner family on this evidence.

Three sequential passes by one worker, not independent agents. Visible backend Codex/GPT-6 family; exact serving variant and measured token cost unknown. Same frozen profile/census/assembly and EXP-006 history.

