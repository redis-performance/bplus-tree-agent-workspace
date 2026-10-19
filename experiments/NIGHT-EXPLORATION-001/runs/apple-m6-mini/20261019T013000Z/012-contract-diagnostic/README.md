# Matched panic-contract iterator diagnostic — preparation only

This is a harness/adapter diagnostic. It compares the original returning declaration
of an always-aborting panic function with its truthful C11 `_Noreturn` declaration
and definition. It is not a B+ tree candidate, optimization population or acceptance.
No measured phase is authorized by preparation alone. All historical evidence stays
under its original adapter identity; no historical timing subtraction is used.

The target C/header stay exactly d9123c8236ce48f6442dd9f9a60a0de38a012dd2d764240aba895a598bd9afe2 /
496e72ff9dacb26793c64ba8794e2943dc9b678a8476cc1ae99d36d2b1d87a83.
`iterator.c` and `microbench.c` are byte-identical copies from 009. The source tree,
referee semantics, SipHash, libc allocator and assertion evaluation are unchanged.
The only compared inputs are the immutable old adapter under
`worktrees/m6-caller-control/compat` and the corrected current root `compat`.

Both binaries compile the same `src/zset_btree.c` relative path. Identical
`-ffile-prefix-map` and `-fdebug-prefix-map` options normalize the old adapter source
prefix to `compat`, and `-fdebug-compilation-dir=.` avoids a private compilation
directory. Preparation checks that their panic filename literals match, including
`src/zset_btree.c`, rather than comparing accidental source-path differences.
Flags are C11, O3, `-g -Wall -Wextra -Werror -fno-omit-frame-pointer`, with no LTO.
Native/sanitizer correctness builds use the same assertion policy; sanitizers use O1
and `-fsanitize=address,undefined -fno-sanitize-recover=all`.

The eight cells are 100K and 1M members crossed with integer full output forward,
integer full output reverse, integer score only forward, and fractional full output
forward. Full output is mask7 (pointer/length/score); score only is mask4. Every
measured child requests exactly 100 million items, 16-byte binary members, and
three actual-contract warmup traversals. Counts are fixed before observations.
Six process-level ABBA blocks use seeds1/2/3 twice. Cell order rotates each block;
the first adapter alternates between blocks.

Preparation runs four contracts at size1000/requested2003/seed1/warmup1 on each
adapter in native and ASan/UBSan builds: 16 bounded correctness runs, each rounding
to 3000 visited items. All frozen member/order/score-bit/iterator-copy/exhaustion,
checksum/count and owned-memory checks remain. Existing original43-test native and
sanitizer evidence is reused only after source/header/adapter/vendor/test hashes
match 004's frozen original baseline, 010's reviewed private identities, and 011's
corrected baseline. `reused-tests.json` records those evidence identities.

After root and independent driver review plus publication ACK, phase1 measures
both adapters separately against themselves: 2×8×6×4 =384 processes. Phase2 measures
old(A)/new(B): 8×6×4 =192 processes. The phases are strictly serial on an otherwise
idle runner, with no concurrent agents, builds, tests, profiles or publication.
Phase2 is preregistered even if A/A is noisy, because this is a harness diagnostic.

Each phase has 300 seconds of summed timed work and 900 seconds of wall time.
Each child is limited to the minimum of 120 seconds, remaining phase wall time,
remaining timed budget treated conservatively as a child wall bound, and the
absolute **04:45 UTC** stop. Completed rows are retained before post-child
budget checks. A timeout kills/reaps the process group, preserves partial output,
and marks the phase incomplete with unknown timed work for that child. No phase
retry, outlier removal, count retuning or silent row exclusion is allowed.

Every measurement verifies frozen source/binary identities before and after the
child, then checks CSV case/size/seed/ops/traversals/length/mask/direction/encoding,
warmup count, expected checksum and owned bytes. Raw stdout/stderr, process UTC
bounds, hashes, timeout and return status are retained. Six-block effects use
`100*(mean inner B ns/item / mean outer A ns/item - 1)`; negative means less elapsed
time. Each adapter/cell A/A qualifies only if all effects lie within ±1% and every
window is at least10ms. Comparison effects remain conditional unless BOTH adapters'
same-cell controls qualify and comparison windows also meet the 10ms minimum.
Each ABBA block must have identical operation counts, checksums, construction
fingerprints and exact tree-owned bytes. No source-optimization acceptance follows from any
result, including a large matched adapter effect.

Prepare from the repository root:

```
python3 experiments/NIGHT-EXPLORATION-001/runs/apple-m6-mini/20261019T013000Z/012-contract-diagnostic/driver.py prepare
```

Root must then review/publish the exact freeze with an independent reviewer and
create an authorization JSON containing:

```
{
  "status": "authorized",
  "freeze_sha256": "exact freeze.json hash",
  "driver_sha256": "exact driver.py hash",
  "plan_sha256": "exact PLAN.json hash",
  "reviews": [
    {"reviewer": "/root", "status": "PASS"},
    {"reviewer": "actual independent reviewer identity", "status": "PASS"}
  ],
  "published_commit": "full 40-character published Git commit",
  "exclusive_runner": true,
  "authorized_phases": ["aa", "compare"]
}
```

The ACK asserts that reviews and publication completed and all other work is idle.
The driver verifies its hashes and identities; it does not discover remote access
or publish Git state. Only root may launch the measured phases after the ACK:

```
python3 <campaign>/012-contract-diagnostic/driver.py aa --ack <authorization.json>
python3 <campaign>/012-contract-diagnostic/driver.py compare --ack <authorization.json>
```

Participant `/root/followup_proposal_b`, inherited Codex/GPT-6 family; exact serving
model, measured token usage and monetary cost unknown. Preparation makes no speed
claim and performs no target edit, Git write, shared-memory change or agent spawn.

Preparation notes: 011's manifest omits `tests/upstream.c`, so that specifically
omitted identity is taken from 010's exact reviewed snapshot; all compiled inputs
still require their original baseline/011 hashes. The initial metadata KeyError
occurred before any child and is preserved in `build-logs/prepare-attempt001.failure.json`.
Six synthetic driver checks cover timeout, interruption, process-exit races,
short windows, exact memory and fixture-fingerprint rejection. Their three short
Python child processes are protocol controls, not benchmark measurements.

Synthetic cleanup commands initially recorded an absolute interpreter path.
The original command journal is retained privately with its hash; public command
metadata uses `python3` and the executable hash. Future invocations preserve exact
original commands privately and publish generic executable identities. No benchmark
data or flags changed. `public-metadata-curation.json` records the correction.
The first preparation freeze is retained as `freeze-pre-review.json`; the final
freeze is resealed after driver-review refinements, with the same four validated
binaries and no measured phase started.
