# Independent pre-execution review

**GO for the frozen baseline-only qualification. No candidate timing or adoption approved.**

Reviewer: `/root/intel_b_review`, Codex; exact model and token cost unknown. Reviewed source and protocol independently; no SSH or benchmark execution. This continues the retained exact-B population, not a new implementation population.

Prior Intel TMA and code-local iterator samples justify this research priority, but neither proves the cached offset addresses the measured memory stalls. The fresh secondary-host timing binary must supply its own TMA and baseline qualification.

The final protocol resolves the initial review blockers:

- Frozen baseline is `c6112e052e8c11dfa1fef051d704de598b367f52`; preparation verifies copied tree/referee bytes. B patch remains exact and isolated. No original referee is changed.
- Ops-only range extension preserves existing parser limits and oracles; rounded operation count is overflow-checked. uint64 checksum wrap is intentional. Planned 64 original/new semantic pairs, completed >100M boundary, original native/sanitizer tests and both retained baseline/B cache oracles precede measurement. Inspected local parser validation has 11 passing cases; runner correctness remains pending.
- Three fixed calibration seeds determine whole-traversal counts using integer arithmetic, target600ms, maximum2B with no clipping/recalibration. Eight cells × six blocks × four same-binary rows =192. Each window must reach500ms, every block meet1%, with exact output/memory/fixture invariants.
- Timing/occupancy failures finish the fixed schedule within its budget; timeout/nonzero/semantic/affinity failures preserve partial evidence and stop. No retry and no candidate launch. Failed rows are never silently discarded.
- CPU2/NUMA0 placement, sibling50 occupancy and workload/CPU jiffy accounting are explicit. L2 TMA requires all four unique finite slot categories, sum100±0.3pp,100% scheduling and the declared occupancy/accounting bounds. Raw collector streams are saved before post-capture process checks, including an exited workload.
- One executable serves profiling and timing; readiness is outside the timed region. Long profile workloads are terminated, so their full post-traversal checks are unavailable; completed timing/check workloads provide separate semantic evidence.
- Whole work is bounded to25minutes plus10s kill grace, with owned-process-group cleanup before coordinator restoration and a30minute recovery timer. Coordinator STOPPED and absence of containers are checked before work. Live reservation/restoration verification remains the controller's responsibility.

Python syntax, shell syntax and schedule cardinality checked. Static retained-B review finds all initialization/seek and leaf-transition cache resets present; mutation already invalidates iterators. No immediate semantic blocker found. Acceptance still requires the broader optional-output/seek/direction/external-member guards, actual ABI state-size checks, matched candidate TMA, qualified comparison and independent confirmation/review.

SMT occupancy is an average over each whole process envelope, not proof that the timed loop saw zero contention. TMA is CPU-wide; clock stability and exclusive ownership cannot be inferred solely from those counters. These limits must remain in the results.

## MCP provenance

Own local stdio `library_status` succeeded at `a5a05e6bf7c9`,0/287 sources indexed and0 passages; [raw availability record](reviewer-mcp-availability.json). Direct tool discovery exposed topdown but no cpu-perf tool. Consumed controller's **shared**, not own, `ask` from2026-10-20T11:50:27.218355+00:00. It recognized no tool output and retrieved no supporting passages. Consultation is recorded without claiming methodological support from unread references.

## Reviewed identities

- `protocol.json`: `97f3bd73ff127c76fc0b35a8a1d7f30b4e1b46dead9fcc6376ad23cb9235c73a`
- `campaign.py`: `ac9f71516936b6216912cc65a61f923260e6a5e41c77212263933b9710fa4721`
- `run.sh`: `ada6d87d7ada075d5f5ff2192652e2d262c250298509e33a3b75e24c6587f5e6`
- `work.sh`: `7843eeb4d29f737de34360eed94ffcec5e3c5eaa5c2444f11fe00f6f8ef2dc22`
- `prepare.py`: `7ba470e34a9acfb27bb26f914fb9c8aea3173050b504678f34db82b9f85538dc`
- `ops.h`: `29abceb9480323deb1dbaf509beaab67d06836bb048b8ede1c1ca30852c2ae67`
- `ready.c`: `68d5d3a2895463d2bab1df5030cb4d27d54d7911c742bc018bbbb3bfa4e0f886`
- `parser-validation.json`: `3df4c7d6b27d0a35ca33292403cc2f6f1f135aba829575570c02cfdc15109fba`

Reviewed UTC: 2026-10-20T12:00:18.576688+00:00
