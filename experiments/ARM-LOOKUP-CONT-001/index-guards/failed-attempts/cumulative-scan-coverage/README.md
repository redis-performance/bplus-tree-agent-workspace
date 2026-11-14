# Retained verification-oracle weakness

The first288 correctness cells and cross-binary comparisons passed, with no candidate failure. Manual review found that a cumulative callback histogram threshold (`seen[id] >= walk_number`) did not prove every individual walk returned each member: legal duplicate callbacks from an earlier walk could conceal a missing member in a later walk. That was a harness coverage defect, not a source-candidate defect or measured regression.

The corrected verification branch snapshots counts before each walk and requires every member's count to increase. The snapshot/check is verification only and calls no tree API. The affected referee was rebuilt and the correctness matrix rerun. This directory preserves the earlier source, completion summary, oracle result and binary manifest. No timing was performed with either version.
