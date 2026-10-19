# Implementation A

Sequential implementation pass by one native Codex worker; no independent implementer. Exact model variant and measured token cost unknown. Starts from unchanged 8fab511e source.

Carry-free byte addition constructs an exact mask; low seven bits prevent carries across bytes. Only zbtIndexTableFind uses the new helper and drops its redundant candidate-byte check. General tag-mask users, layout, ownership and API are unchanged.
