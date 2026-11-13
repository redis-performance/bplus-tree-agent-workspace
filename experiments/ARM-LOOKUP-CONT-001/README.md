# ARM lookup continuation

**STARTED.** The user requested broader continued optimization after ARM-LOOKUP-GAP-001 rejected one small arithmetic change. That experiment remains sealed. Current upstream unstable is `ee8e7f70152404649ac947157fd662d11b4a00d5`, freshly fetched for this continuation.

Three independent investigations are active:

1. Helper boundaries and existence-only specialization, including the earlier inline-helper lead and explicit compiler/LTO transfer controls.
2. Leaf tag and short-record work, first resolving the unknown libc PCs against the exact captured ELF/build ID.
3. Index-to-record dependencies and repeated leaf metadata computation, with allocation/mutation costs kept explicit.

These are distinct tracks, not three spellings of the rejected arithmetic change. Each selected hypothesis will receive separate implementations, frozen correctness/referee checks, fresh fleet A/A and serial ABBA comparisons. Failure of one track advances to the next supported track. A passing candidate still needs fresh confirmation, matched profiles, Intel guards and independent review. No accepted result or speedup is claimed yet.

All performance measurements run on freshly reserved fleet hardware with bounded cleanup. No active reservation or measurement existed at this STARTED checkpoint. No upstream Redis PR/comment is authorized. Sanitized progress and results will be published to this repository's main branch.

## TMA classification

Frontend_Bound, Bad_Speculation, Backend_Bound and Retiring are unavailable for this new experiment's baseline and candidates. The previous CPU-wide capture remains exploratory; it cannot supply a validated process classification here. Actual collector scope, affinity and collection quality must accompany new captures.
