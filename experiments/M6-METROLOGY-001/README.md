# M6-METROLOGY-001 — offline diagnosis of failed lookup controls

Status: CLOSED offline diagnostic, source NONE. [Final results](RESULTS.md) and
[three-reviewer agreement](review-agreement.json) retain all rows and prior PARK.
No corrective timing method is selected; native cause/accounting bounds remain unresolved.

Historical scope: Authorized by the user’s “continue exploring” request.
Owner: interactive M6 controller. This study reads completed EXP-009 evidence;
it acquires no native measurement lease and launches no benchmark/profile process.
The completed EXP-009 protocol, rows, thresholds and PARK decision stay frozen.

Question: can recorded wall/thread CPU clocks, ABBA positions, CPU endpoints and
warmup times distinguish observed descheduling from unresolved on-CPU variation?
One falsifiable diagnostic hypothesis: descheduling alone accounts for all three
failed 1M wall-clock controls. Recompute identical ABBA contrasts using thread CPU
clocks as a diagnostic, never as a replacement acceptance clock. A failed thread
contrast falsifies that sufficient explanation; a passing contrast does not prove it.

Three actual independent reviewers inspect the same retained rows through separate
lenses: clock attribution; schedule/seed/position effects; instrumentation validity
and alternative explanations. They must not read each other’s new reports. The
controller chairs the result after all reports arrive. This is a diagnostic review,
not a source proposal/implementation population or a new optimization count.

Before review: actual CPU-perf discovery/library_status/ask with machine, compiler,
source identity and failed-control context. Preserve exact call inputs, response
hashes, tool coverage and limits. No causal DVFS/cache/core-type claim from endpoints.

All 48 rows and all 12 blocks are retained. No exclusions, timing rerun, count/seed
retuning, thresholds relaxation or source/referee edits. Analyze both sizes and all
six blocks, report wall and thread effects plus clock residuals. Treat correlations
and post-hoc associations as descriptive. Do not pool another architecture’s data.

Deliverables: reproducible offline analysis; three independently authored reports;
chair decision with a concrete future diagnostic if evidence supports one; updated
shared status on main. Independent verification must reconstruct raw CSV inputs,
not merely trust prior summary output. Backend Codex/GPT-6 family; exact model,
token and currency costs unknown. No tree speedup or acceptance can result here.

Budget: one offline pass per reviewer plus bounded corrections for analysis errors;
no native workload and no measurement lease. Finish with explicit decision/limits.

## Historical intermediate reconstruction (9cb7a600f)

Root verifies all96 raw streams, all48 rows, all12 blocks and both old frozen seals
(69 input pins and297 timing pins). Thread diagnostics also qualify100K6/6 and1M3/6.
The same failed1M blocks have thread effects−1.401384%,+1.008640%,+2.542454%.
At this checkpoint three independent reviews were pending; see [analysis](analysis.json),
[reproducer](analyze.py) and [actual MCP consultation](cpu-perf/README.md).

![All original M6 ABBA contrasts on both clocks](wall-thread.png)

Clock caveat discovered during review: thread_start precedes wall_start and thread_end
follows wall_end. There is no measured wrapper/accounting-error bound. The initial
wording “falsifies” above is too strong for a causal descheduling conclusion: the
recorded contrast diagnostic fails, but precise off-CPU attribution is unestablished.
This correction preserves the original scope/history and changes no old timing gate.
