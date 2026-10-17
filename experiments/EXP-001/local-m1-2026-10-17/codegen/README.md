# Diagnostic code generation

Generated before the timing matrix with the same compiler and release optimisation
flags as the benchmark (remarks do not change optimisation):

```sh
cc -std=c11 -g -Wall -Wextra -fno-omit-frame-pointer -O3 \
  -Isrc -Icompat -Ivendor/redis -S src/zset_btree.c \
  -o scratch/exp001/zset_btree.s \
  -Rpass=loop-vectorize -Rpass-missed=loop-vectorize
```

The committed `.s` files are diagnostic extracts for selected symbols. Debug location,
CFI/LOH directives and debug-value comments are omitted; they are not standalone
assembler inputs. No target-source edit or candidate binary was produced.

Observed in these compiler outputs:

- `zbtreeScore` checks the SDS representation and tail-calls `zbtreeScoreRaw`.
  The benchmark's fixture strings always use SDS64, but the separately compiled API
  retains the general dispatch. A future raw-API fixture can separate this caller cost.
- `zbtreeScoreRaw` calls the hash wrapper and includes inlined member-index work;
  tag-mask decoding includes `rbit`/`clz`. Bucket width and member representation
  branches remain. This is not evidence that branch misses dominate runtime.
- `zbtScoreLeafLowerBound` contains `csel`/`csinc` in a search-bound update. Some
  conditional selection already exists, alongside other branches and comparison paths;
  blanket requests to make all search branchless would miss the current code shape.
- `remarks.txt` records vectorisation decisions, including many missed loops. A missed
  vectorisation remark is not itself a defect or a performance opportunity.

Use the sampled function evidence and the original source to choose a specific mechanism
to test. Static assembly alone does not provide cache misses, branch misses or IPC.
