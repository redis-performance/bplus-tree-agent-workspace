# Implementation C

Sequential implementation pass by one native Codex worker; no independent implementer. Exact model variant and measured token cost unknown. Starts from unchanged 8fab511e source.

Compiler vector extension compares eight bytes in parallel; memcpy preserves numeric byte order, with scalar carry-free fallback for other compilers. Only zbtIndexTableFind uses the new helper and drops its redundant candidate-byte check. General tag-mask users, layout, ownership and API are unchanged.
