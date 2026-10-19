# Lookup and batch referee preparation

PASS: both new frontends compile in native and ASan/UBSan modes with
`-Wall -Wextra -Werror`. Baseline validation retains 102 passing semantic process
rows, 42 passing invalid-argument runs, and six detected fault-control runs.
This is bounded semantic validation, with no comparative speed claim or profile.
All experimental child processes have finished.

Participant `/root/followup_proposal_b`, actual independent agent. Visible backend
is inherited Codex/GPT-6 family; exact serving model, measured token usage and
monetary cost are unknown. Only the assigned new frontend/evidence files and
ignored `scratch/m6-caller/harness-lookup` were written. Shared source, old
referees, variants, Git and shared memory were not changed.

`lookup.c` copies frozen `004-lookup/lookup-bench.c`, preserving its independent
construction/query permutations, binary members, hash seed, original hit/miss
checks, checksum consumption, observations and cleanup. It adds `lookup-mixed`
as a deterministic alternating stream: operation0 hits, operation1 misses, and so
on. A hit queries `query_order[i % n]`; a miss queries the corresponding absent
key at offset+n. Warmup executes the selected actual case and checks every returned
presence/result. Mixed timed work checks the full presence/score value and sums
`score+1` for hits; its expected checksum is computed independently before timing.
Existing hit checksums remain sums of scores and miss checksums remain zero.
An additional complete exact hit/miss scan validates all members after timing.
The optional sampler include moves to the correct new relative location.

`batch.c` reconstructs the added `bench/batch_lookup.c` from corrected
`HARNESS-007/attempt-002/harness.patch`. It retains that frontend's public
`zbtreeScores` call, complete found-mask checks, exact warmup lane values,
outside-count canaries, expected checksum/hit/API-call checks, full final
hit/miss validation, independent query fingerprint and owned-memory stability
assertions. New changes add the uniform `--case lookup-*` alias, report the
uniform case name, bound size to1M, and restrict batch size to1 or16. The original
`--layout hit|miss|mixed` alias remains accepted. No original check was removed.

Both accept:

```
--case lookup-hit|lookup-miss|lookup-mixed
--size N --ops N --seed N --member-bytes N --warmup-passes N
```

Lookup sizes are1..1M, member bytes8..65536, operation count1..100M; numeric zero,
negative/invalid numeric arguments and unsupported cases are rejected. Batch
additionally accepts `--batch-size 1|16` and `--query-seed N`. Both report one CSV
row with `elapsed_ns`, `operations`, `ns_per_op`, `tree_bytes` and `checksum`.
Batch `operations` counts individual lanes; `api_calls=ceil(ops/batch_size)`.
The final call may be partial and its full mask/canaries remain checked.
Batch checksum sums score+1 for hit lanes, with misses contributing zero.

Construction and query seed diversity are separate. Lookup query seed derives
from `--seed` XOR a fixed constant, preserving the frozen independent permutation.
Batch construction uses `--seed`, while its independently shuffled query stream
uses explicit `--query-seed`, default2 as in the corrected historical frontend.
The baseline validation used seed1/query-seed2. A campaign can preregister
`--query-seed seed+1000` before freezing to vary both streams for held-out seeds;
changing construction seed alone does not change the batch query permutation.

Native and ASan/UBSan validation each ran:

- Lookup: hit/miss/mixed at all five sizes with16-byte members and2,003 operations;
  all six lengths8/16/319/320/321/1024 at size100 with17operations:33cells/build.
- Batch: size10K,16-byte members, hit/miss/mixed, batch1/16, and operation counts
  1/17/2003, covering partial batches:18cells/build.
- Lookup9 and batch12 invalid-argument cases/build, all exiting2.
- Deliberate lookup mixed-score corruption, batch missed-lane mask corruption,
  and batch mixed-score corruption, each detected by the intended unchanged
  presence or exact-value assertion in native and sanitizer builds.

Independent Python code reconstructs the query permutations and every one of
the102 reported checksums. All match; no elapsed values were compared. Four
extra strict-warning builds pass, for164 recorded build/run windows total.
`lookup-batch-validation.json` contains exact flags, equivalent workspace-relative
commands, return codes, timestamps, source/referee/binary and log hashes, semantic
rows and all six fault outcomes. Raw private-path output remains ignored scratch;
public logs and command paths are generic. The validation scripts and fault
patches are retained in `lookup-batch-logs/`.

An initial reporting-only audit failed because its public-path scanner matched
its own literal search marker. The split-marker correction and explanation are
retained. All102 checksum reconstructions had already passed; no experimental
row or semantic check was changed or rerun for this reporting correction.

Qualification and all candidate comparisons remain root's separate work. These
new referees require a common freeze and fresh same-session baseline controls.
