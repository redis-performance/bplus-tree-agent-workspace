# Overnight continuation active

Authorized through **2026-11-14 07:24:14 UTC**, with final 30 minutes reserved for review, reporting and verified cleanup. See OVERNIGHT.md. No source is accepted.

- H1: all three helper variants rejected after 216 native comparisons and independent audit. The best hit gain loses score, miss and update guards.
- H2: all three metadata implementations pass correctness. Native discovery gives B −4.80% and C −5.66% hit time, with every six-case guard passing and unchanged memory. A fails memory (+1.23%) and is excluded from further timing. B/C LTO and Intel comparisons are running. Extra iterator/rank/churn guards are being corrected after independent review, before their freeze and qualification.
- H3: three isolated short-inline equality implementations are correctness-ready; code-generation screening and fleet measurements follow.
- Controls: renewed ARM native 18/18 blocks pass; separate ARM long-window/controller-pinned LTO cohort 18/18 passes. Intel native and LTO each pass 18/18 (144 rows total). The original short-window and noisy-LTO failures remain PARK and unchanged.
- Intel baseline profiles: the invalid over-limit launch is preserved. All three corrected native and all three LTO captures are complete. Independent TMA audit passes both baselines under the registered CPU-wide scope limits; candidate profiles remain pending. No invalid profile is used as evidence.

ARM and Intel hold independent bounded leases with cleanup. Intel cleanup restores the saved Parca service, SMT sibling and coordinator states. Busy hosts are untouched. Upstream remains ee8e7f701, rechecked around 02:04 UTC; every comparison keeps that pin. Earlier experiments remain sealed. Public results are standalone evidence, not server-command recovery. Continue supported options through the six-hour window.
