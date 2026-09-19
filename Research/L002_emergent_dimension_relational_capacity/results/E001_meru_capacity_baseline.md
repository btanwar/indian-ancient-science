# Result E001 - Meru Capacity Baseline

**Runbook step:** [../runbook.md](../runbook.md) step #1
**Experiment:** \(experiments/E001_meru_capacity_baseline/\)
**Status:** SUCCESSFUL

## What was tested

Whether the Meru Prastara baseline supplies a precise count of binary histories grouped by Hamming weight.

## Method

For binary strings of length `n`, group each of the \(2^n\) strings by the number of ones. The groups are indexed by weights `0` through `n`, giving `n+1` classes. This is the Pascal/binomial identity recorded in the Phase 1 analogy.

## Actual output

Number of microstates: \(2^n\). Number of weight classes: `n+1`. Class sizes are `C(n,k)` for `k=0,...,n`, and their sum is \(2^n\).

## Interpretation

The compression rule is exact and reproducible mathematics. It does not establish a physical dimension or show that Meru Prastara is physically privileged.

## Pass / fail

Passes R002 requirement #1 at the mathematical baseline level. R002 requirements #2-#5 remain open.

## Next action

Compare the same observables against matched generic partitions and alternative grouping rules before assigning physical meaning.
