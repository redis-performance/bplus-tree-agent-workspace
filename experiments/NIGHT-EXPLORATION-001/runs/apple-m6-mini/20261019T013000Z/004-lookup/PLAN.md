# M6 LOOKUP-001 — public independent queries

Frozen before observations, round 3, 2026-10-19. Baseline source HEAD 25a44adc;
exact file hashes in freeze.json after builds. Launcher Apple M6 metadata is the
host authority; direct sysctl remains unavailable and is not retried. Compiler
Apple Clang21 C11 -O3 -g -Wall -Wextra -fno-omit-frame-pointer, no LTO, standard
allocator/SipHash/assertions. O1 ASan/UBSan is correctness only. No source adoption.

Reuse the cached M1 lookup referee at 4c48fa7ed2d8cf4f1144626276bfb2a602c63bf9,
with explicit origin/hash and local changes in harness-origin.json. This is cached
published context, not a fresh remote observation. M1/M6 measurements stay separate.
EXP-006 C/PARK and single-lane regression reviewed before proposing.

1. Validate public hit/miss at five sizes, seeds1/2; boundary member lengths
   8/16/319/320/321/1024 at 1K, plus invalid input and deliberate result faults.
   Reuse launcher original native/sanitizer tests without rerunning the inventory.
2. Separate instrumented source: hit/miss 10K/100K/1M, seeds1/2, 100K queries;
   count index candidates, leaf calls, tag candidates, full comparisons, memchr
   invocations/requested bytes, first-match distance and leaf cardinality histogram.
   Instrumented elapsed times are excluded. No hardware counter interpretation.
3. Two sampler controls; six public timed-loop profiles with 10M queries each,
   requested 1000us SIGPROF cadence. PC counts identify regions, not time fractions.
   No external attach retry. Release leaf-search and public-lookup assembly retained.
4. Baseline only: three 200K-query observations per size/hit-miss cell. Freeze ops
   using fastest positive ns/op, target50ms/cap100M. A/A6 ABBA blocks at100K/1M hit,
   seeds1/2/3 repeated. No compilation/test/profile overlap. Total timing cap300s.
5. Three sequential proposal passes/chair after profiles, not independent agents.
   A distinct mechanism must explain why it avoids EXP-006's single-lane losses.
   NONE ends this target without an invented implementation population. Otherwise
   freeze the hypothesis, three isolated implementations and full shared gates.

Public hit100K and1M are dual primaries. All shared LOOKUP-001 guards remain required
for adoption: hit/miss/mixed five sizes, lengths8/16/319/320/321/1024 at100K,
batch1/16 at10K, collisions/bounded reads/first match/resize/ownership/memory.
Primary-only evidence can reject, never accept. No repeated failed A/A schedule.
Exact serving model/token cost unknown; visible backend Codex/GPT-6 family.
