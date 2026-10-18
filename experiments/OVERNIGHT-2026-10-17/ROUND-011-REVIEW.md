# Round 11 adversarial review — sequential coordinator pass

Independent reviewer startup failed before execution (thread-store/no-rollout error).
This review is not an independent participant. Backend/model/token cost unknown;
supervisor usage remains separately recorded. No new source population is represented.

## Semantics and ownership

Main tree/header and previous snapshots stay unchanged. HARNESS-006 builds the tree as
a separate translation unit and uses public sentinel insert/minimum delete/clone APIs.
Sentinel is strictly below the first finite model score and distinct from fixture members;
it is removed before verification/timing and freed through the normal SDS adapter.
Existing full byte/order, exact score bits, absent-output sentinels, iterator-copy state,
exhaustion, effective counts/checksum and per-window memory checks remain. New histories
passed both build types and deliberate length/sign/state faults were caught.

Controlled allocator metadata is aligned with max_align_t; returned capacity is backed
by real payload storage, rounding arithmetic is checked, realloc preserves the smaller
capacity and SDS deallocation uses the matching wrapper. Unit tests cover full-capacity
writes/realloc/calloc/SDS lifetime. Metadata and libc slack are deliberately excluded
from diagnostic accounting. Thus controlled adapters CANNOT support optimization memory
claims or replace the native referee. Their role is a capacity intervention only.

## Measurement and interpretation

AA-011's initial analyser retained a stale200-traversal literal. The original files are
preserved; a separate corrected analyser uses the already preregistered ceil(20m/95)
count. No measurement rerun, row deletion, changed threshold or weaker invariant.
One compact guard qualifies jointly; seven do not. A/B passing this added guard cannot
repair the original unqualified mixed-output guard. C's interval crossing the regression
bound is uncertainty, not a proven regression or acceptance.

Longer warmup in DIAG-013 reduces absolute bias in three pairs but fails the all-four
precision condition. It is not adopted. Avoid calling it a frequency fix or selectively
using its one qualifying long-policy cell. Public CPU endpoints/QoS and thread clocks
cannot establish constant clock, effective QoS or no mid-window migration.

Profiles are interrupted-PC captures. The first matched set is representative-mode
coverage, not the exact timed mask; a separately planned exact-mask set addresses that
coverage gap without becoming independent timing confirmation. Signal bias/delivery
cadence remain uncertain; no cycle, cache, branch-predictor or portable-speed inference.

## Capacity explanation and portability

O1/O3 x native/sanitizer with fixed exact/rounded capacity distinguishes compiler level
from reported allocation capacity on the tested oracle. Orientation counters change under
capacity intervention, and selected traces show different compaction-threshold decisions.
Per-fixture layout hashes also include record positions: a differing hash alone does not
mean orientation changed. First divergence traces were selected after discovery, so they
are exploratory. Fresh seeds and n97/513 extend coverage, still sequential confirmation.

Allocators, compiler/instrumentation, address placement and metadata can interact. The
controlled-policy evidence does not establish a unique explanation for every conceivable
native/ASan difference. Do not compare native and ASan timing or owned bytes as equivalent
implementations. Architecture remains local M1; no M4 CPU IDs/frequency/results transferred.

## Decision boundary

ACCEPT remains unavailable: original broader guard precision, independent confirmation/
review and committed provenance are still missing. Source selection NONE; EXP-004 A/PARK,
EXP-005 PARK/NONE. All losing patches retained. No new population, source adoption,
publication, permission changes, git retries or supervisor/runtime/STOP modifications.
