# Additive external-buffer and natural narrowing reachability

Two fixed serial whole-oracle captures after semantic validation and fresh confirmation:
external-extension control seed67511 mode2; narrowing-extension/attempt-002 control seed68501.
Exact frozen source/test/support, -O1/debug LLVM mapping;120schildren/240swhole budget.
No simultaneous build/test/capture work. Raw profiles/exports under scratch, public
mapped branch/function summaries with hashes. Existing COUNTERS-009 files untouched.

Require full original PASS and geometry assertions. External capture must call
zbtDefragExternalMember and both accept/decline branches; narrowing capture must call
zbtScoreRenumberLeaves and zbtIndexRebuild, observing actual source-wide→new-narrow and
nonzero scan continuation. Counts include setup and all oracle work; no hotness or speed
claim. Same diagnostic scope/count29; preserve failures and do not weaken predicates.
