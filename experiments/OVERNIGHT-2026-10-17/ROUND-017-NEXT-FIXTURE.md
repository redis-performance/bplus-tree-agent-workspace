# Next distinct fixture: promotion with smaller and all-miss batches

Preparation only. Round17 now executes the earlier batch recipe, including a corrected
ID1/2 lane expression and a detected stale-table-cache fault. The transition batch has
16lanes and mixed hit mask0x7777. Counts0..16 run during active migration, but this does
not prove promotion inside each smaller count or an all-miss call.

Possible next recipe: reach the natural mixed-width state using public construction and
read lookups, inspect remaining uncopied leaves read-only, and clone a state just before
promotion. Run a fixed preregistered set of counts1/2/3/7/15/16 and all-hit/all-miss/mixed
layouts on independent clones. Require actual transition inside each intended batch;
account for the final completion step after the last leaf copy. Advance only via public
lookups, never mutate private cursor/generation/IDs. Preserve exact current-score model
and external ownership, and do not mistake active-entry state for completed transition.

Miss score slots remain unspecified; only outside-count canaries and hit results are
constrained. All-miss lookups still advance migration. Save independent expected masks,
exact bits and clone ownership checks. Preserve any unachieved transition preconditions
as fixture failures rather than loosening them. Inspect lifetime after old-table release;
whole-process counters can establish branch reachability but not time or speed.

This is untested, not preregistered. Do not repeat failed timing methods unchanged or
replace the original performance guard. Main source stays baseline for morning review.
The final worker still owes MORNING-REPORT.md by07:00UTC /08:00Europe/Lisbon.
