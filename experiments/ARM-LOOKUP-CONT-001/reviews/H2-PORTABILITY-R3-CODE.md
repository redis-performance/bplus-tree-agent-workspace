# Portability operational revision3 review

**SOURCE REVIEW PASS; eligible for separate input staging and metadata admission.** R3 repairs only receipt export after the preserved r2 metadata failure. It does not retry a guest source result, recreate the image, alter correctness coverage or renew the deadline. H2 remains PARK.

The reviewer independently rehashed all56 manifest entries, verified every prior original/r2 pin and manifest unchanged, and recomputed `driver.diff` exactly. The31-test synthetic Python suite passes independently. No Docker, guest, source build, timing or profiling execution was performed by this reviewer.

The new exporter is permitted only in image-receipt mode. It creates one stopped, never-started container using the existing exact check name, three ownership labels and pinned image. Before every copy and before removal, inspection binds the canonical immutable ID, name, image, labels, state `created`, Running=false, PID zero, read-only root, no mounts/network/capability additions, cap-drop ALL and `/bin/true` command. There is no start/run call for this export container.

Exactly six fixed items are copied through Docker's host API with archive preservation and no symlink-follow flag: apt update/install logs, package TSV, apt configuration, apt lists and package archive checksum receipt. The host inventory records lstat mode, UID/GID, size, file hashes and symlink targets. Both restricted `partial` and `auxfiles` directories must remain present; the archive checksum file must be nonempty; special files fail admission. Only the inspected immutable container ID is removed. A failure preserves the copied prefix and stopped owned container for the already-reviewed cleanup. Source/receipt identities and live isolation bracket the operation.

All ordinary metadata and correctness containers retain their previous cap-drop ALL, no-new-privileges, network, resource, CPU and absolute timeout constraints. Correctness mode explicitly rejects the host exporter. Synthetic tests cover successful exact-six-copy/no-start orchestration, foreign-ID rejection before copy/removal, correctness-mode refusal, restricted directory and symlink inventory, and the unchanged prior admission/matrix failures.

| Artifact | SHA-256 |
| --- | --- |
| R3 manifest | `9fb8801533bef28b78f0d01d4439f4e2589100926fb240815c095bf26b099078` |
| R3 driver | `dde7363b1d25e2b7c6ce4920b1fc22f3e5a306d4fb6be2bfb6865d4aaa592e80` |
| R3 protocol | `b369e174d32b86d5a5273aaf552fe8dcc816a7509daaff00b25877c07d6e0fb7` |

R3 uses new single-use phase paths and must bind a new complete successful staging receipt. The same previously created image, source pair, operational record and05:24:45.781 UTC task deadline remain. This source review grants no guest correctness admission. Actual metadata receipts and tool support still require independent review; failure or insufficient remaining time closes incomplete without reduced counts or additional repair by implication.

## Actual staging and metadata admission

The fetched r3 staging receipt SHA-256 `bdbb3a49906fe8b3a194baa662e4ebd86fdf8e89a90e9b1dcb7b8b1e65bad983` passes the independent complete-schema/root/manifest/record join for all56 file entries. The controller reports57 staged files including the manifest, successful live isolation, and completion before its remaining-time gate. A phase-specific approval SHA-256 `8e2571fcf841791fa56768c8c3823da3e23a093a0ccb38b4fde5466d0e6970cc` now admits **metadata collection and stopped-container receipt export only** against the existing image. It binds the exact staging receipt, manifest and unchanged operational record. Guest correctness still requires review of the actual metadata receipt; the original deadline remains unchanged.
