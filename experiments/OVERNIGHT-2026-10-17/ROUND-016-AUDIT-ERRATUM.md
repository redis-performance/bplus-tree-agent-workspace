Initial final audit reached the workspace check and failed because README linked
ROUND-016.md before that report had been written. The report now exists. No source/test
change and no experimental child rerun. Original verifier, outputs and workspace error
remain; audit2 uses fresh output names and recomputes all read-only checks. Raw traceback
remains ignored in scratch; the public copy replaces the workspace path.
