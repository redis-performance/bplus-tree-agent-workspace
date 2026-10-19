# Static adapter inventory review — PASS after duplicate-label correction

The revised inventory agrees with independent parsing of every retained012
disassembly body. All five selected function metrics are correct. This is a static
assembly inventory, with no performance result, source candidate, acceptance or
optimization population.

Reviewer `/root/followup_proposal_c`, GPT-6/Codex family; exact serving model, token
usage and monetary cost unknown. I inspected the script but did not import or run
it. Only an independent in-memory parser and file/hash reads were used. No executable,
disassembler, build, profile, timing campaign, source edit or Git write was performed.

| Symbol |Instruction lines, old→new|Entry-prefix frame bytes, old→new|
|---|---:|---:|
|`_traverse`|280→288|144→144|
|`_zbtreeIteratorNext`|155→114|96→0|
|`_zbtreeScoreRaw`|345→491|176→160|
|`_zbtScoreLeafFindMember`|161→142|144→144|
|`_zbtreeRank`|443→596|192→192|

Both original disassembly files match their012 captured-command stdout hashes,
private raw hashes and recorded successful `otool -tvV` commands. The complete22-file/
binary012 freeze still matches, and C/header remain the unchanged `d9123c…` /
`496e72…` identities. All four015 input identity hashes match. Reviewed revisions:

- `inventory.py`: `ce0bac90a6460b72080d8efba7c11fac2a057d0b11ecc399d32e7d2b35c98fa8`
- `inventory.json`: `ebaa288d1613cad6afc4e32e9749c214270150f821dcb541ac9de8dfb0da3038`

## Initial finding and preserved correction

My first independent parser rejected duplicate symbol labels. The initial inventory
used a dictionary that silently replaced earlier bodies sharing the names
`_OUTLINED_FUNCTION_0` and `_OUTLINED_FUNCTION_1`. This affected the broad function
census, while all five selected target functions were unique and unaffected.
The issue was reported before any input edit or final review.

Root preserved the exact initial script, JSON, README and issue record in
`attempt001/`; their recorded hashes match. Root then revised the parser without
new disassembly or measurement. Independent reconstruction now confirms:

- All108 old and105 new body-occurrence summaries are retained, spanning106 and103
  unique emitted names respectively.
- Both duplicate outlined names retain both occurrences per binary. They have
  `comparison_eligible=false` and no old/new paired summary. Ordinal occurrence
  order is not used to assert cross-binary identity.
- All108 union-name inventory rows, occurrence metrics and eligibility flags match.
  There are39 changed eligible unique-name summaries.

The initial audit AssertionError and root's correction are disclosed in the JSON.
They were parser-review findings, not an experimental failure or reason to rerun
measurements.

## Meaning and limits

Instruction lines count addressed disassembly entries between emitted labels.
They do not measure retired instructions, cycles or elapsed cost. Equal summary
metrics do not establish identical instruction streams or semantic equivalence;
compiler-generated labels can also change meaning when outlining changes. The39
changed rows describe metric/presence differences among eligible labels.

Entry-frame bytes recognize a contiguous function-entry prefix within the first16
instruction lines. This is not a whole-function control-flow or stack-depth proof.
I also scanned each actual prefix without that16-line cap: no frame metric changes
for these inputs. The corrected iterator's zero entry-prefix frame excludes its
separately emitted cold panic frame and all callee frames.

The textual stack-reference count recognizes `[sp` or explicit `sp, sp` patterns;
it omits accesses expressed only through the frame pointer and cannot measure
dynamic stack traffic. Direct-call counts cover `bl` lines, not all indirect or
tail calls. None of these metrics supports a speed direction. The larger corrected
ScoreRaw/Rank instruction inventories and smaller iterator inventory are compatible
compiler consequences of the same truthful adapter contract.

The report correctly scopes these counts to the exact012 binaries and preserves
historical candidate/profile identities. It makes no runtime, cache, CFG, source
optimization or population claim. Future source comparisons still require a shared
corrected-adapter baseline and their own qualification, profiling and review.

`INDEPENDENT-AUDIT.json` records the independent reconstruction, selected rows,
input/attempt hashes, source identity, initial finding and parser limits. All review
activity is finished.
