# Fleet restoration

**All three campaign reservations are released.** No candidate was accepted and no further workload is admitted under this campaign. These are restoration observations at the recorded times, not a promise of future runner availability.

| Campaign host | Released UTC,14 November | Retained restoration evidence |
|---|---|---|
| AMD | 02:47:49 | Original coordinator identity resumed; owned work absent; recovery timers inactive; saved profiler-inactive state preserved. |
| ARM | 04:40:22 | Independent04:41:36 check: original coordinator resumed, profiler active with all33 observed threads on saved CPUs, six recovery timers inactive, no owned processes/containers or work-cgroup members. The completed work unit retained a failed status with MainPID0. |
| Intel | 06:27:53 | Root06:29 and independent06:30:30 checks: original coordinator resumed, saved CPU/profiler state restored, owned work absent, four recovery timers inactive, seven unrelated stopped containers unchanged. |

The independent Intel check observes39 profiler threads; the earlier root check observes37. Both inspect every observed thread and match the same saved CPU set. The changing thread count is not a restoration failure or a performance observation.

The first Intel release attempt at06:21:09 stopped before any restoration step. Its cleanup called `systemctl stop` on the completed transient work service after systemd had unloaded it. The lease correctly became RELEASE_INCOMPLETE with an empty restoration proof; the coordinator stayed paused, CPU50 offline and the profiler inactive. That failed lease, journal and original cleanup remain preserved.

The narrow repair accepts an already absent work unit only when LoadState is not-found, ActiveState inactive, MainPID0 and ControlGroup empty, with independently checked empty expected cgroup and no owned process/container before and after. A loaded service still requires successful stop; unknown state, read failure, a newly appearing unit or residual work blocks restoration. All37 mocked tests passed, and independent review confirmed every executable component outside this function remained unchanged.

A separately reviewed deployment procedure pinned the exact failed lease and old/new cleanup hashes, preserved exclusive original backups, atomically replaced the same cleanup basename, and started the same bounded generation-bound service. It changed no lease deadline, recovery schedule or workload. Cleanup then restored CPU50, the saved profiler policy and every observed thread affinity, rechecked owned work and resumed the exact original coordinator using pidfd. Only after the released lease and successful cleanup were verified were the two remaining owned recovery timers stopped. No unrelated container was removed.

See the [selected restoration facts](restoration-results/intel-release-projection.json), [repair diff](restoration-results/absent-work-unit.patch), [independent code review](restoration-results/cleanup-portability-final-independent-review.md), [deployment review](restoration-results/cleanup-portability-deployment-independent-review.md) and [publication manifest](restoration-results/manifest.json). Raw machine identities, leases and container records remain private; the projection binds their hashes without publishing arguments or configuration.

| Evidence anchor | SHA256 |
|---|---|
| AMD retained release proof | `97064316df195b928f588cbf6761eaced3172bec049ddb39d10d82c3bcaf5ddf` |
| ARM independent release proof | `fbb3d29171b667fddbfa1984661f035ef9b619c37c242f43b677f8c5f01a25d4` |
| Intel first failed lease | `37b2645a29b57709a1e3fa50a8d6625fae0d5a222ef4685db1e72d72ac8aa9b7` |
| Intel released lease | `5f723ca9db6417dbc63b7f3ad7cbfbeb77e5040bdd665959700fe71fd3a90319` |
| Intel fresh root proof | `3a8de1076190e80590adb493393a1ca62f254c6be106cec02e32c059787838ae` |
| Intel independent live proof | `cac295c0db3c8988856ff70d88f53f529465a46adae9632e619ea371df681130` |
| Intel original/repair/final evidence archive | `f55f968a980b969e5b3f41d7a5e8ddcad218c3a161dba242da73e730918809f8` |

Successful fleet restoration is separate from the lifecycle diagnostic's object-destruction assertions. Neither changes H2/Q4 PARK, the47-entry completed performance ledger, or selected source NONE.
