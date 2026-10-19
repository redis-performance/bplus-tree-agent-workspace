# AMD packed-score move census

Diagnostic preparation only, no hypothesis selected. Instrument frozen8fab511e target in an isolated snapshot; root remains unchanged. Reset counters immediately before existing timing loop and disable/dump immediately after. Never report instrumented elapsed time as baseline performance. Count insert/delete packed shifts by bit width and moved fields, per-score writes, encoding calls/items and full leaf builds.

Cases: update100K101717ops,1M52593ops,100K3Mops; insert/delete100K/1M;seed1,16byte keys. Separate disabled reset control must report zero counters and matching semantic checksum/memory. Existing frozen packed_move_oracle and packed_decode_oracle available for later candidates. Public profile evidence from previous round shows insertion/rebuild, including score-field writing, is material; byte-aligned move frequency is currently UNKNOWN.
