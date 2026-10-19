# Variant B

Sequential implementation by the same native Codex worker. No independent implementer; exact model variant and token cost unknown.

Empty-range return first, then a count==1 scalar branch with bulk in the alternate branch. All count2+ source algorithms remain the frozen EXP-007 B algorithm. Only exact scalar helper outputs are materialized for count1. No root source or public API changes.
