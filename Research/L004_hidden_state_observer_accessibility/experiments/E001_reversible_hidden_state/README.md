# Experiment E001 - Reversible Hidden State

**Source:** `indian-philosophy-modern-physics/V3/shared/test/PGA-IIVM-5.md`, `IIVM-1` through `IIVM-4`
**Line:** L004 / R004 requirement 1
**Status:** HISTORICAL DERIVATION; REQUIRES_REPRODUCTION

## Question

Can a reversible finite microscopic system become hidden under restricted observation while the underlying dynamics remain reversible?

## Model

Let the microscopic state be `X_t` in a finite state space with:

`|Omega| = 65,536 = 2^16`.

Microscopic evolution is a permutation:

`X_(t+1) = F(X_t)`, where `F` is bijective.

An observer sees only a projection:

`Y_t = Pi(X_t)`.

For an 8-bit observer, the accessible alphabet has at most `2^8=256` values. A coarse entropy can be measured as:

`H(Y_t) = -sum_y p_t(y) log_2 p_t(y)`.

Because `F` is reversible, the microscopic state can be returned by `F^(-1)`, while `Y_t` need not be one-to-one.

## Historical parameters and output

- Finite state size: `65,536`.
- Projection: 8-bit observer channel.
- Historical observer entropy after mixing: approximately `7.18 bits`.
- Inverse dynamics: entropy fluctuated and reversed.

## Interpretation

Restricted access can produce effective information loss in the observed channel without destroying microscopic information. The result does not establish a fundamental thermodynamic arrow and requires reproduction before numerical promotion.
