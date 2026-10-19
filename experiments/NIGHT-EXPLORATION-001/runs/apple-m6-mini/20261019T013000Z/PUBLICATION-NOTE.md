# Final publication cache exclusion

The coordinator rejected request r1-final-audit-handoff-20261019T015824Z:
`Public-evidence review required: 002-rank/__pycache__/compare.cpython-313.pyc`.
The diagnostic loader had generated that bytecode cache through importlib. It was
moved intact to ignored scratch/m6-rank, and diagnose.py now disables bytecode
creation before importing the driver. Source patches, timing binaries and measured
rows are unchanged. No Git operations, credentials or permissions were changed.
A fresh final-publication request follows this correction; publication remains
unresolved until the coordinator acknowledges it.
