# Experiment E002 - Observer Capacity Comparison

**Source:** `indian-philosophy-modern-physics/V3/shared/test/PGA-IIVM-5.md` and IIVM records
**Line:** L004 / R004 requirement 2
**Status:** HISTORICAL PROTOCOL; REQUIRES_REPRODUCTION

## Question

Do observers with 4, 8, and 12 bits produce different effective descriptions from the same microscopic trajectory?

## Formal structure

Use a common microscopic trajectory `X_t` and observer maps:

`Y_t^(b) = Pi_b(X_t)`, for `b in {4,8,12}`.

Compare accessible descriptions using entropy, distinguishability, and reconstruction error. The underlying `X_t` must be identical across capacities.

## Required controls

- Same trajectory and initial state.
- Same dynamics and random seed.
- Explicit projection definitions.
- Capacity-specific entropy and reconstruction metrics.
- Inverse-dynamics check where the microscopic dynamics are reversible.

## Current state

The chat archive reports different effective descriptions, but the exact source parameters and executable are not present in the migrated project. This folder preserves the derivation and reproduction requirements only.
