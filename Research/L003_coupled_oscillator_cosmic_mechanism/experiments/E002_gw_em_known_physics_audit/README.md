# Experiment E002 - GW-EM Known-Physics Audit

**Source:** `indian-philosophy-modern-physics/V2/experiments/V2.7-gravitational-wave-em-coupling/README.md`; V3 shared audit records
**Line:** L003 / R003 requirement 2
**Status:** NEGATIVE FOR NOVELTY; KNOWN-PHYSICS BRIDGE

## Question

Does a gravitational-wave to electromagnetic response exceed established Einstein-Maxwell and GW-EM conversion physics?

## Physical decomposition

\(source dynamics -> metric perturbation h_{mu}_nu -> changing geometry -> interaction with background EM field or charged medium -> EM perturbation -> observable spectrum\).

Weak-field geometry:

\[
g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad |h_{\mu\nu}|\ll 1.
\]

Field split:

\[
F_{\mu\nu}=F^{(0)}_{\mu\nu}+\delta F_{\mu\nu}.
\]

Linearized coupling is schematically:

\(Box delta A ~ F^(0) * h\).

A reduced two-mode null model is:

\[
\frac{dA_{\rm EM}}{dx}=\kappa B A_{\rm GW},\qquad
\frac{dA_{\rm GW}}{dx}=-\kappa B A_{\rm EM}.
\]

With \(A_{EM}(0)=0\), the solution is:

\(A_{EM}(L)=A_{GW}(0) sin(kappa B L)\),
\(A_{GW}(L)=A_{GW}(0) cos(kappa B L)\).

Weak coupling gives:

\[
R=\left|\frac{A_{\rm EM}}{A_{\rm GW}}\right|=|\sin(\kappa B L)|\approx\kappa B L.
\]

The conserved toy norm is:

\(|A_{EM}|^2 + |A_{GW}|^2 = constant\).

## Historical outputs

For normalized `kappa=1` and `B L = 0.02, 0.04, 0.08, 0.16`, the reported amplitude ratios were approximately `0.0199987, 0.0399893, 0.0799147, 0.1593182`. For `B=0`, the response vanishes.

## Existing-physics decision

The reduced model is a structural coupled-mode null test. It does not calculate the physical conversion coefficient and does not establish a new law. The known-physics audit therefore remains the controlling result.
