# Independent diagnostic design review

**Offline investigation GO; fresh workload execution NOT READY.** Root reports a
current competing PR15967 profiler reservation and active capture service.
Read-only DSO acquisition/PMU inspection may proceed; this review authorizes no
runner workload, lease takeover, source implementation or acceptance decision.
Reviewer `/root/intel_b_review`, Codex; actual model/token cost unknown.

## Ownership correction to the earlier sweep

The newly discovered reservation timestamp1792505959 precedes the earlier
14:25–14:42UTC profile interval. Its historical activity throughout that interval
is not yet established. The earlier CPU2/workload-accounting and sibling gates
remain observed facts; they do not prove exclusive ownership or exclude shared
LLC, memory-bandwidth or uncore interference from other CPUs.

Thus32/36 configurations were **capture-quality-qualified**, not established as
exclusive-host measurements. Earlier lookup/iterator/scan priorities are provisional
diagnostic leads. No timing winner/source adoption existed to revoke. Preserve
sealed rows and decisions, append this ownership limitation, and reconcile lease
timestamps and historical service activity from available records. Do not infer
that an active service now was active throughout the old captures, or that old
Docker emptiness proves no competing capture.

Fresh execution requires verified owner release, fleet reservation consistency,
absence of unrelated capture services/processes, and a new bounded lease with
recovery and restoration proofs. An elapsed or apparently stale timestamp is not
release authorization.

## Annotation denominator correction

Independent unfiltered `perf script` aggregation of actual sampled periods confirms
that the old `perf annotate --symbol zbtreeIteratorNext --percent-type global-period`
numbers were normalized within the selected symbol. They were incorrectly described
as shares of all workload sampled period, including in my prior final review.
[Exact numerator/denominator reconstruction](INDEPENDENT-ANNOTATION-DENOMINATOR.json)
supersedes that interpretation; original artifacts remain intact.

| Site,1M full output | Baseline | A | B |
|---|---:|---:|---:|
| Packed-length line589, actual workload period | 18.64069% | 13.46117% | 13.08542% |
| Width-test attribution358, actual workload period | 11.03793% | 10.85756% | 10.82710% |
| IteratorNext share of workload period | 90.48347% | 89.64614% | 89.60956% |

The old20.60/15.02/14.60% and12.20/12.11/12.08% match selected-symbol denominators;
B's cache-presence instruction is0.16832% of workload period versus0.18784% of symbol
period. TMA roots and whole-function hotspot shares are unaffected. Corrected
instruction shares remain sampled attribution, not instruction latency, and retain
the ownership limitation above. Every future annotation must verify its denominator
against unfiltered raw period sums rather than trust the option name.

## Offline evidence first

1. Resolve the captured update libc PC using DSO build ID
   `a4a7992a8e66555c8141ab2a08a8465ff6e0ea65`. Verify downloaded ELF build ID/hash,
   captured mmap address/offset and matching debug-symbol identity. Resolve the
   actual mapped instruction and annotation; do not name a function from an
   address in a different libc. Record unresolved aliases/inlining explicitly.
2. Map exact native lookup instructions (`FindForAdd`, `LeafFindMember`) and
   iterator transition/packed-record loads. Preserve raw period counts, denominators,
   and optimized DWARF limitations. About68% Memory Bound and64–69% lookup samples
   motivate attribution; they do not establish a cache level or per-operation cost.
3. Annotate corrected scan baseline/B primary and trim/resize guards. Separate
   tag-chunk, scalar tail, fixed setup and callback/hash paths. A seven-member
   fixture cannot directly exercise a full8/16-tag chunk; branch/layout effects
   remain hypotheses. Prior guard baseline TMA is unavailable.

## Required preregistration before fresh execution

| Area | Required evidence/gate |
|---|---|
| Identity | Exact old native binaries as transfer controls; source/patch/compiler/flags/harness hashes, fixture seeds and ordered stages frozen. Any census/instrumentation belongs to a separately identified diagnostic harness with semantic parity; never replace old controls silently. |
| Capability | Read PMU topology, event encodings/formats, precision support, virtualization, permissions and perf versions. Capability listings alone are insufficient. Freeze one bounded probe per proposed event mode through the actual CPU2 launcher; unsupported/empty/invalid results become unavailable, with no event substitution after results. |
| Precise loads | Record actual encoded event, `precise_ip`, latency threshold, sample period/frequency, data-source/weight fields and supported decoded meanings. Verify collected attributes, samples and mappings. Thresholded samples describe that selected population, not all loads or total stall time. |
| Branch attribution | Record exact branch event and branch-stack filters/privilege scope. Verify branch records/flags and matching code addresses. A branch stack by itself is not a measured misprediction rate; collect a qualifying denominator if making that claim. |
| Collector quality | Keep raw data, command/status, supported event values, scheduling, lost/throttled records, sample counts/periods and CPU/PID scope. Preregister minimum sample support and precision requirements before inspecting results; sparse/unsupported bins remain inconclusive. Do not require PEBS and LBR to fit simultaneously without a validated event combination. |
| Matched conditions | Collect baseline/candidate anew under the same new isolation condition. Preregister serial order and repeats; preserve every failure. Update100K/1M same/position needs explicit warmup/phase ordering. Separate captures from evolving state are not automatically matched phases. |
| Attribution | Record completed-work/phase counts if claiming per-operation quantities. Otherwise restrict results to conditional sample distributions and interval ratios. Instrumented census may explain fixtures but cannot provide missing counts for an uninstrumented capture. |
| TMA | Use actual topdown glue with explicit CPU scope. Retain four finite total-slot roots, sum tolerance, units, intervals,100% scheduling and unchanged CPU/workload accounting gates. Mixed/underscheduled deeper levels remain unavailable. |
| Shutdown | Bounded owned process group, recovery timer before coordinator suspension, exact state restoration, fresh release proof. Do not interfere with another owner's capture service. |

## Isolation change is a prerequisite, not a retry label

The four old scope failures remain. Before any replacement TMA, define and verify
a concrete changed condition: for example, a permitted sibling-offline condition
with exact pre-state/restoration, or a demonstrated scheduler/interrupt isolation
change. Merely waiting for the same online sibling to look idle is an unchanged
retry. If neither condition is safely available, keep those comparisons unavailable.

If the sibling is offline, record topology and model/denominator behavior and
explicitly define the offline-state verification gate; do not divide an absent
sibling counter delta or silently mark it0%. Requalify the new baseline and
candidate together. Old online-sibling captures remain a separate measurement
condition. No current PMU or isolation capability has been established by this note.

## TMA classification

```text
Pipeline Slots — INTEL-FOLLOWUP-001, baseline and candidate
├── Frontend_Bound     unavailable
├── Bad_Speculation    unavailable
├── Backend_Bound      unavailable
│   ├── Memory_Bound   unavailable
│   └── Core_Bound     unavailable
└── Retiring           unavailable
```

No fresh capture is authorized to start on the occupied runner. Historical trees
remain in the sealed prior experiment, now subject to the ownership limitation
above. Source selection remains NONE; future code hypotheses require the prescribed
population process and independent qualified timing/guards.

Own `library_status`/`ask` calls and limits are recorded in
[reviewer consultation](reviewer-consultation.json). MCP revision `a5a05e6bf7c9`
was available,1/287 sources indexed with27 passages. The returned pmu-tools overview
does not establish this runner's PEBS/LBR capability or causal mechanisms. This is
one independent reviewer applying the benchmark adversarial skill's parity,
replicability and attribution lenses, not a claimed multi-reviewer skill audit.
