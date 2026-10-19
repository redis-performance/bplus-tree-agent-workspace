# EXP-008 post-discovery full correctness validation

**PASS: all 16,512 canonical cells, no retry.** This is explicitly additional correctness evidence obtained after discovery, not a timing campaign or retroactive performance qualification. The earlier discovery rows/audits remain unchanged.

The original unchanged validate.py was launched by absolute script path from fresh ignored scratch cwd `scratch/m6-exp008-post-validation`. Its relative `build` path is a symlink to the original isolated M6 checkout build. Its relative matrix output lands only inside that scratch cwd. No source/referee/script was changed, no binary rebuilt, and no historical validation file was overwritten. The original root/checkout matrix paths were absent when inspected; their absence is preserved.

The declared prelaunch owned-process-group wall bound was 300 seconds, clipped to 07:15 UTC; the canonical script uses 10 seconds per child. It completed in 72.005689seconds, return 0, driver reaped and owned group empty. It ran serial subprocesses through the unchanged canonical source. Raw stdout/stderr remain scratch-only originals with hashes and generic public copies. No child remains active.

Independent cardinality and every row/argument/returncode verify: native and ASan/UBSan, base/A/B/C, widths 0..64, both physical directions, counts 1/2/4/7/8/16/32/96, shifts sorted{0,min(63,64-width)}, leaves 8, samples 1, rounds 1, warmup 1, default seed 1. There are 8,256 native cells and 8,256 sanitizer cells; 2,064 for each count. Each mode/variant contributes 2,064 cells. All returncodes are 0 and no sanitizer-error diagnostic appears.

The prior 1820-fixture selftest omitted counts 4/16/32; this full original validator supplies 2,064 cells for each. Its benchmark executable retains exact decoder/reference validation around the small fixture. Canonical validate.py discards child timing CSV; this audit does not read or use timing values. Stored stderr calibration fields are preserved verbatim as evidence, not performance data. No clock, source, guard or selection gate was changed.

All 53 frozen source/helper/script/object/binary identities match before/after, including all 8 native/sanitizer executables. The exact matrix is copied byte-for-byte to boundary-matrix.json: SHA256 `a0090251cfb2b9ad54bbc0f9ce028b381af181bc94ba7bb0a7ebb73108a29c62`. No privacy metadata rewrite was needed. AUDIT.json preserves exact identity/cardinality checks and cwd mapping; COMMAND.json gives declared bounds, UTCs, cleanup and original/public log hashes. Source selection stays NONE, and failed A/A/short-window/guard conclusions remain unchanged.

Participant `/root/followup_proposal_a`, inherited GPT-6/Codex family; exact serving model/token/currency cost unknown. No new timing/profile/capture, confirmation, shared-document/Git edit or retry occurred.
