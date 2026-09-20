# PGA 1.12.2.6 — Coverage Threshold / Equivalence-Class Stability Test

**Research Tree Node:** 1.12.2 — Observable Reconstruction / Information / Causality

## Objective

Test whether increasing relational information coverage reduces microscopic ambiguity and produces a stable coarse-grained observable structure, while microscopic differences remain unresolved.

## Construction

An 8×8 microscopic relational system was used:

- 64 microscopic elements.
- 16 coarse-grained regions, each formed from a 2×2 block.
- Multiple microscopic configurations were allowed to share the same coarse-grained structure.

Definitions:

X = microscopic configuration

M(X) = coarse-grained configuration

For coverage C and observation map A_C:

X_a ~_C X_b  iff  A_C(X_a) = A_C(X_b)

The stability question was whether M(X) becomes uniquely determined and remains unchanged as additional microscopic information is acquired.

## Coverage result

Representative central-outward coverage experiment:

| Coverage | Microscopic elements observed | Fraction with unique macro reconstruction |
|---:|---:|---:|
| 12.5% | 8 | ~0.2% |
| 25% | 16 | ~59.1% |
| 37.5% | 24 | ~99.7% |
| 50% | 32 | 100% |
| 62.5% | 40 | 100% |
| 75% | 48 | 100% |
| 87.5% | 56 | 100% |
| 100% | 64 | 100% |

The experiment therefore exhibited a transition from ambiguous reconstruction to stable coarse-grained reconstruction.

A set of 30 random coverage orders gave effective macro-identification thresholds spanning approximately 37.5%–62.5%, with a median around 43.75%.

The exact threshold is therefore not universal; it depends on the information geometry, sampling path and underlying relational structure.

## Structural result

The experiment supports the distinction:

X ≠ [X]_C ≠ M(X)

where:

- X is the complete microscopic state;
- [X]_C is the observational equivalence class under coverage C;
- M(X) is the stable coarse-grained structure.

A key surviving result is:

increasing information coverage → reduced observational ambiguity → stable coarse-grained structure.

Microscopic uncertainty can remain while macroscopic identity becomes stable.

## Status

**🟢 SURVIVES AS A STRUCTURAL / OPERATIONAL TOY RESULT**

The result supports the possibility that sufficient relational information can stabilize an effective coarse-grained description.

## Critical limitations

The coarse-graining structure was prescribed by the experiment. Therefore this does **not** establish:

- that physical objects are fundamentally coarse-grained structures;
- that nature selects the same coarse-graining;
- physical spacetime;
- physical time;
- physical c;
- quantum measurement;
- particles or Standard Model structure.

The threshold percentage is also not a candidate universal physical constant.

## Research protection

Do not identify:

stable reconstruction = fundamental object

or

coverage threshold = physical constant.

The stronger question remains open:

Can stable equivalence classes arise from microscopic relational dynamics **without prescribing the macroscopic coarse-graining in advance**?

## Branch consequence

This result strengthens the information/reconstruction layer:

S∞ ↔ B∞
→ relational dynamics
→ propagation / interaction
→ information acquisition
→ coverage
→ observational equivalence
→ stable coarse-grained structure

It should also be treated as an input to the quantum, geometry and particle branches rather than as an isolated result.

## Next substantive research question

Test whether the coarse-grained structure can emerge naturally from the relational dynamics itself, without imposing the macroscopic partition beforehand.

This is the substantive next PGA.

