# C — Filter misses before leaf search / prefetch

Census shows only0.016–0.028 leaf calls per miss and1.007–1.014 per hit. Miss PCs
mostly map to hash/index code; two smaller miss profiles are insufficient. Stronger
filtering or prefetch might help some distributions but current logical counts/PCs
do not establish latency stalls or material avoidable false candidates. New metadata
would expand mutation/memory risks. No supported portable bounded prefetch trial.
Recommendation: NONE for this family pending distinct path/stall evidence.

Three sequential passes by one worker, not independent agents. Visible backend Codex/GPT-6 family; exact serving variant and measured token cost unknown. Same frozen profile/census/assembly and EXP-006 history.

