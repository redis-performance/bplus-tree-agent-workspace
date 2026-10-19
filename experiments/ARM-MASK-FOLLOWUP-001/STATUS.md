# ARM mask follow-up status

**PARK; fixed original-operation diagnostic comparison granted.** Fresh primary gain
remains −7.78% / −7.21% elapsed, but only 18 of 29 required original controls qualify.
Eleven fail the ±1% precision gate; none of those is below 10ms. All 11 prospectively
declared diagnostics have short windows. Root and Intel audits agree. Held-out
confirmation is ineligible. The fixed 120-process comparison may run once under 600s;
unqualified cases cannot establish a calibrated gain or regression. Source NONE.
ARM lease remains active; hard handback at 10:15 UTC / 11:15 Lisbon. [Results](RESULTS.md).
New user authorization supersedes the completed overnight lease for this ARM-only
follow-up. Intel and AMD hosts remain released.

- Same exact historical EXP-005 A, corrected source `13e459ff8`; source adoption NONE.
- Plan `b56bf0cac`: 82 required iterator guards plus 29 required original-operation
  cases, with 11 prospectively declared diagnostics. Qualified diagnostic losses block progression under the frozen rules; no post-result waivers.
- Fresh primary seeds 1101–1103; independent confirmation 1201–1203; guards 1301–1303;
  matched profiles 1401–1403; correctness 1501/1502. Old A/A does not transfer.
- AMD semantic review `1832e20fc` finds no exact-patch semantic blocker; correctness execution reviewed at `d17da59d9`. Uniform identical-bit width-zero performance is not measured
  by the existing alternating signed-zero fixture and remains an explicit gap.
- ARM prepares executable drivers and freezes; Intel prepares independent confirmation.
  Each phase needs root review/grant and must fit the unchanged lease deadline.

[Activity](ACTIVITY.md) · [Plan](README.md) · [Lease acquisition](LEASE-ACQUISITION.json).
