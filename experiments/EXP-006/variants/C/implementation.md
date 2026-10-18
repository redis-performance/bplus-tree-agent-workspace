# Variant C

Sequential implementation pass, not an independent agent. Backend/model/cost unknown.
Exact baselinea2ff0c5ddc00ffc11ff7d73e202d6384df77c84cplus frozen HARNESS-007attempt002; isolated ownsource/build.
Implementation: two8-byte chunks per bounded16-byte iteration,8-byte cleanup and scalar tail/fallback.
Only leaf tag search changes. Lowest matching byte is returned; packed layout/hash/
length/full-member comparison, score mapping, allocation and assertions unchanged.
Word zero-byte borrow may mark higher bytes after a zero, but ctz selects the first
true zero on little endian; non-little-endian uses byte loop. Loads require n>=8;
16-byte version checks n>=16 before both chunks. No unaligned typed loads or overread.
Risk: extra instructions/register pressure can outweigh avoided memchr boundary;
compiler/codegen and measured guards decide. Keep losing patch regardless of outcome.
