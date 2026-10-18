# Variant B

Sequential coordinator implementation pass B; not independent agent. Same frozen base.
Separate noinline specialized/generic helpers; public function dispatches.
Only iterator dispatch changed; decoder/state representation unchanged. End-of-leaf and
optional-output/reverse behavior require existing tests. Tree memory unchanged by design.
Exact backend/model/cost unknown. Patch preserved regardless of outcome.
