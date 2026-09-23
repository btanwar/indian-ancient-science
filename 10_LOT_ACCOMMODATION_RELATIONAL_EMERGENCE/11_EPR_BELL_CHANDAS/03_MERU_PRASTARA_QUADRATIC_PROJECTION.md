## RT-013 — Meru / Prastāra Quadratic Projection → Bell Route

**Research-tree registration:** `1.12.2.10.12`
**Detailed record:** `10_LOT_ACCOMMODATION_RELATIONAL_EMERGENCE/11_EPR_BELL_CHANDAS/03_MERU_PRASTARA_QUADRATIC_PROJECTION.md`

### Purpose

Test whether the Meru/Prastāra structure associated with Chandas supplies a natural projection/coarse-graining mechanism for the quadratic structure required by binary measurement probabilities, and whether that route can reach the Bell benchmark.

### Structural result

For two binary alternatives, Prastāra gives `00, 01, 10, 11`. Meru groups these by the number of selected components, giving the binomial multiplicities `1, 2, 1`.

`(a+b)^2 = a² + 2ab + b²`.

The outer classes provide `a²` and `b²`; the middle class provides the cross term `2ab`. For normalized amplitudes, `a²+b²=1`.

With the parameterization `a=cos(theta/2)`, `b=sin(theta/2)`:

- `P0=a²=cos²(theta/2)`
- `P2=b²=sin²(theta/2)`
- `P0-P2=cos(theta)`
- `2ab=sin(theta)`

Thus Meru/Prastāra supplies a candidate quadratic projection structure containing both complementary squared components and a cross/interference component.

### Bell-route benchmark

Using the additional two-component relational geometry `u(a)=(cos a,sin a)` and `u(b)=(cos b,sin b)`, their overlap is `cos(a-b)`. With anti-correlation, the candidate correlation is `E(a,b)=-cos(a-b)`.

For the standard CHSH settings `a=0°`, `a'=90°`, `b=45°`, `b'=-45°`, this benchmark gives `|S|=2sqrt(2)≈2.828`.

### Audit

🟢 Meru/Prastāra naturally supplies binomial multiplicity and a quadratic expansion.

🟢 The outer classes can form normalized complementary squared components when amplitudes are normalized.

🟢 The middle class is naturally the cross term.

🟡 The half-angle amplitude parameterization is not yet derived from Meru alone.

🟡 Selection of the outer classes as physical binary outcomes is not yet derived.

🟡 The two-sided nonseparable relational state is not yet derived from S∞ ↔ B∞.

🟡 The probabilistic interpretation is not yet derived from the substrate.

🔴 Therefore the CHSH value `2sqrt(2)` must be recorded as a downstream benchmark of the proposed construction, not as a demonstrated Bell violation derived from Meru/S∞ ↔ B∞ alone.

### Comparison with previous Chandas route

The earlier local 3-gaṇa-mode projection produced `E=-(1/3)cos(theta)` and stayed below the Bell bound. The Meru route is structurally different because its `1,2,1` binomial projection supplies a quadratic two-component construction without the `1/3` suppression.

### Next gate

**PGA 1.12.2.10.13 — Parameter-free Meru/S∞↔B∞ derivation:** derive the two-dimensional state, half-angle parameterization, outcome selection, and nonseparable A/B relational state without importing quantum projection rules.