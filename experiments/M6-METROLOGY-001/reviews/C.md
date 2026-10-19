# C — clock attribution and instrumentation review

**Observed wall/thread differences do not explain the three failed controls. The physical native cause remains unresolved.** The initial diagnostic README statement that a failed thread contrast “falsifies” descheduling alone is too strong without an independent bound on timer-wrapper work and clock/accounting error. It is sound only as a narrowly defined operational test of the *recorded* clock differences. EXP-009 remains PARK/source NONE; no alternate clock rescues its acceptance gate.

I reconstructed all48 public raw CSVs plus96 stream hashes against the command ledger, schedule and summary, then independently calculated all12 contrasts without importing the driver calculation. Every row/failed block remains; outputs/operations/owned bytes match within each quad and every journaled child is reaped/group empty. This is one offline analysis with a bounded derived-report refresh for root's later bracket-design question, no measurement rerun. No peer's new review was read.

| Members | Block / seed | Wall effect % | Thread effect % (diagnostic) | Δ(wall−thread) ms | Original wall gate |
|---:|---:|---:|---:|---:|---|
| 100000 | 0 / 1 | +0.066263479 | +0.062960679 | +0.039749 | PASS |
| 1000000 | 0 / 1 | -0.614488378 | -0.619500479 | +0.050832 | PASS |
| 1000000 | 1 / 2 | -0.593164636 | -0.596221004 | +0.027126 | PASS |
| 100000 | 1 / 2 | +0.220645724 | +0.237541376 | -0.195543 | PASS |
| 100000 | 2 / 3 | -0.016886574 | +0.004118000 | -0.247459 | PASS |
| 1000000 | 2 / 3 | -1.414059483 | -1.401383575 | -0.183208 | FAIL |
| 1000000 | 3 / 1 | +0.841156694 | +0.843930685 | -0.018460 | PASS |
| 100000 | 3 / 1 | +0.299162159 | +0.288095987 | +0.134293 | PASS |
| 100000 | 4 / 2 | +0.147093637 | +0.146666931 | +0.007416 | PASS |
| 1000000 | 4 / 2 | +1.036273240 | +1.008640024 | +0.354667 | FAIL |
| 1000000 | 5 / 3 | +2.567324587 | +2.542454495 | +0.342167 | FAIL |
| 100000 | 5 / 3 | -0.636547769 | -0.629650654 | -0.092625 | PASS |

Qualification remains6/6 at100K and3/6 at1M for both recorded metrics. Individual wall windows are586.347–630.314ms. For the three failed1M blocks, residual contrasts account for only−0.014772,+0.028978,+0.028029 percentage points when all components use the wall-A denominator. The exact identity is ΔW=ΔT+Δ(W−T); subtracting wall% and thread% directly would mix denominators. All48 residuals W−T are positive:0.623167–1.058542ms, median0.8419165ms. These are clock residuals, not measured descheduling durations.

The nearest thread-gate margins are4.97075075ms,0.10560467ms and18.80635008ms in the corresponding signed-side contrast. In particular the+1.008640024% thread block is only about105.6µs beyond the boundary. No existing wrapper/error calibration justifies treating that margin as a strict causal exclusion. The larger margins are suggestive against a sufficient descheduling explanation under stable timer overhead, but their size does not manufacture a proven error bound.

## Actual instrumentation and why subtraction is insufficient

Frozen native lookup.c orders CPU-start observation, thread-clock start(T0), monotonic-wall start(W0), lookup body, wall end(W1), thread-clock end(T1), then CPU-end observation. The native binary has no LOOKUP_PROFILE/LOOKUP_COUNTS hooks. Existing retained native `_main` disassembly confirms the last four clock_gettime argument IDs are0x10,0x6,0x6,0x10, consistent with this nested ordering. Actual instruction windows, raw hashes and all row/block arithmetic are in C.json. No new disassembly or native command was run.

Let C be the lookup interval's consumed CPU time, S its off-CPU wall time, and B consumed CPU work in the outer thread interval but outside the inner wall interval. Under ideal compatible accounting, W=C+S and T=C+B, hence **W−T=S−B**, before any clock error. The extra bracket includes portions of the clock wrappers, returns and boundary instructions. Its size and variability were not independently bounded. The observed0.6–1.1ms residual cannot upper-bound S: a larger S and larger B can produce the same difference. With nonideal clocks, the expression gains unmeasured differential timestamp/accounting error. Clock read resolution, quantization, accounting lag and accuracy are distinct; observed wall durations being multiples of1000ns is not a measured accuracy bound.

Therefore replacing wall time with thread time is neither a measurement repair nor a causal demonstration. The diagnostic does refute the operational claim that the *recorded residual contrast alone* removes all failures. It does not prove DVFS, cache placement, core class, same-core residency, pure on-CPU causal slowdown or every possible descheduling-only model false. Profile rows are especially unsuitable for pooling: their sample start/stop and symbolization occur inside the outer CPU bracket but outside the inner wall interval.

Endpoint CPUs differ in20/48 rows and match in28; all observed values are6/7 and effective QoS is unknown. The snapshots lie outside the timed interval. Equal endpoints do not exclude intermediate migration; different endpoints establish only different observations, without migration time, residency fraction, core class or frequency. Do not condition inclusion/gates on endpoints or use a correlation as a mechanism test.

## Root-suggested next design: conditionally concrete

I independently assessed root's suggestion `w0,t0,w1 / unchanged body / w2,t1,w3`; it is a new instrumentation-validity diagnostic, not a selected source experiment or another600ms/count retry. Keep CPU/QoS observations outsidew0..w3 and retain every raw timestamp. Define inner wall I=w2−w1, outer CPU T=t1−t0 and margins M=(w1−w0)+(w3−w2). If timestamp sample instants lie within their calls and the clocks/accounting have justified error terms, all extra boundary CPU B is within[0,M]. Then inner CPU C is within[max(0,T−M),min(T,I)], and off-CPU S within[I−T,I−T+M] intersect[0,I]. Call-completion latency is covered by the outer wall brackets; preemption in those margins makes the bound wider and the result potentially inconclusive, never an excluded row.

Sum the row-wise C lower/upper bounds by ABBA side. For positive denominators the contrast interval is[C_B_low/C_A_high−1,C_B_high/C_A_low−1]. Only an interval wholly outside±1% conditionally excludes the stable-inner-CPU/descheduling-only explanation at that block; overlap is inconclusive, not proof. Extend these bounds conservatively for timestamp and CPU-accounting uncertainty first. `clock_getres` supplies nominal resolution; it does not establish accuracy or accounting-lag bounds. Empty brackets measure that control's distribution rather than a guaranteed worst-case workload overhead. Bad/inconsistent or too-wide bounds must yield INCONCLUSIVE with no retry/filter.

This is narrow enough for a separately published harness/design review: fixed empty and work controls, inspected actual read ordering, explicit error assumptions, budgets and inconclusive rules before any native authorization. It cannot requalify a future candidate or all101 guards through a two-primary pilot. No new native work is queued or authorized by C. Prior012 already recorded clock inflation/endpoints without causal claims;017 selectedNONE for a resident-process method because fixture lifecycle/context and guard transfer were unresolved; EXP-009 already lengthened target windows to600ms. Neither resident-process repetition nor further count inflation follows from this analysis.

## Actual CPU-perf consultation and limits

My own tool-catalog discovery found zero directly exposed CPU-perf tools. I copied the authorized stdio client into a unique ignored directory, connected to cpu-perf0.1.1 with offline package resolution and auto-index/update disabled, discovered the catalog, checked library_status, asked the actual nested-clock question and read the linked clock manual. A material bracket-design follow-up used ask and check_evidence. The server was reaped after each retrieval session; no native measurement lease or benchmark overlapped. Server library was bundled revisiondeb5a0bac467, initially0/287 sources/0passages, later2/287/84passages. Root's separate consultation was also consumed and is explicitly labelled shared, never my calls.

Own ask initially reported unrecognised pasted output and no source passages. The [Linux manual](https://man7.org/linux/man-pages/man2/clock_gettime.2.html) explicitly says the thread clock “measures CPU time consumed by this thread”; this is conceptual Linux documentation, **not** evidence of Darwin implementation accuracy/resolution. Shared root retrieved [LLVM benchmarking guidance](https://llvm.org/docs/Benchmarking.html), which cautions “low noise is required, but not sufficient.” Its Linux controls are not automatically an Apple recipe. The later retrieved Coz passage does not establish these timer bounds and is not cited as support; bracket algebra is my conditional deduction from the source ordering.

check_evidence returned a heuristic drop_number verdict, partly misreading compact context and correctly warning of unmeasured frequency/microarchitecture. I preserve that response hash and do not claim a portable speed figure or complete machine control. Our forensic raw observations remain visible under the user's all-row rule with unknowns explicit: one lookup thread/process, actual placement uncontrolled; AppleM6/macOS, microarchitecture and frequency/DVFS residency unestablished; AppleClang21/C11/O3/g/strict warnings/frame-pointer/noLTO; public hit lookup16-byte keys,100K/1M, frozen counts13,834,448/4,978,427; identical native baseline; six serial process-level ABBA blocks per size and exact integer gates. No M4/other-host MCP benchmark number is transferred.

C.json publicly embeds exact tool call inputs/UTC intervals/response hashes (without source bodies), distinguishing own/shared. Full source bodies and private client/server logs stay ignored, referenced by generic paths and hashes. Actual own calls:

- 2026-10-19T11:34:43.048069+00:00 — initialize; response SHA256 `94f9e6263ec985723193fbc586aa2d74d483edbcfca236463cba43f2d14e8ec1`.
- 2026-10-19T11:34:43.438438+00:00 — tools/list; response SHA256 `8b6c76b96502db52f8a2b29f5b604cb515664e75c19b11731a9acd96d2ea56c1`.
- 2026-10-19T11:34:43.439560+00:00 — library_status; response SHA256 `717d9fb7c3d739ca4d7043e7f6a87d35c8841d73aa428edca3fe27807b5576d0`.
- 2026-10-19T11:34:49.690154+00:00 — initialize; response SHA256 `94f9e6263ec985723193fbc586aa2d74d483edbcfca236463cba43f2d14e8ec1`.
- 2026-10-19T11:34:50.090570+00:00 — library_status; response SHA256 `908114e38b8178e4cd3561795f4fd720ee4e4d57cdac4f8f7da2ee06874a5253`.
- 2026-10-19T11:34:50.092586+00:00 — ask; response SHA256 `5d59c61da31eefad83def25d73735751a3bd74e38bd343a26a1dbca2d6f2ea17`.
- 2026-10-19T11:34:50.105323+00:00 — read_source; response SHA256 `e804b096b0c6bf1ae39cf1b60394ebdbf95ff362309de52d7ebe721311de76b3`.
- 2026-10-19T11:38:37.019247+00:00 — initialize; response SHA256 `94f9e6263ec985723193fbc586aa2d74d483edbcfca236463cba43f2d14e8ec1`.
- 2026-10-19T11:38:37.419214+00:00 — ask; response SHA256 `58e342c0bf87b712fdc2a6be34b25603fc7e411cf39e467d5d3cc8ff39983334`.
- 2026-10-19T11:38:37.441549+00:00 — check_evidence; response SHA256 `767dca17e874408111f1d093faaaf85040d73416af8284a7e59f02e292022a88`.

Participant `/root/followup_proposal_c`, Codex/GPT-6 family; exact serving model/token/currency cost unknown. Prior EXP-009 harness/decision reviewer disclosed; this diagnostic is independent from root's analysis and peer reviews, but is not a source proposal/implementation population or candidate confirmation. Source NONE, original wall gates/PARK, all failure history and raw evidence remain unchanged. Only C.md/C.json/analyze-c.py plus the explicitly allowed private consultation directory were written. All activity stopped; no native work queued.
