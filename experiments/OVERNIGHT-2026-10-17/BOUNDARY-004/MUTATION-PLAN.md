# Relocation oracle sensitivity controls

Written after baseline passes, before fault runs. Two isolated sanitizer/debug builds,
one bounded120s run each. No candidate or performance claim. Root source unchanged.

- Remove leaf ID table repair from zbtDefragScoreNode: expect model failure or ASan
  use-after-free after moved leaf is released and looked up.
- Disable zbtDefragAdjustSize: expect exact allocation delta assertion with callbacks
  deliberately selecting different usable sizes.

Save all patches, commands, source/binary hashes, stdout/stderr and outcomes. A passing
fault remains an undetected control; do not change the oracle retrospectively to hide it.
