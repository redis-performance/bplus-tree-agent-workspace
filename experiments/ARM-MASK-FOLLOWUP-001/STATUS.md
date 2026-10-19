# ARM mask follow-up status

**ACTIVE lease; correctness validation running.** Started 08:27:44 UTC under the
reviewed 600s cap. ARM OSS coordinator remains stopped; automatic restoration is
armed for 10:15 UTC / 11:15 Lisbon. No performance benchmark launched.
New user authorization supersedes the completed overnight lease for this ARM-only
follow-up. Intel and AMD hosts remain released.

- Same exact historical EXP-005 A, corrected source `13e459ff8`; source adoption NONE.
- Plan `b56bf0cac`: 82 required iterator guards plus 29 required original-operation
  cases, with 11 prospectively declared diagnostics. Independent review is tightening
  qualified diagnostic-loss handling before execution freeze; no post-result waivers.
- Fresh primary seeds 1101–1103; independent confirmation 1201–1203; guards 1301–1303;
  matched profiles 1401–1403; correctness 1501/1502. Old A/A does not transfer.
- AMD semantic review `1832e20fc` finds no exact-patch semantic blocker; execution
  review remains pending. Uniform identical-bit width-zero performance is not measured
  by the existing alternating signed-zero fixture and remains an explicit gap.
- ARM prepares executable drivers and freezes; Intel prepares independent confirmation.
  Each phase needs root review/grant and must fit the unchanged lease deadline.

[Activity](ACTIVITY.md) · [Plan](README.md) · [Lease acquisition](LEASE-ACQUISITION.json).
