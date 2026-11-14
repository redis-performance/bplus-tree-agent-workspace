# H8-A independent source review

PASS for source semantics and artifact identity; ARM static admission remains pending. The reviewer did not author A or its tests. The patch reconstructs source `e63caad0a6f81066a67ff964333cf0391c4a2ba71b592ce335bedefbd289f7f0` from the frozen baseline, and all71 artifact checksums match.

The change is confined to interpreting a candidate record inside the existing leaf helper. Ordinary headers0–253 directly produce their original length and payload pointer. Remaining records retain full external-hash rejection before the unchanged generic decoder. Header254 still uses the original unaligned length decode; header255 retains pointer assertion and external length handling. Equality bounds, memchr traversal, optional output writes, all generic decoder callers, layout, allocation and mutation/index paths are unchanged. No query-length shortcut or source assumption selects a fixture-specific path.

Required native/sanitizer, fixtures and supplied output oracles pass. Focused baseline/candidate oracles cover all header/representation boundaries, physical reversal, output modes, guard ends, external short/empty and mismatching-null rejection, plus an independent mutation model. These are correctness observations, not performance or broad portability certification.

This is the smallest H8 source scope and the preregistered maintenance preference among candidates that satisfy every gate. It must still demonstrate one ordinary classifier, unchanged frames and decoder boundaries in the exact ARM native/target ELFs. Extra external-path classification remains a binding performance guard. Source selection remains NONE.
