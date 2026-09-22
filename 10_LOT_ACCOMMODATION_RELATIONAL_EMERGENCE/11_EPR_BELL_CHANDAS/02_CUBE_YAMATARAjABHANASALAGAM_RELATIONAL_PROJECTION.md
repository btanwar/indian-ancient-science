# 1.12.2.10 — Cube + Yamātārājabhānasalagam + Relational Projection

**Branch:** EPR / Bell / Chandas relational correlation
**Parent:** 1.12.2.10
**Status:** 🟡 PARKED AFTER SUBSTANTIAL PROGRESS
**Purpose:** Consolidate the later insight chain developed after the initial EPR/Bell/Chandas record.

## 1. Research question

Can a combined state of three binary variables be represented geometrically as an eight-vertex cube, ordered using the Yamātārājabhānasalagam structure, and then treated as a relational state whose binary measurement projections reproduce characteristic quantum correlations?

The investigation is deliberately separated into structural mathematics, model construction, and physical interpretation.

## 2. Three binary variables → cube

For

\[
(X,Z,Q)\in\{0,1\}^3,
\]

there are exactly

\[
2^3=8
\]

combined states. These can be represented by the eight vertices of the 3-dimensional Boolean cube \(Q_3\).

An edge connects states differing in exactly one binary coordinate.

This reframes the Bell/X–Z–Q combinatorial structure as a geometric configuration space rather than only an eight-row table.

### Important interpretation

The cube is a **configuration space**, not a claim that the physical EPR system is literally a cube.

## 3. Why the cube matters for Bell

A classical predetermined assignment chooses one vertex:

\[
(X,Z,Q).
\]

That simultaneously fixes the pairwise relations

\[
XZ,\quad ZQ,\quad XQ.
\]

For binary values \(\pm1\),

\[
(XZ)(ZQ)(XQ)=1.
\]

Thus the pairwise disagreement structure is constrained by a common predetermined assignment. This is the geometric/combinatorial side of the Bell counting argument.

A cube by itself therefore does **not** evade Bell.

## 4. Yamātārājabhānasalagam as an ordering

The three-syllable windows of the traditional Yamātārājabhānasalagam pattern provide the eight binary configurations once the two syllable classes are encoded as 0/1. The ordered windows used in the branch are:

\[
011\rightarrow111\rightarrow110\rightarrow101
\rightarrow010\rightarrow100\rightarrow000\rightarrow001.
\]

This gives a specific traversal of the eight configuration states.

The structural idea is therefore:

\[
\boxed{\text{configuration space} + \text{ordered traversal}}
\]

rather than configuration space alone.

The ordering should not be interpreted as a physical time sequence without an independent physical derivation of time.

## 5. Standalone Bell comparison

For the standard singlet target,

\[
E(a,b)=-\cos(a-b),
\]

with

\[
a=0^\circ,\quad a'=90^\circ,\quad b=45^\circ,\quad b'=-45^\circ,
\]

one obtains

\[
|S|=2\sqrt2\approx2.828>2.
\]

This is the standard mathematical quantum benchmark.

A classical cube with predetermined local outcomes remains subject to

\[
|S|\le2.
\]

## 6. Cube + ordered path + deterministic projection

The first modified-path test treated the ordered eight-state structure as a discrete shared variable and used local deterministic binary projections.

Result:

\[
|S|=2
\]

for the tested construction.

This is consistent with the Bell bound and is an important negative result: **Yamātārājabhānasalagam ordering alone does not produce Bell violation.**

Therefore:

\[
\text{cube} + \text{ordering} \neq \text{Bell violation by itself}.
\]

## 7. Relational-mode interpretation

The next modification was to stop treating the eight vertices as containers of predetermined measurement values.

Instead, the ordered configuration space is treated as supporting a relational mode.

For an 8-state cyclic representation, a discrete Fourier mode can be written as

\[
\psi_k(n)=\frac1{\sqrt8}e^{i2\pi kn/8}.
\]

The fundamental mode has a two-dimensional real representation

\[
u(n)=\cos(2\pi n/8),
\qquad
v(n)=\sin(2\pi n/8).
\]

Thus periodic ordering naturally supplies a phase-plane representation.

This establishes a mathematical route

\[
\boxed{\text{ordered finite state space}\rightarrow\text{periodic mode}\rightarrow\text{phase structure}.}
\]

## 8. Relative phase → cosine correlation

For a common periodic mode,

\[
\langle\cos\phi\cos(\phi+\theta)\rangle
=\frac12\cos\theta.
\]

After normalization, the relative-phase correlation is

\[
C(\theta)=\cos\theta.
\]

With the singlet anti-correlation convention,

\[
E(\theta)=-\cos\theta.
\]

The important insight is that the cosine can arise from the geometry of a common periodic relational mode rather than being inserted directly as the correlation law.

However, this does not by itself derive the physical quantum state or measurement law.

## 9. Binary projection of a relational mode

The proposed distinction is:

**Classical:**

\[
\text{vertex}\rightarrow\text{predetermined binary value}.
\]

**Relational-mode model:**

\[
\text{combined relational state}\rightarrow\text{measurement projection}\rightarrow\text{binary outcome}.
\]

For a two-component phase representation, a measurement basis at angle \(\alpha\) can be represented by orthogonal components. The projection amplitudes have the familiar form

\[
c_+=\cos\frac{\beta-\alpha}{2},
\qquad
c_-=\sin\frac{\beta-\alpha}{2}.
\]

Using quadratic weighting,

\[
P_+=|c_+|^2,
\qquad
P_-=|c_-|^2,
\]

gives

\[
P_+-P_- = \cos(\beta-\alpha).
\]

For the anti-correlated pair this yields the standard target

\[
E(a,b)=-\cos(a-b),
\]

and therefore

\[
|S|=2\sqrt2.
\]

### Protection

This step reproduces the quantum structure only after the projection geometry and quadratic probability rule are specified. It is therefore **not yet a derivation of quantum mechanics from Chandas**.

## 10. The norm / orthogonality insight

The investigation then isolated the role of orthogonality.

If a normalized state decomposes into orthogonal alternatives,

\[
\psi=\psi_++\psi_-,
\]

then Euclidean/Hilbert-like geometry gives

\[
\|\psi\|^2
=\|\psi_+\|^2+\|\psi_-\|^2.
\]

Under the assumptions of rotational symmetry, orthogonal additivity, normalization, and zero weight for a zero component, the natural normalized measure is quadratic:

\[
P_i=\frac{\|\psi_i\|^2}{\sum_j\|\psi_j\|^2}.
\]

This provides a **conditional structural route** to Born-type weighting.

It does not prove that nature must satisfy these assumptions, nor does it independently derive Hilbert-space structure from S∞ ↔ B∞.

## 11. What the branch has actually learned

The most useful conceptual distinction is:

\[
\boxed{\text{binary observed outcome} \neq \text{binary underlying state}.}
\]

A relational state can contain continuous/mode/phase information while a local measurement produces a discrete binary outcome through projection.

This architecture is capable of reproducing several familiar quantum structures in the controlled mathematical model:

- binary measurement outcomes;
- projection-dependent probabilities;
- cosine correlations;
- singlet-style \(-\cos\theta\) correlation;
- CHSH value \(2\sqrt2\);
- a no-signalling target distribution when
  \[
  P(A,B|a,b)=\frac14[1-AB\cos(a-b)];
  \]
- a distinction between shared relational state and locally accessible outcome.

This is a **promising structural mechanism**, not a completed explanation of quantum mechanics.

## 12. What remains unresolved

The following steps have not been derived from the S∞ ↔ B∞ framework:

1. Why the physical state should have the required phase geometry.
2. Why the relevant measurement components should be orthogonal.
3. Why probabilities should use the quadratic norm.
4. How the binary joint-outcome rule emerges without importing quantum measurement postulates.
5. How operational isolation is physically implemented while retaining the shared relational state.
6. Whether the mechanism generalizes beyond the tested Bell scenario to other quantum phenomena.

These are the correct future questions; they should not be silently treated as solved.

## 13. Color + charge — parked future direction

A further insight was identified but deliberately **not pursued in this branch**.

### Color

QCD has three color components conventionally labelled red, green, and blue. This is not the same mathematical object as the Boolean cube and should not be identified with it.

However, it supplies a potentially relevant physical clue:

\[
\boxed{\text{three-component internal structure}}
\]

can occur in established particle physics.

A possible future question is whether a three-component internal relational degree of freedom, when each component has two relational states, naturally produces a configuration space with

\[
2\times2\times2=8
\]

states.

### Charge / orthogonality

Charge or charge-sector structure may provide a future physical clue for distinguishing relational sectors and/or defining compatibility/orthogonality. The speculative chain to test later is

\[
\text{internal relational sectors}
\rightarrow
\text{compatibility / conservation}
\rightarrow
\text{inner product / orthogonality}
\rightarrow
\text{quadratic norm}.
\]

No physical identification is claimed here.

## 14. Final branch conclusion / stopping point

This branch has reached a logical checkpoint.

The controlled progression is:

\[
\boxed{
\text{3 binary variables}
\rightarrow
\text{8-state cube}
\rightarrow
\text{Yamātārājabhānasalagam ordering}
\rightarrow
\text{periodic relational mode}
\rightarrow
\text{phase/cosine structure}
\rightarrow
\text{binary projection}
\rightarrow
\text{quantum-like correlation}
}
\]

The branch does **not** claim that this sequence derives quantum mechanics. It establishes a concrete model architecture that can reproduce several standard quantum phenomena once its projection/norm assumptions are supplied, and it identifies exactly where a deeper S∞ ↔ B∞ derivation would have to enter.

This is therefore a **logical stopping point**, not a failed branch.

The Color + Charge direction is explicitly parked for possible future work rather than extended now.

## 15. Research protection

- Cube ≠ physical EPR geometry.
- Yamātārājabhānasalagam ordering ≠ physical time.
- Chandas ≠ quantum mechanics.
- Color ≠ Boolean cube.
- Charge ≠ orthogonality by identification.
- Cosine correlation ≠ proof of S∞ ↔ B∞.
- Reproducing CHSH violation under supplied quantum projection rules ≠ deriving Bell violation from S∞ ↔ B∞.
- The branch's value is the identification of a plausible relational-state → projection architecture and its exact unresolved assumptions.
