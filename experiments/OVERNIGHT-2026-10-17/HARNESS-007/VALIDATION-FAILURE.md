# Retained first validation failure

`python3 experiments/OVERNIGHT-2026-10-17/HARNESS-007/validate.py` exits1 at its
elapsed>0 assertion (line46), after release build and release-0000 both exited0.
The raw row reports n1,ops1,batch1,hit,8bytes,elapsed_ns0,checksum1,thread291ns.
Its ops_per_sec1000000000 came from a1nsfallback and is invalid reporting.
The manifest's running status reflects the assertion stopping the driver; no child
remains. Original source/build/raw/driver preserved; traceback is in the private
supervisor transcript. Attempt002 separately fixes zero-duration reporting and the
invalid validation precondition while preserving all semantic checks.
