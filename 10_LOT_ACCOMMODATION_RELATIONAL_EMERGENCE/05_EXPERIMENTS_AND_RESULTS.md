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


## E10 — PGA 1.12.1.2: Pre-quantization superposition/interference test

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.2  
**Objective:** Test whether the relational model itself can generate quantum-like superposition/interference before canonical quantum postulates are introduced.

### Minimal test

Take two independent classical normal modes of the same relational B∞ system, with amplitudes (q_1(t)) and (q_2(t)). Because the underlying linear relational dynamics is linear, any combination

\[
q(t)=c_1q_1(t)+c_2q_2(t)
\]

is also a valid classical solution.

For a harmonic pair with equal frequency, write

\[
q_1(t)=A\cos(\omega t),
\qquad
q_2(t)=A\sin(\omega t).
\]

A general linear combination is therefore

\[
q(t)=A[c_1\cos(\omega t)+c_2\sin(\omega t)].
\]

This demonstrates **classical linear superposition**.

If two contributions are measured through a quadratic observable, cross terms can appear:

\[
|q_1+q_2|^2=|q_1|^2+|q_2|^2+2q_1q_2.
\]

Thus an interference-like pattern can also arise classically from the relational wave dynamics.

### Critical audit

This is an important negative/boundary result.

The model can generate:

- linear superposition of classical solutions;
- phase-dependent interference-like cross terms.

But these facts **do not distinguish classical wave mechanics from quantum mechanics**.

Nothing in this test by itself supplies:

- quantum state vectors;
- Born probabilities;
- noncommuting observables;
- entanglement;
- Bell-type nonlocal correlations.

Therefore:

\[
\boxed{\text{classical superposition + interference} \neq \text{quantum theory}}
\]

### Status

**🟡 BOUNDARY RESULT — classical mechanism insufficient**

The test survives as a consistency result but fails as a quantum-emergence demonstration.

### Research implication

The next quantum test should not merely search for stronger interference. It must target a feature that cannot be reproduced by an ordinary classical linear wave model, while still avoiding insertion of the desired quantum structure by hand.

Candidate next target:

**PGA 1.12.1.3** — investigate whether coupled S∞↔B∞ subsystems can produce a genuine nonseparable state structure (an entanglement analogue) from the relational dynamics alone.


## E10 — PGA 1.12.1.2: Pre-quantization superposition/interference test

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.2  
**Objective:** Test whether the relational model itself can generate quantum-like superposition/interference before canonical quantum postulates are introduced.

### Minimal test

Take two independent classical normal modes of the same relational B∞ system, with amplitudes q₁(t) and q₂(t). Because the underlying linear relational dynamics is linear, any combination

q(t) = c₁q₁(t) + c₂q₂(t)

is also a valid classical solution.

For a harmonic pair with equal frequency,

q₁(t) = A cos(ωt),   q₂(t) = A sin(ωt).

A general linear combination is therefore

q(t) = A[c₁ cos(ωt) + c₂ sin(ωt)].

This demonstrates classical linear superposition.

If two contributions are measured through a quadratic observable, cross terms can appear:

|q₁ + q₂|² = |q₁|² + |q₂|² + 2q₁q₂.

Thus an interference-like pattern can also arise classically from the relational wave dynamics.

### Critical audit

This is an important boundary result.

The model can generate:
- linear superposition of classical solutions;
- phase-dependent interference-like cross terms.

But these facts do not distinguish classical wave mechanics from quantum mechanics.

Nothing in this test by itself supplies:
- quantum state vectors;
- Born probabilities;
- noncommuting observables;
- entanglement;
- Bell-type nonlocal correlations.

Therefore:

**classical superposition + interference ≠ quantum theory.**

### Status

**🟡 BOUNDARY RESULT — classical mechanism insufficient**

The test survives as a consistency result but fails as a quantum-emergence demonstration.

### Research implication

The next quantum test should target a feature that cannot be reproduced by an ordinary classical linear wave model, while still avoiding insertion of the desired quantum structure by hand.

**PGA 1.12.1.3** — investigate whether coupled S∞↔B∞ subsystems can produce a genuine nonseparable state structure (an entanglement analogue) from the relational dynamics alone.


## E11 — PGA 1.12.1.3: Coupled-subsystem nonseparability test

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.3  
**Objective:** Test whether coupled S∞↔B∞ subsystems can produce a genuinely nonseparable state structure without inserting quantum entanglement by assumption.

### Minimal classical relational model

Consider two subsystems, A and B, each represented by a single relational degree of freedom, with coupled quadratic energy

E = 1/2 k_A x_A² + 1/2 k_B x_B² + κ x_A x_B.

The coupling term means the equations for A and B are not independent:

m_A ẍ_A + k_A x_A + κx_B = 0,

m_B ẍ_B + k_B x_B + κx_A = 0.

Diagonalizing the coupled system produces collective normal modes that are linear combinations of the local coordinates:

u₊ = c_A x_A + c_B x_B,

u₋ = d_A x_A + d_B x_B.

### Result

The coupled relational system produces **collective/nonlocal-in-coordinate modes**: the normal modes of the whole system cannot, in general, be assigned to A or B independently.

However, this is still ordinary classical coupled-oscillator physics.

A classical state of the coupled system remains describable by the joint phase-space variables

(x_A,p_A,x_B,p_B).

No quantum tensor-product state space has been derived, and no quantum entanglement has been generated.

### Stronger diagnostic

A genuine quantum-entanglement claim would require a state description for which the joint state cannot be represented as a product of subsystem states,

|Ψ_AB⟩ ≠ |ψ_A⟩⊗|ψ_B⟩,

together with quantum observables and a probability rule.

Those ingredients are not supplied by the classical relational model.

### Status

**🔴 FAILS AS A QUANTUM-EMERGENCE MECHANISM / 🟢 SURVIVES AS RELATIONAL COLLECTIVITY**

The experiment is therefore valuable because it separates two ideas that had been close together:

**shared relational coupling ≠ quantum entanglement.**

The S∞↔B∞ mechanism can already produce collective modes spanning multiple localized subsystems, but that alone does not provide nonclassical entanglement.

### Protection

Do not relabel a collective classical mode as an entangled quantum state.

### Next question

The research should now move one level deeper: determine whether there is any **pre-quantization algebraic structure** in S∞↔B∞—for example constrained composition, noncommuting transformations, or contextual state update—that can produce a quantum state space rather than merely coupled classical dynamics.

**PGA 1.12.1.4** — test whether the relational composition/update algebra itself can generate noncommuting observables or an equivalent quantum structure, without postulating Hilbert-space quantum mechanics at the start.


## E12 — PGA 1.12.1.4: Relational composition/update algebra test

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.4  
**Objective:** Test whether the S∞↔B∞ relational composition/update rules themselves can generate noncommuting transformations, rather than inserting quantum commutators by assumption.

### Minimal test

Represent a local relational update as an operator acting on the background state. For two updates A and B, compare the two orders:

A(B(X)) versus B(A(X)).

Define the commutator-like difference

[A,B]X = A(B(X)) - B(A(X)).

A nonzero result would establish **order dependence of relational updates**.

### Controlled toy construction

Let X=(x,y) and define two shear-type relational updates:

A(x,y) = (x + αy, y),

B(x,y) = (x, y + βx).

Then

A∘B(x,y)
= ((1+αβ)x + αy, y+βx),

while

B∘A(x,y)
= (x+αy, βx + (1+αβ)y).

For nonzero α and β these are generally different.

Thus

A∘B ≠ B∘A.

### Critical audit

This demonstrates that **noncommuting transformations can arise naturally from composition of relational updates**.

However, noncommutativity alone is not quantum mechanics.

The model has not derived:

- Hermitian quantum observables;
- canonical commutation relations;
- Planck's constant;
- Hilbert-space amplitudes;
- Born probabilities;
- quantum measurement statistics.

Therefore the result is:

**🟢 relational noncommutativity survives as a mathematical possibility**

but

**🔴 noncommutativity alone fails as a quantum-emergence mechanism.**

### Important distinction

The earlier branch had already recorded that **noncommutativity alone does not establish time or quantum mechanics**. This experiment sharpens that boundary:

[
	ext{order-dependent relational updates}

eq
	ext{quantum observables}.
]

The research value is that noncommutativity can now be treated as a possible structural ingredient rather than a claimed explanation.

### Next question

The next experiment should ask whether the relational update algebra can acquire the additional structure required for a physical observable algebra—especially a scale with the dimensions and empirical role of (hbar)—without inserting those structures by hand.

**PGA 1.12.1.5** — dimensional/scale audit of the relational algebra and search for a dynamically generated action scale.


## E13 — PGA 1.12.1.5: Relational action-scale audit

**Research Tree Node:** 1.12.1 — Quantized B∞ Modes  
**PGA:** 1.12.1.5  
**Objective:** Determine whether the existing relational dynamics naturally contains an action scale that could play a structural role analogous to ℏ, without inserting ℏ by hand.

### Dimensional audit

The present classical relational model contains quantities such as mass (M), stiffness/coupling (K), displacement (x), time (t), and energy/action derived from the chosen Lagrangian.

For a harmonic mode,

[
H_n=rac12 p_n^2+rac12omega_n^2 q_n^2
]

after suitable normalization. The action scale associated with a trajectory is

[
S=int L,dt,
]

but the magnitude of (S) is determined by the chosen physical normalization of (M,K,q,t).

No dimensionless relational invariant in the current model fixes a universal action quantum.

### Rescaling test

Under a change of normalization of the dynamical coordinate,

[
qightarrow a q,
]

the numerical coefficients in the action and canonical momentum change correspondingly. Likewise, changing the overall energy/coupling scale changes the numerical value of the action while leaving the qualitative normal-mode structure intact.

Therefore the present relational equations possess **scale freedom**: the model does not select one universal action scale from its internal structure.

### Result

**🔴 No dynamically derived ℏ-like universal action scale was found in the present model.**

The relational framework can certainly be assigned an action dimension, but dimensional compatibility is not derivation.

### Important interpretation

This does **not** prove that S∞↔B∞ cannot generate ℏ.

It establishes a more precise boundary:

> The current quadratic relational model does not contain enough internal structure to determine a universal quantum action scale.

A future derivation would therefore need an additional dimensionless invariant, quantization condition, topological number, compact phase, or other mechanism that fixes an action scale rather than allowing arbitrary rescaling.

### Status

**🔴 FAIL / OPEN GATE**

- ✅ Action can be defined for the relational dynamics.
- ❌ Universal action quantum is not derived.
- ❌ ℏ must not be inserted and then claimed as emergent.

### Next question

The quantum branch should now investigate whether a **compact/topological relational degree of freedom** can introduce a discrete invariant that removes the continuous action-scale freedom.

**PGA 1.12.1.6** — test compact phase/topological quantization as a possible source of a discrete action scale.


## E14 — PGA 1.12.2.2: Observable Reconstruction / Emergent Time / Emergent-c Audit

**Research Tree Node:** 1.12.2 — Observable Reconstruction / Time / Causal Ordering  
**PGA:** 1.12.2.2  
**Status:** 🟡 PARTIAL SUCCESS / OPEN GATE

### Branch purpose
Audit the earlier framing–sampling–coverage–sequence–reconstruction work and determine whether it established emergent time, observer-independent temporal scale, finite causal speed, and Lorentzian spacetime.

### Historical findings
- Physical information acquisition: 🟢 toy-level support.
- Accumulated coverage → reconstruction/frame: 🟢 toy-level support.
- Different information subsets → compatible reconstruction: 🟢 toy-level support, with geometry still present in the toy substrate.
- Local causal precedence without a global clock: 🟢 toy-level support.
- Global causal ordering: 🟢 reconstructed as a DAG/topological partial order.
- Unique global sequence: 🔴 not established and not required; causally incomparable events remain possible.
- Continuous physical time: 🔴 not derived.
- Observer-independent temporal scale: 🔴 not derived.

### Emergent-c audit
Earlier work did investigate finite propagation. Discrete/local models produced finite causal fronts with representative scale c_D = a√(κ/m), and long-wavelength behavior ω ≈ c_D k. Ordered-local dynamics similarly produced c* = ℓ*/τ* and a finite causal front.

These results establish **finite propagation in toy models**, not a universal physical speed c.

A random 256-node 4-regular network instead produced rapid reachability saturation and failed to produce a geometric causal cone.

A fixed lattice produced finite propagation and approximate IR linearity but retained a preferred microscopic frame, with v_g = c_D cos(ka/2). Therefore exact Lorentz invariance was not derived.

The earlier dimensional audit also rejected identifying ordinary sampling frequency with c because 1/s ≠ m/s. The refined hypothesis is c* = emergent relational distance / emergent relational duration.

### Lorentz audit
Three requirements were identified for a stronger emergent Lorentz claim:

1. isotropy;
2. universal low-energy propagation speed;
3. observer-independent reconstruction of the same causal/null structure.

The existing experiments do not establish all three simultaneously. A mathematical Lorentz reconstruction from an already-given causal structure was demonstrated, but the causal structure itself has not yet been derived from the microscopic S∞ ↔ B∞ substrate.

### Corrected result
The previous coarse statement "finite causal speed c not demonstrated" is too broad. The correct statement is:

> **Finite propagation speed has been demonstrated in several toy relational models; a universal, observer-independent physical c has not been derived. Lorentzian spacetime has not been derived.**

### Closure
PGA 1.12.2.2 is closed as a **partial-success audit checkpoint**, not as a failed branch.

### Next node
**PGA 1.12.2.3 — Metric-Free Relational Time + c + Causal-Cone Test.**

The next test must remove coordinates, metric, physical time, and assumed c from the microscopic rules and measure relational ordering, distance, operational duration, propagation reach, isotropy, observer reconstruction, and dispersion.


## E15 — PGA 1.12.2.3: Metric-Free Relational Time + c + Causal-Cone Test

**Research Tree Node:** 1.12.2 — Observable Reconstruction / Time / Causal Ordering  
**PGA:** 1.12.2.3  
**Objective:** Test the integrated branch using relational graph distance and causal update depth, without inserting a coordinate metric, physical time, or a named physical c.

### Minimal construction

The substrate is represented only by a graph G=(V,E) and local nearest-neighbour update propagation.

Define relational distance operationally as shortest-path length:

\[
D_G(A,B)=\text{number of relational links on the shortest path}.
\]

Define operational duration as causal update depth:

\[
T_G(E)=\text{number of local causal update layers required to reach }E.
\]

No seconds, metres, spacetime metric, or physical c are inserted.

The candidate relational propagation ratio is then

\[
c_R=\frac{D_G}{T_G}.
\]

### Test A — Local ordered networks

For local square and triangular lattice graphs, a disturbance propagating one relational edge per causal update produces a finite causal front. In relational units,

\[
D_G=T_G
\]

for the leading front, giving

\[
c_R=1\ \text{relational link/update}.
\]

The square and triangular constructions show expanding fronts rather than instantaneous all-to-all reachability. The triangular connectivity gives a more directionally distributed local neighbourhood than the square case.

### Test B — Random relational network

The previously audited 256-node 4-regular random network again provides the required control: reachability saturates rapidly rather than forming a geometric expanding cone.

Representative cumulative reach from one source:

\[
1\rightarrow5\rightarrow17\rightarrow51\rightarrow125\rightarrow226\rightarrow256.
\]

Thus local relational connectivity is not sufficient by itself; locality/organization of connectivity is essential.

### Test C — Observer reconstruction

An observer that samples only the event/propagation relations can reconstruct graph distance and causal depth from the retained relational links. Because both quantities are defined from the same underlying relational graph, observers with sufficient compatible coverage recover the same dimensionless relational ratio.

This survives as a **relational operational consistency result**.

### Critical audit

The result \(c_R=1\) is not yet a derivation of physical c. The numerator and denominator were both defined using the same graph/update units. Therefore the experiment demonstrates a coherent internal causal speed scale, but not a universal physical dimensional constant.

In particular, the experiment has not derived:

- a metre-like spatial unit;
- a second-like temporal unit;
- a unique conversion between them;
- an observer-independent dimensional value of c;
- Lorentz invariance;
- Lorentzian spacetime.

This is exactly the distinction anticipated in PGA 1.12.2.2: **finite propagation is established in toy relational models, while universal physical c remains open.**

### Result

**🟢 Local relational causality survives:** organized local connectivity + local updates produce finite causal cones.

**🟢 Dimensionless relational propagation ratio survives:** (c_R=D_G/T_G) is stable in the ideal local-update model.

**🔴 Universal physical c is NOT derived:** the scale is still defined in substrate units.

**🔴 Lorentzian spacetime is NOT derived.**

### Stronger inference

The branch can now legitimately claim:

\[
\boxed{\text{organized local relational dynamics can generate a causal cone and an internal propagation ratio.}}
\]

It cannot yet claim:

\[
\boxed{\text{the physical speed of light or Lorentzian spacetime emerges.}}
\]

### Next required gate

The next experiment must remove the hidden calibration freedom. The key question is whether **relational distance and relational duration can acquire independent, observer-independent scales from the same S∞↔B∞ dynamics**, rather than both being measured in the same graph/update unit.

**Next node: PGA 1.12.2.4 — Independent Relational Space/Time Scale and Observer-Clock Consistency Test.**

## E16 — PGA 1.12.2.4: Information Coverage / Boundary Interaction / Propagation Test

**Research Tree Node:** 1.12.2 — Observable Reconstruction / Time / Causal Ordering  
**PGA:** 1.12.2.4  
**Objective:** Test the recovered hypothesis that the role of light may be understood operationally as propagation of information between physical boundaries, while observable objects/frames arise through accumulated information coverage and coarse-graining. The experiment specifically separates propagation speed from total boundary coverage and reconstruction sufficiency.

### Refined hypothesis

The working hypothesis is not that physical c is simply coverage per second.

Instead:

t_arrival(x) = d(x) / c_*

and boundary coverage at duration t is

C(t) = measure{x in boundary : d(x) <= c_* t} / measure(boundary).

Here c_* is the propagation limit, while C(t) is the amount of boundary information that has become accessible. The two quantities must not be conflated.

### Test A — Same propagation speed, different boundaries

A point source was placed at the centre of three idealized 2D boundaries, with propagation speed normalized to c_* = 1:

1. circle of radius 10;
2. square with half-side 10;
3. rectangle with half-width 10 and half-height 5.

For each boundary point, arrival time was taken as its source-to-boundary distance. Coverage was the fraction of boundary reached by time t.

Representative results:

| t | Circle C(t) | Square C(t) | Rectangle C(t) |
|---:|---:|---:|---:|
| 5.0 | 0.000 | 0.000 | ~0.000 |
| 5.5 | 0.000 | 0.000 | 0.274 |
| 6.0 | 0.000 | 0.000 | 0.373 |
| 7.0 | 0.000 | 0.000 | 0.494 |
| 8.0 | 0.000 | 0.000 | 0.570 |
| 9.0 | 0.000 | 0.000 | 0.625 |
| 10.0 | 1.000 | ~0.000 | 0.667 |
| 10.5 | 1.000 | 0.395 | 0.881 |
| 11.0 | 1.000 | 0.547 | 0.973 |
| 11.5 | 1.000 | 0.658 | 1.000 |

The propagation law is identical in all three cases, but the coverage function is strongly geometry-dependent.

### Result A

coverage rate is not itself a universal propagation constant.

The same propagation speed can produce radically different coverage histories because boundary geometry determines how much boundary becomes reachable at each time.

### Test B — Coverage amount is not sufficient for reconstruction

Consider two possible boundary configurations B1 and B2 that are identical over the observed subset S, but differ over the unobserved complement. An observer receiving exactly the information from S cannot distinguish B1 from B2 even if the observed coverage fraction is large.

Therefore:

coverage fraction alone does not determine reconstruction.

The location, independence, and relational content of the observations matter.

### Coarse-graining interpretation

The useful hierarchy is therefore:

propagation
→ boundary interaction
→ information acquisition
→ coverage pattern
→ coarse-graining
→ reconstruction.

This gives a more precise interpretation to the earlier photon/observer/frame line of thought.

A photon need not be treated as creating the object. Rather, interaction with a physical boundary changes the propagating information, and an observing system can use an accumulated set of such interactions to reconstruct a stable coarse-grained description.

### Critical audit

The experiment does not derive physical c, photon ontology from S∞ ↔ B∞, a universal information rate, a unique reconstruction algorithm, physical spacetime, or Lorentz invariance.

What it does establish at toy/logical level is narrower:

1. finite propagation can control the arrival envelope of information;
2. boundary geometry controls the resulting coverage function;
3. coverage is an information-access variable, not itself a universal speed;
4. coverage fraction alone is insufficient for reconstruction;
5. the earlier observer/frame idea is better formulated in terms of distributed relational information and coarse-grained reconstruction.

### Status

**🟢 SURVIVES AS A STRUCTURAL/OPERATIONAL RESULT**

**🔴 Fails if interpreted as c = d(coverage)/dt.**

The stronger hypothesis that remains open is:

physical c may be the invariant limit governing the propagation of information,

while observable-frame formation may depend on the accumulated and structured coverage of boundary interactions.

### Protection

Do not identify:

c = coverage rate,
photon = observer,
coarse-grained object = fundamental object.

These remain hypotheses unless independently derived.

### Next node

**PGA 1.12.2.5 — Observer-Coverage / Reconstruction Invariance Test**

The next test should hold the underlying boundary configuration fixed while varying observer sampling paths, angular coverage, temporal sampling, and coarse-graining resolution. The target is to determine whether sufficiently complete relational information produces an observer-independent coarse-grained object/frame, and whether the propagation limit enters only through the information-arrival boundary rather than through the reconstruction rule itself.
