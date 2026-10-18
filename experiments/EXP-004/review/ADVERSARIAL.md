# Sequential adversarial review — no acceptance

Reviewer is coordinator in separate pass,not independent agent. Independent agent
failed startup before execution;exact backend/model/cost unknown. No invented reviewers.

Semantics:all three predicates equivalent for internal width1..64,bitoffset0..7;sum<=71
cannot overflow unsigned int. Merge condition implies shift>0,so64-shift is1..63 and
shift64 UB is avoided. Width0 outer guard retained. Ninth-byte access remains conditional,
not speculatively read. Physical order/endian/mask/finite IEEE values unaffected. Packed
oracle and two sensitivity faults support correctness;no tree layout or owned data edit.
Public API ordering/ownership covered by original and mixed mutation tests. NaN support
not assumed. Portability proof applies to supported unsigned-width hosts;performance
limited to M1. Width invariant is internal to existing construction,not a new assumption
about arbitrary malformed leaves supplied by users.

Measurement:baseline profile/codegen and structural census preceded proposals. Three
separate sequential proposals/chair;three isolated source snapshots,shared exact referee.
Current AA-007 gates supersede prior qualification;all504screen/216fresh rows retained.
A preference passes currently qualified controls and tested fresh0/4/7;B/C not eligible
from uncertainty. Mask6 possible slowdown cannot be waved away. AA-008 fails joint
long-duration qualification;comparison skipped exactly per plan. Diagnostic caller
change cannot cure original guard or authorize candidate acceptance. DIAG-011 two-seed
criterion fails and premise is partly invalid:compiler already unswitches mask6 tests.
Its only valid interpretation is descriptive altered-caller evidence with register/layout
confounds. Do not rerun the same failed schedules or claim branch-predictor attribution.

Profiles:20matched captures across EXP-004 and DIAG-011 plus4known-function calibrations
pass. Conditional branch removal visible,not a precise cost attribution. Instrumented
wall times excluded. Timer cadence/aliasing/placement/frequency remain unknown. Some
boundary-runtime samples retained. Static whole-function branch counts are not loop
execution counts. No normalized GHz/cycle claims. MCP checker drop_number noted.

Maintainability:one-condition source change is small,alllosing patches preserved. No
code accepted until independent confirmation/review,broader score-consuming operation
performance guards,and committed provenance. Original3referee/source baselines and all
prior evidence retained;no git retry,publishing,permission/runtime changes. Verdict PARK.
