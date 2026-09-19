# Experiment Source Inventory

This index records which Phase 4 experiment folders contain migrated equations, derivations, executable code, or historical protocols from the sibling projects.

## Evidence labels

- `REPRODUCIBLE CODE` — executable source is present in the Phase 4 experiment folder and has been run here.
- `SOURCE DERIVATION` — equations, assumptions, parameters, and decision boundary were extracted, but no local executable was available or rerun.
- `HISTORICAL PROTOCOL` — the chat/source record defines a test, but important parameters or code are missing.
- `PLANNED/BLOCKED` — folder reserved for a future experiment; no result is implied.

## Migrated experiments

| Phase 4 experiment | Source material | Evidence label | Related result |
|---|---|---|---|
| L001/E001 Coverage/order separation | V2.1 VCR experiment README and `experiment.py` | REPRODUCIBLE CODE | `L001.../results/E001_coverage_order_separation.md` |
| L001/E002 Reparameterization boundary | V2.4 time-free relational separation | SOURCE DERIVATION | `L001.../results/E002_reparameterization_boundary.md` |
| L002/E001 Meru capacity baseline | V3 `PGA-IIVM-6`, `IIVM-7` | SOURCE DERIVATION | `L002.../results/E001_meru_capacity_baseline.md` |
| L003/E002 GW-EM known-physics audit | V2.7 coupling audit and V2.8 polarization pretest | SOURCE DERIVATION | `L003.../results/E002_gw_em_known_physics_audit.md` |
| L003/E003 Common projective invariant | V2.10 common transition invariant | SOURCE DERIVATION | `L003.../results/E003_common_projective_invariant.md` |
| L004/E001 Reversible hidden state | V3 IIVM records and reproduction queue | SOURCE DERIVATION | `L004.../results/E001_reversible_hidden_state.md` |
| L004/E002 Observer capacity comparison | V3 IIVM/PGA records | HISTORICAL PROTOCOL | `L004.../results/E002_observer_capacity_comparison.md` |
| L005/E001 Dual-channel reconstruction | V3 PGA-152/PGA-153 records | HISTORICAL PROTOCOL | `L005.../results/E001_dual_channel_reproduction.md` |
| L006/E001 Geometry and persistence audit | V3 S-infinity/B-infinity E001 and mathematical models | SOURCE DERIVATION | `L006.../results/E001_geometry_and_persistence_audit.md` |
| L006/E002 Landmark-free reconstruction | V3 S-infinity/B-infinity E001 audit | HISTORICAL PROTOCOL | `L006.../results/E002_landmark_free_reconstruction.md` |
| L006/E003 Ordered coverage controls | V3 S-infinity/B-infinity E002 | SOURCE DERIVATION | `L006.../results/E003_ordered_coverage_controls.md` |

## Preservation rule

A source-derived derivation is not automatically a reproduced result. Upgrade a folder only after its code, parameters, environment, raw output, and validation are recorded locally. Chat identifiers remain provenance labels, not evidence of validation by themselves.
