# Implementation B

Sequential implementation pass by one native Codex worker; no independent implementer. Exact model variant and measured token cost unknown. Starts from unchanged 8fab511e source.

Three successive OR-shifts fold every byte into its low bit, then extract and shift the exact zero-byte indicators. Only zbtIndexTableFind uses the new helper and drops its redundant candidate-byte check. General tag-mask users, layout, ownership and API are unchanged.
