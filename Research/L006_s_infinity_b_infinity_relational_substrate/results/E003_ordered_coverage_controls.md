# Result E003 - Ordered Coverage Controls

**Runbook step:** [../runbook.md](../runbook.md) step #3
**Experiment:** \(experiments/E003_ordered_coverage_controls/\)
**Status:** NEGATIVE

## What was tested

Whether relational observations recover the intended ordering in the historical minimal ordered-coverage implementation.

## Method

Historical E002 used periodic latent modes, a random observation map, nonlinear response, noise, pairwise distances, Gaussian affinity, and graph-Laplacian spectral ordering. The source explicitly identifies the periodic latent parameter as an ordering primitive and calls for stronger controls in the next test.

## Actual output

Pairwise circular-distance rank correlation was approximately `rho = -0.029`, effectively no useful recovery for the tested configuration.

## Interpretation

The implementation failed as a demonstration of robust ordered reconstruction. It does not show that time cannot emerge or that S-infinity/B-infinity is falsified.

## Pass / fail

R006 requirement #4 FAILED for the tested implementation, matching R001 requirement #4.

## Next action

Run the full controlled battery shared with L001: shuffled observations, independent maps, noise levels, non-periodic trajectories, multiple methods, a relational null, and pre-registered criteria.
