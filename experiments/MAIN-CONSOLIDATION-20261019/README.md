# Published performance history consolidated into main

On 19 October 2026, the user requested that main be brought up to date. This
integration merges the published AWS AMD, ARM, Intel and Apple M6 histories.
Both Apple M1 branches were already ancestors of main. No optimization is
adopted and no experiment decision or population count changes.

## Branches and evidence

| History | Published tip | Evidence files |
| --- | --- | ---: |
| AWS AMD | `f1ffd7e1741a036b8a5de0a6d5d4f430f205ddd2` | 4,489 |
| AWS ARM | `59ef4391f2a5a5be3eda90c4f6ddfd56e1974c77` | 38,271 |
| AWS Intel | `16118f4419a1d675f74117ae751ffbd973298de7` | 20,287 |
| Apple M6 overnight | `85afa6c7b798130452ca9dbd63082337e8bd78b7` | 90,656 |
| Apple M1 overnight | `2baeafcef68a39baabee15c6825f656a10d9b29a` | 1,124 |
| Apple M1 lookup A/A | `1d45ec70ced9f242e966b1899006462788ffe56e` | 128 |

[History validation](HISTORY-VALIDATION.json) records ancestry and exact Git mode
and blob equality for all 154,955 evidence files. Run
`python3 experiments/MAIN-CONSOLIDATION-20261019/verify-history.py` to repeat it.
All 14 existing files under source, adapters, vendor, benchmark, Makefile and the
original test entry point match pre-integration main `f46efccb3` exactly.
Losing variants and failed controls remain intact in their experiment directories.

## Resolutions

Current consolidated shared documents take precedence over earlier worker status
text. Exact worker versions are retained under [shared-history](shared-history/),
with source blob IDs and resolution records in each `*-merge.json`. This includes
the M6 coordination and next-step documents. The Intel root ledgers are explicitly
labelled historical and link to the canonical `experiments/` ledgers.

The M6 rank referee, `bench/night-rank.c`, is added unchanged from its branch.
The campaign publisher combines M6 publication requests, acknowledgement and path
isolation with main's AWS host support, runtime summaries and Linux privacy checks.
The publication tests include real pushes to temporary local bare repositories;
no measurement host or external campaign is started by validation.

All **30 validation commands passed**: 19 Python tests, 43 original tree tests,
and 24 rank oracle smoke runs (12 native, 12 ASan/UBSan).
[Executed validation](validation/checks.json) includes publisher, release-audit and
supervisor tests, original tree correctness, and bounded native and ASan/UBSan rank
oracle checks across four modes and three score layouts. These smoke timings are
not new performance measurements, baselines or acceptance evidence.

The upstream CPU performance MCP [PR #13](https://github.com/usamahz/cpu-performance-engineering/pull/13)
is separate and remains open; this integration does not merge it. The unrelated
manager-contact documentation branch is outside this performance consolidation.

## Session scope

This was Git integration and functional verification, with no new performance
interpretation, proposal or optimization round. No performance MCP consultation or
independent agent review is claimed for this integration. The mandatory CPU MCP
rule and prior consultations remain in the canonical documentation. Executor:
Codex, GPT-6; measured token cost unknown. No runner lease requested or resumed.
