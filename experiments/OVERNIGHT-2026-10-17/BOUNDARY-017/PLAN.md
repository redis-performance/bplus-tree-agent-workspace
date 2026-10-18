# BOUNDARY-017 — compact index storage boundaries

Additive oracle, preregistered before builds. Exhaust all legal narrow storage IDs
0..65534 plus deleted sentinel, and wide IDs0..65535 plus selected32-bit edges,
in each of8slots under both bucket widths. Independent byte-buffer reference
checks the entire four-bucket allocation and surrounding canaries after each store;
verify decoded ID, untouched tags/filter/adjacent IDs and runtime bucket stride.
Also exercise tag writes at every slot for all256 bytevalues and scalar tag-mask
coverage across eachquery/pivot/adjacent-byte pattern, permitting documented borrow
falsepositives but requiring every realmatch and correct first-candidate order.

Control and retained EXP-004A/B/C isolated snapshots, release/debug andASan/UBSan.
Same baseline/referee/allocator; source included only to access private primitives,
not for timing. All eight cells must pass and deterministic digest must agree.
Two isolated sanitizer sensitivity faults: narrow deleted sentinel decoded as a live
ID; tag update clears its adjacent tag. Existing tests unchanged. No NaN API input,
no speedclaim or sourcecandidate. Preserve all failures and patches. Child120s,
whole validation400s; no concurrent measurements. Backend/model/costunknown;
sequential review. New suite counts only after full validation and fault detection.
