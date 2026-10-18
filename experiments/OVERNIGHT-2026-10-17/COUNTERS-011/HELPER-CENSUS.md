# Descriptive helper census from the existing captures

This is post-hoc source-counter arithmetic, not a new trial or decision criterion.
Each column represents 32,768 all-hit, 16-byte queries. Every number is identical
across C's batch1/16 and prefetchon/off conditions for the given seed.

| Logical observation | Seed 83103 | Seed 83111 |
|---|---:|---:|
| Leaf-search entries | 33,048 | 33,040 |
| Inline tag-helper entries | 37,456 | 37,568 |
| Eight-byte word examinations in source branches | 152,780 | 158,444 |
| Scalar tag comparisons | 6,688 | 5,828 |
| Non-null tag returns | 37,176 | 37,300 |
| Full member-byte comparisons that reject a matching tag | 4,408 | 4,532 |
| Helper no-match returns | 280 | 268 |
| Leaf scan ends without another helper call | 0 | 4 |

[helper-census.py](helper-census.py) checks branch-flow conservation: the first word
is examined once per entered16-byte loop body, the second only after the first misses,
the8-byte tail only when its length test passes, and successful returns plus no-match
returns equal helper entries. Public raw-mapped leaf branches show all candidate
record lengths equal the requested length in these fixed-length streams. Thus a
length prefilter would not remove these comparisons in these particular fixtures.

Do not confuse word examinations with load instructions, unique bytes, cache traffic,
cycles or time. Instrumentation changes generated code. A rejected byte-tag candidate
can leave the loop at its end without invoking the helper again; the four such cases
in seed83111 explain why extra leaf entries are not equal to helper no-match returns.
The pattern is evidence about logical work, not the observed batch-size timing contrast.

The heterogeneous-prefix correctness oracle now covers unequal lengths, but no mixed-
length timing referee or qualification has run. Any performance hypothesis about
length filtering needs that new, independently validated scope before a population.
