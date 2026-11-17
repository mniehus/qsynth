# Quantum circuits and QAOA

QAOA — Quantum Approximate Optimization Algorithm — is the initial quantum baseline.

\[
|\psi(\boldsymbol\gamma,\boldsymbol\beta)\rangle=\prod_{r=1}^{p}e^{-i\beta_rH_M}e^{-i\gamma_rH_C}|+\rangle^{\otimes n}.
\]

- \(H_C\): cost Hamiltonian.
- \(H_M\): mixer Hamiltonian.
- \(\gamma_r,\beta_r\): variational parameters optimized classically.

First baseline: shallow standard QAOA. Later comparisons: greater depth, constraint-preserving mixers, compact encodings, noise and device-aware compilation. QAOA is a baseline, not a presumption that it is optimal.
