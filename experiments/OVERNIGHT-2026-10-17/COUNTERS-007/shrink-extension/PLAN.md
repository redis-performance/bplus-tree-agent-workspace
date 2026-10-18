# Separate shrinking-resize branch capture

Preregistered after8cell correctness passes, before capture. One baseline whole-oracle
coverage run of BOUNDARY-019/shrink-extension, its existing fixed four fixtures,
-O1 debug LLVM instrumentation, child120s. No source/callback changes. Same capture
method as the prior three, which remain immutable. Require source-semantic PASS;
report EOF/nonvalid cursor branch and NULL fallback separately from freed-ID branch.
Expected public sentinel state observed in the oracle is not itself proof of branch
execution; inspect exported true/false counts. No timeprofile, timings, speedclaim
or unreachability proof. Rawprofiles local with hashes, curated mappedbranches.
