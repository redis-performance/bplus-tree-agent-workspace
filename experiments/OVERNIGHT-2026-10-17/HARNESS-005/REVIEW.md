# Sequential adversarial design review

Independent reviewer failed startup; no agent work or independent confirmation claimed.

Alternating +/-0 scores compare numerically equal, so member order must be lexical.
New big-endian keys solve the prior little-endian model mismatch above ID255; old
encodings keep prior byte fixtures. Exact bit checks prevent accidental +0/-0 collapse.
The full oracle sees every member/length/score, and iterator-copy state checks cover
mask0 even when no outputs are requested. Two exhaustion calls must preserve sentinels.

A plain sum of raw sign bits cancels for an even count of negative zeros; folding
high bits into low32 preserves a contribution from every negative zero in the fixed
sizes/counts. This is not a collision-free hash; full ordered comparison remains the
correctness oracle outside timing. Timed checksum changes require new qualification.

Construction only changes insertion permutation before timing. Fingerprints record
that order; identical fixtures must reproduce them. Reported memory equality is within
the same binary/allocator; do not compare ASan usable sizes to native usable sizes.
All original numerical limits1..100m stay enforced. On this64bit host size*bytes/rounded
traversal counts fit size_t; enormous allowed allocations remain impractical, not tested.

Boundary CPU observations and thread/wall ratios cannot establish no in-window migration,
stable frequency, effective QoS or isolated-machine execution. Frequency unknown.
Default workload code generation may change from checksum folding; old/new timing
cannot be pooled. New fixtures add coverage; they never remove the old mask6 guard.
