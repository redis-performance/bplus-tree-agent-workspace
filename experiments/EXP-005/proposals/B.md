# Cache iterator packed metadata

Sequential coordinator pass, not an independent agent. Same frozen HARNESS-004 source, EXP-004 baseline profiles/codegen, prior experiment history. Backend/model/cost unknown.

The same profile localizes score work; repeated loads of width/base/shift may be reusable within leaf. Hypothesis: metadata cache lowers per-item loads. Requires public iterator structure/layout changes, lifetime care across leaf transitions and output masks. Existing dispatch/outlining failures warn of fallback regressions. Unqualified guards make this broader change risky; exact target iterator struct/start/next. Reject if register pressure increases or any semantic/memory guard fails.
