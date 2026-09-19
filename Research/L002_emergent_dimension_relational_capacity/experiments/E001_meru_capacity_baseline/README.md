# Experiment E001 - Meru Capacity Baseline

**Source:** `indian-philosophy-modern-physics/V3/shared/test/PGA-IIVM-6.md`, `IIVM-7.md`
**Line:** L002 / R002 requirement 1
**Status:** SUCCESSFUL MATHEMATICAL DERIVATION; NOT A PHYSICAL DIMENSION DERIVATION

## Question

What exact capacity/counting quantity does binary Meru/ Pascal grouping provide?

## Derivation

For binary strings of depth \(n\), the microscopic state count is:

\[
N_{\rm micro}(n)=2^n.
\]

Group strings by Hamming weight \(k\), the number of ones. There are \(n+1\) possible weights:

\[
N_{\rm class}(n)=n+1.
\]

The class with weight `k` contains:

\[
|C_k|=\binom{n}{k}.
\]

The partition is complete because:

\[
\sum_{k=0}^{n}\binom{n}{k}=2^n.
\]

The observation map is:

\[
\Pi(x_1,\ldots,x_n)=\sum_i x_i=k.
\]

Thus distinct microscopic states can be observationally equivalent:

\[
X_a\ne X_b\quad\text{while}\quad\Pi(X_a)=\Pi(X_b).
\]

Expansion from class \(k\) has \(\binom{n}{k}\) compatible microstates. For \(n=20\), there are \(2^{20}=1,048,576\) microstates and \(21\) classes; the average class size is \(2^{20}/21=49,932.190476\ldots\).

## Assumptions

- Binary elements are distinguishable microscopically.
- The observer measures only Hamming weight.
- Grouping by weight is chosen as the observation channel; it is not derived as physically privileged.

## Decision

This is an exact combinatorial mechanism and satisfies the mathematical baseline. It does not derive 2D/3D physical space. Generic grouping controls remain required.
