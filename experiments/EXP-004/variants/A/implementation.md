# Variant A

Sequential implementation pass,not independent agent;backend/model/cost unknown.
Predicate: `if (bits + shift > 64)`. One condition only in zbtScoreLeafScore.
Proof assumes valid packed widths1..64 inside nonzero guard and shift0..7.
Conditional access unchanged; no shift64 when merge executes. Root preserved.
