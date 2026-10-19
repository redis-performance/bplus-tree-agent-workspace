# Fresh corrected-adapter iterator profile — preparation only

This is a new baseline PC profile under the corrected standalone adapter, before
any tree hypothesis. Source remains NONE. The original009profile is retained under
its original adapter; no samples/timings are pooled or subtracted. Preparation builds
binaries and runs eight bounded native/sanitizer checks. It never executes the profile
binary. Captures require the root's separate exclusive-runner ACK after B's plot and
C's raw-data audit finish.

Exact byte copies from009: iterator.c, microbench.c and apple-sampler-bridge.c.
The bridge continues including the unchanged002-rank/night-rank-sampler.h. No
profiler hook, target, adapter, hashing, allocator or assertion-policy source is
changed. Current target C/header are d9123c/496e72; corrected adapter hashes are fixed
in PLAN.json. Compiler flags match009: C11 -O3 -g -Wall -Wextra
-fno-omit-frame-pointer, no LTO. Sanitizers use O1/ASan/UBSan; profile adds only
PROFILE_SAMPLE and the unchanged bridge.

The fixed16capture cells are100K/1M × four contracts (integer full forward/reverse,
integer score-only forward, fractional full forward) × seeds1/2. Each requests100M
items,16-byte binary members,3actual-contract warmup traversals and1000us requested
sample interval. Every capture retains the fixed25-PC sufficiency criterion. Sparse
captures remain insufficient; no duration/count/threshold retuning or retry occurs.
Raw counts are diagnostic PCs, not unbiased time shares, cycles, cache misses,
frequency, core residency or a performance effect. All emitted frontend times are
explicitly unused. These ordinary contracts do not establish physically reversed-
leaf or broad packed-width coverage.

The byte-identical PROFILE_SAMPLE hooks retain009boundaries: setup/warmup/full
verification are outside; QoS/CPU/thread-clock observations around the traversal
remain inside. No external profiler attachment or permission change is attempted.
Existing known-work sampler controls are read/pinned rather than repeated; their
unchanged sampler text is reused, not relabeled as a fresh corrected-adapter control.

Preparation checks all four contracts n1000/ops2003/seed1/warmup1 in native and
ASan/UBSan builds: eight processes,3000visited items each. Original43-test evidence
is reused only when target/header/adapter/vendor/test input hashes match the corrected
baseline evidence in012/011. Referee member/order/score bits, copy/next-state,
nullable-output/end, checksum/count and memory checks remain unchanged.

run.py prepare writes a freeze over source/header/support/referee/bridge/sampler,
flags/plan/driver/docs/planned-command inputs and all three binaries before capture.
Separate builds/raw logs stay under scratch/m6-corrected-iterator-profile. Commands
and hashes are public with generic paths; absolute runtime PCs stay in private raw
logs. Public bins contain module/symbol-relative offsets only; unresolved symbol
starts produce null offsets, never absolute-address substitutes.

After preparation, only root may authorize captures with an ACK containing:

```
{
  "status": "authorized",
  "authorized_action": "captures",
  "exclusive_runner": true,
  "other_work_idle": true,
  "freeze_sha256": "exact final freeze hash",
  "driver_sha256": "exact final run.py hash",
  "plan_sha256": "exact final PLAN.json hash"
}
```

The ACK attests B/C work has finished and all other work is idle. It is an internal
runner gate, not an additional user permission request. The driver checks identities
before/after each capture and uses a process-group timeout bounded by120s, remaining
900s capture-phase wall budget and07:15UTCreporting cutoff. It retains failed/partial
output, reaps children and marks the phase incomplete. No capture resume/retry exists.

From repository root:

```
python3 <013-corrected-iterator-profile>/run.py prepare
# Only after matching root exclusive-runner ACK:
python3 <013-corrected-iterator-profile>/run.py captures --ack <root-ack.json>
```

The planned sixteen commands are frozen in planned-commands.json. Native/sanitizer
checks are not baseline timing results. Any subsequent hypothesis/populations, full
performance guards, qualified comparisons and review remain separate. Participant
/root/followup_proposal_a, inherited GPT-6/Codex family; exact serving model/token/
currency cost unknown. No Git/shared-status/target edit or new agent is performed.
