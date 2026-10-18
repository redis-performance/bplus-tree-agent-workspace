# Variant C

Sequential coordinator implementation pass C; not independent agent. Same frozen base.
Inline specialized helper and noinline generic fallback; public dispatch.
Only iterator dispatch changed; decoder/state representation unchanged. End-of-leaf and
optional-output/reverse behavior require existing tests. Tree memory unchanged by design.
Exact backend/model/cost unknown. Patch preserved regardless of outcome.
