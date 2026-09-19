# Result E001 - Coverage and Order Separation

**Runbook step:** [../runbook.md](../runbook.md) step #1
**Experiment:** `experiments/E001_coverage_order_separation/`
**Status:** REQUIRES_REPRODUCTION

## What was tested

Whether changing acquisition order changes the ordered record while leaving reconstruction of the same spatial field unchanged.

## Method

Historical V2 VCR synthetic-field test. The source record reports fixed sample locations with changed acquisition permutations, followed by reconstruction after restoring spatial coordinates. The original executable and full parameter file are not present in this project.

## Actual output

The source reports an ordered-record relative difference of approximately `1.46`, with unchanged static spatial reconstruction. This value is historical and has not been independently rerun here.

## Interpretation

Within the reported toy model, coverage and ordering are separable observables. This is a reconstruction result, not evidence that ordering is physical time.

## Pass / fail

Passes the scoped mathematical/computational intent of R001 requirement #1 as a historical result. It does not address R001 requirements #4-#6.

## Next action

Recover or recreate the exact V2.1 parameters and rerun the test with a recorded script, environment, and raw output.
