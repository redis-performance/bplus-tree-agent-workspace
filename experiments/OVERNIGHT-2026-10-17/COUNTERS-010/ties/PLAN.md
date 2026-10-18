# Tie rejection coverage extension

Two additional fixed serial whole-oracle captures, baseline finite-ties seed72503 and
baseline tie-neighbors seed73501. Use frozen source/oracle snapshots and the original
COUNTERS-010 O1/debug Clang coverage procedure,120schildren, no overlap with confirmation.
The purpose is to distinguish actual equal-neighbor rejection from merely generating
equal final scores. Require PASS and map both lower/upper zbtScoreUpdateInPlace lexical
comparison branch outcomes. Report whether each branch rejects; do not assume previous
finite-only recipe reaches it. Preserve raw maps/checksums. No time/hotness/speed claim;
no additional diagnostic count, sourceNONE and existingPARK unchanged.
