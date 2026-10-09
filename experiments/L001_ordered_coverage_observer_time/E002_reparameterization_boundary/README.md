# Experiment E002 - Reparameterization Boundary

**Source:** `indian-philosophy-modern-physics/V2/experiments/V2.4-time-free-relational-separation/README.md`
**Line:** L001 / R001 requirements 2-3
**Status:** HISTORICAL DERIVATION; REQUIRES_REPRODUCTION

## Question

Does a state-space separation remain unchanged when the acquisition label is replaced by a nonlinear monotonic label, such as \(u -> u^{3}\)?

## Equations

For normalized complex states \(S_{i}\) and \(S_{j}\), define:

\(d_{L2}(S_{i},S_{j}) = ||S_{i}-S_{j}||_2\).

To quotient global phase, define projective fidelity:

\(F(S_{i},S_{j}) = |<S_{i},S_{j}>|^2 / (<S_{i},S_{i}><S_{j},S_{j}>)\).

The Fubini-Study separation is:

\(d_{FS}(S_{i},S_{j}) = arccos(sqrt(F(S_{i},S_{j})))\).

A reparameterization changes only labels \(u_{i}\) to \(u_{i}^3\); it does not change \(S_{i}\). Therefore a valid state separation must satisfy:

\(d'(S_{i},S_{j}) - d(S_{i},S_{j}) = 0\)

within numerical tolerance.

## Historical parameters and output

- State dimension `N=17`.
- Five normalized complex states.
- Nonlinear relabeling \(u -> u^{3}\).
- Historical Fubini-Study successive separations: `[1.37284357, 1.38185430, 1.40071725, 1.31183020]`.
- Historical result: zero numerical change in L2 and Fubini-Study separations.

## Boundary

An invariant dimensionless separation does not provide metres. A proposed conversion \(L=kappa d_{FS}\) requires an independently measured or derived length scale `kappa`; \(d_{FS}/c\) is not physical time without that scale.
