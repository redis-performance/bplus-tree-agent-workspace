# Independent release-auditor fix review

No blocking semantic or false-release defect found in the reviewed patch. This is one independently authored static review; no runner was accessed and no test pass is claimed. Exact source/diff hashes and review time are in provenance.json. Root retains ownership of the change and targeted mocked tests.

The systemd slice name encodes nested bplus.slice/bplus-night.slice/bplus-night-20261019.slice. Inspecting the former top-level path could silently report zero while jobs ran in the real descendant path. The fix queries ControlGroup, validates the exact expected nested path and uses that expected path only when the property is empty. It enumerates every descendant directory and deduplicates all listed process IDs.

Unexpected paths, nonzero property-query status, missing active cgroups, missing process listings and directory traversal/read failures all add inspection_errors. The final released predicate requires that list empty alongside inactive slice, zero collected processes, successful empty active-unit listing, nonempty release marker/saved status and a live coordinator PID. Thus those errors prevent release instead of being interpreted as zero processes. A timeout or uncaught read/exists exception produces a failed remote query and likewise cannot verify release.

An inactive slice with an absent expected cgroup is allowed, which matches systemd removing an empty inactive slice. This still needs the other live-state predicates; a directory's absence alone is not release proof. The implementation is a point-in-time observation, not an atomic snapshot across supervisor/systemd/proc/cgroup. Existing independent stop timers and lease controls remain responsible for preventing new work; this auditor does not change services or timers.

Useful targeted mocks: nested descendant processes (including duplicate IDs), inactive absent expected cgroup, active absent cgroup, unexpected ControlGroup, property-query failure, os.walk onerror, missing cgroup.procs and read failure. These distinguish a safe empty result from an incomplete inspection. No alteration to acceptance criteria or benchmark evidence follows from this operational fix.

Published follow-up: main507de297e contains exactly the reviewed source hash. Root reports six targeted mocked tests and live generic preflight; those executions were not rerun by this reviewer.
