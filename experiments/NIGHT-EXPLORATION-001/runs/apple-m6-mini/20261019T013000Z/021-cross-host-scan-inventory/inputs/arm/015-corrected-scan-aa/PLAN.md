# Corrected-adapter SCAN fixed fresh A/A

Exact source13e459ff8800be3f02b6b45c87dd7b0c39453fa9, corrected adapter; original
microbench and all tree/referee options retained. Separate isolated build, serialCPU2.
48 processes: sixABBA blocks per100K/1M, alternate size order eachblock, seeds401/402/
403 twice,5M requestedops,16-byte original fixtures. Fresh seeds and5M fixed before
any data, consistent with longer-window protocol; not selected from A/A outcomes.
Hardcap300s measurement in one owned300s job including audit (build in prior600s
profile job). Source/referee/binary hashes frozen before first A/A and checked after.
All six effects must satisfy abs<=1% and everywindow>=10ms; exact same fixture,
operations/checksum/ownedbytes/CPU2/serial windows mandatory. Missing/failed controls
means NONE before implementation, no reruns, exclusions, count changes or retries.
No candidate code or measurements. Distinct harness identity; cannot repair original
8fab A/A or transfer existing architecture gains. Parent reviews full raw record.
