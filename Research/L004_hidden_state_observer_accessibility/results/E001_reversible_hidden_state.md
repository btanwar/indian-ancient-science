# Result E001 - Reversible Hidden State

**Runbook step:** [../runbook.md](../runbook.md) step #1
**Experiment:** `experiments/E001_reversible_hidden_state/`
**Status:** REQUIRES_REPRODUCTION

## What was tested

Whether a finite reversible microstate system can become less observable under a restricted projection while retaining reversibility in the underlying dynamics.

## Method

Historical IIVM model with `|Omega| = 65,536`, permutation dynamics, an 8-bit projection, and observer entropy measurement. The source code and exact parameters are not included in this package.

## Actual output

The historical report gives observer entropy of approximately `7.18 bits` after mixing, followed by fluctuation and reversal under inverse dynamics.

## Interpretation

This supports hidden-state/coarse-graining as a toy-model behavior if reproduced. It does not support a fundamental arrow of time.

## Pass / fail

R004 requirement #1 requires reproduction and is not yet passed here. The historical result supports the current negative interpretation of requirement #3.

## Next action

Recover the exact permutation, projection, seed, and entropy calculation, then rerun with an inverse-dynamics check.
