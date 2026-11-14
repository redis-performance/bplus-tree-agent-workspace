# H2 portability final independent disposition

**INCOMPLETE: no cross-ABI source correctness was exercised. H2 remains PARK.** The bounded portability task closed after r3 metadata collection failed. No fourth operational revision, new guest admission, reduced test matrix or deadline extension follows. This task adds no performance population and makes no source-adoption claim.

The final failure is precise: `qemu-i386 -cpu help` returned exit status 1 with empty stderr. Its stdout contains `x86 max` at line 132. The driver rejected the nonzero status before evaluating its CPU-model support expression. This is a command-status admission incompatibility; it is **not evidence that max is unavailable**, nor a baseline or H2-B correctness failure. The failed phase is consumed and its artifacts remain intact.

The independent audit joined the actual admission fields to the approved image, manifest, operational record, review and successful staging hashes. The r3 command log has 34 entries: 33 returned zero and the final CPU-help command returned1. Eight metadata containers ran. One additional export container was created but never started, inspected eight times, used for six fixed archive-preserving receipt copies and removed by its immutable ID. All 19 admission/pre/post isolation property grids independently pass, including coordinator identity, CPU topology, profiler absence, timer schedules/caps/precision, inactive retired timers and command hashes.

Metadata collected before failure includes matching package TSVs, GNU timeout identity/tool hashes, exported apt/package receipts, the i686 GCC 12.2.0 version and target string, and QEMU-i386 7.2.22 version. These tool queries do not compile or execute candidate C. No s390x tool query was reached. Neither r2 nor r3 produced a final complete image receipt, so neither could authorize the correctness phase.

| Intended guest coverage | Actually completed |
| --- | --- |
| Four baseline/B × ABI cells | 0 |
| Four runtime ABI reports | 0 |
| 228 original unit tests | 0 |
| 72 fixed fixture verifications | 0 |
| 540,000 supplied output checks | 0 |
| Four paired 7,693-validation mutation schedules | 0 |
| Two unchanged B-only metadata schedules | 0 |
| Direct four-site cache-refresh/flag checks in guest cells | 0 |

The source-review and synthetic Python tests established harness behavior only. They do not close the 32-bit little-endian or 64-bit big-endian ABI gap. No cross-target source build, guest ELF, runtime metadata layout, interpreted lookup result, native performance result, sanitizer result or TMA observation was obtained.

The complete history remains visible: preparation 001 failed at its incorrect offline-sibling assertion before any Docker command; explicitly approved r2 corrected that operational assertion and successfully prepared the pinned image; r2 metadata export failed on permission/ownership-preservation errors under the unchanged capability restrictions; explicitly approved r3 exported receipts through a stopped owned container, then stopped at the nonzero CPU-help status. Source/referee/oracle bytes, test counts, guest capability policy and the original 05:24:45.781 UTC task deadline remained unchanged across these repairs.

Receipt export produced 37 inventory entries. File contents/hashes, symlink targets and item kinds match the fetched copy. Raw inventory records remote UID/GID/mode; the local fetch does not reproduce those permissions. An initial stricter local-mode audit failed: ten fetched directories are 0775 while the remote inventory records 0755, with partial 0700. The controller reports extraction with Python's data filter and current process identity; the transport archive was not retained. This limitation is preserved rather than treating local metadata as source-ownership proof. The stopped-container export requested ownership preservation with `docker cp -a`; no separate pre-copy source ownership inventory was collected. The earlier permission failure therefore does not prove a particular source UID.

A fresh controller receipt reports no task-owned containers. Independently normalizing only field names, all seven unrelated stopped containers' complete IDs, names, states, labels and mounts match their pre-task retained records. The saved closed-state receipt shows work MainPID zero and cleanup timers still armed. These are reviewed controller observations, not an independent live fleet query by this reviewer; fleet release is a separate operation.

Key evidence hashes:

| Artifact | SHA-256 |
| --- | --- |
| Final failure result | `b7aa7ee75134c9b55cb5fac00af994caa15c453ceabf96bcb000cf829c8fd87c` |
| Actual r3 command log | `51c7e26caef781484bef1a9d99b503a6cf06f5ca5ce8fa72e53a15f5cbc73253` |
| CPU-help stdout | `a19fdb80264375f76a14385ec569625fb9be8cd052a26d32ae90ede3b679444f` |
| Closed-container receipt | `11650da807b229a785fca129abe5d87b9cf58a1ff6d5ebf9fe6a870c6c5906cd` |

Detailed raw joins, export checks, preserved reviewer-check failures and operational identities remain in the private audit. No source edits, guest execution, fleet mutation or performance measurement was performed by this reviewer during final adjudication.
