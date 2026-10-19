# CPU Performance Engineering MCP: improvement review

Reviewed cpu-perf 0.1.1 and upstream revision
`deb5a0bac46760503b6f4a2608bdfed470c8532e` on 19 October 2026.
Actual controller-only MCP calls: library_status, ask, and three check_evidence
cases. [Call inputs, outputs and hashes](CONSULTATION.json) preserve reproduction.
No benchmark, source candidate, runner work, upstream issue or PR was created.

## Highest priority: distinguish unknown from known

A synthetic input explicitly says nominal frequency only, runtime frequency not
measured, turbo state unknown and SMT state unknown. With otherwise recognizable
fields and `6 runs`, the actual checker marks all seven fields present and returns
`quotable`. This is a false positive under its own metadata-completeness rule.
The synthetic 2.6 GHz and 7% figures are test inputs, not AWS observations.

Code cause: evidence.py checks whether frequency/turbo/SMT regexes have any matches;
it does not determine whether their states are known, negated or merely mentioned.
Fix direction: distinguish known, unknown, missing, conflicting and not-applicable
states; separate nominal from measured frequency; preserve evidence spans and never
turn a declared unknown into a known state. Add negative fixtures for unknown and
unmeasured fields, plus positive fixtures for explicit known states. Keep editorial
metadata completeness separate from measured-result validity or causal support.

## Structured metadata and robust text parsing

The checker misses `one pinned core`, `Clang18.1.3` and ABBA blocks in our actual
context. The synthetic `Six runs` case also fails its run-method recognition while
`6 runs` passes. Code review confirms the number-word allowlist omits six and the
compiler regex requires a word boundary before a digit suffix. Our earlier compressed
prose contributed to other misses; it should be replaced with readable metadata.

Add optional typed metadata for CPU, OS, core count/affinity, measured clock state,
compiler/version/flags, source and binary identities, workload, baseline, and method.
Represent A/A, ABBA, repetitions and statistics explicitly. Retain the text interface
and flag contradictions between text and supplied metadata. Test the real AWS
consultation plus these minimal pairs. Typed inputs still require evidence; they do
not automatically validate a performance claim.

## Populate our library; improve readiness reporting

Our 0/287 indexed sources are partly a setup failure: we explicitly disabled automatic
indexing and never populated the library. This is not evidence the MCP cannot index.
Its existing `cpu-perf index` command builds the library, and multiple local clients
already share it. Prepare the library on the controller, outside measurement windows;
check relevant Arm/Intel/AMD coverage before relying on retrieved evidence.

The MCP already reports empty coverage honestly. An improvement would be a
machine-readable readiness state and an actionable next command when indexing is
disabled and no passages exist. Avoid repeatedly treating a source-list lookup as a
completed source consultation. A useful setup check must retrieve an actual relevant
passage, not merely establish that the server responds.

## Vendor document recovery and explicit target selection

Our Arm Neoverse V2 manual request returned an empty vendor landing page. The current
resolver already follows candidate PDF/download links from HTML anchors; suggesting
that basic feature as new would be incorrect. Improve it with tested vendor-specific
metadata resolution where available, or a user-supplied official-document import
linked to its canonical URL, revision, checksum and page numbers. Keep blocked/empty
states explicit and do not bypass access restrictions. Successful resolution of this
particular Arm page is not demonstrated here.

`ask` already parses raw perf/compiler/assembly context and filters hardware sources
when it infers a vendor. We supplied prose summaries, which it explicitly treated as
search words. Pass actual raw output in future calls. Optional explicit architecture,
CPU and OS fields would improve routing for ambiguous generic counters or prose;
add evaluation cases ensuring macOS investigations do not receive Linux-only actions
as directly applicable. Source relevance and numerical portability remain separate.

## Proposed order and validation

1. Correct unknown-state handling and add the demonstrated regression cases.
2. Build our existing library and verify real passage retrieval on the controller.
3. Add typed metadata and text-parser compatibility tests.
4. Improve vendor resolution and architecture/OS routing with captured fixtures.

These are reviewed recommendations, not implemented upstream changes. Existing
benchmark decisions remain unchanged. Exact serving model and token/currency costs
are unknown. No optimization-population counts change.

Primary sources inspected:

- [MCP documentation](https://github.com/usamahz/cpu-performance-engineering/blob/deb5a0bac46760503b6f4a2608bdfed470c8532e/misc/mcp/README.md)
- [Evidence checker](https://github.com/usamahz/cpu-performance-engineering/blob/deb5a0bac46760503b6f4a2608bdfed470c8532e/misc/mcp/src/cpu_perf/evidence.py)
- [Question routing](https://github.com/usamahz/cpu-performance-engineering/blob/deb5a0bac46760503b6f4a2608bdfed470c8532e/misc/mcp/src/cpu_perf/brain.py)
- [Vendor link resolver](https://github.com/usamahz/cpu-performance-engineering/blob/deb5a0bac46760503b6f4a2608bdfed470c8532e/misc/mcp/src/cpu_perf/library/resolve.py)
