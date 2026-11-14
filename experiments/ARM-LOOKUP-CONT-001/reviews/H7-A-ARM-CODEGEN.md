# H7-A independent ARM emitted-code audit

Role: execution-owner review, independent of candidate implementation. Read-only audit of actual saved ARM ELF bytes and complete disassembly; no workload execution or performance measurement.

**STATIC REJECT / NONE.** The target general raw frame grows from176 to192 bytes, violating the frozen frame gate. No timing follows.

| Artifact | ELF SHA-256 | Verified instruction words |
|---|---|---:|
|baseline-native|`2eb912b89e950ff00f5d08bb6b1b4d0393b111e1797114f183a13dbbc655afbf`|20264|
|baseline-lto|`77cab5362267de71388a294683e5b8d16bf2a0c599b9ef1313c870d669e39abb`|12025|
|H7-native|`d98799e206395c37949ef90515585d00673ef941ab1351687b90d7dfa991cfdb`|20160|
|H7-lto|`677b438f8f44a2cb315a3b2a2a0ab91aa34c8bbc81ea8607045fb8ad725484ac`|11969|

Every four-byte instruction word in the complete saved disassembly was compared with the corresponding PT_LOAD bytes of its actual ELF. All words match. Candidate and baseline hashes match retained build metadata. This establishes the emitted-code identity; it does not measure instructions retired.

| Cohort / function | Entry instruction | Frame bytes |
|---|---|---:|
|native / `zbtScoreLeafFindMember.constprop.0`|`3714:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|native / `zbtScoreLeafFindMember`|`38a0:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|native / `zbtreeScoreRaw`|`c1c0:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|
|native / `zbtreeScoreRawWithHash`|`c9c4:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|
|lto / `zbtScoreLeafFindMember`|`404bc0:	a9b87bfd 	stp	x29, x30, [sp, #-128]!`|128|
|lto / `zbtreeScoreRaw`|`405f20:	a9b47bfd 	stp	x29, x30, [sp, #-192]!`|192|
|lto / `zbtreeScoreRaw.constprop.0`|`4067c0:	a9b57bfd 	stp	x29, x30, [sp, #-176]!`|176|

The target general `zbtreeScoreRaw` entry405f20 allocates192 bytes versus baseline176. Its no-score clone4067c0 remains176; both native raw entries remain176. The [frozen selection](../H7-selection.md) rejects any raw-frame growth. This is sufficient to reject A without a latency trial, regardless of intended exact-mask instruction savings.

ARM Frontend_Bound, Bad_Speculation, Backend_Bound, Retiring and children remain unavailable: no qualified candidate pipeline-slot profile exists. Static word counts and frame inspection do not replace these metrics. The controller consultation and its limited retrieved material are recorded in the population selection; this audit makes no new consultation or causal attribution.
