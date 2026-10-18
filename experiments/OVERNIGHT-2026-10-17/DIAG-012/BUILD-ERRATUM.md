# Preserved assembly preparation failure

First preparation builds placement0 release/sanitizer binaries, then Python fails
reading upstream-test assembly as UTF-8. Clang emits raw binary bytes inside test
string constants. No validation or timing ran for this attempt. Its scripts/logs and
snapshot remain. Attempt002 performs a byte-preserving Latin-1 decode/encode around
ASCII directive insertion. All compiler output outside the two padding directives
must round-trip exactly. No compiler/source/test changes or gate relaxation.
