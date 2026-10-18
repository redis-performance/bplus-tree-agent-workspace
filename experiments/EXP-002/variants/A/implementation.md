# Variant A

Sequential coordinator implementation pass A; not independent agent. Same frozen base.
Inline early-return specialized body; generic body retained verbatim after guard.
Only iterator dispatch changed; decoder/state representation unchanged. End-of-leaf and
optional-output/reverse behavior require existing tests. Tree memory unchanged by design.
Exact backend/model/cost unknown. Patch preserved regardless of outcome.
