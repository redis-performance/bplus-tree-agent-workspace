# Native ARM fallback correctness

The unchanged C patch fromd1921d793 was applied to exact baseline8fab511e in an isolated build on the assigned ARM runner. Native architecture reportsaarch64; Clang18.1.3. No SSE2 or forced-fallback flag was defined, so the original portable path was selected naturally. Final source hash matches the immutable C manifest.

Native-O3 and ASan/UBSan-O1 both pass the unchanged all-match guard oracle:297,984 checks,78,376 positions,3,072 zero spans, digestf04089fc9f619605. Both builds also pass43 original upstream tests. Every command ran serially onCPU2 through the lease-aware bounded helper; job completed in14.1seconds within300seconds. No performance comparison was run. This adds native little-endian ARM correctness evidence; it does not establish big-endian behavior or an ARM speedup.
