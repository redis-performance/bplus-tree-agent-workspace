# Actual controller CPU-perf consultation

Transport: local stdio MCP, since no direct cpu-perf tool was exposed in the host
catalog. Server cpu-perf0.1.1, bundled list deb5a0bac467 (2026-10-05). Discovery,
library_status, contextual ask, explicit source reads and a result reconsultation
were actually performed. Exact inputs/times and canonical response hashes are in
tool-calls.json; full local responses remain under ignored scratch. This directory
contains no downloaded source body or corpus. No indexing crawl/embedding/update,
settings change or native benchmark occurred. Library initially0/287 indexed,
keyword-only; each ask returned no matched source passages and marked its narrative
context unrecognised. Tool retrieval does not validate the measured inference.

Root read https://llvm.org/docs/Benchmarking.html: noise controls depend on the OS;
low noise does not establish absence of bias. Linux instructions were not applied
to macOS. Root also read the linked clock_gettime Linux manual (entry5.4.3), which
separates per-thread CPU clocks from wall clocks. This is explicitly NOT Darwin
clock-resolution/accounting validation; no Linux implementation guarantee transfers.

Actual result reconsultation supplied all three wall/thread failures and nested clock
ordering. check_evidence returned drop_number, missing frequency and failing to parse
some explicitly stated one-thread/method fields; it also counted the word
microarchitecture despite its being unknown. This heuristic is not our acceptance
gate or evidence for a cause. Source/build context is the unchanged corrected-adapter
baseline. The exact native compiler command is retained in ../analysis.json inputs
and EXP-009/bench-results/build/commands.jsonl, including -Werror and -fno-lto, omitted
from the concise initial context but unchanged in all measured binaries.

Impact: retain all failed controls and wall-clock acceptance rules; do not diagnose
DVFS, migration or cache placement from the residual or endpoint snapshots. A thread
contrast is descriptive evidence, not a replacement qualification. A new diagnostic
must measure interval/accounting uncertainty before a strict descheduling falsification.
Actual backend Codex/GPT-6 family; exact serving model and token/currency costs unknown.
