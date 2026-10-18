# Analysis-only correction; no measured rerun

Initial analyser retained HARNESS-005's literal 200-traversal invariant, despite the
preregistered n95 and rounding rule. Every child correctly reports 210527 traversals
and 20000065 effective items. This stale literal incorrectly marks all rows invalid.
Original analyser, summary, eligibility and output retained. Corrected analyser changes
only that literal to ceil(20m/95), as already required by PLAN.md. No gate, count, row,
or threshold changed; no child rerun. Outputs use separate *-corrected filenames.
