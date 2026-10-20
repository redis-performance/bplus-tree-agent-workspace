# Independent offline review

**PASS for corrected offline attribution. Fresh execution remains conditional on
exclusive secondary-host preflight and a frozen, reviewed protocol.** No source
selection or cross-host performance comparison follows.

[Independent audit](INDEPENDENT-OFFLINE-AUDIT.json) regenerates all36 profiles from
raw perf data, totaling21,601 samples. Every symbol period, whole-workload denominator,
sample count and365 selected hot-instruction numerators agrees with `offline.json`.
Report event-count totals agree with exported period sums. Raw and native ELF hashes
match sealed records; no sample/capture was changed.

Captured libc, acquired ELF and debug ELF share build ID
`a4a7992a8e66555c8141ab2a08a8465ff6e0ea65`. Debug package version2.39-0ubuntu8.9
and SHA256 `c4b086cef3a6bbb6a90299969b3c0bf3867f40cb8e9bbbb0edfe5ae23f2c04f0`
match retained apt metadata. This reviewer independently checked bytes/build IDs,
not the remote repository's signature chain.

## What the resolved symbols establish

| Update1M | Same | Position |
|---|---:|---:|
| `__memchr_evex`, workload sampled period | 13.22% | 14.36% |
| `__memcmp_evex_movbe`, workload sampled period | 5.22% | 5.43% |

These are exact-symbol sampled attribution, not operation costs or proof of a
memory-stall mechanism. Source calls need further discrimination:

- The exact update ELF's three direct `memchr@plt` calls map to leaf membership
  source1287: addresses5890/5ef0 inline into `zbtreeScores`, andd9a8 is in
  `zbtScoreLeafFindMember`. This supports investigating contiguous tag scanning.
  Current samples contain no callchain assigning dynamic libc shares among callers.
- The ELF has both `memcmp@plt` and `bcmp@plt` calls. Leaf member equality at
  source1302 compiles to `bcmp` atda48. Exact libc exports `bcmp` and `memcmp` at
  the same IFUNC addressb1730. Therefore the resolved implementation's samples
  cannot be described as exclusively one source-level `memcmp` call's cost.
- Selected hot IPs are valid addresses/periods. The16-byte disassembly snippets
  may truncate a following instruction and print `(bad)` or byte directives.
  Those trailing fragments are an output boundary, not evidence of bad code.

The [annotation denominator correction](INDEPENDENT-DESIGN-REVIEW.md) remains
necessary: selected-symbol percentages in the prior annotation were not
whole-workload percentages. This new analysis uses unfiltered period totals.
The earlier ownership-overlap limitation is unchanged; these are provisional leads.

## Secondary Intel diagnostic decision

A new bounded session is justified **after** exclusive availability is established:
it can test whether the same lookup/transition/branch observations recur under a
distinct host and verified sibling-offline condition. Matching Sapphire Rapids
names alone does not establish equal software, topology, PMU model or workload state.

Before execution, root must reconcile the current fleet reservation and local
lease/service records; old September files plus a later release are supporting
history, not proof that no subsequent owner exists. Verify active systemd services,
processes and cgroups, including collectors/builds outside Docker, and establish a
fresh bounded lease. Retain metadata for ambient agents such as the listed
`parca-agent`; do not kill unrelated agents or call the host pristine. Qualification
must account for the actual background collector condition.

Freeze the secondary host's exact kernel/perf/toplev/PMU/compiler/libc identities.
Transfer verified binaries as controls where compatible; revalidate completed
semantics on that host. Any rebuild creates a distinct binary condition. Confirm
actual CPU2/NUMA placement and sibling topology, arm recovery before changing
sibling50, save its prior online state, and independently verify restoration.
PEBS/LBR event listings require a bounded preregistered actual-collection validity
probe; invalid modes remain unavailable.

Collect all comparison baselines/candidates under the same new condition and keep
that evidence separate from the earlier online-sibling profiler results. New
measurements cannot establish that offlining the sibling caused a cross-host
difference. They do not repair earlier raw failures, qualify timing, or select an
implementation. Detailed scope/scheduling/phase/termination gates remain in the
[design review](INDEPENDENT-DESIGN-REVIEW.md); execution code still needs review.

## TMA classification

```text
Pipeline Slots — new secondary-host baseline/candidate
├── Frontend_Bound     unavailable
├── Bad_Speculation    unavailable
├── Backend_Bound      unavailable
│   ├── Memory_Bound   unavailable
│   └── Core_Bound     unavailable
└── Retiring           unavailable
```

No fresh measurements exist. Old TMA classifications are unchanged and retain
their ownership limitation; libc samples do not replace them.

Own fresh CPU-perf `library_status`/`ask` calls included these resolved shares:
[record](reviewer-offline-consultation.json). MCP available, revisiona5a05e6bf7c9,
1/287sources and27passages; retrieved overview material does not establish a
mechanism or host capability. Reviewer `/root/intel_b_review`, Codex; model/cost
unknown. No remote workloads or source changes performed.
