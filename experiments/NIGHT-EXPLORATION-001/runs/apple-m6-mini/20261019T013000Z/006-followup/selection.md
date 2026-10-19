# Chair decision — select B / M6-LOOKUP-CALLER-001

Chair: /root, not a fourth proposal. Actual independent proposers are
/root/followup_proposal_a, /root/followup_proposal_b and /root/followup_proposal_c.
All three had the same frozen source/input hashes and did not read each other.
Exact serving variants and per-agent token/monetary costs remain unknown.

Rank B first: distinct generated-code mechanism with baseline profile support. Root
verified the separate144-byte leaf frame,176-byte caller frame, and two read-only
call sites setting x5=NULL before calling the generic leaf helper. Exposing that
call boundary can let the compiler specialize optional outputs/register lifetimes.
No speed benefit is assumed; inlining may instead increase spills/code size.

Rank A second and C third: both correctly choose NONE for extending old size-only
leads. A records a genuinely new raw-delta transformation but lacks eligibility/cost
evidence. C gives strong adversarial reasons against arbitrary tree-size gates and
relabeling prior wins. Those objections are accepted; no size threshold, repacking,
new decoder or scanner is selected. The frame mechanism is a new alternative that
B established from the shared assembly, so selection is evidence-weighted rather
than a majority vote. All prior decisions stay closed.

Select ONE hypothesis: compiler exposure of the generic leaf-search call boundary
will reduce optional-output and frame bookkeeping enough to improve successful
public score lookup at BOTH100K and1M by>=2%, retaining all guards/memory semantics.
Keep memchr/memcmp, hashing, traversal, packed layouts and decoder source unchanged.
No physical-decoder B reuse, prefetch, layout change or population mixing.

The proposal's96-cell feasibility estimate is refined BEFORE implementations or
measurements to101 distinct guards/primaries: standard40, independent lookup15,
additional lengths15, batches6, update patterns25. Different referees/query orders
are not silently deduplicated. At100ms/window, full six-block ABBA is242.4timed
seconds; three dual-primary screens add14.4s, total256.8s below300s timed cap.
Fixture/setup overhead has a separate900s wall phase cap. If this cannot fit,
retain partial evidence and PARK; do not drop cells. New controls/fixtures are
preregistered, not an unchanged retry of the old two-cell50ms schedule.

Three actual independent implementation agents receive the exact same source pin,
frozen lookup referee, this selected hypothesis and guard plan. Each owns one
worktree/build and only its variant artifacts. Root owns the shared guard harness;
its separate freeze and baseline requalification precede comparisons. All source
patches and failed checks are retained. A primary-only screen can reject, never
accept. Full controls, discovery guards, fresh confirmation, matched profiles,
independent confirmation/adversarial review remain required. Main src stays unchanged.
