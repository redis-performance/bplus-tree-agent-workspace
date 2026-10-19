# Adapter compiler-contract static inventory

This analyzes the already captured old/new disassemblies from012. No executable is launched, source edited, or timing/profile data collected. Both original disassembly hashes are checked against their captured command log below; frozen source and binary hashes are reverified. Static size is not dynamic work or speed.

|Symbol|Instruction lines old→new|Entry-prefix frame bytes old→new|
|---|---|---|
|`_traverse`|280→288|144→144|
|`_zbtreeIteratorNext`|155→114|96→0|
|`_zbtreeScoreRaw`|345→491|176→160|
|`_zbtScoreLeafFindMember`|161→142|144→144|
|`_zbtreeRank`|443→596|192→192|

The compiler-contract correction changes more than the iterator frame. Other functions can shrink or grow as inlining and cold-path decisions change. A smaller entry frame combined with larger code is not evidence of either a speedup or regression. The leaf search helper keeps a144-byte entry frame in these binaries.

The iterator has no function-entry frame after correction; its cold panic frame remains16bytes, independently mapped in013. Entry-prefix inventory is a simple assembly parser, not a general control-flow/stack-depth proof. Full rows, source/binary identities, method and limits are in inventory.json.

Historical tree candidates and old-adapter profiles retain their original identity. These static observations do not adopt, re-rank or reconfirm any candidate; future comparisons need a corrected-adapter baseline and local evidence. Counts unchanged.

Reproduce from the repository root: `python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/015-adapter-codegen/inventory.py`. Actual participant/root; inherited Codex/GPT-6 family, exact serving backend/token/currency costs unknown.
