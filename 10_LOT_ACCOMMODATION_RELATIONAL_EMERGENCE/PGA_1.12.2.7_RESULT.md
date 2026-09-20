# PGA 1.12.2.7 — Emergent Coarse-Graining / Unprescribed Equivalence-Class Test

**Research Tree Node:** 1.12.2 — Observable Reconstruction / Information / Causality

## Objective

Test whether a stable coarse-grained relational structure can be recovered from the microscopic relational structure **without supplying the macroscopic partition to the reconstruction algorithm**.

This follows PGA 1.12.2.6.

The distinction is:

- PGA 1.12.2.6 prescribed the coarse-graining and tested coverage/stability.
- PGA 1.12.2.7 asks whether relational structure itself contains enough information for a coarse-graining to be discovered.

## Minimal construction

A 64-node weighted relational network was generated with three internally dense relational regions and sparse inter-region coupling.

The microscopic node assignment was retained only as a hidden reference for auditing; it was **not supplied to the reconstruction algorithm**.

The reconstruction used the relational Laplacian spectrum and spectral clustering of low-frequency relational modes.

Thus:

microscopic relational network
→ Laplacian
→ low-frequency relational modes
→ inferred partition

No predefined 22/21/21 partition was given to the inference procedure.

## Result

For the modular relational network:

- 64 microscopic nodes.
- Three hidden relational regions.
- Spectral reconstruction recovered the hidden partition with adjusted Rand index (ARI) = **1.00** in the baseline realization.
- The first nonzero Laplacian eigenvalues were approximately 0.347 and 0.516, followed by a much larger gap to approximately 4.49.

This spectral gap indicates that the network contains a low-frequency structural separation that can be detected without directly specifying the macroscopic regions.

## Stability test

The inferred partition was recomputed after random edge perturbations.

Representative mean ARI relative to the baseline inferred partition:

| Edge perturbation | Mean ARI | Range |
|---:|---:|---:|
| 1% | 1.000 | 1.000–1.000 |
| 5% | 1.000 | 1.000–1.000 |
| 10% | ~0.983 | ~0.552–1.000 |
| 20% | ~0.891 | ~0.536–1.000 |

Small perturbations therefore preserved the inferred coarse structure in this realization.

## Control

A homogeneous Erdős–Rényi relational network with comparable edge density was used as a control.

Repeated 10% edge perturbations gave a mean ARI of approximately **0.324**, with a wide range including values near zero.

This indicates that the stable three-way partition was not a generic consequence of applying spectral clustering to any network.

## Interpretation

The experiment provides a stronger result than PGA 1.12.2.6 in one specific sense:

[
oxed{
	ext{coarse structure can be inferred from relational structure without prescribing the macro partition}
}
]

and, for the tested modular network,

[
oxed{
	ext{low-frequency relational modes}
ightarrow
	ext{stable effective partition}
}
]

The important conceptual chain is now:

microscopic relations
→ collective relational modes
→ emergent equivalence/partition structure
→ effective coarse-grained description.

## Status

**🟢 STRUCTURAL RESULT — stronger than PGA 1.12.2.6, but still a toy-model result.**

## Critical limitations

The modularity itself was built into the microscopic network generation through stronger intra-region coupling and weaker inter-region coupling.

Therefore this experiment does **not** establish that arbitrary microscopic S∞↔B∞ dynamics spontaneously generates physical objects.

It establishes a narrower point:

> When microscopic relational dynamics contains dynamically meaningful collective structure, a macroscopic partition can be recovered from relational information without explicitly supplying that partition to the reconstruction algorithm.

The result therefore removes one piece of observational scaffolding but does not remove the need to explain why the underlying S∞↔B∞ dynamics would generate such modular structure.

## Protection

Do not identify:

[
	ext{spectral cluster}=	ext{physical object}
]

or

[
	ext{spectral gap}=	ext{mass/particle/geometry}
]

without independent derivation.

Also do not identify this result with physical spacetime, time, c, quantum mechanics, or the Standard Model.

## Whole-research significance

This result connects the 1.12.2 branch to the broader S∞↔B∞ program:

[
S_inftyleftrightarrow B_infty
ightarrow
	ext{relational dynamics}
ightarrow
	ext{collective modes}
ightarrow
	ext{stable effective structures}
]

The same collective-mode machinery already appears in the quantum branch, while relational tensor/geometry work exists in the geometry branch.

This makes the result a possible **common intermediate layer**, but that cross-branch interpretation remains a hypothesis requiring separate tests.

## Next research question

The next substantive question is not another coverage test.

It is:

> Can the same relational dynamics simultaneously produce stable effective structures, causal propagation, and the spectral structure required by the quantum branch, without introducing separate mechanisms?

That is the point at which the 1.12.2 result should be transferred into the broader research architecture.
