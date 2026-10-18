# Sequential proposal A — outline member decoding

Coordinator pass A,not independent agent;backend/model/cost unknown. Shared baseline:
HARNESS-004 source/referee,AA-00610 qualified modes,PROFILE-003 and EXP-002 expanded
profiles/codegen. Baseline generic IteratorNext saves six register pairs even without
member outputs. EXP-002 special-path entry guards regress fallback modes.

Hypothesis: move member record decoding only into a noinline helper called under the
EXISTING ele||len test,so score/no-output paths use fewer registers without a new
public entry guard. Reduce primary forward score-only wall time>=2% with no>1% guard
or memory regression. Only IteratorNext/local helpers;score/state decoder untouched.
Correctness risks optional outputs,returned member ownership,length,copying packed
records. Guard risk helper call overhead on member-output paths;no tradeoff authorised.
Falsify if no prologue reduction,primary fails,or qualified guards regress. Prior
source/profile evidence supports register-pressure investigation,not a predicted win.
