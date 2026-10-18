# DIAG-002 descriptive association results

All 24 fixed lookup windows retained, no exclusions. Primary wall-time
correlation r=-0.0651; CV(Y/X)/CV(Y)=1.0019. Preregistered criterion
(r>=0.70 AND ratio<=0.50): **not met**.
Invariants stable: True; minimum region 39.961ms.
Process-mean correlation -0.2464; see summary.json
for all within-process ranges and correlations. Four repeated windows/process are
clustered observations, not independent random samples. No p-value or causal claim.

X is mean before/after dependent-add wall duration per add; Y is lookup wall duration
per operation. Y/X is a diagnostic ratio, never a replacement for wall-time gates.
No measured GHz, core type or CPU-cycle count; instruction latency and runtime
placement not independently established. Brackets do not measure the lookup's clock.
