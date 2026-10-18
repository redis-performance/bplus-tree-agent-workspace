# Step 2 discovery selection

Shortlist B for the fixed fresh-seed diagnostic confirmation; production selection
NONE. Candidate snapshots remain frozen. All variants passed semantic/sanitizer
checks and retain the same allocated leaf bytes, fixture fingerprints and checksums.

| Variant | Primary median time change | Guards with median regression >1% |
|---|---:|---:|
| A | -34.62% | 7 |
| B | -32.78% | 3 |
| C | -27.02% | 7 |

The preregistered rule ranks by fewest regressing guards before primary magnitude,
so B wins the diagnostic shortlist. It is not acceptance:13/30 A/A cells fail the
strict all-block ±1% precision condition, and B has +21.75% at width 60/count1,
+9.93% at width63/count1, and +5.89% at width63/count7. All three candidates fail
broad guard eligibility. They remain preserved, with no after-the-fact retuning.

Discovery completed2880 processes/371520 measured batches in45.09seconds. Raw rows,
per-process statistics, paired minimum/median effects and full ranges are retained.
The classifier is outside per-score loops in generated code. A/C inline into the
bulk wrapper; B is outlined. Output stores and checksum reloads remain in all four.
Dispatch, inlining, metadata hoisting and code shape can all contribute to timing;
no exact-cycle or sole-cause claim follows.

Fresh phase: same 30 cells, six ABBA blocks, 129 samples, seeds 82037/82051, new A/A,
180-second total budget. No iterator integration follows from a bulk-only win.

## Final decision after fixed confirmation

B primary median time change is -33.14%; the same three short-range losses recur
(+20.79%,+10.60%,+6.49%). Their discovery controls qualified and every discovery
comparison block was slower by >1%. B therefore fails as an all-range replacement,
not merely because broad A/A qualification remains incomplete. Experiment PARK
retains the bulk-only direction; source selection NONE. See [results](RESULTS.md)
and the cross-author adversarial review. No implementation was retuned after timing.
