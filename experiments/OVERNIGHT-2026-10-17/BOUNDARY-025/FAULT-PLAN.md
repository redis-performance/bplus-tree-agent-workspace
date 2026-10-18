# Promotion-specific sensitivity controls

Sensitivity refinement before fault execution: gate last-hit omission and output
overrun on active-entry/completed-exit promotion, so earlier generic batches cannot
detect them before the new matrix. Treat result-mask corruption as an existing fault
family; only outside-count output writes are a new distinct type if detected.
