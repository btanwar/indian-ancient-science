# Experiment E002 - Reparameterization Boundary

**Source:** `indian-philosophy-modern-physics/V2/experiments/V2.4-time-free-relational-separation/README.md`
**Line:** L001 / R001 requirements 2-3
**Status:** HISTORICAL DERIVATION; REQUIRES_REPRODUCTION

## Question

Does a state-space separation remain unchanged when the acquisition label is replaced by a nonlinear monotonic label, such as `u -> u^3`?

## Equations

For normalized complex states `S_i` and `S_j`, define:

`d_L2(S_i,S_j) = ||S_i-S_j||_2`.

To quotient global phase, define projective fidelity:

`F(S_i,S_j) = |<S_i,S_j>|^2 / (<S_i,S_i><S_j,S_j>)`.

The Fubini-Study separation is:

`d_FS(S_i,S_j) = arccos(sqrt(F(S_i,S_j)))`.

A reparameterization changes only labels `u_i` to `u_i^3`; it does not change `S_i`. Therefore a valid state separation must satisfy:

`d'(S_i,S_j) - d(S_i,S_j) = 0`

within numerical tolerance.

## Historical parameters and output

- State dimension `N=17`.
- Five normalized complex states.
- Nonlinear relabeling `u -> u^3`.
- Historical Fubini-Study successive separations: `[1.37284357, 1.38185430, 1.40071725, 1.31183020]`.
- Historical result: zero numerical change in L2 and Fubini-Study separations.

## Boundary

An invariant dimensionless separation does not provide metres. A proposed conversion `L=kappa d_FS` requires an independently measured or derived length scale `kappa`; `d_FS/c` is not physical time without that scale.
