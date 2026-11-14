# Portability operational revision2 review

**SOURCE REVIEW PASS; eligible for input staging.** Actual successful staging, a separately bound image-preparation review, and later image/tool receipt review remain required before their respective operations. No guest correctness or performance result exists; H2 remains PARK.

The reviewer independently rehashed all50 manifest entries, verified that all44 entries of the previous frozen packet and its manifest remain unchanged, and recomputed `driver.diff` exactly. All original C sources, shell wrappers, oracles, fixtures, counts and build flags are reused unchanged. The actual revised operational record preserves every field of the previous record, including the original task interval ending05:24:45.781 UTC; only topology/provenance and supersession fields are added. Offline record-schema validation passed.

R2 checks CPU2 online, its exposed sibling list exactly2, and CPU50 offline. It does not accept both possible sibling lists. The original reservation source explicitly asserted the pair2,50 before offlining50; that is historical controller provenance, separate from the currently observed offline topology. The prior incorrect census-branch citation is not used. The task timestamps are now exact constants, preventing a renewed budget.

New phase paths preserve the consumed image-preparation001 failure and every original artifact. A complete successful staging receipt must bind exact root, r2 manifest, revised operational record and every file/hash, with no failed files. The driver checks that receipt before constructing its runner or invoking Docker and rehashes it with later identity checks. Its single-use phase claim may occur before that validation; failure still consumes the new claim. The separate image launcher checks the receipt before driver import, phase claim or any subprocess. This distinction is explicit and preserves the intended no-work boundary.

The frozen26-test Python driver suite and two synthetic launcher negatives passed independently. The negatives prove missing/failed staging makes no subprocess call or phase directory; static control flow also places the gate before import. No guest, Docker, shell wrapper, source build, timing or profiling ran during this review. The earlier controller sequencing error is addressed by an executable dependency gate, not merely an instruction to stop after staging failure.

| Artifact | SHA-256 |
| --- | --- |
| R2 manifest | `c5d51e2d2f7ffdd9b49b7cac263c6d6b5a7b52bf53dc17c852daa11d316d33f1` |
| R2 driver | `89b29ab43722c80553c09e3670719ebb26fe0d76c2c02f7c625deab5aa3ebf90` |
| R2 protocol | `504704de7f715fcf916f9c721516cfdc699bfda5171832447e29166ef4abc9fb` |
| R2 operational record | `66c805dc8eaa4f6f168a09aca177d5d6df2e81c9ea17d0a22e7d7aeeab63ed98` |
| Reviewed launcher at source gate | `d66f2103f190b0afcfd9bedc87c49aebca750bd36891a4ab56fab16d59876e23` |

The launcher otherwise preserves exact container identity/name/labels/base, absolute in-container deadline, immutable commit/remove checks and cleanup obligations from the previous review. Its final operational approval must bind the actual successful staging receipt and final launcher hash. Native performance, full-platform portability, sanitizer coverage and source adoption are outside this review. Private operational receipts and detailed identities remain private.

## Successful staging and bounded image admission

The controller completed r2 input staging with successful live isolation and51 exact files (50 manifest entries plus the manifest). The fetched successful receipt SHA-256 `4a1a34ffcd3e6107db64bb1ebf347d4db2d10b5a0e57ff3f1bf8eaae9d13a97c` independently joins all50 entries, root, r2 manifest and revised operational record; no failed files are recorded. The staging code writes that receipt only after exact file verification and live isolation pass. This is a reviewed controller receipt, not a separate live observation by the reviewer.

The final launcher adds staging-receipt rehashing before each subprocess; its SHA-256 is `e5ccf10126b9f4056feeb1e418703d24de02116ff728a07c99e6b88ae36342d7`. Both launcher negative tests pass on these final bytes. A private approval binds that exact launcher, manifest, record and actual staging receipt. **Image preparation002 is admitted within the unchanged deadline.** This does not admit guest correctness, reset the first failed attempt, or change the prior performance disposition.
