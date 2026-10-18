# Actual equal-neighbor rejection branches

Both fixed baseline captures pass. The earlier finite-ties fixture executes neither
lexical neighbor comparison in zbtScoreUpdateInPlace: both true and false counts are
zero. The new neighbor fixture executes each comparison once and rejects both times.
This explains the original fault survival and its later detection with stronger
coverage. UpdateScore calls are 260 and 262 respectively.

These are whole-oracle execution counts, not timing profiles. Source snippets are
mapped using LLVM file IDs, and raw exports plus checksums remain in the manifest.
This extends COUNTERS-010; it does not add a diagnostic count or establish speed.
