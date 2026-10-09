# Equation Audit

## Scope

Scanned `92` maintained Markdown files under the project root. Skipped raw `chat_records/`, `promtps/`, fenced code blocks, and non-Markdown assets.

## Formatting pass

- Files modified: `70`
- High-confidence inline expressions converted: `350`
- Ambiguous inline-code spans intentionally left unchanged: `299`
- Display-math fenced blocks found: `0` in the baseline scan; no math-fence syntax was introduced.
- Scientific content changed: **NO**.

## Rules applied

High-confidence equation-like inline code was changed from backticks to `\(...\)` and common Unicode operators/Greek symbols were mapped to LaTeX commands. Code fences, paths, identifiers, source provenance, numerical values, and historical claims were left unchanged.

## Manual review

Ambiguous expressions and plain-text equations outside high-confidence inline spans remain for manual review. No signs, constants, approximation symbols, proportionality symbols, conclusions, or historical statuses were intentionally changed.

## Renderer assumption

The repository uses Markdown with KaTeX-compatible inline `\(...\)` and display `\[...\]` mathematics. No dedicated math-fence blocks were introduced.

## Modified files

- `AI_RESEARCH_PROTOCOL.md`
- `README.md`
- `Analogies/A001_damru.md`
- `Analogies/A002_orchestra.md`
- `Analogies/A003_vcr_cinema_sequential_coverage.md`
- `Analogies/A004_audio_video_channels.md`
- `Analogies/A005_fan_sampling.md`
- `Analogies/A006_bead_string.md`
- `Analogies/A007_fabric_spacetime.md`
- `Analogies/A008_space_as_capacity.md`
- `Analogies/A009_sugar_dissolving_visibility.md`
- `Analogies/A010_indra_net.md`
- `Analogies/A011_meru_prastara.md`
- `Analogies/A012_meru_parvat.md`
- `Analogies/A013_ramanujan_mathematics.md`
- `Analogies/A014_sri_meru_yantra.md`
- `Analogies/A015_mala_dna.md`
- `Analogies/A016_gunas_chakras_bandhas.md`
- `Analogies/A017_observer_cinema_audience.md`
- `Analogies/A018_s_infinity_b_infinity.md`
- `Analogies/A019_illumination_observable_capacity.md`
- `Analogies/README.md`
- `Line-Of-Thoughts/L001_ordered_coverage_observer_time.md`
- `Line-Of-Thoughts/L002_emergent_dimension_relational_capacity.md`
- `Line-Of-Thoughts/L003_coupled_oscillator_cosmic_mechanism.md`
- `Line-Of-Thoughts/L004_hidden_state_observer_accessibility.md`
- `Line-Of-Thoughts/L005_complementary_channel_unification.md`
- `Line-Of-Thoughts/L006_s_infinity_b_infinity_relational_substrate.md`
- `Line-Of-Thoughts/README.md`
- `Requirements/R001_ordered_coverage_observer_time.md`
- `Requirements/R002_emergent_dimension_relational_capacity.md`
- `Requirements/R003_coupled_oscillator_cosmic_mechanism.md`
- `Requirements/R004_hidden_state_observer_accessibility.md`
- `Requirements/R005_complementary_channel_unification.md`
- `Requirements/R006_s_infinity_b_infinity_relational_substrate.md`
- `Research/EXPERIMENT_SOURCE_INVENTORY.md`
- `Research/README.md`
- `templates/RESEARCH_RUNBOOK.md`
- `Research/L001_ordered_coverage_observer_time/runbook.md`
- `Research/L002_emergent_dimension_relational_capacity/runbook.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/runbook.md`
- `Research/L004_hidden_state_observer_accessibility/runbook.md`
- `Research/L005_complementary_channel_unification/runbook.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/runbook.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/results/E001_geometry_and_persistence_audit.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/results/E002_landmark_free_reconstruction.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/results/E003_ordered_coverage_controls.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/experiments/E001_geometry_and_persistence_audit/README.md`
- `Research/L006_s_infinity_b_infinity_relational_substrate/experiments/E002_ordered_coverage_controls/README.md`
- `Research/L005_complementary_channel_unification/results/E001_dual_channel_reproduction.md`
- `Research/L005_complementary_channel_unification/results/E002_known_physics_residual.md`
- `Research/L005_complementary_channel_unification/experiments/E001_dual_channel_reproduction/README.md`
- `Research/L004_hidden_state_observer_accessibility/results/E001_reversible_hidden_state.md`
- `Research/L004_hidden_state_observer_accessibility/results/E002_observer_capacity_comparison.md`
- `Research/L004_hidden_state_observer_accessibility/results/E003_arrow_of_time_controls.md`
- `Research/L004_hidden_state_observer_accessibility/experiments/E001_reversible_hidden_state/README.md`
- `Research/L004_hidden_state_observer_accessibility/experiments/E002_observer_capacity_comparison/README.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/results/E001_literal_mechanism_audit.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/results/E002_gw_em_known_physics_audit.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/results/E003_common_projective_invariant.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/experiments/E002_gw_em_known_physics_audit/README.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/experiments/E003_common_projective_invariant/README.md`
- `Research/L003_coupled_oscillator_cosmic_mechanism/experiments/E004_e2_e4_e6_transition_invariant/README.md`
- `Research/L002_emergent_dimension_relational_capacity/results/E001_meru_capacity_baseline.md`
- `Research/L002_emergent_dimension_relational_capacity/experiments/E001_meru_capacity_baseline/README.md`
- `Research/L002_emergent_dimension_relational_capacity/experiments/E002_generic_capacity_controls/README.md`
- `Research/L001_ordered_coverage_observer_time/results/E001_coverage_order_separation.md`
- `Research/L001_ordered_coverage_observer_time/results/E002_reparameterization_boundary.md`
- `Research/L001_ordered_coverage_observer_time/experiments/E001_coverage_order_separation/README.md`
- `Research/L001_ordered_coverage_observer_time/experiments/E002_reparameterization_boundary/README.md`
