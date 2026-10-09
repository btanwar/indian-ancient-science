# Experiment E002 - Ordered Coverage Controls

**Source:** \(indian-philosophy-modern-physics/V3/research/S_{INFINITY}_B_INFINITY/experiments/E002_ordered_coverage_effective_time.md\)
**Line:** L006 / R006 requirement 4; shared with L001 R001 requirement 4
**Status:** HISTORICAL NEGATIVE IMPLEMENTATION; REPRODUCTION REQUIRED

## Model

Latent periodic state:

\(z(theta) = (sin(theta), cos(theta), sin(2 theta), cos(2 theta))\).

Observation map:

`y(theta) = tanh(A z(theta)) + epsilon`,

where `A` is a random observation matrix and `epsilon` is Gaussian noise.

The reconstruction receives observation vectors and pairwise distances, forms a Gaussian affinity matrix, and uses a graph-Laplacian spectral embedding to infer an ordering.

## Metric

Compare recovered cyclic order with the generating order using pairwise circular-distance rank correlation `rho`.

## Historical output

`rho approximately -0.029` for the tested configuration, indicating no useful recovery.

## Required controls

- Shuffled observations.
- Independent random observation maps.
- Multiple noise levels.
- Non-periodic trajectories.
- Multiple reconstruction methods.
- A null relational process with no designed temporal sequence.
- Pre-registered metric and success threshold.

## Interpretation

The implementation fails as robust ordered reconstruction. It does not prove that physical time cannot emerge and does not falsify S-infinity/B-infinity generally.
