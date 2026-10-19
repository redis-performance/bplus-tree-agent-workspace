# Preparation execution freeze — no launch implied

2124 fixed serial commands,600s including all builds and fixture setup. Four original43
runs,512 HARNESS-004 cells,1536 HARNESS-005 cells,12 packed/mutation/signed-zero oracles,
14 expected negative detections. Exact command list retained. Seven fault transformations
are retained historical families, not new faults. HARNESS-005 mutations affect only
isolated fault snapshots; no oracle weakening or actual binary mutation.

Both actual baseline and historicalA timing binaries are protected. Reconstructed
control/A .text must match their respective existing actual binaries exactly. A mismatch
stops before performance; no rebuild of protected binaries. Mode4/mode5 native binary
hashes are frozen only after successful validation and must be independently reviewed
before guard timing. Native/sanitizer flags and relative frontend/output paths are
identical across source snapshots. Unchanged refs and all faults/source hashes pinned.

Driver checks exact CPU2 affinity, all input hashes, original source/protected hashes
before commands, exact semantic output/expected fault diagnostic, timeout partial streams,
all snapshots before/after and final protected identities. On failure, no rerun; root
must obtain a separate read-only postidentity/idle proof if failure precedes final checks.
Fresh lease helper supplies hard deadline/cgroup enforcement. New lease is separate from
the released night lease; rootgrant required. No compilation or runner activity has
occurred during preparation. Local AST/manifest/patch-application checks only.
