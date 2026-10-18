# Adversarial review — sequential coordinator only

Semantics: specialization condition requires non-NULL score, no member/length outputs
and forward direction. Leaf NULL returns0; ordinary advance and end-of-leaf position
match original; physical reversed encoding handled by unchanged score decoder. Generic
function is source-identical apart from name/linkage. No persistent memory/state added.
Portability: existing compiler attributes already used by local toolchain; no architecture
specific data operation. GCC/other architecture confirmation absent. No new shift/UB.
Tests: all original checks plus every iterator output mask/direction and finite-score/
range/ownership suite pass both builds. Failure controls from BOUNDARY-011 are separately
retained; candidate tests not weakened. Timing referee/source pins identical across arms.
Measurement: fixed72 discovery and24 held-out-seed rows, no filtering/optional stopping.
B/C intervals overlap; C selected using declared smaller-patch rule, not asserted superior.
Sampling descriptive only; codegen supports reduced generic register-save work. Clocks,
effective QoS and within-window residency unknown. Single machine scope.
Maintainability/performance risk: duplicated specialized advancement must stay aligned
with generic path; added dispatch may hurt reverse/full-output paths. No guard evidence
there. This alone prevents ACCEPT. Independent confirmation/reviewer and source commits
also absent. Final PARK; no merge/main mutation. Reviewer startup failed, this is not an
independent review or a second backend. Unknown model/cost retained.
