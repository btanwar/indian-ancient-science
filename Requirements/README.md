# Requirements

For each line of thought, this folder defines **what must be true, proven, measured, or built** for
it to evolve into a successful theory, law, postulate, or technology — written before deep research
begins, so success criteria are not redefined after the fact to fit whatever result appears.

Copy [`templates/REQUIREMENTS.md`](../templates/REQUIREMENTS.md) to create a new requirements doc, name it `R###_short-name.md` (matching the
corresponding `Line-Of-Thoughts/L###_short-name.md`), and add a row to the index table below.

## Rules

- Requirements are **falsifiable**: each one should have a clear pass/fail condition.
- List requirements in the order they should be attempted (a runbook in `Research/` will follow
  this order, or explicitly justify a deviation).
- Distinguish requirements that are:
  - mathematical/theoretical (must be formally derivable),
  - experimental/computational (must be demonstrated numerically or physically),
  - comparative (must be shown to differ from, or reduce to, known existing science).
- Update the status of each requirement as research produces results; never silently remove a
  requirement that failed — mark it `FAILED`/`ABANDONED` instead.

## Index

Constructed (Phase 3) for each `Line-Of-Thoughts/` entry from Phase 2. Requirement lists reuse the
source projects' own gates/decision-criteria where available (e.g. V2's hard-gate sequence, E002's
required controls) rather than inventing new pass/fail conditions.

| ID | Name | Line of thought | # Requirements | Status |
|---|---|---|---|---|
| [R001](R001_ordered_coverage_observer_time.md) | Ordered Coverage and Observer Time | [L001](../Line-Of-Thoughts/L001_ordered_coverage_observer_time.md) | 6 | IN_PROGRESS |
| [R002](R002_emergent_dimension_relational_capacity.md) | Emergent Dimension from Relational Capacity | [L002](../Line-Of-Thoughts/L002_emergent_dimension_relational_capacity.md) | 5 | PROPOSED |
| [R003](R003_coupled_oscillator_cosmic_mechanism.md) | Damru as Cosmic Phenomenon (Coupled Oscillator / GW–EM / Ramanujan Transition Line) | [L003](../Line-Of-Thoughts/L003_coupled_oscillator_cosmic_mechanism.md) | 5 | PAUSED |
| [R004](R004_hidden_state_observer_accessibility.md) | Hidden State, Visibility, and Observer Accessibility | [L004](../Line-Of-Thoughts/L004_hidden_state_observer_accessibility.md) | 5 | PARTIAL |
| [R005](R005_complementary_channel_unification.md) | Complementary-Channel Unification (Audio/Video, GW/EM) | [L005](../Line-Of-Thoughts/L005_complementary_channel_unification.md) | 4 | OPEN |
| [R006](R006_s_infinity_b_infinity_relational_substrate.md) | S∞/B∞ Relational Substrate | [L006](../Line-Of-Thoughts/L006_s_infinity_b_infinity_relational_substrate.md) | 6 | IN_PROGRESS |
