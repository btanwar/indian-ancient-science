# Experiment E002 - Landmark-Free Reconstruction

**Status:** NEGATIVE / HISTORICAL AUDIT
**Line:** L006 / R006 requirement 3

The historical observer reconstruction reported `rho approximately 0.9966`, but its setup supplied spatial landmark structure. This folder preserves the audit boundary: a valid replacement must remove supplied coordinates and landmarks, use shuffled/null controls, and preregister the reconstruction metric. The high historical correlation is not treated as a successful derivation of space or time.
