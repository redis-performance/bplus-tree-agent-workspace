# H2 cross-ABI portability attempt: incomplete

No guest correctness coverage was obtained. H2 remains **PARK / NONE**, and the 32-bit little-endian and 64-bit big-endian validation gaps remain open. This bounded correctness task adds no performance attempt or accepted source.

The intended matrix paired the exact baseline and H2-B source under i686 ILP32 and s390x LP64, using cross compilers and user-mode emulation on the reserved Intel fleet runner. All four cells required the original unit suite, unchanged fixtures and output oracles, runtime ABI evidence, and paired allocation/layout checks. None of those cells reached compilation or execution.

| Phase | Result |
| --- | --- |
| Original preparation | Failed before Docker work: the operational check incorrectly expected both SMT siblings in the online CPU's topology after the other sibling was offlined. |
| R2 preparation | Corrected the offline topology assertion; created the pinned tool image and preserved package evidence. |
| R2 metadata | Failed while copying apt receipt directories under the unchanged capability restrictions. No guest source was compiled. |
| R3 metadata | Exported the six required receipt items through an inspected, owned, stopped container. Then `qemu-i386 -cpu help` returned status 1 and triggered the frozen command-status gate. |
| Guest correctness | Not admitted. Zero ABI cells, unit tests, fixture verifications or guest oracle checks completed. |

QEMU's output contains `x86 max`; its stderr is empty. The failure does not establish that this CPU model is unavailable. It establishes that the metadata command's exit status was incompatible with the harness's strict success check. The failed phase remains consumed. No fourth revision, shortened test matrix or extension of the original 05:24:45.781 UTC deadline was admitted.

The operational revisions left the source, referees, test matrix and guest privilege policy unchanged. Synthetic Python checks and source review support the harness preparation only; they do not establish guest correctness or performance. No complete final image receipt was produced, and no target ELF or runtime ABI report exists.

Topdown-profiler assessment: no profiling query or measurement was admitted for this correctness task. Frontend Bound, Bad Speculation, Backend Bound and Retiring are all unavailable for this attempt; no pipeline category or child metric is inferred from tool metadata or earlier experiments.

The [independent final review](reviews/H2-PORTABILITY-FINAL.md) records exact phase joins, actual command counts, the absence of guest execution, and the export provenance limits. In particular, fetched directory permissions differ from the recorded remote inventory; the local copy is not evidence of original source ownership. All failed prefixes and original hashes remain retained. Published evidence uses explicit original/published hash mappings where private paths are normalized.

After closure, the task work unit had MainPID zero, no owned containers remained, and all seven unrelated stopped containers matched their retained records. Intel's reservation and recovery timers remained active for separately admitted diagnostic work. This is not a fleet-release claim.
