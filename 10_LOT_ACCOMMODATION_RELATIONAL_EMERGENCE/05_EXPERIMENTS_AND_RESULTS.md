# Experiments and Results

## E1 — Hilbert-hotel accommodation
**Type:** ANALOGY / KNOWN MATHEMATICS. Infinite rooms can be re-indexed to accommodate another countably infinite population. Does not establish physical time, elasticity or spacetime.

## E2 — Finite response model
**Type:** TOY / MATH. Candidate `M x¨ + Γx˙ + Kx = -J`, static limit `δx=-K⁻¹J`. Provides a controlled response model, not spacetime elasticity.

## E3 — 2D weighted-network spectrum
**Type:** TOY / MATH. A localized coupling modification changes the global eigenvalue spectrum. Interpretation: local relational modification can alter collective modes. Boundary: expected network mathematics, not new physics.

## E4 — Coupling-dependent effective distance
**Type:** TOY / ILLUSTRATIVE. A radial coupling profile was explored using `ℓ_ij=1/√K_ij`. Path lengths changed after local coupling modification. Boundary: the mapping is arbitrary and is not evidence that physical distance obeys this law.

## E5 — Normal-mode / quantum direction
**Type:** HYPOTHESIS / OPEN. `L_Ku_n=λ_nu_n` suggests collective modes. Future quantization must determine whether known quantum structure can be recovered.

## E6 — Critical response
**Type:** HYPOTHESIS / OPEN. `det L_K→0` can indicate a zero/soft mode and loss of ordinary linear restoring response. Not identified with any astrophysical phenomenon.

## E7 — Parent-branch constraints
Existing S∞ ↔ B∞ work records failures of symmetry-only realization, naive feedback, memory-only persistence, noncommutativity alone, generic antisymmetry = time, and first-order diffusion/drift as a route to relativistic causal structure.

## Required next experiments
1. Derive K from S∞ rather than choosing it ad hoc.
2. Compare multiple distance constructions.
3. Test metric consistency.
4. Test finite-speed propagation.
5. Test two-source interaction through the modified background.
6. Test nonlinear response and criticality.
7. Establish the continuum limit before geometric claims.
8. Independently test known GR/QM benchmarks.

## Interpretation discipline
A toy-model success means only that the mechanism is mathematically possible in the tested model.

## Migration note
These are the preserved exploratory results available at the time of migration; they are not upgraded in status by relocation.

## E8 — PGA 1.6.4.2.1: Naive 3D → 2D relational projection

**Research Tree Node:** 1.6.4.2 — Pattern → 2D / Mandala Representation  
**PGA:** 1.6.4.2.1  
**Objective:** Test the simplest possible flattening of an organized relational structure and identify which relational information survives.

### Toy construction

Use a 3 × 3 × 3 cubic relational lattice:

- 27 relational nodes.
- Nearest-neighbour connectivity in 3 dimensions.
- 54 original nearest-neighbour edges.

Apply a naive 2D projection by dropping the third coordinate:

(x,y,z) → (x,y)

### Result

- 27 original nodes collapse onto only 9 distinct 2D positions.
- Three distinct nodes occupy each projected position.
- 27 distinct node-pairs become indistinguishable under the projection.
- The original lattice has 54 nearest-neighbour relations.
- If 2D adjacency is inferred only from projected (x,y) separation, 108 pairwise adjacencies are inferred.

### Status

**🔴 NAIVE FLATTENING FAILS as an information-preserving representation.**

The experiment does **not** show that 2D representation is impossible. It shows that simply projecting away one relational degree of freedom loses identity and creates ambiguous/false relations.

### What survives

A valid 2D/mandala representation would therefore need an additional encoding mechanism, such as:

- layer/index information;
- cuts and boundary markers;
- crossings/over-under information;
- labels or relational weights;
- or another invariant-preserving representation.

### Protection

This is a toy graph result. It does not imply that physical 3D space is literally projected from a higher-dimensional structure.

### Next test

**PGA 1.6.4.2.2:** test whether a structured unfolding/flattening can preserve a deliberately selected set of relational invariants (for example connectivity and boundary structure) without adding arbitrary physical assumptions.

## E9 — PGA 1.12.1.1: Quantization of B∞ normal modes

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.1  
**Objective:** Test whether the existing S∞ ↔ B∞ relational operator can support genuine quantum-mode structure, and explicitly separate what follows from the relational model from what must be added as a quantum postulate.

### Minimal toy system

Use a finite 1D B∞ relational chain with 5 nodes, unit mass matrix (M=I), and nearest-neighbour coupling (k=1).

The relational stiffness/Laplacian matrix is

[
K=
egin{pmatrix}
1&-1&0&0&0\\
-1&2&-1&0&0\\
0&-1&2&-1&0\\
0&0&-1&2&-1\\
0&0&0&-1&1
end{pmatrix}.
]

The classical normal-mode problem is

[
K u_n=lambda_n u_n,
qquad
omega_n=sqrt{lambda_n}.
]

The eigenvalues are approximately

[
0,;0.38197,;1.38197,;2.61803,;3.61803.
]

The zero mode corresponds to uniform translation of the finite free chain; it is not treated as an ordinary oscillator mode in the quantum-mode test.

### Quantum construction

For each nonzero normal mode, the standard canonical quantization gives

[
H_B=sum_n hbaromega_n
left(a_n^dagger a_n+rac12ight),
]

with

[
[a_n,a_m^dagger]=delta_{nm}.
]

Therefore each mode has the discrete energy spectrum

[
E_n=hbaromega_n
left(N_n+rac12ight),
qquad
N_n=0,1,2,ldots
]

and linear combinations of quantum states provide superposition; phase evolution provides interference in the usual quantum formalism.

### Critical audit

The **normal-mode spectrum is genuinely obtained from the relational B∞ model**.

However, the following ingredients were **not derived from S∞ ↔ B∞**:

- Hilbert-space structure;
- canonical commutation relations;
- the quantum state postulate;
- Born/probability interpretation;
- operator observables.

They were supplied by the standard canonical-quantization procedure.

Therefore this experiment does **not** establish that quantum mechanics emerges from S∞ ↔ B∞.

It establishes a narrower result:

> A relational B∞ system with a quadratic dynamical structure can provide a discrete set of collective modes that is mathematically compatible with canonical quantization.

### Status

**🟡 PARTIAL / BOUNDARY RESULT**

**Survives:** the existing relational operator supplies normal modes suitable for a quantum harmonic-mode construction.

**Fails as a derivation:** quantum structure itself is not generated by the relational model; it is imposed through canonical quantization.

This is an important boundary because it prevents the research from silently relabeling classical normal modes as quantum particles.

### Protection

[
	ext{B∞ normal mode} 
eq 	ext{quantum particle}
]

unless a further derivation establishes the quantum postulates or an equivalent emergent mechanism.

### Next question

The next quantum experiment should therefore ask whether any **pre-quantization relational mechanism** can produce a quantum-like state space, amplitudes, interference, or nonclassical correlations without simply inserting the canonical quantum postulates.

Potential routes remain open and must be tested separately rather than assumed.
