# Experiment E001 - Coverage and Order Separation

**Source:** `indian-philosophy-modern-physics/V2/experiments/V2.1-vcr-ordered-coverage/`
**Line:** L001 / R001 requirement 1
**Status:** SOURCE-MIGRATED; REQUIRES_REPRODUCTION IN THIS PROJECT
**Executable:** `experiment.py` copied from the source experiment

## Question

Can acquisition order change the ordered record while the same spatial coverage reconstructs the same static field?

## Model and derivation

Define a spatial field on `D=[0,1)`:

`f(x) = 0.8 sin(4 pi x + 0.2) + 0.35 cos(10 pi x - 0.4) + 0.2 sin(18 pi x + 0.7)`.

Sample fixed positions `x_i`, producing `y_i=f(x_i)`. Let `P` be a permutation of the sample indices. The ordered record is:

`R_P = ((x_{P(1)}, y_{P(1)}), ..., (x_{P(N)}, y_{P(N)}))`.

The static reconstruction operator sorts by spatial coordinate before interpolation:

`F_P = A(sort(R_P))`.

Therefore a permutation can change the ordered record while leaving `F_P` unchanged, provided coordinates are retained by the reconstruction operator.

## Parameters

- `N=64` samples on a uniform grid.
- Dense reference grid: `4096` points.
- RNG seed: `20260905` for the nontrivial permutation.
- Reconstruction: one-dimensional linear interpolation after spatial sorting.

## Source output

The source experiment records the ordered-record difference, reconstruction error, reparameterization cases, and dimensional-analysis boundary in `results.json`. The original result is retained in the Phase 4 result record and must be rerun locally before being promoted.

## Decision boundary

This experiment can establish separability of coverage and ordering. It cannot establish physical time. The traversal label remains an ordering parameter only.

## Reproduction

Run `python experiment.py` from this experiment folder. The copied script writes its output under the local experiment result path only after it is adapted to this project layout.
