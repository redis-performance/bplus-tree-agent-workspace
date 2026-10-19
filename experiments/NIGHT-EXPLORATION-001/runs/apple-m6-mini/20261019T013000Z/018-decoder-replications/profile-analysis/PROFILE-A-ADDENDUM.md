# Selected EXP-007 A profile — separate addendum

The fixed selected-A capture passes its read-only audit: sampler and child returned
zero, and root's owner metadata records the driver reaped, owned group empty and
exclusive release safe. Its exact binary hash matches the native build/freeze:
`95cb988bffbfbd4312d71be221d16261175e3dae5edcc72532026dceccb0e95a`.
All source/referee and raw capture identities verify. The original three-capture
report and audit script are preserved unchanged.

All **776 stack-root observations** have exclusive leaves in `decoder_batch`.
A's range decoder is inlined there alongside the round/leaf loop, output
materialization and checksum consumption. This supports that the intended decoder
region was captured; collapsed symbol/offset records do not isolate the cost of
its individual operations. No setup-only leaf was observed, which does not imply
zero setup cost. The profile boundary still includes setup, warmup, work and output.

The 64 CSV rows retain the exact count96/width60/eight-leaf/65536-round/seed81031
fixture and checksum metadata of the earlier EXP-007 base/B profile workloads.
All profile timing fields remain excluded from discovery and confirmation.
The count of captured locations is not a cycle, latency, speed or independent
source-line cost estimate; it cannot qualify a comparative mechanism or tree gain.

PROFILE-A-ADDENDUM.json contains commands and raw/source/binary/owner hashes.
Raw sample text and sampling JSON remain private. No build, test, timing or profile
was rerun. Participant /root/followup_proposal_b; exact model/token/cost unknown.
