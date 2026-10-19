# One bounded exploratory rank screen — frozen before implementation

Acknowledged M6 profile/calibration210c06a2; A/A b5ebd930. Public referee originally
ca5cacfb; source/referee exact SHA256 in freeze.json. Candidate source baseline is
b5ebd930 plus exact unchanged src/. Current coordinator publication will pin this
plan and population files before constructing candidates. Seed schedule1/2/3/1/2/3,
fixed counts from calibration.json, clang C11-O3-g-Wall-Wextra-framepointers,noLTO,
compat allocator/assertions/hash unchanged. No machine frequency/counter assumptions.

Hypothesis only: shorter-side child-count sum using existing subtree totals reduces
public successful rank time. Three sequential implementation passes, no agents:
A branch-local direct prefix additions or suffix subtractions; B one local sum
followed by subtree correction; C one selected contiguous span and direction correction.
All target only zbtScoreRank. No root src edits, no layout or mutation changes.

Create scratch/m6-rank/variants/{base,A,B,C} as isolated copied source/build trees,
verify every referee hash and baseline source hash before building. Preserve exact
patches and rebuilt binary/source hashes. Native upstream tests, ASan/UBSan upstream
tests and targeted semantic harness checks precede timing. Failed variant ineligible.

Screen all3variants serially: public rank16bytes, integer layout at10K/100K/1M;
100K and1M are preregistered primary cells,10K a screen guard. Six ABBA blocks per
variant/cell, three warmed batches/process. Rotate variant order and cell order by
block. Unchanged base A versus candidate B. Fixed counts identical to baseline A/A;
no per-candidate adaptation.300s timing-window budget;120s child cap; hard stop
before02:03UTC to leave audit/handoff margin. No concurrent work during timing.
No outlier removal, no reruns, no optional stopping for wins. Preserve per-batch rows.

Because A/A failed, small/noisy gains have no ranking. Any variant with no clear
consistent public benefit is PARK or REJECT; a large consistent direction may be an
exploratory lead only. Never choose a universal winner from this primary-only screen.
A candidate can fail this screen, but cannot pass adoption from it. All shared full
rank/mutation/memory/all-eight-operation guards remain deferred and mandatory.
No fresh adoption confirmation for ineligible candidates. A separately planned
exploratory fresh confirmation may be justified only by large consistent results.
Independent adversarial review remains pending even if local checks pass.

After timing inspect exact release assembly/code size and baseline/lead self-profile
if there is a material lead. Profile outcomes must agree with claimed mechanism;
coarse self-sampling does not provide exact timing fractions. Missing mechanism,
qualified controls, full guards or independent review keeps adoption PARK/NONE.
