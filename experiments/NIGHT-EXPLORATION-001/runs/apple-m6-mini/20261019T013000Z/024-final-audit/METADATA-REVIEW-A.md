# Supplemental existing-metadata review A

PASS. Independently parsed all 48 public raw CSVs, verified their retained hashes and recomputed all twelve wall/thread ABBA percentages using exact integer sums and Fraction arithmetic. The root analyzer was not imported or executed. Every published percentage agrees within final float representation.

The failed 1M blocks (zero-based 1 and 4, seed 402) have thread-clock differences **−1.440358832%** and **+1.587802879%**, alongside the original wall differences −1.466505207% and +1.641392986%. Thread time is descriptive; the preregistered wall-clock gate and PARK/source NONE decision remain unchanged.

Exactly **20/48** rows have differing CPU endpoints; observed IDs are 6 and 7. All reported QoS endpoint pairs are user-interactive/user-interactive. These endpoints do not establish full residency or the number of migrations, and cannot assign variance to scheduling, frequency, preemption, cycles or cache behavior.

The exact frozen benchmark source hash matches the diagnosis. Actual source order is `thread_start = thread_ns()` before wall `start = now_ns()`, followed by the operation, wall elapsed read, then `thread_end = thread_ns()`. These brackets differ slightly, so thread/wall observations are not an exact identical-interval decomposition. No clock substitution, alternative CPU-time gate, causal claim, count change or retry is proposed.

All exact fractions and evidence identities are in [METADATA-REVIEW-A.json](METADATA-REVIEW-A.json). No native workload/build/performance rerun or frozen edit occurred. Participant `/root/followup_proposal_a`; inherited Codex/GPT-6 family, exact serving model/token/currency costs unknown. Findings: none. Idle.
