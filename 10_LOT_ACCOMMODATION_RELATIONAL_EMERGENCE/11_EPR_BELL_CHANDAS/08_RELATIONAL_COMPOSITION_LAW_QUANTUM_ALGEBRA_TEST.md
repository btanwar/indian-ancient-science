# PGA 1.12.2.10.18 — Relational Composition Law → Quantum Algebra Test

## Objective

Attempt to derive orthogonality, completeness, tensor-product composition, noncommutativity, and no-signalling from one relational composition principle, rather than importing these as separate quantum axioms.

## 1. Composition principle

Let a relational state be a set of distinguishable projection channels. Define composition by preservation of the quadratic relational weight.

For mutually exclusive channels i and j, impose:

  W(i ∪ j)=W(i)+W(j).

For coherent channels, retain the cross term:

  W(i+j)=W(i)+W(j)+2 Re(z_i* z_j).

This immediately distinguishes two relations:

- additive/exclusive relation;
- coherent/phase-sensitive relation.

## 2. Orthogonality

Define two channels to be orthogonal when their composition has no cross contribution for every relative phase:

  Re(z_i* z_j)=0 for all allowed phase rotations.

The only stable way for this to hold under arbitrary common phase rotation is

  z_i* z_j=0.

Thus orthogonality can be defined operationally by absence of relational interference.

This is stronger than simply postulating a Hilbert-space inner product: orthogonality is tied to a measurable composition property.

## 3. Completeness

A measurement is complete when its mutually exclusive outcome channels exhaust the total relational weight:

  Σ_i W_i = W_total.

For normalized states:

  Σ_i P_i=1.

Thus completeness follows from conservation/additivity of the total quadratic weight, provided the measurement partition is exhaustive.

## 4. Projector structure

Associate each exclusive outcome class C_i with a map M_i satisfying

  M_i²=M_i.

Mutual exclusivity gives

  M_i M_j=0, i≠j.

Completeness gives

  Σ_i M_i=I.

Therefore the standard orthogonal-projector relations arise from the algebra of exhaustive mutually exclusive relational coarse-grainings.

### Audit

The operational meaning is derived; the full linear-operator representation remains a mathematical realization of that operational structure.

## 5. Tensor-product composition

For two systems with local relational classes i and j, the joint classes are ordered pairs (i,j).

The number of joint classes is d_A d_B.

If amplitudes compose independently:

  z_ij=a_i b_j.

The joint norm factorizes:

  Σ_ij |z_ij|²=(Σ_i|a_i|²)(Σ_j|b_j|²).

This is exactly the norm behavior required by tensor-product composition.

Entangled states are the general non-factorizable joint amplitude arrays.

Thus tensor-product dimension and factorized states have a direct relational-combinatorial origin.

## 6. Noncommutativity

Consider two different coarse-grainings A and B.

If A changes the relational equivalence classes used by B, then sequential conditioning differs from the reverse order:

  M_A M_B ψ ≠ M_B M_A ψ.

Therefore noncommutativity has a direct relational interpretation:

  order-dependent coarse-graining
      → noncommuting projections.

However, this is not universal: commuting coarse-grainings remain possible. The remaining task is to derive the exact quantum commutator structure and its numerical scale.

## 7. No-signalling

For a joint relational probability P(A,B|a,b), operational isolation requires:

  Σ_B P(A,B|a,b)=P(A|a)

independent of b, and

  Σ_A P(A,B|a,b)=P(B|b)

independent of a.

The existing Meru Bell construction satisfies this benchmark.

At the structural level, no-signalling follows if local projection/conditioning on A cannot alter the marginal weight assigned to B's local classes except through the shared relational correlation.

This is consistent with the project's principle:

  operational isolation ≠ relational independence.

## 8. What one composition law now explains

The quadratic relational composition principle can account for:

  exclusive addition
  → orthogonality criterion
  → completeness
  → projector structure
  → tensor-product dimension
  → factorized vs entangled states
  → order-dependent projections
  → no-signalling constraint.

This is a significant unification of previously separate quantum ingredients.

## 9. What remains genuinely unexplained

The following are still not derived uniquely:

1. Why the relational amplitude field must be complex rather than another normed algebra.
2. Why the inner product must be exactly sesquilinear.
3. Why all physical measurements admit the projector/coarse-graining structure above.
4. The exact commutator [A,B] and the universal constant ħ.
5. The dynamical generator H.
6. Position/momentum and spacetime representation.
7. Relativistic quantum field structure.

## Verdict

**🟢 Structural quantum algebra largely survives as a relational construction.**
**🟡 Uniqueness and physical derivation remain open.**

The important result is not that every quantum axiom has been proved. It is that several apparently independent rules can now be traced to one underlying distinction:

  relational composition may be either exclusive/additive or coherent/phase-sensitive.

## Next gate

**PGA 1.12.2.10.19 — Derive the quantum commutator and ħ from relational phase/coverage dynamics.**

This is the next decisive gate because it connects the static quadratic state structure to dynamical quantum mechanics.
