# Initial audit failure retained

The first audit incorrectly compared the current round16 SHA manifest with the
seal's pre-seal manifest hash. Round16's seal script explicitly updates the manifest
with the closed stdout hash and adds its own seal/script entries. This was an auditor
assumption error, not changed prior evidence.

The corrected verifier reconstructs the pre-seal dictionary, verifies that exact hash,
and then checks every current immutable file against the sealed manifest. The original
verifier and failed stdout/stderr remain; raw private-path stderr is retained under
scratch and the public copy uses <workspace>. No experimental child is rerun, no hash
check is removed and no prior evidence is edited.

The next reconstruction attempt used full-string ordering instead of the original
component-wise Path ordering. That failure is also retained. Applying the original
serialization order reconstructs the exact recorded pre-seal hash; both original and
sealed provenance are checked, with no experimental rerun or omitted hash gate.
