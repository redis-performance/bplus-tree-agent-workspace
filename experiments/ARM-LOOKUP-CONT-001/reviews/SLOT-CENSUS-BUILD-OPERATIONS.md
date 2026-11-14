# Slot-hint census: completed build operational review

**PASS for the completed native and LTO build operations.** Combined with the separate [exact target-code PASS](SLOT-HINT-CENSUS-TARGET-CODE.md), this admits the frozen twelve-case structural census within its existing deadline. It does not admit timing, performance qualification, candidate adoption, retries or changed fixtures. H2 and Q4 remain PARK; selected source remains NONE.

This reviewer reviewed the operational driver and controller wrappers, authored their independent synthetic tests, and reviewed the actual staging. The diagnostic source and target-code review have separate authors. This audit only read saved artifacts and ran Python consistency checks. It executed no diagnostic binary and made no fleet requests.

| Bound artifact | SHA256 |
|---|---|
| Source freeze | `f2f8f882de6d48a6207ffff86f9af5fae53461ff0593e9e06bcc39c4fa82849b` |
| Actual execution configuration | `5398c7efc9367a0f6b75db40ae8a85fe9d060ef2b015e7f9dc7e5f128cc6edf1` |
| Successful staging receipt | `f02f7d742f9ccd8c974acd7ccf227ff48e785fdcb0465b976ea5ce0c0e06748e` |
| Overall build receipt | `3e1cc2e88d5ae7eb14e113182da1823c00d46e3161d446b3458b6f2dd4f1fc13` |
| Native ELF | `8facf50e3c68a07ecc738aed446a0f0f9290e85e5d69c26e82d727e98031687c` |
| LTO ELF | `0a9c7f0dca40d181bd8770dcd0c46c7eb9030ca584749dfc2e0db6514cedaf39` |
| Published target-code review | `77734bd5c87c0569b2a793494bf749b1ed527ab8838f5f4f3261cff5c46f2167` |
| Independent operational audit | `4c2d4f4b57712b451d7aaf70813342114e4c08342ec9c40afa2288553ad702f1` |

All 105 required inputs were independently rehashed and the required mapping recomputed. The fetched configuration, staging receipt, build approval and both stage approvals match their approved bytes. All 42 entries across the two build receipts match the actual artifacts or frozen source files. Actual ELF, assembly and compiler records match the overall receipt. Native records GCC 13.3.0 and `-O3`; LTO records GCC 15.2.0 and `-O3 -flto=auto`. Saved Docker inspection and the actual command select the same pinned Linux/amd64 image.

The five successful build command records comprise image inspection, native compilation, an empty owned-container-name check, LTO compilation and static validation. The frozen build script reconstructs source, compiles and inspects binaries without running them. The static validator reports zero diagnostic executions and the terminal record is `COMPLETE_BUILD_ONLY`. Compiler and command stderr files are empty. These records support a build-only phase; no census count or runtime correctness result is inferred.

Thirteen raw isolation grids were replayed: one prelaunch grid plus admission, ten command boundaries and final build isolation. All 130 recorded inspection commands succeeded. The coordinator identity and stopped state, CPU selection, exact saved profiler unit and inactive state, empty container listings, both active bounded cleanup timers, exact cleanup command hashes, service caps, timer precision and both retired timers agree with the immutable infrastructure record. This is review of captured checks, not continuous monitoring between them.

Actual service properties agree with the reviewed launch: `Type=exec`, a 30-second startup limit, a 900-second runtime ceiling, a 15-second stop allowance, control-group termination and SIGKILL enabled. The service executes through the unchanged absolute-deadline wrapper on CPU 0. Both native and container commands have outer termination limits; the container also has its own absolute ceiling. Its exact owned name and labels, CPU 0, read-only source mount, separate writable build output, dropped capabilities, disabled networking and resource limits match the contract. The outer absolute deadline remains **06:45 UTC on 2026-11-14**. No expired portability task window was changed or reused.

The fetch receipt reports successful inactivity, zero main PID and absence of owned work before and after transfer. Those are controller-reported checks, not an independently observed live release. The recorded archive size is 1,168,692 bytes and its controller-recorded SHA256 is `f39b1533edb37fd45e0257b1f306a3c636af9c97769581d84948656c19bce444`. This reviewer independently rehashed the extracted content; the archive byte stream was not available for a second digest. Extraction does not prove original remote ownership or permission bits.

The target review's original and publication-normalized versions were joined, with an exact single-paragraph replacement verified against the retained original. Its technical findings, evidence and PASS are unchanged. The operational audit's first assertion incorrectly expected a bare systemd property argument; the actual command correctly uses `--property=RuntimeMaxSec=900`. That reviewer assertion was corrected, with its initial script and correction record retained. No source or operational evidence was edited.

Admission covers one fixed sweep of `hit`, `score`, `miss`, `long`, `external` and `update` for each of the two exact ELFs, followed by the frozen strict output checker. The single-use phase, per-case input and isolation checks, failure preservation and deadline remain mandatory. Actual results still need independent model, structural-count and lifecycle review. These instrumentation counts cannot be converted into speed estimates, and this diagnostic adds no performance population.
