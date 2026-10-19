# Exact corrected NEON sources — preparation READY

Four isolated, explicitly partial Git worktrees now have detached HEAD at13e459ff8800be3f02b6b45c87dd7b0c39453fa9: worktrees/m6-neon-base, worktrees/m6-neon-A, worktrees/m6-neon-B and worktrees/m6-neon-C. None existed before this preparation. Each materializes60 exact original blobs from src/, compat/, vendor/, bench/, tests/, Makefile, AGENTS.md, docs/POPULATION.md and the three workspace instruction files. They are deliberately not complete checkouts. Git worktree creation used --no-checkout; blobs were materialized directly, and no git add/index staging, commit or push occurred. Full file identities and commands are retained.

The single canonical manifest is **source-manifest.json**. Its variants[base|A|B|C] entries include worktree, exact Git HEAD, source_hashes keyed by paths relative to each worktree, portable_macro, patch_sha256, target_c_sha256, original_author and referee_additions. This naming/schema was coordinated directly with validation and timing authors; no uppercase duplicate exists.

Baseline target C is d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2; header496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83. Corrected adapter header468a5811ad80fa4dc47196b90835586cbbbd8b7d235af225092637e930708fa7 and Cc9237cd2e2fb08fff5c67431a9de5d6d1596d6211082a068116040c477689fb3 come from the exact corrected commit, not the remote evidence branch's legacy root adapter.

Exact ARM017 patches were read from the pinned021 input copies, checked against their original inputs-freeze hashes, checked/applied without --index, and verified against original target C hashes. No patch bytes changed. Every other original materialized file remains byte-identical to the common13e baseline.

| Variant | Original actual author | Patch SHA256 | Target C SHA256 | Correctness-only portable macro |
|---|---|---|---|---|
| base | Unmodified baseline | — | d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 | — |
| A | /root/aws_arm | 42fed5c2de1a863f0f1a415d2a348694bfb8f773ef2ffbff562c2472d2b76b53 | 0f8568f36ea0ed3d48c13906302c2df6983d6271568b88e0b5c380f7ce2070eb | ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE |
| B | /root/aws_intel | 978134f54562ab6cff239bfbd15152cfc08e8defb19aa71c8cae122ceb870eac | 1788f2b5e48ef74440079a9a3da67a67a3b5b5bae1d18f617d42784b10ba8825 | ZBT_LEAF_TAG_MATCHES_FORCE_PORTABLE |
| C | /root/aws_amd | 7335e122597ba6fa74cee42f13e5ee3ecbb52753efb7c56a8abdf7a4775f27e8 | 1600c035103a0dd30b49a5a266da73707963039647443ffd3ee88cd5f6827fe2 | ZBT_FORCE_PORTABLE_LEAF_TAGS_C |

The unchanged V2 oracle is a separately identified referee addition at the same relative tests/all_match_guard_oracle_v2.c in every worktree, SHA256b01a762f925a679a6342f5258824ca4743b0020a47982f015be4916050953ded. It was absent from13e and copied unchanged from pinned ARM017 evidence. All other original tests/referees, including scan_interval, wide_scan, live_widen_scan and resize_generation, were present in13e and copied from that exact commit; no fallback commit or invented source was needed. The manifest distinguishes this one addition from60 original materialized files. It does not claim that tests have executed.

Common future paths are src/zset_btree.c, bench/microbench.c, tests/upstream.c and tests/all_match_guard_oracle_v2.c, with outputs build/native/btree-bench and separate build/san paths in each owned worktree. Native/sanitizer options remain exactly023 PLAN; no ISA option or timing-only fallback macro was added. Mac CPU placement remains unpinned. The600s validation,300s A/A,300s discovery and07:15UTC cutoff remain root's frozen limits, not executed work.

No build, native correctness process, profile or timing ran. No shared/root target, original referee, other campaign or another session's edits were changed. This prepares a bounded new-host falsification of the exact previously authored family; it creates no new independent implementations or population count and makes no source adoption claim. Original authors' exact models/token/currency costs remain unknown. Current preparer is /root/followup_proposal_c, inherited Codex/GPT-6 family; exact serving model/token/currency cost unknown. My022 NONE dissent remains preserved.
